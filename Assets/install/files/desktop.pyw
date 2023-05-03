#Author: Samuel Tamakloe
#Version: 00.01
#folder organizer

import os
import time
import random
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# list of file type to enable sorting.
images = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff','psd']
docs = ['pdf', 'docx', 'doc', 'txt', 'xlsx',
        'rtf', 'tex', 'wks', 'wpd', 'csv', 'pptx']
video = ['avi', 'AVI', 'flv','FLV', 'wmv', 'WMV','mov', 'mp4', "MP4", 'mkv', 'MKV']
proj = ['py', 'ipynb', 'pyw','ps1', 'html', 'js', 'css', 'php', 'db', 'bat','xml','bin', 'log']
shucut = ['tpm']
audio = [".aac", ".aa", ".AAC", ".dvf", ".m4a", ".m4b", ".mp4", ".mp3" ".MP3",
   ".msv", "ogg", "oga", ".raw", ".vox", ".wav","WAV",".wma", ".WMA"]
myzp=["zip", "rar", "cpgz", "gz", "xz", "bz2"]
executable= ["dmg", "exe", "deb", "pkg", "msi", "iso", 'whl']

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(fold_to_track):
            src = fold_to_track + '/' + filename
            if os.path.isfile(fold_to_track + '/' + filename):
                # ignore current temp dl files (crdownload) + hidden files (.DS_STORE)

                if filename.split('.')[-1] == 'crdownload':
                    pass
                elif filename.startswith('.'):
                    pass
                else:
                    # Do nothing if file is currently downloading (file size changing)
                    historicalSize = -1
                    while (historicalSize != os.path.getsize(fold_to_track + '/' + filename)):
                        historicalSize = os.path.getsize(
                            fold_to_track + '/' + filename)
                        time.sleep(0.1)
                   # creation_date = ' '.join(time.ctime(
                    #    os.stat(fold_to_track + '/' + filename).st_mtime).replace('  ', ' ').split(' ')[1:3])

                    if filename.split('.')[-1] in images:
                        file_folder = '/Pictures/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)

                    elif filename.split('.')[-1] in docs:
                        file_folder = '/Document/'
                        
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:   
                            os.mkdir(fold_to_track + file_folder)
                            
                    elif filename.split('.')[-1] in video:
                        file_folder = '/Videos/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)

                    elif filename.split('.')[-1] in myzp:
                        file_folder = '/Zip_files/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)

                    elif filename.split('.')[-1] in proj:
                        file_folder = '/Project/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)
                            
                    elif filename.split('.')[-1] in executable:
                        file_folder = '/Software/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)

                    elif filename.split('.')[-1] in executable:
                        file_folder = '/Music/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                        else:
                            os.mkdir(fold_to_track + file_folder)
                                                 
                    else:
                        file_folder = '/other/'
                        if (os.path.isdir(fold_to_track + file_folder)):
                            pass
                            for root, dirs, files in os.walk("."):
                                for i in files:
                                    if i.endswith('.tpm'):
                                        shutil.remove()
                        else:
                            os.mkdir(fold_to_track + file_folder)
                            

                    if (os.path.isdir(fold_to_track + file_folder)):
                        if os.path.isfile(fold_to_track + file_folder + '/' + filename):
                            filename = filename.split(
                                '.')[0] + '_dup' + str(random.randint(0, 200)) + '.' + filename.split('.')[-1]
                            os.rename(src, fold_to_track + file_folder +
                                    '/' + filename)
                        else:
                            os.rename(src, fold_to_track + file_folder +
                                       '/' + filename)
                    else:
                        os.mkdir(fold_to_track + file_folder)
                        os.rename(src, fold_to_track + file_folder +
                                '/' + filename)
                    #print(Fore.RED, Back.BLACK, fold_to_track + '/' + filename, Style.RESET_ALL, 'moved to', Back.BLACK, Fore.GREEN, fold_to_track +
                          #file_folder +'/' + filename, Style.RESET_ALL)
       
                    #saving subdirectories
                    file = fold_to_track + file_folder + '/' + filename 
                    source = fold_to_track + file_folder 
                    
                    #Save to word Document
                    wrd = ['docx', 'txt']
                    if filename.split('.')[-1] in wrd:
                        file_f = '/Word_Document/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)   
                        if os.path.isdir(source):
                            src = source + file_f
                            try:
                                shutil.move(file, src)
                                print('copied', filename)
                            except shutil.Error as err:
                                os.remove(file)
                        
                    #Save to excel Document
                    exel = ['xlsx', 'csv']    
                    if filename.split('.')[-1] in exel:
                        file_f = '/Excel_Document/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)  
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                    
                    
                    #Save to pdf Document
                    if filename.endswith('.pdf'):
                        file_f = '/Pdf_Document/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)     
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass  
                    
                    #Save to powerpoint Document 
                    if filename.endswith('.pptx'):
                        file_f = '/Powerpoint/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)     
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                       
                    
                    if filename.endswith('.lnk'):
                        pass
                    
                    #Save to images    
                    imag = ['jpg', 'jpeg', 'png','PNG', 'gif', 'bmp', 'tiff']
                    if filename.split('.')[-1] in imag:
                        file_f = '/images/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass  
                        
                    #Save to software
                    execu = ["dmg", "exe", "deb", "pkg", "msi"]
                    if filename.split('.')[-1] in execu:
                        file_f = '/Setup_Apps/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                                      
                    
                    #Save all ISO file 
                    if filename.endswith('.iso'):
                        file_f = '/ISO_Apps/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)  
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                           
                    
                    #Save photoshop design
                    if filename.endswith('.psd'):
                        file_f = '/Photoshop/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)  
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass    
                        
                    #Save python files
                    pyth = ['py', 'ipynb','pyw']
                    if filename.split('.')[-1] in pyth:
                        file_f = '/Python/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass   
                        
                    #Save powershell and bat files
                    pwer = ['ps1', 'bat','xml']
                    if filename.split('.')[-1] in pwer:
                        file_f = '/Shell_Script/'                    
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass 
                        
                    if filename.endswith('.bin'):
                        file_f = '/Bin_files/'
                        if (os.path.isdir(source + file_f)):
                            pass
                        else:
                            os.mkdir(source + file_f)
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass   
                        
                    if filename.endswith('.log'):
                        file_f = '/Log_files/'
                        if (os.path.isdir(source + file_f)):
                            pass
                        else:
                            os.mkdir(source + file_f)
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                                 
                        
                    #Save web development
                    web = ['html', 'js', 'css', 'php']
                    if filename.split('.')[-1] in web:
                        file_f = '/Web_Script/'
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass
                        
                    # Save web development
                    web = [".html5", ".html", ".htm", ".xhtml"]
                    if filename.split('.')[-1] in web:
                        file_f = '/HTML/'
                        if (os.path.isdir(source + file_f)): 
                            pass
                        else:
                            os.mkdir(source + file_f)    
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                    
                        
                    # Save database
                    if filename.endswith('.db'):
                        file_f = '/Database/'
                        if (os.path.isdir(source + file_f)):
                            pass
                        else:
                            os.mkdir(source + file_f)
                        if os.path.isdir(source):
                            src = source + file_f
                            shutil.move(file, src)
                        else:
                            pass                               


fold_to_track = os.path.expanduser("~") +"/"+ "Desktop"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, fold_to_track, recursive=True)
observer.start()

try:
    time.sleep(1)
except KeyboardInterupt:
    observer.stop()
observer.join()

