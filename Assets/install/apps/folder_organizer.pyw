#Author: Samuel Tamakloe
#Version: 00.01
#folder organizer

import os
import subprocess as sub
import shutil 
from threading import Thread
from os.path import expanduser

source = "C:\\folder organizer"

#sub.run(['pythonw', source,'\desktop.pyw'])

#print(source+"\desktop.pyw")

if os.path.isdir(source):
    t1 = Thread(target=sub.run, args=(["pythonw", source+"\desktop.pyw"],))
    t2 = Thread(target=sub.run, args=(["pythonw", source+"\document.pyw"],))
    t3 = Thread(target=sub.run, args=(["pythonw", source+"\picture.pyw"],))
    t4 = Thread(target=sub.run, args=(["pythonw", source+"\downloads.pyw"],))
    t5 = Thread(target=sub.run, args=(["pythonw", source+"\music.pyw"],))
    t6 = Thread(target=sub.run, args=(["pythonw", source+"\videos.pyw"],))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
else:
    pass