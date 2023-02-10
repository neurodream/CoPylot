. ~/.bashrc

branch_name=$(git rev-parse --abbrev-ref HEAD)

# if main: needs to start with new issue

if [ $branch_name == "main" ]
then
    source scripts/shell/issuework_begin.sh
else
    echo "You are currently on an issue branch,"
    echo "meaning you have local unpushed changes."
    read -p "Do you want to continue working on this issue and finish it (recommended)? [Y/n]" continue_yn
    if [ $continue_yn == "n" ]
    then
        echo "WARNING: Please try to finish an issue before working on another one,"
        echo "in order to prevent pull chaos."
        source scripts/shell/issuework_begin.sh
    fi
    source scripts/shell/issuework_setup_env.sh
fi

# $SHELL
read