import os
import re
import requests
import unidecode
from tqdm import tqdm

language = "German"
levels = ["C1.4"]

baseURL = "https://www.lingoda.com/german/learning-material/cefr"

failed_downloads = []

for level in levels:
    file = os.path.join("pages", level + ".html")

    with open(file, 'r', encoding='UTF-8') as f:
        html_string = f.read()

    # Get the names of the lessons
    names_types = re.findall(r'body1 MuiTypography-displayBlock">(.+?)</span>.+?">(.+?)</div', html_string)

    names = [n for (n, t) in names_types]
    types = [t for (n, t) in names_types]

    newnames = []
    names_save= []

    for name in names:
        newname = unidecode.unidecode(str.lower(name))
        newname = newname.replace("-", " ").replace("   ", " ").replace("  ", " ")
        newname = newname.replace(' ', '-')
        newname = re.sub("[!¡@#$?¿':,]", '', newname)
        newnames.append(newname)
        names_save.append(re.sub("[/?\:]()", '', name))

    save_folder = os.path.join(language, level)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    for i, newname in enumerate(tqdm(newnames)):

        url = f"{baseURL}/{level}/{newname}/download"
        response = requests.get(url)
    
        # Start of a PDF file
        # b '%PDF-1.5\r\n%\xb5\xb5\xb5\xb5\r\n1 0 obj\r\n<</'

        # Start of a non-pdf file, but html "Not found page"
        # b'<!DOCTYPE html>\n<!--[if IE 9]>\n<html lang...'

        if not str(response.content[0:10]).startswith("b'%PDF"):
            #print(f"Failed: {i+1}. {names[i]}")
            failed_downloads.append((level, i+1, newname, url))

        else: 
            with open(os.path.join(save_folder, f"{i+1}. ({types[i]}) {names_save[i]}.pdf"), 'wb') as f:
                f.write(response.content)

print("Failed downloads")
[print(l,i,n, u) for l,i,n,u in failed_downloads]