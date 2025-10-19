#!/bin/bash

# Read the commit message from stdin
MSG=$(cat)

# Process the first line: lowercase, truncate to 40 chars, remove #1
FIRST_LINE=$(echo "$MSG" | head -1 | tr '[:upper:]' '[:lower:]' | cut -c1-40 | sed 's/#1//g')

# Output the new message
echo "$FIRST_LINE"
echo "$MSG" | tail -n +2