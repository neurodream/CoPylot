. ~/.bashrc

branch_name=$(git rev-parse --abbrev-ref HEAD)

# if main: needs to start with new issue

if [ $branch_name == "main" ]
then
    source scripts/shell/issuework_begin.sh
else
    echo "You are currently on an issue branch,"
    echo "meaning you have local unpushed changes."
    echo "It is RECOMMENDED to finish this issue before starting a new one"
    echo "    to avoid pull request chaos."
    echo "Do you want to continue working on this issue?"
    read -p " [Y/n]" continue_yn
    if [ $continue_yn == "n" ]
    then
        echo "WARNING: pull request chaos imminent."
        echo "IMPORTANT TO FINISH ISSUES YOU ARE IN MIDDLE OF FIXING ASAP."
        source scripts/shell/issuework_begin.sh
    else
        echo "you are now continuing to work on ${branch_name}. happy coding :)"
    fi
    source scripts/shell/issuework_setup_env.sh
fi

# $SHELL
read