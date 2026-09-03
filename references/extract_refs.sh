#!/bin/bash
# Ré-extrait le texte des ouvrages de référence vers /tmp.
# À relancer au début d'une session si search_refs.py dit « Texte absent ».
# Les PDF sources restent dans le dossier uploads de la session.

U="/sessions/focused-admiring-hawking/mnt/uploads"

extract () {  # $1 = nom cible, $2 = fichier PDF
  if [ -f "$U/$2" ]; then
    if [ -f "/tmp/$1.txt" ]; then
      echo "  = /tmp/$1.txt déjà présent"
    else
      pdftotext -layout "$U/$2" "/tmp/$1.txt" 2>/dev/null
      echo "  + /tmp/$1.txt"
    fi
  else
    echo "  ! PDF introuvable : $2"
  fi
}

echo "Extraction des ouvrages de référence…"
extract copstead       "COPSTEAD - Pathophysiology.pdf"
extract goldman        "Goldman-Cecil Medicine 26th - Lee Goldman, Andrew I. Schafer(2020).pdf"
extract gphc_entrevue  "GPHC (2016) - Petit guide de l'entrevue médicale 3.pdf"
extract gphc_habiletes "GPHC (2018) - Petit guide des habiletés cliniques 3.pdf"
extract lilly          "LILLY (6e édition, 2015) - Pathophysiology of Heart Disease (2) (1).pdf"
extract demarche       "801596881-De-marche-clinique.pdf"
extract beaulieu       "BEAULIEU - Précis de pharmacologie.pdf"
extract querin        "L'essentiel sur la néphrologie et l'urologie (Serge Quérin et Luc Valiquette (1).pdf"
extract cardiomedik   "David Laflamme - Cardiomedik_ A Cardiology Handbook-CRC Press_frison-roche _ Boca Raton (2016).pdf"
extract rej           "REJ_2023-2024.pdf"
echo "Terminé."
