#!/bin/bash
set -e

echo "Executant META-F4_D4 automàticament..." | tee cycle_log.txt

pip install --no-cache-dir -r requirements.txt 2>&1 | tee -a cycle_log.txt

python3 main.py 2>&1 | tee -a cycle_log.txt
