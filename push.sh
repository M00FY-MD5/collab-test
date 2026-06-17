#!/bin/bash
cd /home/administrator/shared-code
git add -A
git commit -m "update $(date +%H:%M)" 2>/dev/null
git push origin main 2>&1
