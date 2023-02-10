. ~/.bashrc

branch_name=$(git rev-parse --abbrev-ref HEAD)
issue_id=$(echo "$branch_name" | cut -d'_' -f2)
remote_url=$(git config --get remote.origin.url)
user_name=$(git config user.name)
env_name=$(head -n 1 environment.yml | sed "s/name: //")

# issue title is the commit message
commit_msg=$(gh issue view $issue_id --json title --jq '.title')

# capture all new packages installed while working on issue (if any)
# TODO somehow check for errors (save to output var?)
conda activate $env_name # in case closed in the meantime
conda env export > environment.yml
git add .
git commit -m "$commit_msg"
git push origin $branch_name

gh pr create -b "closes #${issue_id}" -a $user_name -t $branch_name --repo $remote_url
git branch -m "PULL_REQUESTED_issue_${issue_id}"
git checkout main
clear