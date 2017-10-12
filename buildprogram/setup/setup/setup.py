# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:15:57 2017

@author: Ivan
"""
#python setup.py build
from cx_Freeze import setup, Executable

setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("reandurllib.py")])
