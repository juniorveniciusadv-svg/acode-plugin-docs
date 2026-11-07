#!/data/data/com.termux/files/usr/bin/bash
# Instalador do ambiente jurídico no Termux (Android).
# Debian via proot-distro + Python, Pandas e Requests já compilados.
set -u

RAW="https://raw.githubusercontent.com/juniorveniciusadv-svg/acode-plugin-docs/ccr-3b8c9989-psikde/juridico"
PROJETO="$HOME/projetos/jurimetria"

echo "==> 1/5 Instalando o proot-distro"
pkg install -y proot-distro || { echo "❌ Falha no pkg install"; exit 1; }

echo "==> 2/5 Instalando o Debian (download de ~100 MB)"
if proot-distro login debian -- true 2>/dev/null; then
  echo "   Debian já instalado, seguindo."
else
  proot-distro install debian || { echo "❌ Falha ao instalar o Debian"; exit 1; }
fi

echo "==> 3/5 Instalando Python, Pandas e Requests (pré-compilados)"
proot-distro login debian -- bash -c \
  "export DEBIAN_FRONTEND=noninteractive; apt-get update && apt-get install -y python3 python3-pandas python3-requests" \
  || { echo "❌ Falha no apt-get"; exit 1; }

echo "==> 4/5 Baixando o script do DataJud para $PROJETO"
mkdir -p "$PROJETO"
curl -fsSL "$RAW/datajud.py" -o "$PROJETO/datajud.py" || echo "⚠️ Não consegui baixar o datajud.py"

echo "==> 5/5 Criando os atalhos 'juridico' e 'datajud'"
grep -q "alias juridico=" ~/.bashrc 2>/dev/null || \
  echo "alias juridico='proot-distro login debian --termux-home'" >> ~/.bashrc
grep -q "alias datajud=" ~/.bashrc 2>/dev/null || \
  echo "alias datajud='proot-distro login debian --termux-home -- python3 $PROJETO/datajud.py'" >> ~/.bashrc

echo ""
if proot-distro login debian -- python3 -c "import pandas, requests; print('Pandas', pandas.__version__, '| Requests', requests.__version__)"; then
  echo ""
  echo "✅ TUDO PRONTO."
  echo "   Feche e reabra o Termux. Depois digite:"
  echo "     datajud    -> consulta um processo no DataJud"
  echo "     juridico   -> entra no Debian (Python com Pandas)"
else
  echo "❌ Algo falhou. Envie as últimas 30 linhas."
fi
