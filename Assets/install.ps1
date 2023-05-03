#Author: Samuel Tamakloe 
#$user = $env:username 
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$path = $DesktopPath + '\folder_organizer\Install\apps'
$path2 = $DesktopPath + '\folder_organizer\Install'
$install = 'setup.pyw'
#Write-Host $path
Start-Process -Wait -FilePath $path\python-3.10.4-amd64.exe -ArgumentList '/S','v','/qn' -PassThru

#$py = $path2+"\"+$install
#Write-Host $py

Start-Process py $py
#Start-Process -FilePath $path2 "C:\Program Files\Python\python.exe" -ArgumentList '"\setup.pyw" "abcd"';