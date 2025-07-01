#!/bin/bash
set -euo pipefail

SRC_FILE=${1:-code.py}
DEVICE=$(lsblk -o NAME,LABEL -rn | grep CIRCUITPY | awk '{print "/dev/" $1}')
MOUNT_POINT="/mnt"

echo "Unmounting (in case still mounted)..."
sudo umount "$DEVICE" 2>/dev/null || true
sleep 0.5

echo "Mounting..."
sudo mount "$DEVICE" "$MOUNT_POINT"

echo "Copying code.py..."
sudo cp "$SRC_FILE" "$MOUNT_POINT"/code.py
sync

echo "Waiting briefly before unmount..."
sleep 0.5

echo "Unmounting..."
sudo umount "$MOUNT_POINT"

echo "Done."

