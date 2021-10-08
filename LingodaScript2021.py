import os
import re
import requests
import unidecode
from tqdm import tqdm

language = "German"
levels = ["A1.2", "A2.1", "A2.2", "B1.1", "B1.2", "B1.3", "B2.1","B2.2", "B2.3", "C1.1","C1.2", "C1.3", "C1.4"]

baseURL = "https://www.lingoda.com/german/learning-material/cefr"

for level in levels:
    file = os.path.join("pages", level + ".html")

    with open(file, 'r', encoding='UTF-8') as f:
        html_string = f.read()

    # Get the names of the lessons
    names = re.findall(r'body1 MuiTypography-displayBlock">(.+?)</span>', html_string)

    newnames = []
    names_save= []

    for name in names:
        newname = unidecode.unidecode(str.lower(name).replace(' ', '-'))
        newname = re.sub("[!¡@#$?¿']", '', newname)
        newnames.append(newname)
        names_save.append(re.sub("[/?\:]", '', name))

    save_folder = os.path.join(language, level)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for i, newname in enumerate(tqdm(newnames)):

        url = f"{baseURL}/{level}/{newname}/download"
        response = requests.get(url)

        with open(os.path.join(save_folder, f"{i+1}. {names_save[i]}.pdf"), 'wb') as f:
            f.write(response.content)