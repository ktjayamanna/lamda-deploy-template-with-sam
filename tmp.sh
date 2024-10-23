#!/bin/bash

# Define the old and new names
OLD_NAME="download_counter_update"
NEW_NAME="src"

# Rename the directory
mv "$OLD_NAME" "$NEW_NAME"

# Update references in all files that may contain the old name
sed -i "s/$OLD_NAME/$NEW_NAME/g" README.md template.yaml samconfig.toml tests/unit/test_handler.py

# Inform the user that the process is complete
echo "Renamed '$OLD_NAME' to '$NEW_NAME' and updated references in relevant files."
