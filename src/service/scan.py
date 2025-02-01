




from dataclasses import dataclass
import os

from service.scanning.programentry import ProgramEntry


class CopyEntry:
    path:str

    with_registry=False

    def __init__(self,path:str,name:str):
        self.path=path
        self.name=name
        if path.lower().endswith("putty"):
            # HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions
            self.with_registry=True
        
        # HKEY_CURRENT_USER\Software\HeidiSQL

        # maybe just copy entire HKEY_CURRENT_USER\Software 🤔
        
        # user env variables: HKEY_CURRENT_USER\Environment
        # sys env HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment 
        
        # for right click menu in explorer: reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve



def scan_dir(path:str):

    progams_folder = os.path.join(path,"Program Files")
    programs=os.listdir(progams_folder)

    # also copy %userprofile%
    desktopicons="HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Bags\1\Desktop"



    return [ ProgramEntry(os.path.relpath(os.path.join(progams_folder,p),path),p) for p in programs]
