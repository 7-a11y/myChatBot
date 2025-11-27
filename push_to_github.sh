#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Usage: ./push_to_github.sh \"Your commit message\""
  echo "Using default commit message: 'Update'"
  COMMIT_MSG="Update"
else
  COMMIT_MSG="$1"
fi

# Add all changes
echo "Adding changes..."
git add .

# Commit changes
echo "Committing changes with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# Push changes
echo "Pushing to GitHub..."
git push

echo "Done!"
