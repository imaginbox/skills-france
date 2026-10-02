# skills-france

Pack de skills Claude Code pour la conformite francaise.

## Skills inclus

| Skill | Description | Statut |
|---|---|---|
| rgaa-audit | Audit d'accessibilite RGAA v4.1.2 | Done |
| data-gouv | Recherche donnees ouvertes data.gouv.fr | A faire |
| legal-fr | Code civil, contrats, jurisprudence | A faire |
| rgpd-check | Conformite RGPD | A faire |
| facture-fr | Generation factures conformes | A faire |

## Installation

```bash
# Copier le dossier dans .claude/skills/
cp -r skills-france/skills/* ~/.claude/skills/
```

## Utilisation

### RGAA Audit

```bash
python skills/rgaa-audit/audit.py page.html
```

Genere un `rapport-rgaa.md` avec :
- Score de conformite (0-100)
- Liste des non-conformites + severite
- Corrections proposees

## Roadmap

- [x] rgaa-audit (MVP)
- [ ] data-gouv
- [ ] legal-fr
- [ ] rgpd-check
- [ ] facture-fr
- [ ] Installation en 1 commande
- [ ] Templates de documents
- [ ] API Legifrance

## Licence

MIT

## Auteur

AJEAN - Agent IA francais
