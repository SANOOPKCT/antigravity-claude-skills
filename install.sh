#!/usr/bin/env bash
# Antigravity Claude Skills Pack - Global Installer
# Compatible with Linux & macOS

set -euo pipefail

PLUGIN_NAME="antigravity-claude-skills"
GLOBAL_PLUGINS_DIR="${HOME}/.gemini/config/plugins"
TARGET_DIR="${GLOBAL_PLUGINS_DIR}/${PLUGIN_NAME}"

# Determine directory where install.sh lives
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Installing Antigravity Claude Skills Pack (67 Skills)..."
echo "📂 Target destination: ${TARGET_DIR}"

mkdir -p "${GLOBAL_PLUGINS_DIR}"

# Check if target already exists
if [ -d "${TARGET_DIR}" ] || [ -L "${TARGET_DIR}" ]; then
  echo "⚠️  Existing installation detected. Creating backup..."
  mv "${TARGET_DIR}" "${TARGET_DIR}.backup-$(date +%s)"
fi

# Link or copy
if [ -d "${SCRIPT_DIR}/skills" ] && [ -f "${SCRIPT_DIR}/plugin.json" ]; then
  echo "🔗 Linking local repository to global plugins directory..."
  ln -sfn "${SCRIPT_DIR}" "${TARGET_DIR}"
else
  # If executed via curl pipeline directly from github
  echo "📥 Cloning from GitHub repository..."
  git clone https://github.com/YOUR_USERNAME/antigravity-claude-skills.git "${TARGET_DIR}"
fi

echo "✨ Installation complete! 67 skills are now globally registered in Antigravity."
echo "💡 You can now trigger skills using / or by describing what you need in your prompts."
