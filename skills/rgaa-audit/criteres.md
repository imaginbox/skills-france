# Criteres RGAA v4.1.2 (WCAG 2.1 AA)

Liste des criteres a verifier. Chaque critere a :
- un numero
- un titre
- une severite (critique / majeur / mineur)
- une correction type

## Niveau 1 - Perceptible

### 1.1 - Textes d'images
- Severite : critique
- Verifier : toutes les images ont un alt
- Correction : ajouter alt="description"

### 1.2 - Videos
- Severite : majeur
- Verifier : les videos ont une transcription
- Correction : ajouter une transcription textuelle

### 1.3 - Audios
- Severite : majeur
- Verifier : les audios ont une transcription
- Correction : ajouter une transcription textuelle

### 1.4 - Contraste
- Severite : critique
- Verifier : contraste texte/fond >= 4.5:1
- Correction : ajuster les couleurs

## Niveau 2 - Utilisable

### 2.1 - Clavier
- Severite : critique
- Verifier : toutes les fonctionnalites accessibles au clavier
- Correction : ajouter tabindex, handlers keydown

### 2.2 - Temps
- Severite : majeur
- Verifier : pas de temps limite sans extension
- Correction : permettre d'augmenter le temps

### 2.3 - Navigation
- Severite : majeur
- Verifier : pas de navigation par le seul positionnement
- Correction : ajouter des liens de contour

### 2.4 - Focus visible
- Severite : critique
- Verifier : l'element focus est visible
- Correction : ajouter outline sur :focus

## Niveau 3 - Compréhensible

### 3.1 - Langue
- Severite : majeur
- Verifier : la langue de la page est declaree
- Correction : ajouter lang="fr" sur html

### 3.2 - Structure
- Severite : majeur
- Verifier : les titres sont hierarchiques
- Correction : h1 > h2 > h3 (pas de saut)

### 3.3 - Erreurs
- Severite : majeur
- Verifier : les erreurs de formulaire sont expliquees
- Correction : ajouter aria-describedby

## Niveau 4 - Fiable

### 4.1 - Compatibilite
- Severite : critique
- Verifier : le HTML est valide
- Correction : corriger les balises mal fermees

### 4.2 - ARIA
- Severite : majeur
- Verifier : les roles ARIA sont corrects
- Correction : utiliser les bons roles
