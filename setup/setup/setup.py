
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:36:17 2017

@author: Ivan
"""
#to built
# run Python setup build
#to built the installer
#Python setup.py bdist_msi

import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

#the file name is your executable    
executables = [cx_Freeze.Executable("tkinterVid28.py",base = base, icon = 'iconname')]

#
cx_Freeze.setup(
        name = "SeaofBTC-Client",
        options = {"build_exe": {"packages": ["tkinter", "matplotlib"], "incluede_files":["iconname.ico"]}},
        version = "1.0",
        description = "Sea of BTC trading application",
        executables = executables)