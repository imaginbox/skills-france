---
name: facture-fr
description: Generer et verifier une facture conforme au droit francais (mentions obligatoires, TVA, e-facture). A utiliser pour creer, valider ou corriger une facture.
---

# Facture FR

Genere et verifie des factures conformes au droit francais.

## Quand l'utiliser
- Creer une facture (prestation, vente, service)
- Verifier la conformite d'une facture existante
- Comprendre les obligations legales (mentions, TVA, e-facture)

## Mentions obligatoires (art. 242 C + CGI)
Une facture doit contenir :
1. **Numero d'identification** unique et chronologique
2. **Date d'emission**
3. **Identite du vendeur** : raison sociale, adresse, SIRET
4. **Identite du client** : nom, adresse
5. **Date de livraison** (si differente)
6. **Nature et quantite** des biens/services
7. **Prix unitaire** hors taxes
8. **Taux et montant de TVA** (ou mention de l'exoneration)
9. **Montant total TTC**
10. **Conditions de paiement** (delai, mode)
11. **Regime d'imposition** (TVA, franchise en base)

## Regles de calcul
- **TVA standard** : 20%
- **TVA reduite** : 10% (restauration, travaux logement), 5.5% (denrees)
- **TVA 0%** : export, certaines denrees
- **Franchise en base de TVA** : si CA < 77 700 EUR (services) ou 93 900 EUR (ventes), pas de TVA mais mention obligatoire

## E-facture (nouvelle obligation)
Depuis le 1er sept. 2026 (grandes entreprises > 250 salaries) puis 2027 (toutes les entreprises) :
- Facturation electronique via plateforme PDP (Plateforme de Designation Publique)
- Factures XML au format Factur-X ou UBL
- Conservation legale 10 ans

## Verification rapide
Voir `mentions.md` pour la liste complete + template.

## Template
Voir `templates/facture.md` pour un modele de facture.

## Exemple d'usage
```
"Genere une facture pour une prestation de 2000 EUR HT, client ACME SAS, TVA 20%"
"Verifie si cette facture est conforme : [contenu]"
```

## Limites
- Ce skill est un aide-memoire, pas un conseil fiscal
- Pour les cas complexes (export, subvention, e-facture), consulter un expert-comptable
