#Author: Samuel Tamakloe
#Version: 00.01
#folder organizer
import os
import subprocess as sub
import shutil
from os.path import expanduser

source = os.path.expanduser("~") + "/Desktop/folder_organizer/Install/files"
dist = os.path.expanduser("~") + "/AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
srt = os.path.expanduser("~") + "/Desktop/folder_organizer/Install/apps"
srt2 = os.path.expanduser("~")+ "/Desktop/folder_organizer/Install/apps/folder_organizer.pyw"
path = "C://"

file_f = 'folder organizer'
if (os.path.isdir(path + file_f)):
    pass
else:
    os.mkdir(path + file_f)
src = os.path.join(path, file_f)
files = os.listdir(source)
for fname in files:
    shutil.copy2(os.path.join(source, fname), src)

shutil.copy2(srt2, dist)

sub.call(['pip', 'install', 'watchdog'])
os.chdir(dist)
sub.run(['pythonw','folder_organizer.pyw'])
sub.run(["powershell", "Shutdown /r /t 0"])
