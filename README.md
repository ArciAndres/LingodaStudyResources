# Lingoda study resources

The execution of this script allows the user to download automatically the available material in PDF format from Lingoda language lessons. These PDFs are completely available for each student, but manual downloading could take time. 

## Instructions

### Download HTML layout from course
The HTML layout from the course overview is required, and it must be downloaded manually (as it requires authentication to access, and doing it programmatically is just longer, and the task is pretty easy tbh). 

For level A1.2, navigate to: 
https://www.lingoda.com/en/account/course-overview/A1.2.
For the next levels, modify the end of the URL, or just navigate in the webpage. 

Save the website with `Ctrl+S` with Chrome, or other web browser, in the folder `webpages`. It should be saved with the name of the level. For instance, the level A1.2 should have the name `A1.2`.  
This repository includes the HTML files for GERMAN. The other languages are not accessible from my account, and they should be downloaded and included in the respective folder.

### Dependencies
A Python 3.6+ version should work just fine. No futher libraries are required. 

### Execution
In the command line, run the script, with arguments: language and levels (separated by space). The name of the language shuold be correspondent with the name of the folder. Likewise the name of the levels with the name of the HTML files.
```
python LingodaScript2021.py {language} {levels}
```
For example:
```
python LingodaScript2021.py german A1.2 A2.1 A2.2 B1.1 B2.1 B2.2 B2.3 C1.1 C1.2 C1.3 C1.4
```

The files will be downloaded in the folder `pdfs`, inside the corresponding language folder. 

### Troubleshooting
There could be a few exception of files that will not be downloaded due to inconsistancies in their URL with the lesson name. For now, those should be downloaded manually, since automate this task would require to navigate inside the lesson name. Any contribution is highly appreciated. 

