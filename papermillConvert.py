#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nickgould
"""

import subprocess

from datetime import datetime

def Today():
    return datetime.now().strftime("%Y%m%d")

def ThisTime():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


myNotebook = 'Input-MonteCarloPi.ipynb'
# myOutput = myNotebook.split('.')[0] + '_OUTPUT.' + myNotebook.split('.')[1]
myOutput = 'output/' + 'Output-MonteCarloPi' + ThisTime() + '.ipynb'
print(myOutput)


bashCommand = f'papermill {myNotebook} {myOutput}'
# bashCommand = f'jupyter nbconvert --to html {myOutput} --output {myFile}'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()


