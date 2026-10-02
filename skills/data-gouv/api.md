# API data.gouv.fr

API publique : https://www.data.gouv.fr/api/
Aucune cle API requise pour un usage modere (rate limit ~ 300 req/min).

## Recherche de datasets

```bash
# Recherche par mot-cle
curl "https://www.data.gouv.fr/api/1/datasets/?q=population&page_size=10"

# Filtrer par licence ouverte
curl "https://www.data.gouv.fr/api/1/datasets/?q=transports&license=etalique-2.0"

# Filtrer par organisation
curl "https://www.data.gouv.fr/api/1/datasets/?organization=insee"
```

### Parametres utiles
| Parametre | Description |
|---|---|
| q | Mot-cle de recherche |
| page_size | Resultats par page (1-100) |
| page | Pagination |
| license | Filtre par licence (ex: etalique-2.0) |
| organization | Filtre par producteur |
| territory | Filtre par territoire |
| sort | Tri (ex: `-created_at`, `relevance`) |

## Detail d'un dataset

```bash
curl "https://www.data.gouv.fr/api/1/datasets/{uuid}/"
```

Retourne : titre, description, licences, ressources (formats, urls), metadonnees.

## Ressources d'un dataset

```bash
curl "https://www.data.gouv.fr/api/1/datasets/{uuid}/resources/"
```

Chaque ressource a : `title`, `format` (csv, geojson, xlsx...), `url`, `filesize`.

## Organisations

```bash
# Liste des organisations
curl "https://www.data.gouv.fr/api/1/organizations/?q=etatique"

# Datasets d'une organisation
curl "https://www.data.gouv.fr/api/1/organizations/{id}/datasets/"
```

## Licences courantes
| Licence | Code | Reutilisation |
|---|---|---|
| Licence Ouverte 2.0 | `etalique-2.0` | Libre, y compris commerciale |
| Open Database License | `odbl` | Libre + share-alike |
| CC BY 4.0 | `cc-by` | Libre avec attribution |
| CC BY-SA 4.0 | `cc-by-sa` | Libre + share-alike |

## Bonnes pratiques
- Toujours citer la source : `Source : data.gouv.fr, {titre du dataset}, extrait le {date}`
- Verifier la date de mise a jour du dataset (`updated_at`)
- Pour les gros fichiers : verifier `filesize` avant telechargement
