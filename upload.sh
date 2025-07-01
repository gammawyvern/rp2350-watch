#!/bin/bash
set -euo pipefail

sudo mount /dev/sda1 /mnt
sudo cp ./code.py /mnt/code.py
sudo umount /dev/sda1 /mnt

