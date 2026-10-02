# Obligations RGPD (extraits)

Reference : Reglement (UE) 2016/679 + Loi Informatique et Libertes (modifiee).

## Principes (art. 5)
| Principe | Verification |
|---|---|
| Legalite, transparence | Base legale identifiee + mention claire |
| Limitation des finalites | Finalite precisee a la collecte |
| Minimization des donnees | Seules les donnees necessaires collectees |
| Exactitude | Mise a jour possible par l'utilisateur |
| Limitation de la conservation | Delai de retention defini |
| Integrite et confidentialite | Chiffrement / securisation des donnees |

## Obligations concretes
### 1. Base legale (art. 6)
- Severite : critique
- Verifier : chaque traitement a une base legale (consentement, contrat, obligation legale, interet legitime...)
- Correction : documenter la base legale pour chaque donnee

### 2. Information des personnes (art. 13-14)
- Severite : critique
- Verifier : politique de confidentialite accessible + mentions a la collecte
- Correction : ajouter une page "Confidentialite" + mentions au formulaire

### 3. Consentement cookies (art. 6 + ePrivacy)
- Severite : critique
- Verifier : banner cookies avec acceptation/refus, pas de cookie avant acceptation
- Correction : implementer un CMP (Consent Management Platform)

### 4. Droits des personnes (art. 15-22)
- Severite : majeur
- Verifier : acces, rectification, effacement, portabilite, opposition
- Correction : procedure + formulaire d'exercice des droits

### 5. Delai de conservation
- Severite : majeur
- Verifier : duree de retention definie pour chaque categorie
- Correction : documenter les delais + procedure de suppression

### 6. Securite (art. 32)
- Severite : critique
- Verifier : HTTPS, chiffrement des mots de passe (hash), sauvegardes, controle d'acces
- Correction : HTTPS force, bcrypt/argon2, RBAC

### 7. Registre des traitements (art. 30)
- Severite : majeur
- Verifier : registre tenu a jour (obligatoire si > 250 salaries OU traitement a risque)
- Correction : creer le registre des traitements

### 8. DPO (art. 37)
- Severite : majeur
- Verifier : DPO designe si traitement a grande echelle / categories speciales
- Correction : designer un DPO (interne ou externalise)

### 9. Sous-traitants (art. 28)
- Severite : majeur
- Verifier : contrat de sous-traitance (DPA) avec chaque sous-traitant
- Correction : signer les DPA (ex: AWS, Stripe, Sendinblue)

### 10. Transferts hors UE (art. 44-49)
- Severite : majeur
- Verifier : clauses contractuelles types ou adequation pour les transferts
- Correction : ajouter les CCT (Commission Europeenne)

### 11. Breach notification (art. 33-34)
- Severite : critique
- Verifier : procedure de notification CNIL sous 72h
- Correction : procedure interne + template de notification

### 12. Categories speciales (art. 9)
- Severite : critique
- Verifier : donnees de sante, religion, orientation... seulement si base legale explicite
- Correction : eviter de collecter, ou base legale + garanties renforcees
