#!/usr/bin/env python3
"""
RGAA Audit - skills-france
Audit d'accessibilite RGAA v4.1.2 (WCAG 2.1 AA)
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def audit_html(html: str) -> dict:
    """Analyser un fichier HTML et retourner les non-conformites."""
    issues = []

    # 1.1 - Images sans alt
    imgs = re.findall(r'<img\b[^>]*>', html, re.IGNORECASE)
    for i, img in enumerate(imgs, 1):
        if not re.search(r'alt\s*=\s*["\'][^"\']+["\']', img, re.IGNORECASE):
            issues.append({
                'critere': '1.1',
                'titre': 'Image sans alt',
                'severite': 'critique',
                'detail': f'img #{i} manquant de alt',
                'code': img[:80],
                'correction': 'Ajouter alt="description"'
            })

    # 1.4 - Contrast (heuristic)
    # On ne peut pas verifier le contraste sans CSS, on le note
    issues.append({
        'critere': '1.4',
        'titre': 'Contraste texte/fond',
        'severite': 'critique',
        'detail': 'A verifier manuellement (>= 4.5:1)',
        'code': '',
        'correction': 'Ajuster les couleurs'
    })

    # 2.1 - Clavier (heuristic)
    if 'onkeydown' not in html.lower() and 'tabindex' not in html.lower():
        issues.append({
            'critere': '2.1',
            'titre': 'Navigation clavier',
            'severite': 'critique',
            'detail': 'Pas de gestion clavier detectee',
            'code': '',
            'correction': 'Ajouter tabindex et handlers keydown'
        })

    # 2.4 - Focus visible
    if ':focus' not in html.lower():
        issues.append({
            'critere': '2.4',
            'titre': 'Focus visible',
            'severite': 'critique',
            'detail': 'Pas de style :focus detecte',
            'code': '',
            'correction': 'Ajouter outline sur :focus'
        })

    # 3.1 - Langue
    if 'lang="fr"' not in html.lower() and "lang='fr'" not in html.lower():
        issues.append({
            'critere': '3.1',
            'titre': 'Langue non declaree',
            'severite': 'majeur',
            'detail': 'Pas de lang="fr" sur <html>',
            'code': '',
            'correction': 'Ajouter lang="fr" sur html'
        })

    # 3.2 - Structure des titres
    titles = re.findall(r'<h([1-6])\b', html, re.IGNORECASE)
    if titles:
        levels = [int(t) for t in titles]
        if levels[0] != 1:
            issues.append({
                'critere': '3.2',
                'titre': 'Pas de h1',
                'severite': 'majeur',
                'detail': f'Premier titre est h{levels[0]}',
                'code': '',
                'correction': 'Ajouter un h1'
            })
        for i in range(1, len(levels)):
            if levels[i] > levels[i-1] + 1:
                issues.append({
                    'critere': '3.2',
                    'titre': 'Saut de niveau de titre',
                    'severite': 'majeur',
                    'detail': f'h{levels[i-1]} -> h{levels[i]}',
                    'code': '',
                    'correction': 'Ne pas sauter de niveau'
                })
                break

    # 4.1 - HTML valide (heuristic)
    open_tags = len(re.findall(r'<[a-zA-Z][^>]*[^/]>', html))
    close_tags = len(re.findall(r'</[a-zA-Z][^>]*>', html))
    if abs(open_tags - close_tags) > 5:
        issues.append({
            'critere': '4.1',
            'titre': 'HTML potentiellement invalide',
            'severite': 'critique',
            'detail': f'{open_tags} balises ouvertes vs {close_tags} fermees',
            'code': '',
            'correction': 'Corriger les balises mal fermees'
        })

    return issues


def calculate_score(issues: list) -> int:
    """Calculer le score de conformite (0-100)."""
    if not issues:
        return 100
    poids = {'critique': 3, 'majeur': 2, 'mineur': 1}
    total = sum(poids.get(i['severite'], 1) for i in issues)
    max_total = 81 * 3  # 81 criteres, max 3 points chacun
    score = max(0, 100 - int((total / max_total) * 100))
    return score


def generate_report(issues: list, filepath: str, output: str = 'rapport-rgaa.md'):
    """Generer le rapport d'audit."""
    score = calculate_score(issues)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    lines = [
        '# Rapport d\'audit RGAA',
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
        ])
        if i['code']:
            lines.append(f"- Code : `{i['code']}`")
        lines.extend([
            f"- Correction : {i['correction']}",
            ''
        ])

    lines.extend([
        '## Prochaines etapes',
        '',
        '1. Corriger les criteres critiques en priorite',
        '2. Re-auditer apres corrections',
        '3. Viser un score >= 80 pour la conformite',
        ''
    ])

    Path(output).write_text('\n'.join(lines), encoding='utf-8')
    return output, score


def main():
    if len(sys.argv) < 2:
        print('Usage: python audit.py <fichier.html> [rapport.md]')
        sys.exit(1)

    filepath = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else 'rapport-rgaa.md'

    html = Path(filepath).read_text(encoding='utf-8')
    issues = audit_html(html)
    report_path, score = generate_report(issues, filepath, output)

    print(f'RGAA Audit : {filepath}')
    print(f'Score : {score}/100')
    print(f'Non-conformites : {len(issues)}')
    print(f'Rapport : {report_path}')


if __name__ == '__main__':
    main()
