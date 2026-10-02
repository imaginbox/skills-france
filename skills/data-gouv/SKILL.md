# Skill Data-Gouv

Recherche et exploitation des donnees ouvertes francaises (data.gouv.fr).

## Quand utiliser
- Quand l'utilisateur cherche des donnees ouvertes (statistiques, cartographie, referentiels)
- Pour construire une application qui consomme des API francaises
- Pour verifier l'existence d'un jeu de donnees avant de le collecter

## Methode
1. Identifier le besoin en donnees (theme, territoire, format)
2. Interroger l'API data.gouv.fr (voir api.md)
3. Filtrer par licence (etalique-2.0 est la plus ouverte)
4. Renvoyer : titre, description, format, licence, URL de telechargement
5. Si besoin, telecharger un echantillon et le documenter

## API data.gouv.fr
Voir api.md pour les endpoints et exemples cURL.

## Points d'attention
- La licence **etalique-2.0** autorise usage commercial + reutilisation sans restriction
- Les donnees "ouverte" ne sont pas garanties exactes : citer la source + date d'extraction
- Pour les donnees massives : preferer l'API ou S3 si disponible

## Sortie
- Liste des jeux de donnees correspondants (titre, licence, format, url)
- Extrait d'API cURL pret a l'emploi
- Note de licence pour le reemploi
