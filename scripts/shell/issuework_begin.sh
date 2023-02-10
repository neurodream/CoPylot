. ~/.bashrc

remote_url=$(git config --get remote.origin.url)
env_name=$(head -n 1 environment.yml | sed "s/name: //")

gh issue list --repo $remote_url
echo "Enter issue ID (WITHOUT the hashtag #): "
read -p "" issue_ID
echo ""

# make sure you're on branch "main" (otherwise danger of merge conflicts/overwriting):
git checkout main # should not be needed anymore

# pull current state:
echo ""
echo "[COMPUTING] move to most recent state of main branch (in case other people pushed to main in meantime)"
git pull

# create a new branch (checkout) with the issue number:
git checkout -b "issue_$issue_ID"

echo ""
echo "[COMPUTING] setup the packages from environment"
# update environment of packages
# conda update -n base -c defaults conda # TODO leads to problems apparently
conda env update "$env_name" --file environment.yml --prune
source scripts/shell/issuework_setup_env.sh