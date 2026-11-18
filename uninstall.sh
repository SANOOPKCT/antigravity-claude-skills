#!/usr/bin/env bash
# Antigravity Claude Skills Pack - Uninstaller

set -euo pipefail

PLUGIN_NAME="antigravity-claude-skills"
TARGET_DIR="${HOME}/.gemini/config/plugins/${PLUGIN_NAME}"

if [ -e "${TARGET_DIR}" ]; then
  echo "🗑️ Removing Antigravity Claude Skills Pack from ${TARGET_DIR}..."
  rm -rf "${TARGET_DIR}"
  echo "✅ Successfully uninstalled."
else
  echo "ℹ️ Plugin was not found in ${TARGET_DIR}."
fi
