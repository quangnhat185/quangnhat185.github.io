python pdf_to_image.py

printf "UPDATING FILE TO GIT REPO..."
printf "\n"

dt=$(date '+%H:%M %d_%m_%Y')
comment="Update on ${dt}"
printf "$comment\n"

git add . && git commit -m "${comment}" && git push origin master
printf "\nUPDATE SUCCESSFULLY!!!"
