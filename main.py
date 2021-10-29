from termcolor import cprint, colored
from os import path, getcwd, getlogin, system as system_run
from platform import system
import json
from vars import _VERSION

# red = error
# green = success
# yellow = input
# blue = info

try:
    configFile = 'C:/Users/{}/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json'.format(getlogin())
except FileNotFoundError:
    configFile = input(' (File path) > ')

configFileExists = path.isfile(configFile)

cprint('Powered by https://github.com/atomcorp/themes. Developed by RainWashedROM/KingRetracted', color='blue')

if system().lower() != 'windows':
    cprint('Not designed for {}. Developed for Windows. Be Weary.'.format(system().lower()), color='red')
    input(colored(' > I understand the risk. < \n', color='yellow'))

if not configFileExists:
    def couldNotBeFound():
        cprint('{} could not be found. Enter a manual path (do not include settings.json and ending in /)', color='red')
        global configFile
        configFile = input(colored(' > ', color='yellow')) + '/settings.json'
    couldNotBeFound()
    if not path.isfile(configFile):
        couldNotBeFound()
    else:
        cprint('{} was found. Continuing execution.', color='green')

with open(configFile, 'r+') as f:
    global configDat
    configDat = json.loads(f.read())

with open(path.join(getcwd(), 'themes.json')) as f:
    global themeDat
    themeDat = json.loads(f.read())

def listThemes():
    for index, obj in enumerate(themeDat):
        cprint('[{}] - {}'.format(index, obj['name']), color='blue')
    cprint('Visit https://windowsterminalthemes.dev/ to see your theme in action.', color='blue')
    input(colored(' > Press Enter to Return < \n', color='yellow'))

def installTheme():
    maxNum = len(themeDat) - 1
    cprint('Enter Theme Number', color='blue')
    indexInput = int(input(colored(' > ', color='yellow')))

    if indexInput > maxNum:
        cprint('Theme is out of range.', color='red')
        input(colored(' > Press Enter to Return < \n', color='yellow'))
        installTheme()
    else:
        dataObj = themeDat[indexInput]

        cprint('Are you sure you want to install {}? (Y/n)'.format(dataObj['name']), color='blue')
        
        if input(colored(' > ', color='yellow')) in ('Y', 'y', '', 'yes'):
            with open(configFile, 'r+') as f:
                configDat['schemes'].append(dataObj)
                updatedConfig = json.dumps(configDat)
                f.write(updatedConfig)

                cprint('Updated configuration file.', color='green')
                cprint('Ejecting... (don\'t worry, it worked.)', color='red')
                quit()
        else:
            cprint('Ejecting...', color='red')
            quit()

    input(colored(' > Press Enter to Return < \n', color='yellow'))

def printAbout():
    cprint(
'''
Powered by https://github.com/atomcorp/themes. Developed by RainWashedROM/KingRetracted.
Running on version: {}
'''.format(_VERSION), color='blue'
    )
    input(colored(' > Press Enter to Return < \n', color='yellow'))        

functonToSelection = {
    '0': listThemes,
    '1': installTheme,
    '2': printAbout,
}


def main():
    system_run('clear' if system().lower() != 'windows' else 'cls')
    cprint(
'''
Windows Terminal Terminal
[0] - List Themes
[1] - Install Theme
[2] - About
[3] - Quit
''', color='blue')
    userSelect = input(colored(' > ', color='yellow'))
    if userSelect in ('0', '1', '2', '3'):
        if userSelect == '3':
            quit()
        else:
            functonToSelection[userSelect]()
        main()
    else:
        cprint('Not a valid index.', color='red')
        input(colored(' > Press Enter to Return < \n', color='yellow'))        
        main()

if __name__ == '__main__':
    main()