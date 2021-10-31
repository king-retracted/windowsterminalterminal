import requests as r
from termcolor import cprint, colored
from os.path import join
from os import getcwd

defaultThemesUrl = 'https://raw.githubusercontent.com/atomcorp/themes/master/themes.json'
customThemesUrl = 'https://raw.githubusercontent.com/atomcorp/themes/master/app/src/custom-colour-schemes.json'
wTTUrl = 'https://raw.githubusercontent.com/king-retracted/windowsterminalterminal/master/vars.py'

def writeUpdate(srcUrl):
    with open(str(srcUrl).split('/')[-1], 'w') as f:
        content = str(r.get(srcUrl).text)

        f.write(content)

def checkUpdate():
    dThemeC = str(r.get(defaultThemesUrl).text)
    cThemeC = str(r.get(customThemesUrl).text)
    wTT = str(r.get(wTTUrl).text)

    with open(join(getcwd(), 'themes.json'), 'r') as f:
        global currentThemeContents
        currentThemeContents = f.read()
    
    with open(join(getcwd(), 'custom-colour-schemes.json'), 'r') as f:
        global customThemeContents
        customThemeContents = f.read()

    with open(join(getcwd(), 'vars.py'), 'r') as f:
        global wTTCodeContent
        wTTCodeContent = f.read()

    needsUpdating = []
    if dThemeC != currentThemeContents:
        needsUpdating.insert(0, True)

    if cThemeC != currentThemeContents:
        needsUpdating.insert(1, True)

    if wTT != wTTCodeContent:
        needsUpdating.insert(2, True)

    print(needsUpdating)

def main():
    cprint('Would you like to check for updates? (Y/n)\n', color='blue')
    if input(colored(' > ', color='yellow')).lower() in ('Y', 'y', '', 'yes'):
        checkUpdate()
    else:
        cprint('Continuing execution...', color='green')

main()