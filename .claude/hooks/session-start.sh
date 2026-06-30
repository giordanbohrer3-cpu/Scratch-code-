#!/bin/bash
# Prepara o ambiente de desenvolvimento antes do Claude Code iniciar.
set -euo pipefail

# Só roda em sessões remotas (Claude Code on the web)
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

echo "==> Verificando ferramentas de desenvolvimento"

install_apt_pkg() {
  local pkg="$1"
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq && apt-get install -y -qq "$pkg" >/dev/null
  fi
}

check_tool() {
  local label="$1" cmd="$2" version_flag="$3" apt_pkg="${4:-}"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "  ok $label: $("$cmd" "$version_flag" 2>&1 | head -1)"
  elif [ -n "$apt_pkg" ]; then
    echo "  .. $label nao encontrado, instalando ($apt_pkg)"
    install_apt_pkg "$apt_pkg" || echo "  !! falha ao instalar $label"
  else
    echo "  !! $label nao encontrado"
  fi
}

check_tool "Node.js" node --version
check_tool "npm" npm --version
check_tool "Python" python3 --version
check_tool "pip" pip3 --version python3-pip
check_tool "Git" git --version
check_tool "zip" zip -v zip
check_tool "unzip" unzip -v unzip

echo "==> Garantindo estrutura de pastas para novos projetos/jogos"
mkdir -p "$PROJECT_DIR/projects" "$PROJECT_DIR/games" "$PROJECT_DIR/assets"
touch "$PROJECT_DIR/projects/.gitkeep" "$PROJECT_DIR/games/.gitkeep" "$PROJECT_DIR/assets/.gitkeep"

echo "==> Configurando variaveis de ambiente da sessao"
{
  echo "export PROJECTS_DIR=\"$PROJECT_DIR/projects\""
  echo "export GAMES_DIR=\"$PROJECT_DIR/games\""
  echo "export ASSETS_DIR=\"$PROJECT_DIR/assets\""
  echo "export NODE_ENV=development"
  echo "export PYTHONDONTWRITEBYTECODE=1"
  echo "export PIP_DISABLE_PIP_VERSION_CHECK=1"
  echo "export NPM_CONFIG_FUND=false"
  echo "export NPM_CONFIG_AUDIT=false"
} >> "$CLAUDE_ENV_FILE"

echo "==> Ambiente pronto para desenvolvimento"
