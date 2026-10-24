#!/usr/bin/env bash
# Automatically stages, commits, and pushes updates to GitHub
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

git status --short
if [ -z "$(git status --porcelain)" ]; then
    echo "Everything is already clean and in sync with GitHub."
    exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
git add .
git commit -m "Sync FoVL coursework updates: ${TIMESTAMP}"
git push origin main

echo "Successfully synchronized with GitHub (origin/main) at ${TIMESTAMP}."
