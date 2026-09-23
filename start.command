#!/usr/bin/env bash
# HANDTONE desktop launcher — double-click this file to run
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Make sure the venv exists
if [ ! -f "$DIR/venv/bin/python" ]; then
    echo "Installing dependencies..."
    python3 -m venv "$DIR/venv"
    "$DIR/venv/bin/pip" install --quiet pywebview
fi

# Launch the desktop app
exec "$DIR/venv/bin/python" "$DIR/desktop.py"