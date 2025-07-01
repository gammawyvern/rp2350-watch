#!/bin/bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 /dev/sdX path/to/files"
    exit 1
fi

DEVICE="$1"
SRC_DIR="$2"
MOUNT_POINT="/mnt"

if [[ ! -b "$DEVICE" ]]; then
    echo "Error: '$DEVICE' is not a block device."
    exit 1
fi

if [[ ! -d "$SRC_DIR" ]]; then
    echo "Error: '$SRC_DIR' is not a directory."
    exit 1
fi

echo "Unmounting $DEVICE (if mounted)..."
sudo umount "$DEVICE" 2>/dev/null || true
sleep 0.5

echo "Mounting $DEVICE to $MOUNT_POINT..."
sudo mount "$DEVICE" "$MOUNT_POINT"

echo "Copying from '$SRC_DIR' to '$MOUNT_POINT'..."
sudo cp -r "$SRC_DIR"/* "$MOUNT_POINT/"
sync

echo "Unmounting $MOUNT_POINT..."
sleep 0.5
sudo umount "$MOUNT_POINT"

echo -e "\033[1;32mDone.\033[0m"

