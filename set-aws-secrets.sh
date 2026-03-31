# This script uses the GitHub CLI to set AWS secrets for your repository.
# Prerequisites:
# - Install GitHub CLI: https://cli.github.com/
# - Authenticate with: gh auth login
# - Replace <OWNER>/<REPO> with your repo (e.g., vickysmalls/secdevops-pipeline)
# - Replace the placeholder values with your actual AWS keys

REPO="vickysmalls/secdevops-pipeline"

# Set AWS_ACCESS_KEY_ID
read -sp "Enter your AWS_ACCESS_KEY_ID: " AWS_ACCESS_KEY_ID
echo

gh secret set AWS_ACCESS_KEY_ID --body "$AWS_ACCESS_KEY_ID" --repo "$REPO"

echo "AWS_ACCESS_KEY_ID set."

# Set AWS_SECRET_ACCESS_KEY
read -sp "Enter your AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY
echo

gh secret set AWS_SECRET_ACCESS_KEY --body "$AWS_SECRET_ACCESS_KEY" --repo "$REPO"

echo "AWS_SECRET_ACCESS_KEY set."

echo "Both AWS secrets have been set for $REPO."
