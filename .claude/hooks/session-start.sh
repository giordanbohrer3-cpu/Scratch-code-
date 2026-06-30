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

echo "==> Carregando variaveis de ambiente (.env)"
ENV_FILE="$PROJECT_DIR/.env"
if [ -f "$ENV_FILE" ]; then
  while IFS='=' read -r key value; do
    # ignora linhas em branco e comentarios
    [ -z "$key" ] && continue
    case "$key" in \#*) continue ;; esac
    # resolve caminhos relativos (./pasta) para absolutos dentro do projeto
    case "$value" in
      ./*) value="$PROJECT_DIR/${value#./}" ;;
    esac
    echo "export $key=\"$value\"" >> "$CLAUDE_ENV_FILE"
  done < "$ENV_FILE"
else
  echo "  !! .env nao encontrado em $ENV_FILE"
fi

echo "==> Ambiente pronto para desenvolvimento"
