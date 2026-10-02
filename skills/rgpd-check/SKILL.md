# Skill RGPD-Check

Verification de conformite RGPD (Reglement General sur la Protection des Donnees).

## Quand utiliser
- Quand on developpe une application qui collecte des donnees personnelles
- Avant une mise en ligne (conformite RGPD)
- Quand l'utilisateur demande un audit de conformite RGPD

## Methode
1. Identifier les donnees personnelles collectees (nom, email, IP, cookies...)
2. Verifier les obligations legales (voir obligations.md)
3. Generer un rapport de conformite
4. Proposer des corrections

## Obligations RGPD (extraits)
Voir obligations.md pour la liste complete.

## Sortie
- rapport-rgpd.md : liste des non-conformites + severite + correction
- score : 0-100 (taux de conformite)
