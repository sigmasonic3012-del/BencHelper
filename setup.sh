#!/data/data/com.termux/files/usr/bin/bash

echo "Installing dependencies for Android-Sys-Bench..."
pkg update -y && pkg upgrade -y
pkg install python -y

echo "-------------------------------------------"
echo "Installation Complete! Starting Benchmark..."
echo "-------------------------------------------"

python benchmark.py
