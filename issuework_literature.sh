proj_name=$(echo "${PWD##*/}")

echo "MANUAL STEPS REQUIRED!!"
echo "after opening Zotero:"
echo "---------------------"
echo "(1) If there is a collection called ${proj_name}:"
echo "    right-click on this collection and select: Delete Collection"
echo "(2) Press CTRL-SHIFT-I"
echo "    then import from docs/literature/${proj_name}.bib"
echo "(3) right-click on ${proj_name} and select: Export Collection..."
echo "    select Format: Better BibTex"
echo "    check: [x] Keep updated (!!!)"
echo "(4) when done, return to this window and press Enter"
echo "---------------------"
read -p "Press enter to open Zotero and start with these manual steps..."

"C:/Program Files (x86)/Zotero/zotero.exe" &

read -p "Press enter when you completed the manual steps above..."
clear