#!/usr/bin/env python3
"""
RGPD Check - skills-france
Audit de conformite RGPD (heuristique) sur un site web (HTML/CSS/JS).

Usage:
    python check.py <fichier.html> [rapport.md]

Genere un rapport-rgpd.md avec :
- Score de conformite (0-100)
- Liste des non-conformites + severite
- Corrections proposees
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def check_html(html: str) -> list:
    """Analyser le HTML et retourner les non-conformites RGPD."""
    issues = []
    low = html.lower()

    # 1. Politique de confidentialite
    if not re.search(r'politique\s*(de\s*)?(confidentialite|vie\s*privee)', low):
        issues.append({
            'critere': '1.3',
            'titre': 'Politique de confidentialite',
            'severite': 'critique',
            'detail': 'Aucun lien vers une politique de confidentialite detecte',
            'correction': 'Ajouter une page "Confidentialite" liee dans le footer'
        })

    # 2. Banner cookies
    has_cookie_banner = any(k in low for k in ('cookie', 'consentement', 'cnil'))
    if not has_cookie_banner:
        issues.append({
            'critere': '1.1',
            'titre': 'Banner cookies',
            'severite': 'critique',
            'detail': 'Aucun gestionnaire de consentement detecte',
            'correction': 'Implementer un CMP (accepter/refuser, pas de cookie avant acceptation)'
        })

    # 3. Formulaires : mention de finalite
    forms = re.findall(r'<form\b[^>]*>.*?</form>', html, re.IGNORECASE | re.DOTALL)
    for i, form in enumerate(forms, 1):
        f_low = form.lower()
        has_fields = '<input' in f_low or '<textarea' in f_low
        has_mention = any(k in f_low for k in (
            'confidentialite', 'rgpd', 'donnees personnelles',
            'finalite', 'cnil', 'gdpr'
        ))
        if has_fields and not has_mention:
            issues.append({
                'critere': '1.2',
                'titre': f'Formulaire #{i} sans mention de finalite',
                'severite': 'critique',
                'detail': 'Formulaire sans mention de la finalite du traitement',
                'correction': 'Ajouter une mention : "Vos donnees sont utilisees pour {finalite}"'
            })

    # 4. HTTPS (heuristic : scripts/ressources en http://)
    insecure = re.findall(r'(?:src|href)\s*=\s*["\']http://[^"\']+["\']', low)
    if insecure:
        issues.append({
            'critere': '2.1',
            'titre': 'Ressources en HTTP non secure',
            'severite': 'critique',
            'detail': f'{len(insecure)} ressources chargees en http://',
            'correction': 'Utiliser https:// pour toutes les ressources'
        })

    # 5. Champs mot de passe (heuristic)
    if 'type="password"' in low:
        issues.append({
            'critere': '2.2',
            'titre': 'Mots de passe',
            'severite': 'critique',
            'detail': 'Formulaire de connexion detecte - a verifier : hash (bcrypt/argon2), HTTPS',
            'correction': 'Ne jamais stocker en clair ; hash avec bcrypt/argon2 + HTTPS'
        })

    # 6. Analytics / tracking tiers
    trackers = [k for k in ('google-analytics', 'gtag', 'facebook', 'matomo', 'hotjar', 'clarity') if k in low]
    if trackers:
        issues.append({
            'critere': '1.4',
            'titre': 'Outils de tracking tiers',
            'severite': 'majeur',
            'detail': f'Tracking detecte : {", ".join(trackers)}',
            'correction': 'Charger uniquement apres consentement (CMP) + DPA avec le sous-traitant'
        })

    # 7. Droit d'acces / effacement
    if not re.search(r'(acces\s*aux\s*donnees|effacement|suppression\s*des\s*donnees|droits\s*des)', low):
        issues.append({
            'critere': '1.5',
            'titre': 'Droits des personnes',
            'severite': 'majeur',
            'detail': 'Aucune mention des droits (acces, rectification, effacement)',
            'correction': 'Detailer les droits dans la politique de confidentialite + contact'
        })

    return issues


def calculate_score(issues: list) -> int:
    """Calculer le score de conformite (0-100)."""
    if not issues:
        return 100
    poids = {'critique': 3, 'majeur': 2, 'mineur': 1}
    total = sum(poids.get(i['severite'], 1) for i in issues)
    max_total = 12 * 3  # 12 criteres checks, max 3 points chacun
    score = max(0, 100 - int((total / max_total) * 100))
    return score


def generate_report(issues: list, filepath: str, output: str = 'rapport-rgpd.md'):
    """Generer le rapport d'audit."""
    score = calculate_score(issues)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    lines = [
        '# Rapport d\'audit RGPD',
        '',
        f'> Fichier : `{filepath}`',
        f'> Date : {now}',
        f'> Score : **{score}/100**',
        f'> Non-conformites : {len(issues)}',
        '',
        '## Resume',
        '',
    ]

    if score >= 80:
        lines.append('Statut : **Conforme** - quelques ameliorations possibles')
    elif score >= 50:
        lines.append('Statut : **Partiellement conforme** - corrections necessaires')
    else:
        lines.append('Statut : **Non conforme** - corrections urgentes')

    lines.extend(['', '## Non-conformites', ''])

    for i in issues:
        lines.extend([
            f"### {i['critere']} - {i['titre']}",
            f"- Severite : **{i['severite']}**",
            f"- Detail : {i['detail']}",
            f"- Correction : {i['correction']}",
            ''
        ])

    lines.extend([
        '## Prochaines etapes',
        '',
        '1. Corriger les criteres critiques en priorite',
        '2. Tenir a jour le registre des traitements (art. 30)',
        '3. Signer les DPA avec les sous-traitants (art. 28)',
        '4. Re-auditer apres corrections',
        '',
        '> Ce rapport est une aide heuristique, pas un audit legal.',
        '> En cas de doute, consulter la CNIL : https://www.cnil.fr',
        ''
    ])

    Path(output).write_text('\n'.join(lines), encoding='utf-8')
    return output, score


def main():
    if len(sys.argv) < 2:
        print('Usage: python check.py <fichier.html> [rapport.md]')
        sys.exit(1)

    filepath = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else 'rapport-rgpd.md'

    html = Path(filepath).read_text(encoding='utf-8')
    issues = check_html(html)
    report_path, score = generate_report(issues, filepath, output)

    print(f'RGPD Check : {filepath}')
    print(f'Score : {score}/100')
    print(f'Non-conformites : {len(issues)}')
    print(f'Rapport : {report_path}')


if __name__ == '__main__':
    main()
