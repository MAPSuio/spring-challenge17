#!/usr/bin/env sh

# Usage: ./torenord.sh < data.txt

awk '{ print length, $0 }' | sort -n | cut -d" " -f2- | head -10000 | tail -1
