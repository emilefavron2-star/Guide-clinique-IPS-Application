⚠️ RÈGLE ABSOLUE — PROTECTION CONTRE LES PERTES DE DONNÉES ⚠️
Avant TOUTE modification de index.html (remplacement de blocs, insertion de sections, Python bash, etc.) :
1. Exécuter d'abord : bash "/sessions/focused-admiring-hawking/mnt/Guide d'étude HTML/backup.sh"
2. NE JAMAIS remplacer un bloc de chars sans d'abord vérifier EXACTEMENT ce que ce bloc contient (début ET fin du bloc)
3. Pour tout remplacement de section, identifier précisément les balises ouvrantes/fermantes avec le contenu exact — ne jamais supposer
4. Après chaque modification : vérifier DIV balance (opens == closes)
5. Les backups horodatés sont dans le dossier /backups/ — conserver les 5 derniers
6. ⚠️ PLACEMENT DU CONTENU : Tout nouveau bloc (table, section, calculateur) inséré dans une section DOIT être à l'intérieur du div `id="sec-[nom]"` correspondant. Vérifier avec Python que le bloc ajouté est bien avant la fermeture `</div>` du div section (utiliser le script de vérification de profondeur div). Un bloc hors du section div sera toujours visible peu importe la section active, et apparaîtra EN BAS des flèches de navigation plutôt qu'à l'intérieur du contenu.
7. ⚠️ PILLS BUTTONS & ALGORITHMES — VÉRIFICATION OBLIGATOIRE AVANT INSERTION : La fonction showPanel(prefix, activeId, count) utilise des IDs NUMÉRIQUES (prefix+0, prefix+1, etc.). Les IDs des panneaux DOIVENT donc être numériques (ex: micro1010, micro1011…) et non alphabétiques (micro101a, micro101b…). Avant d'insérer tout nouveau système de pills buttons ou algorithme interactif, vérifier que : (a) les IDs des panneaux correspondent exactement au format prefix+i attendu par showPanel, (b) les attributs data-panel des boutons matchent ces IDs, (c) les fonctions JS ne contiennent pas d'apostrophes directes dans des strings simples (utiliser &middot; &rarr; &le; au lieu de · → ≤, ou échapper les apostrophes).
8. ⚠️ JAMAIS DE CONTENU EN DOUBLE dans la même section : Avant d'ajouter un nouveau bloc d'information, vérifier qu'il n'existe pas déjà dans la section ou une section proche. Si l'information est déjà dans un tableau de référence complet, ne pas la répéter dans des encadrés séparés. Fusionner les informations si nécessaire plutôt que de créer des doublons.
9. ⚠️ INSERTION DANS LE BON ONGLET — VÉRIFICATION OBLIGATOIRE : Tout nouveau contenu doit être inséré STRICTEMENT à l'intérieur du div `<div class="section" id="sec-[nom]">` correspondant. Méthode de vérification obligatoire avant de sauvegarder : (a) utiliser `content.rfind('\n    </div>', 0, fin_pos)` pour trouver la fermeture RÉELLE de la section (et non après), (b) insérer les blocs AVANT cette position, (c) confirmer avec Python que `sec_start < pos_nd_nouveau < sec_end` pour chaque bloc inséré, (d) confirmer que le contenu N'APPARAÎT PAS dans d'autres onglets en vérifiant qu'aucun keyword du nouveau bloc n'est trouvé dans la plage d'un autre sec-[nom]. Un bloc inséré APRÈS le `</div>` fermant de la section sera visible dans TOUS les onglets simultanément — c'est la cause la plus fréquente de contenu visible partout.
12. ⚠️ MODÈLE DE RÉFÉRENCE — STYLE & ORDRE DES SECTIONS : Pour toute nouvelle section, onglet ou bloc de contenu, le modèle obligatoire à respecter est la section TVP (id="sec-tvp"). Structure à reproduire dans cet ordre : (a) barre de navigation rapide avec boutons goToBlock de couleurs variées (chaque bouton a sa couleur thématique propre — pas tous la même couleur), (b) blocs dans l'ordre : Définition/Physiopath → Étiologies/FdR → Présentation clinique → Paraclinique/Stratégie Dx → Traitement → Suivi, (c) chaque bloc utilise la classe correspondante (`block def`, `block clin`, `block para`, `block rx`, `block flag`) avec `style="margin-top:14px;"`, (d) les cartes de contenu utilisent `display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-top:10px;` avec des divs `background:[pastel];border-radius:10px;padding:14px;` — palette : rouge `#fce4ec`, jaune `#fff3cd`, bleu `#e8f4fd`, vert `#f0fdf4`, violet `#ede9fe`, gris `#f1f5f9`, (e) les encadrés avec accent utilisent `border-left:4px solid [couleur]` (pas border-top), (f) les tableaux suivent le style `<table>` avec `<thead>` et `style="background:#f8f9fa;"` sur les lignes paires, (g) les encadrés informatifs utilisent `<div class="key-fact [color]">` (blue, green, orange, red), (h) les blocs traitement utilisent des pills buttons (showPanel) avec des tableaux de comparaison clairs, (i) les red flags utilisent `<div class="flag-list"><div class="flag-item">`. Avant de créer un nouveau bloc, inspecter sec-tvp dans index.html pour valider le style exact. NE PAS utiliser border-top:4px solid — c'est le style HTA (ancien modèle).

10. ⚠️ BLOC TRAITEMENT — TABLEAUX COMPARATIFS OBLIGATOIRES : Le bloc traitement (class="block rx") de chaque section pathologique DOIT utiliser des tableaux comparatifs ou des boîtes colorées pour présenter les options thérapeutiques. Format obligatoire : (a) pills buttons (showPanel) pour séparer les stades/contextes (ex: faible risque / haut risque / métastatique), (b) dans chaque panel : tableau `<table>` avec colonnes Traitement | Avantages | Inconvénients | Notes, OU grille de boîtes colorées `display:grid` avec `border-left:4px solid` pour chaque option, (c) ne jamais présenter les traitements comme une liste à puces non structurée — toujours organiser visuellement. Le modèle de référence OBLIGATOIRE est le bloc traitement de l'HTA (sec-hta). Inspecter ce bloc avant de créer tout nouveau bloc traitement. Appliquer ce standard à toute nouvelle section ou révision d'une section existante.

11. ⚠️ HOME-CARD OBLIGATOIRE À CHAQUE NOUVELLE GRANDE SECTION : Lors de la création d'un nouveau groupe de navigation (id="grp-[nom]") représentant une nouvelle spécialité ou grande catégorie, TOUJOURS ajouter simultanément une `home-card` correspondante dans la grille de la page d'accueil (`id="sec-home"` > `div class="home-grid"`). La home-card doit inclure : (a) un `onclick` pointant vers la première section du groupe + `openGroup('grp-[nom]')`, (b) une icône emoji pertinente avec couleurs cohérentes (`home-card-icon`), (c) le nom de la spécialité (`home-card-name`), (d) le nombre de sections (`home-card-count`). Ne jamais créer un groupe de navigation sans sa home-card correspondante — le guide d'accueil doit toujours refléter toutes les grandes sections disponibles.

13. ⚠️ PILL BUTTON DE NAVIGATION OBLIGATOIRE À CHAQUE AJOUT DE CONTENU : Lorsqu'un nouveau bloc de contenu (encadré, tableau, calculateur, algorithme) est ajouté à un onglet existant, il DOIT être accompagné d'un bouton `goToBlock` dans la barre de navigation rapide en haut de l'onglet. Ce bouton doit : (a) utiliser `onclick="goToBlock('id-du-bloc')"`, (b) avoir une couleur thématique cohérente avec le contenu (ex: rouge pour red flags, vert pour traitement, bleu pour diagnostic), (c) avoir un libellé court et descriptif avec un emoji pertinent. Si l'onglet n'a pas encore de barre de navigation rapide, la créer avec un `<div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px;">`. Ne jamais ajouter un nouveau bloc sans son bouton de navigation correspondant — cela garantit que tout le contenu reste accessible rapidement.

14. ⚠️ ORDRE DES PILL BUTTONS = ORDRE DES BLOCS : L'ordre des boutons `goToBlock` dans la barre de navigation rapide doit TOUJOURS refléter l'ordre physique des blocs dans la page. Si un bloc est déplacé, renommé ou supprimé, le bouton correspondant doit être mis à jour simultanément. Règle : (a) parcourir la section de haut en bas et lister les IDs des blocs dans l'ordre rencontré, (b) les boutons de navigation doivent apparaître dans ce même ordre, (c) après tout déplacement de bloc, vérifier que chaque bouton pointe vers un `id` qui existe toujours dans la section, (d) supprimer les boutons orphelins (dont la cible `id` n'existe plus). Un bouton dont l'ordre ne correspond pas au contenu crée de la confusion dans la navigation.

15. ⚠️ SOURCES DE CONTENU — HIÉRARCHIE OBLIGATOIRE : Lors de l'ajout ou de la révision de contenu clinique, respecter cet ordre de priorité :

    **Niveau 1 — Documents Notion de l'utilisateur** (notes de cours par spécialité) : source primaire, toujours consulter en premier.

    **Niveau 2 — Manuels de référence.**

    2a. **Lanthier — Guide pratique de médecine interne** ⭐ (7e éd., Dr Luc Lanthier & Dr Donald Echenberg, CHUS / Université de Sherbrooke) — https://lanthiermed.com/publication/fr
    Référence **québécoise, francophone et à jour** (≈ 4 mises à jour/an). C'est la source de niveau 2 à privilégier : contrairement aux manuels américains, elle **peut servir aux conduites thérapeutiques, seuils et algorithmes** en contexte canadien.
    ⚠️ **Accès par abonnement + application JavaScript** : ni WebFetch ni le navigateur ne peuvent en extraire le contenu. Fonctionnement identique à RxVigilance — **demander l'extrait à l'utilisateur** (copier-coller de la section pertinente), puis synthétiser et reformuler dans le style du guide (droit d'auteur — ne jamais recopier tel quel).
    Citer sous la forme « Lanthier, Médecine interne, 7e éd. ».

    2b. **Manuels indexés** dans `references/` : Goldman-Cecil 26e, Copstead-Kirkhorn & Banasik, Lilly (cardio), Beaulieu (pharmaco, FR), Démarche clinique (FR), GPHC Entrevue et GPHC Habiletés cliniques (FR).
    Recherche : `cd references && bash extract_refs.sh` (si /tmp vide) puis `python3 search_refs.py "terme"`.
    ⚠️ Goldman, Copstead et Lilly sont **américains** : les utiliser pour la physiopathologie, les mécanismes et la présentation clinique — **jamais** pour les cibles thérapeutiques, seuils ou protocoles.

    🚩 **ÉTAPE OBLIGATOIRE — NE PAS SAUTER LE NIVEAU 2.** Les fichiers d'extraction vivent dans `/tmp` et **disparaissent entre les sessions** : l'outil paraît donc « absent » alors qu'il suffit de le régénérer. C'est la cause connue du saut de ce niveau.
    ➜ **Dès qu'une session comporte de la rédaction de contenu clinique, exécuter `bash extract_refs.sh` AVANT d'écrire quoi que ce soit**, puis interroger les manuels pour chaque nouvelle section — au minimum sur la **physiopathologie**, les **mécanismes** et la **présentation clinique**.
    ➜ **Preuve de consultation exigée :** toute section dont le contenu provient d'un manuel doit **nommer la source dans le texte** (ex. « Goldman-Cecil, 26<sup>e</sup> éd. », « Copstead »). Une section sans aucune citation de niveau 2 signale que l'étape a été sautée.
    ➜ **Vérification de fin de tâche** — aucune sortie ne doit être vide :
    ```bash
    ls -l /tmp/goldman.txt   # doit exister AVANT la rédaction
    ```
    ```python
    import re
    c = open('index.html', encoding='utf-8').read()
    N2 = ['Goldman','Copstead','Lilly','Beaulieu','GPHC','Lanthier']
    for s in ['<liste des sections créées ou révisées>']:
        st = c.find('<div class="section" id="sec-%s"' % s); nx = c.find('<div class="section" id="sec-', st+10)
        seg = c[st:nx]
        cited = [w for w in N2 if re.search(r'(?<![A-Za-zÀ-ÿ])'+w+r'(?![A-Za-zÀ-ÿ])', seg, re.I)]
        print(s, '->', cited or '⚠️ AUCUNE SOURCE NIVEAU 2 CITÉE')
    ```

    **Niveau 3 — Sources canadiennes en ligne** pour TOUTE conduite thérapeutique (doses, cibles, algorithmes) :
    - **RxVigilance** https://rx.vigilance.ca/module/accueil/#/fr — posologies, interactions, ajustements IRC (⚠️ JavaScript + login : demander l'extrait à l'utilisateur)
    - **Santé Canada BDPP** https://produits-sante.canada.ca/dpd-bdpp/?lang=fre — monographies officielles, disponibilité canadienne
    - **Thrombosis Canada** https://thrombosiscanada.ca/hcp/practice/clinical_guides — référence pour TOUTE l'anticoagulation : TEV, FA, AOD, warfarine, périop, renversement, TIH (⚠️ JavaScript : PDF téléchargeables)
    - **CCS Pocket Guides** https://ccs.ca/pocket-guides/ — guides de poche FA, IC, dyslipidémie, SCA
    - **INESSS — Guides d'usage optimal** ⭐ https://www.inesss.qc.ca/formations-et-outils/outils-cliniques/outils-par-types/guides-dusage-optimal.html — index A–Z avec PDF directs (anticoagulants, ITSS, sevrage alcool, ORL, infection urinaire, cellulite, C. difficile…). Consultable par WebFetch, lire par tranches.
    - Autres : Hypertension Canada, Diabète Canada, Ostéoporose Canada, CANMAT, KDIGO

    C'est le niveau qui prime pour les doses, cibles et algorithmes de traitement.

    **Niveau 4 — Connaissances internes de Claude** : uniquement après avoir AVERTI l'utilisateur et obtenu son accord.

    Règles strictes : (a) ne jamais compléter silencieusement avec des connaissances internes, (b) avertir AVANT toute recherche en ligne ou usage du niveau 4, (c) citer la source dans le contenu quand elle vient d'une ligne directrice (ex. « CCS 2021 »), (d) les manuels étant sous droit d'auteur, synthétiser et reformuler dans le style du guide plutôt que recopier. L'objectif est que le guide reflète fidèlement les sources validées, pas les connaissances générales de Claude.

16. ⚠️ AUCUN CONTENU EN PROSE BRUTE DANS UN BLOC OU UN PANNEAU — DIVISION VISUELLE OBLIGATOIRE : Aucun panneau (showPanel) ni bloc ne doit présenter de l'information sous forme de paragraphe `<strong>...</strong> texte<br>` empilé. Toute information structurable (catégories, étapes, options, critères) DOIT être divisée visuellement selon un des patrons suivants, à l'image de ce qui a été fait dans la section Gynécologie (SUA, Cycles hormonaux, Cancer de l'endomètre, Ménopause, Survivance) :

    (a) **Grille de cartes pastel** — pour 3 à 6 catégories parallèles (ex : histoire clinique, examen physique, bilans) : `display:grid;grid-template-columns:repeat(auto-fit,minmax(220-250px,1fr));gap:12px;` avec des divs `background:[pastel];border-radius:10px;padding:14px;` contenant un `<strong style="color:[couleur foncée]">emoji Titre</strong>` puis `<div style="font-size:13px;line-height:1.7;margin-top:8px;">contenu</div>`. Palette : bleu `#e8f4fd`/`#1d4ed8`, jaune `#fff3cd`/`#d35400`, vert `#f0fdf4`/`#15803d`, rouge `#fce4ec`/`#c0392b`, violet `#ede9fe`/`#6d28d9`, gris `#f1f5f9`/`#334155`.

    (b) **Tableau structuré** — dès qu'il y a une comparaison (molécules, options, stades) : `<table>` avec `<thead>`, lignes paires `style="background:#f8f9fa;"`. Voir aussi règle #10 pour les blocs traitement.

    (c) **Stat-row** — pour des chiffres clés (durées, seuils, %, scores) : `<div class="stat-row">` avec `<div class="stat-card [blue|red|yellow|green|purple|gray|ink|cream]">`.

    (d) **Criteria-list numérotée** — pour des indications/étapes séquentielles : `<div class="criteria-list"><div class="criteria-item"><div class="criteria-num blue">N</div><span>...</span></div></div>` (utiliser `criteria-num red` avec `!` pour un critère d'exception/urgence).

    (e) **Boîtes appariées vert/rouge** — pour contraster deux issues ou enseignement patient (✅ À faire / 🚨 Red flags, ou Si X / Si non-X) : grille `1fr 1fr` avec `background:#f0fdf4;border-left:4px solid #15803d` (vert) et `background:#fef2f2;border-left:4px solid #c0392b` (rouge).

    (f) **Key-fact colorée** pour un point de synthèse isolé : `<div class="key-fact [blue|red|yellow|green|orange|purple|black|ink|cream]">` — toutes ces classes sont maintenant définies en CSS globale (ajoutées en 2026-07-27).

    Avant de créer ou réviser tout panneau/bloc, se demander : « est-ce que cette information a une structure (catégories, séquence, comparaison, chiffres) ? » Si oui, un des patrons (a)-(f) est obligatoire — jamais de texte en `<br>` empilé comme seul format.

17. ⚠️ PILLS BUTTONS — STYLE RECTANGULAIRE OBLIGATOIRE (modèle HTA) : Tout bouton pill/tab (showPanel ou switchTx) doit utiliser le style rectangulaire de sec-hta, PAS le badge arrondi. Actif : `border-radius:8px;padding:8px 18px;font-weight:600;transition:.15s;` avec `background:[couleur thématique]` et `color:#fff`. Inactif : mêmes dimensions avec `background:#e0e0e0;color:#333;`. Ne jamais utiliser `border-radius:20px` avec `padding:5px-6px 13-14px` (ancien style badge arrondi, abandonné). La fonction JS globale `showPanel()` applique déjà `#e0e0e0`/`#333` par défaut aux boutons inactifs — ne pas la modifier sans mettre à jour tous les boutons existants en conséquence.

18. ⚠️ ORDRE PHYSIQUE DES SECTIONS = SECTION_ORDER : Toute nouvelle section (`<div class="section" id="sec-X">`) doit être insérée physiquement dans le fichier au même endroit que sa position dans le tableau JS `SECTION_ORDER` (et dans le menu latéral `specialty-items`). Ne jamais ajouter une nouvelle section à la fin du fichier ou à un autre endroit « pratique » — toujours l'insérer entre les deux sections voisines selon l'ordre logique déclaré. Après toute création/déplacement de section, vérifier avec Python que l'ordre physique (`re.finditer(r'<div class="section" id="([^"]+)"', c)`) correspond à l'ordre dans `SECTION_ORDER` pour le groupe concerné — un désalignement cause une confusion visuelle même si la navigation JS (basée sur `getElementById`) continue de fonctionner.

19. ⚠️ TRAITEMENT DIVISÉ PAR CAUSE — MODÈLE OBLIGATOIRE À 3 ONGLETS (référence : sec-nephrotique / sec-nephritique) : Dès qu'un bloc traitement (`class="block rx"`) couvre plusieurs causes/étiologies distinctes d'une même pathologie (ex : syndrome néphrotique, syndrome néphritique), il DOIT être structuré en **3 onglets** avec une fonction JS de switch dédiée à CE bloc (jamais réutiliser une fonction générique d'un autre bloc — chaque bloc a ses propres IDs `[prefix]tab0/1/2` et `[prefix]p0/1/2`, ex. `switchNritTx()`/`nritp0-2` pour la néphrite, `switchSN()`/`snp0-2` pour le néphrotique) :

    (a) **Onglet 1 — Mesures générales** : cartes pastel (`display:flex;flex-wrap:wrap;gap:10px`) pour les mesures non-pharmacologiques, la néphroprotection universelle et la surveillance communes à toutes les causes.

    (b) **Onglet 2 — Par cause** : **UN SEUL tableau** (pas des pills par cause) avec colonnes obligatoires `Cause | 1re ligne / Induction | Résistance / Entretien | Cible / Suivi` — une ligne par cause/étiologie, avec teinte de fond distincte par ligne (`style="background:#[pastel];"`) pour faciliter le repérage visuel. Condenser le contenu de chaque cause (mécanisme, doses clés, molécules via `drug-badge`) sans perte d'information par rapport à l'ancien format en pills.

    (c) **Onglet 3 — Complications** : cartes pastel pour les complications spécifiques nécessitant une prise en charge active (ex : thromboembolie, infections, hyperlipidémie pour le néphrotique ; infections liées à l'IS, rechute, progression IRC pour le néphritique) — distinct des RED FLAGS diagnostiques qui restent dans leur propre bloc `block flag` séparé.

    Ne jamais garder l'ancien format "pills buttons + 1 panneau par cause" pour ce type de contenu — toujours migrer vers ce modèle à 3 onglets dès qu'une section de traitement par cause est créée ou révisée.

20. ⚠️ ÉCRAN D'ACCUEIL — AUDIT OBLIGATOIRE APRÈS TOUT AJOUT DE SECTION OU DE SPÉCIALITÉ : L'écran d'accueil (`id="sec-home"` > `div class="home-grid"`) doit refléter fidèlement le contenu réel du guide en tout temps. Cette règle complète la règle #11 (création de la home-card) : elle porte sur la **mise à jour et la cohérence** de l'ensemble des cartes.

    **Déclencheurs — exécuter l'audit dès qu'on :**
    (a) crée un nouveau groupe `grp-[nom]` (nouvelle spécialité),
    (b) ajoute, supprime, déplace ou fusionne une section dans un groupe existant,
    (c) renomme une spécialité ou change son icône.

    **Trois éléments à vérifier pour CHAQUE carte :**

    (a) **ICÔNE UNIQUE** — aucune icône emoji ne doit être utilisée par deux cartes. Vérifier aussi que la **palette de couleurs** (`background` + `color` du `home-card-icon`) n'est pas identique à celle d'une autre carte : deux cartes avec la même icône ET les mêmes couleurs sont visuellement indiscernables. Choisir une icône anatomiquement ou thématiquement évocatrice (🫀 cardio, 🫘 néphro, 🫁 pneumo, 🧠 neuro, 🧓 gériatrie, 🦴 MSK…).

    (b) **ICÔNE COHÉRENTE AVEC LE MENU LATÉRAL** — l'emoji de la `home-card-icon` doit être **identique** à celui du `<span class="emoji">` du `specialty-header` correspondant. Si l'on change l'un, changer l'autre simultanément.

    (c) **COMPTEUR EXACT** — le `home-card-count` doit correspondre au **nombre réel de `nav-item` du groupe**, et non à une valeur figée. Accorder le mot : « 1 section » au singulier, « N sections » au pluriel. Exception : les cartes dont le compteur exprime une autre unité (ex. « 105 questions », « Scores cliniques — MDCalc ») ne se comptent pas en sections — les laisser telles quelles.

    **Script de vérification obligatoire avant de conclure** — comparer les groupes réels aux cartes, et détecter les doublons d'icônes :

    ```python
    import re
    from collections import Counter
    c = open('index.html', encoding='utf-8').read()
    grps = [(m.start(), m.group(1)) for m in re.finditer(r'id="grp-([a-z0-9\-]+)"', c)]
    counts = {}
    for s, name in grps:
        j = c.find('</div>\n    </div>', s)
        counts[name] = len(re.findall(r"showSection\('([a-zA-Z0-9\-]+)'\)", c[s:j]))
    hg = c.find('class="home-grid"'); seg = c[hg:hg+16000]
    cards = re.findall(r'openGroup\(\'grp-([a-z0-9\-]+)\'\)"(.*?)home-card-icon" style="([^"]*)">([^<]*)<.*?home-card-name">(.*?)</div>\s*<div class="home-card-count">(.*?)</div>', seg, re.S)
    for grp, _, style, emo, name, cnt in cards:
        real = counts.get(grp); m = re.search(r'(\d+)', cnt)
        if 'section' in cnt and m and int(m.group(1)) != real:
            print('COMPTEUR ERRONÉ:', name, '->', cnt, 'mais', real)
    dups = [k for k, v in Counter(e for _, _, _, e, _, _ in cards).items() if v > 1]
    print('Icônes en double:', dups or 'aucune')
    print('Groupes sans carte:', [g for g in counts if g not in [x[0] for x in cards]])
    ```

    Les trois sorties doivent être vides. Un compteur périmé ou une icône dupliquée rend l'écran d'accueil trompeur — c'est la première chose que l'utilisateur voit.

21. ⚠️ RÉVISION MENSUELLE DES SOURCES — VÉRIFIER QUE LE GUIDE N'EST PAS PÉRIMÉ : Le contenu clinique se démode. Un guide qui affirme avec assurance une recommandation retirée est **plus dangereux qu'un guide incomplet**. Une révision des sources doit donc être faite **chaque mois**.

    **Le registre** : `references/SOURCES.md` liste les sources réellement citées dans `index.html`, la **version utilisée**, l'**URL de vérification** et les **sections touchées**. Il est classé par priorité : 🔴 haute (mensuel), 🟡 moyenne (trimestriel), 🟢 basse (annuel). **Toujours partir de ce fichier** — ne pas repartir de zéro.

    **Procédure (30 à 45 min) :**
    (a) Ouvrir `references/SOURCES.md` et traiter **toutes les lignes 🔴**, plus les 🟡 dont la dernière vérification remonte à plus de 3 mois.
    (b) Pour chaque source : consulter l'URL et comparer la **version en ligne** à la **version citée** dans le registre.
    (c) Si la version a changé : **lire ce qui a changé**, puis mettre à jour les sections listées dans la colonne « Sections touchées ». Corriger aussi la version dans le registre.
    (d) Vérifier les **sources en transition** — un organisme dissous, remplacé ou dont le mandat change (ex. GECSSP → CCNSPS) rend caduques les recommandations citées en son nom.
    (e) Consigner le passage dans le **Journal des vérifications** au bas du registre, même si rien n'a changé — l'absence de changement est une information.
    (f) Mettre à jour les deux dates en tête du registre (dernière / prochaine vérification).

    **Signaux qui déclenchent une révision hors calendrier** — ne pas attendre le mois suivant :
    • l'utilisateur signale qu'une recommandation ne correspond plus à sa pratique;
    • une recherche web incidente révèle une version plus récente d'un document cité;
    • un organisme annonce une refonte, une fusion ou une dissolution;
    • une pénurie de médicament modifie une conduite (ex. pénicilline G benzathine et syphilis).

    ⚠️ **Ce qui prime en cas de contradiction** : la hiérarchie de la règle #15 s'applique intégralement. Une source de **niveau 3 canadienne récente** l'emporte toujours sur un **manuel de niveau 2**, même récent. Exemple rencontré : un précis de pharmacologie affirmait que l'acétate d'ulipristal n'était pas disponible au Canada, alors que l'outil INSPQ 2024 le recommande en première intention dans plusieurs situations. **Quand un manuel et une source canadienne divergent, écrire la conduite canadienne et signaler explicitement l'écart dans le guide** — cela évite au lecteur de se fier à une note de cours périmée.

22. ⚠️ CRITÈRES DIAGNOSTIQUES — TOUJOURS CHIFFRÉS, JAMAIS QUALITATIFS : dès qu'un contenu présente des **critères diagnostiques nommés** (phénotype de Fried, critères de Beers, CAM, DSM-5-TR, scores de Wells, CSRS, Ottawa, ABCD², outil DDS, etc.), chaque critère doit être **opérationnalisé avec son seuil précis** — valeur chiffrée, unité, durée, dénominateur, et la population à laquelle il s'applique.

    **Ce qui est proscrit** : « perte de poids involontaire » sans le seuil (≥ 4,5 kg ou ≥ 5 % en un an) · « ralentissement de la marche » sans la distance ni le repère (4,57 m, quintile inférieur par sexe et taille) · « raideur matinale prolongée » sans les minutes (> 30-60 min) · « fièvre » sans la température · « insuffisance rénale » sans le DFG. Un critère qualitatif n'est pas un critère : il est inapplicable et donne une fausse impression de rigueur.

    **Méthode obligatoire, dans cet ordre :**
    (a) chercher le seuil dans les sources de niveau 1 et 2 (`search_refs.py` sur les 10 manuels indexés + les documents Notion);
    (b) si absent, chercher une source canadienne de niveau 3;
    (c) si toujours absent et que le seuil vient de l'**article princeps ou des connaissances internes**, l'écrire quand même — un critère sans seuil est inutilisable — **mais avec un encadré `key-fact orange` en tête de la grille** qui nomme la source exacte (auteurs, revue, année) et précise qu'aucun manuel de l'utilisateur ne la reproduit;
    (d) quand un critère exige un **instrument ou des tables de normes** non disponibles en consultation (dynamomètre, quintiles par sexe/IMC), le dire explicitement et **orienter vers l'outil clinique équivalent** (ex. Fried → PRISMA-7, CFS).

    **Vérification** : après avoir écrit une grille de critères, relire chaque ligne en se demandant « **est-ce que je pourrais cocher ce critère au chevet, seul, sans rien demander à personne ?** ». Si la réponse est non, il manque un chiffre.

23. ⚠️ COMPARER PLUSIEURS ENTITÉS — MODÈLE OBLIGATOIRE « ONGLETS PAR ENTITÉ + ONGLET COMPARER » (référence : `tnc-3` Les grands types de TNC, et `tnc-5` Outils d'évaluation cognitive) : dès qu'un bloc doit présenter **3 entités parallèles ou plus** — types d'une maladie, outils, classes de médicaments, examens, échelles, stades — **ne jamais empiler un grand tableau à N colonnes**. Un tableau large oblige à défiler horizontalement, écrase le texte dans des cellules illisibles, et la comparaison s'y perd. Utiliser le modèle suivant, sans exception.

    **(a) La structure — `showPanel` avec un panneau de plus que d'entités.**
    Préfixe unique, IDs numériques `prefixe0` à `prefixeN` (règle #7). Le **panneau 0 est toujours l'onglet `⚖️ Comparer`**, affiché par défaut (`display:block`) ; les autres sont masqués (`display:none`). Le premier bouton porte la couleur active, les autres `background:#e0e0e0;color:#333`. Ajouter le préfixe et sa couleur au `colorMap` de `showPanel()`. Style rectangulaire obligatoire (règle #17).

    **(b) L'onglet ⚖️ Comparer — court, et seulement les axes qui discriminent.**
    Un tableau où les **lignes sont les axes** et les **colonnes les entités**, avec des cellules de **quelques mots seulement** — jamais de phrases. Maximum **6 à 8 lignes** : au-delà, ce n'est plus une vue d'ensemble. Choisir les axes qui *séparent* les entités, pas ceux qui les décrivent. En-têtes de colonnes teintés de la couleur de chaque entité, `min-width` + `overflow-x:auto`. Terminer par une `key-fact ink` qui dit **comment lire le tableau** et **quelle question se poser** (« ce n'est pas *lequel est le meilleur* mais *qu'est-ce qui me contraint aujourd'hui* »).

    **(c) Un panneau par entité, tous bâtis exactement pareil.**
    C'est ce parallélisme qui permet de passer d'un onglet à l'autre et de retrouver l'information au même endroit. Squelette imposé :
    ① **Bandeau d'en-tête** — `background:[pastel];border-left:5px solid [encre]` avec le nom, un sous-titre d'une ligne, et **la synthèse en une phrase** (pour une maladie : la chaîne `facteur de risque → lésion → premier symptôme` ; pour un outil : à quoi il sert en une ligne).
    ② **Sous-titres de section** — `font-size:12px;font-weight:800;color:[encre];letter-spacing:.4px` avec emoji, dans le même ordre pour toutes les entités.
    ③ **Grilles de cartes pastel** (règle #16a) pour les blocs à 2-3 volets parallèles.
    ④ **Un tableau à 2 colonnes** `Axe | Ce qu'on observe` pour le tableau clinique ou la description détaillée.
    ⑤ **`criteria-list` numérotée** pour tout ce qui est séquentiel ou chiffré — critères diagnostiques, étapes d'administration, items d'un questionnaire — en terminant par un `criteria-num red` « ! » portant la **règle de décision chiffrée** (règle #22).
    ⑥ **`key-fact` finale** avec la conduite, les doses, ou le « quand le choisir ».

    **(d) Ce qui suit les onglets.** Une seule `key-fact` de synthèse portant les **messages transversaux** — ceux qui ne rentrent dans aucune colonne. Tout le reste doit être *dans* un panneau : ne jamais laisser d'encadré isolé sous les onglets qui répéterait un contenu déjà réparti (règle #8).

    **(e) Vérification obligatoire avant de conclure** — les six sorties doivent être conformes :
    ```python
    import re
    c = open('index.html', encoding='utf-8').read()
    i = c.find('id="<id-du-bloc>"'); j = c.find('<div class="block', i); seg = c[i:j]
    pan = sorted(re.findall(r'id="(<prefixe>\d+)"', seg))
    bou = sorted(re.findall(r'data-panel="(<prefixe>\d+)"', seg))
    print(pan == bou)                                                   # IDs et boutons concordants
    print(set(re.findall(r"showPanel\('<prefixe>','<prefixe>\d+',(\d+)\)", seg)))  # un seul count, = len(pan)
    print(seg.count('style="display:block'), len(re.findall(r'style="display:none', seg)))  # 1 et N-1
    print("'<prefixe>':'#" in c)                                        # couleur au colorMap
    print(seg.count('border-radius:8px;padding:8px 18px;font-weight:600'))  # = nb de boutons (règle #17)
    print('border-radius:20px' not in seg)                              # aucun badge arrondi
    ```
    Puis **test fonctionnel jsdom** : cliquer chaque onglet et vérifier qu'un seul panneau est visible à la fois, que le bouton actif prend la couleur du `colorMap`, et qu'**aucun autre système de pills du guide n'est affecté** (collision de préfixe — `showPanel` filtre par `startsWith`).

    **Quand ce modèle ne s'applique pas** : moins de 3 entités, ou une comparaison qui tient en 3 colonnes courtes — dans ce cas un tableau simple (règle #16b) suffit et vaut mieux qu'une mécanique d'onglets inutile.

24. ⚠️ TOUTE MISE À JOUR COMMENCE PAR UNE RECHERCHE DE DOUBLON — ON FUSIONNE, ON N'AJOUTE PAS À CÔTÉ : quand on intègre un nouveau document (notes de cours, article, PDF d'APP) dans une section qui existe déjà, le réflexe naturel est de créer un nouvel encadré à la fin. **C'est interdit.** Le résultat observé après plusieurs ajouts : deux encadrés sur le même sujet, à deux endroits, avec des chiffres qui se contredisent, et l'un qui renvoie à l'autre par « voir le bloc ci-dessus ». C'est la principale cause de dégradation du guide. Cette règle précise et rend obligatoire la règle #8.

    **(a) L'audit AVANT d'écrire une seule ligne.** Lister les encadrés de la section visée avec leur titre, leur pastille d'objectif et leur taille, puis confronter le plan du nouveau document à cette liste, sujet par sujet. Deux signaux de doublon :
    ```python
    import re, itertools, unicodedata
    c = open('index.html', encoding='utf-8').read()
    a = c.find('<div class="section" id="sec-<nom>"'); b = c.find('<div class="section" id=', a+10); seg = c[a:b]
    # (1) les titres et pastilles : deux encadrés sur le même objectif sont suspects par défaut
    for m in re.finditer(r'block-title" id="([^"]+)"><span class="tag">(.*?)</span>(?:<span class="obj-badge">([^<]*)</span>)?', seg, re.S):
        print(m.group(1), '|', m.group(3), '|', re.sub(r'<[^>]+>', '', m.group(2))[:60])
    # (2) les mots-clés du nouveau document déjà présents dans la section
    for k in ['<terme1>', '<terme2>']:
        print(k, 'DÉJÀ PRÉSENT' if k in seg else 'absent')
    ```
    Un renvoi « ➜ voir le bloc … ci-dessus » entre deux encadrés de la même section est l'aveu d'un doublon : c'est un candidat à la fusion, pas une navigation.

    **(b) Trois issues possibles, dans cet ordre de préférence.**
    ① **Enrichir l'encadré existant** — le nouveau matériel entre dans la carte, la ligne de tableau ou la `criteria-list` qui traite déjà le sujet. C'est le cas le plus fréquent et il ne crée aucun encadré.
    ② **Fusionner deux encadrés** en un seul quand les deux existent déjà (procédé en (c)).
    ③ **Créer un nouvel encadré** — seulement si le sujet est vraiment absent. Alors appliquer les règles #13 (bouton `goToBlock`) et #14 (ordre).

    **(c) Le procédé de fusion sans perte** — outillé dans `outils/fusion_lib.py`, à réutiliser :
    ① découper chaque encadré d'origine en morceaux (`keyfact`, `tableau`, `grille`, `criteres`, sections délimitées par les sous-titres) ; ② les remonter dans **un ordre unique et logique**, jamais « bloc A puis bloc B » bout à bout — c'est le même doublon, dans un seul encadré ; ③ **ne rien réécrire** : on déplace le HTML existant, ce qui garantit l'intégrité du contenu ; ④ le seul texte réécrit est le **chapeau** (les deux chapeaux d'origine fusionnent en un) et les **renvois devenus faux** ; ⑤ supprimer les boutons de navigation orphelins et relibeller celui qui reste.

    **(d) La preuve de non-perte est obligatoire.** Comparer le multiensemble des mots visibles avant et après : la sortie doit être vide, à l'exception des mots des chapeaux réécrits, qui doivent être listés explicitement.
    ```python
    manque = F.controle(corps_avant, corps_apres, tolere=['<mots du chapeau réécrit>'])
    assert not manque, manque   # « contenu perdu : rien »
    ```
    Puis la suite habituelle : balises équilibrées, IDs uniques, profondeur des encadrés = 1, `nav == ordre des blocs`, aucun bouton mort, aucun renvoi vers un id supprimé, et test jsdom.

    **(e) Quand les deux sources se contredisent, on ne choisit pas en silence.** Deux encadrés fusionnés portent parfois deux chiffres différents pour la même chose (vu : ferritine < 12 ou < 30 µg/L · albumine marqueur nutritionnel ou non · 20-25 ou 25-35 kcal/kg/j · rendement plaquettaire ≥ 5-10 ou +15-25 × 10⁹/L). La fusion **conserve les deux**, nomme les deux sources, et ajoute une `key-fact orange` ou `green` qui dit **ce qui tranche** (la hiérarchie de la règle #15, ou un critère clinique comme la CRP > 20 mg/L). Écraser un chiffre pour faire disparaître la contradiction est une perte d'information déguisée en ménage.

La première étape du document est faite avec la structure et l'insertion des thèmes + information de base. 
2e étape: il faut que je mette plus d'informations dans chaque encadrés parce que l'information est maigre. Voici le plan:
J'ai une base de données notion avec plusieurs texte incluant beaucoup d'informations sur les différents sujets. Ta tâche, en excluant la spécialité petit guide, est de créer un document HTLM interactif pour chaque page présente. Assure toi que le thème est similaire à celui-ci du guide que tu es en train de créer. Une fois que tu as créer un fichier HTLM, tu peux le fusionner avec le guide que tu es en train de créer. Le guide doit être concis, mais assez détaillé puisque je vais l'utiliser dans ma pratique clinique en tant qu'IPS.Puisque tu as déjà commencer le guide, si un thème existe déjà, rajoute de l'information pour arriver à avoir une page bien remplie. Si une section n'existe pas, ajoute là dans les grandes catégories (ex: cardio, pneumo., etc.). Si tu penses qu'une nouvelle grande section devrait être crée, ajoute en une. Assure toi de ne pas avoir de doublon, si c'est le cas, fusionne les informations dans une section.