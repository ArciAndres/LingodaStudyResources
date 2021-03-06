import os
import re
import requests
import unidecode
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('language', type=str, default="german", help="Language to process. It shuold be the name of the folder in 'webpages'")
parser.add_argument('levels', nargs='+', help='List of levels to process (separated by space)',  
default=["A1.2", "A2.1", "A2.2", "B1.1", "B2.1","B2.2", "B2.3", "C1.1","C1.2", "C1.3", "C1.4"])

args = parser.parse_args()

## For test purpuses
# language = "german" 
# levels = ["A2.2"]

language = args.language
levels = args.levels

print(">>> Language:", str.upper(language))
print(">>> Levels:")
[print(level) for level in levels]

baseURL = "https://www.lingoda.com/german/learning-material/cefr"

failed_downloads = []

for level in levels:
    file = os.path.join("webpages", language, level + ".html")

    if not os.path.exists(file):
        print("The requested file does not exists:", file)
        print("Continue with the next level...")
        continue

    with open(file, 'r', encoding='UTF-8') as f:
        html_string = f.read()

    # Get the names of the lessons
    names_types = re.findall(r'body1 MuiTypography-displayBlock">(.+?)</span>.+?">(.+?)</div', html_string)

    names = [n for (n, _) in names_types]
    types = [t for (_, t) in names_types]

    newnames = []
    names_save= []

    for name in names:
        newname = unidecode.unidecode(str.lower(name))
        newname = newname.replace("&amp;", "")
        newname = newname.replace("-", " ").replace("   ", " ").replace("  ", " ")
        newname = newname.replace(' ', '-')
        newname = re.sub("[!¡@#$&?¿':,.()]", '', newname)
        newname = re.sub('"', '', newname)
        newnames.append(newname)
        names_save.append(re.sub('[?\/:()"]', '', name))

    save_folder = os.path.join('pdfs', language, level)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    print(f"> Level {level}. Download begins...")
    print("The files will be saved at:", save_folder)

    suffixes = ["", "-1", "-2", "-3", "-4"]
    
    for i, newname in enumerate(tqdm(newnames)):
        for suffix in suffixes:
            #'https://www.lingoda.com/german/learning-material/cefr/A2.2/that-smells-good/download'

            url = f"{baseURL}/{level}/{newname}{suffix}/download"
            response = requests.get(url)
        
            # Start of a PDF file
            # b '%PDF-1.5\r\n%\xb5\xb5\xb5\xb5\r\n1 0 obj\r\n<</'

            # Start of a non-pdf file, but html "Not found page"
            # b'<!DOCTYPE html>\n<!--[if IE 9]>\n<html lang...'

            if not str(response.content[0:10]).startswith("b'%PDF"):
                if suffix == "":
                #print(f"Failed: {i+1}. {names[i]}")
                    failed_downloads.append((level, i+1, newname, url))

            else: 
                with open(os.path.join(save_folder, f"{i+1}. ({types[i]}) {names_save[i]}{suffix}.pdf"), 'wb') as f:
                    f.write(response.content)

print("Failed downloads")
[print(l,i,n, u) for l,i,n,u in failed_downloads]
