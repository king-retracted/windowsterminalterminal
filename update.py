import requests as r
from termcolor import cprint, colored
from os.path import join
from os import getcwd
from vars import _VERSION

defaultThemesUrl = 'https://raw.githubusercontent.com/atomcorp/themes/master/themes.json'
customThemesUrl = 'https://raw.githubusercontent.com/atomcorp/themes/master/app/src/custom-colour-schemes.json'
wTTUrl = 'https://raw.githubusercontent.com/king-retracted/windowsterminalterminal/master/vars.py'

def writeUpdate(srcUrl):
    with open(str(srcUrl).split('/')[-1], 'w') as f:
        content = str(r.get(srcUrl).text)

        f.write(content)

def returnFileContent(file):
    with open(file, 'r') as f:
        return f.read()

def checkUpdate():
    _locals = locals()
    try:
        global wTTUpdateContent
        global defaultThemesContent
        global customThemesContent
        wTTUpdateContent = r.get(wTTUrl).text
        defaultThemesContent = r.get(defaultThemesUrl).text
        customThemesContent = r.get(customThemesUrl).text
    except:
        cprint('Error occured when fetching for the remote content. Do you have internet?', color='red')

    exec(wTTUpdateContent)
    
    cprint('Attempting an update for the project _VERSION...', color='blue')
    if _VERSION != _locals['_VERSION']:
        cprint('Local version: {} does not match remote version: {}!'.format(_VERSION, _locals['_VERSION']), color='red')
        cprint('Attempting an update...', color='yellow')
        writeUpdate(wTTUrl)
        writeUpdate('https://raw.githubusercontent.com/king-retracted/windowsterminalterminal/master/main.py')
        cprint('Updated _VERSION.', color='green')
    else:
        cprint('Local version matches remote version.', color='green')

    cprint('Attempting an update for the project themes.json...', color='blue')
    if returnFileContent(join(getcwd(), 'themes.json')) != defaultThemesContent:
        cprint('Local themes.json does not match remote themes.json!', color='red')
        cprint('Attempting an update...', color='yellow')
        writeUpdate(defaultThemesUrl)
        cprint('Updated themes.json.', color='green')
    else:
        cprint('Local version matches remote version.', color='green')

    cprint('Attempting an update for custom-colour-schemes.json...', color='blue')
    if returnFileContent(join(getcwd(), 'custom-colour-schemes.json')) != customThemesContent:
        cprint('Local custom-color-schemes.json does not match remote custom-colour-schemes.json!', color='red')
        cprint('Attempting an update...', color='yellow')
        writeUpdate(customThemesUrl)
        cprint('Updated custom-colour-schemes.json.', color='green')
    else:
        cprint('Local version matches remote version.', color='green')

    

def main():
    cprint('Would you like to check for updates? (Y/n)\n', color='blue')
    if input(colored(' > ', color='yellow')).lower() in ('Y', 'y', '', 'yes'):
        checkUpdate()
    else:
        cprint('Continuing execution...', color='green')

if __name__ == '__main__':
    cprint('This code should not be ran independently. Continuing execution...', color='yellow')
    main()