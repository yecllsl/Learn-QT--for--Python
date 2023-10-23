import os

ui = 'student.ui'
py = 'student.py'
path = './'
os.chdir(path)
cmdTemplate = 'PySide6-uic  %s -o %s'
os.system(cmdTemplate % (ui, py))