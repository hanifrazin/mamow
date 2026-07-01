#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
WRAPPER="$PROJECT_ROOT/src/executable_scripts/markrow"

chmod +x "$WRAPPER"

echo "Installing Hardcoded Launcher to /usr/local/bin/markrow..."
sudo tee /usr/local/bin/markrow > /dev/null <<EOF
#!/usr/bin/env bash
# Hardcoded launcher to prevent symlink venv resolution errors
exec "$WRAPPER" "\$@"
EOF

sudo chmod +x /usr/local/bin/markrow

echo "Installation complete! You can now use the 'markrow' command globally."
