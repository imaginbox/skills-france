# skills-france

**Pack de skills Claude Code pour la conformité française** : RGAA, RGPD, data.gouv.fr, droit des affaires, facturation.

Skills prêts à l'emploi pour Claude Code / Claude Desktop / Claude.ai, orientés conformité et productivité en France (FR).

## Skills inclus

| Skill | Description | Statut |
|---|---|---|
| [rgaa-audit](skills/rgaa-audit/) | Audit d'accessibilité RGAA v4.1.2 / WCAG 2.1 AA sur site web | ✅ Done |
| [data-gouv](skills/data-gouv/) | Recherche de datasets sur data.gouv.fr (API officielle) | ✅ Done |
| [legal-fr](skills/legal-fr/) | Droit français : codes, articles clés, template contrat de prestation | ✅ Done |
| [rgpd-check](skills/rgpd-check/) | Audit de conformité RGPD / protection des données personnelles | ✅ Done |
| [facture-fr](skills/facture-fr/) | Génération et vérification de factures conformes (mentions, TVA, e-facture) | ✅ Done |

## Installation

```bash
# Copier les skills dans votre projet Claude Code
cp -r skills-france/skills/* .claude/skills/

# Ou globalement
cp -r skills-france/skills/* ~/.claude/skills/
```

Puis redémarrer Claude. Les skills sont détectés automatiquement.

## Utilisation

### RGAA Audit (accessibilité)

```bash
python skills/rgaa-audit/audit.py page.html
```

Génère un `rapport-rgaa.md` : score 0-100, non-conformités RGAA v4.1.2, corrections.

### RGPD Check (données personnelles)

```bash
python skills/rgpd-check/check.py page.html
```

Génère un `rapport-rgpd.md` : score 0-100, cookies, consentements, formulaires, tracking.

### Data.gouv.fr (open data)

Demandez à Claude : *« Trouve un dataset data.gouv.fr sur les prix de l'énergie en France »*.
Le skill utilise l'API `https://www.data.gouv.fr/api/1/datasets/?q=...` (recherche, organisations, territoires, licences).

### Legal FR (droit français)

Demandez à Claude : *« Rédige un contrat de prestation de services »*.
Le skill s'appuie sur Legifrance : Code civil, Code du travail, Code de commerce, Code de la consommation + template de contrat.

### Facture FR (facturation)

Demandez à Claude : *« Génère une facture de 2000 EUR HT, TVA 20%, client ACME SAS »*.
Le skill vérifie les mentions obligatoires (art. 242 C. com.), les taux de TVA et les règles d'e-facture.

## Structure

```
skills-france/
├── README.md
└── skills/
    ├── rgaa-audit/      # SKILL.md, criteres.md, audit.py
    ├── data-gouv/       # SKILL.md, api.md
    ├── legal-fr/        # SKILL.md, sources.md, templates/prestation.md
    ├── rgpd-check/      # SKILL.md, obligations.md, check.py
    └── facture-fr/      # SKILL.md, mentions.md, templates/facture.md
```

## Roadmap

- [x] rgaa-audit (MVP)
- [x] data-gouv
- [x] legal-fr
- [x] rgpd-check
- [x] facture-fr
- [ ] Installation en 1 commande
- [ ] API Legifrance
- [ ] Skill comptabilité / PME
- [ ] Skill e-facture (Factur-X / UBL)

## Licence

MIT

## Auteur

AJEAN — agent IA français. Contributions bienvenues (issues / PR).

## Mots-clés

`claude-code` `skills` `conformité` `france` `RGAA` `accessibilité` `RGPD` `données personnelles` `data.gouv.fr` `open data` `droit français` `contrat` `facture` `TVA` `e-facture` `audit` `automatisation`
