#!/bin/bash
# push.sh — Auto-push du guide clinique IPS vers GitHub
# Appeler depuis : /Users/emile/Claude/Projects/Guide d'étude HTML/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ⚠️ extraire UNIQUEMENT la ligne du compte — un `cat` colle tout le fichier
# (commentaires + les deux jetons) dans l'URL du remote. Bug corrigé le 2026-09-03.
TOKEN=$(grep "^emilefavron2-star=" .github_token 2>/dev/null | cut -d= -f2)
if [ -z "$TOKEN" ]; then
  echo "❌ Token introuvable dans .github_token"
  exit 1
fi

REPO_URL="https://emilefavron2-star:${TOKEN}@github.com/emilefavron2-star/Guide-Eude-IPS.git"
APP_URL="https://emilefavron2-star:${TOKEN}@github.com/emilefavron2-star/Guide-clinique-IPS-Application.git"

# Init git si pas encore fait
if [ ! -d ".git" ]; then
  echo "🔧 Initialisation du repo git..."
  git init
  git remote add origin "$REPO_URL"
  echo "✅ Repo initialisé"
else
  # Mettre à jour l'URL avec le token (en cas de rotation)
  git remote set-url origin "$REPO_URL"
fi

# Commit et push
TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
git add index.html
git diff --cached --quiet && echo "Aucun changement à pousser." && exit 0

git commit -m "Mise à jour guide — $TIMESTAMP"
git push -u origin main 2>/dev/null || git push -u origin master 2>/dev/null

echo "✅ Guide pushé sur GitHub ($TIMESTAMP)"
