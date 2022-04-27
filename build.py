#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Compile the app to a system executable (OS dependent)
'''

from os import path, system, remove, rmdir


# paths
currentPath = path.dirname(path.abspath(__file__))
iconPath = currentPath + '/orange.ico'
scriptPath = currentPath + '/main.py'
buildPath = currentPath + '/bin/'

print(f'Check pyinstaller module ...')
system('pip install pyinstaller')
print(f'🍊 build {scriptPath} to {buildPath}...')
pyinstallerString = f'pyinstaller -F -n clockword --noconsole --distpath="{buildPath}" -i {iconPath} {scriptPath}'
system(pyinstallerString)
remove(currentPath + '/clockword.spec')
rmdir(currentPath + '/build')
print('Successfully created executable!')