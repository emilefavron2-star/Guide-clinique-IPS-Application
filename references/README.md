# Ouvrages de référence — Guide clinique IPS

Sept manuels indexés et interrogeables pour alimenter le contenu du guide.

## Utilisation

```bash
cd "references"
bash extract_refs.sh                          # début de session, si /tmp/*.txt absents
python3 search_refs.py "goutte"               # cherche dans les 7 ouvrages
python3 search_refs.py "gout" -b goldman      # limiter à un ouvrage
python3 search_refs.py "colchicine" -n 10     # plus de résultats
python3 search_refs.py --page goldman 3010    # afficher une page entière
python3 search_refs.py --chapters copstead renal   # chapitres dont le titre correspond
python3 search_refs.py --list                 # liste des ouvrages
```

## Les ouvrages

| clé | ouvrage | pages | usage privilégié |
|---|---|---|---|
| `goldman` | Goldman-Cecil Medicine, 26e éd. (2020) | 4630 | Médecine interne — référence principale |
| `copstead` | Copstead-Kirkhorn & Banasik, Pathophysiology, 6e éd. (2019) | 1205 | Physiopathologie |
| `lilly` | Lilly, Pathophysiology of Heart Disease, 6e éd. (2015) | 480 | Cardiologie |
| `beaulieu` | Beaulieu, Précis de pharmacologie (FR) | 1047 | Pharmacologie |
| `demarche` | Démarche clinique (FR) | 857 | Examen physique, entrevue |
| `gphc_entrevue` | GPHC — Petit guide de l'entrevue médicale (2016, FR) | 343 | Questionnaire par système |
| `gphc_habiletes` | GPHC — Petit guide des habiletés cliniques (2018, FR) | 431 | Examen physique, raisonnement clinique |

## Limites à connaître

**Ouvrages américains.** Goldman, Copstead et Lilly sont excellents pour la physiopathologie, les mécanismes et la présentation clinique. Ils ne doivent **pas** servir de source pour les cibles thérapeutiques, les seuils ou les protocoles — utiliser les lignes directrices canadiennes (CCS, Hypertension Canada, Diabète Canada, INESSS, Ostéoporose Canada, CANMAT, KDIGO).

**Extraction sur deux colonnes.** La mise en page à deux colonnes fait parfois entremêler les phrases de colonnes voisines dans le texte extrait. Vérifier la cohérence d'un passage avant de s'y fier ; au besoin, afficher la page complète avec `--page`.

**Ligatures perdues.** Dans Lilly surtout, les ligatures `ff`, `fi`, `fl` disparaissent à l'extraction (« of » → « o », « cuffing » → « cu f ng »).

**Droit d'auteur.** Ces ouvrages sont sous droit d'auteur. Le contenu du guide doit être synthétisé et reformulé, jamais recopié en longs extraits.

## Fichiers

- `index.json` — carte chapitres → pages PDF pour les 7 ouvrages
- `search_refs.py` — outil de recherche plein texte
- `extract_refs.sh` — ré-extrait le texte des PDF vers `/tmp` (non persistant entre sessions)

Les PDF sources restent dans le dossier `uploads` de la session Cowork.
