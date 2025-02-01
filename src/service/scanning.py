




from dataclasses import dataclass
import os


class CopyEntry:
    path:str

    with_registry=False

    def __init__(self,path:str,name:str):
        self.path=path
        self.name=name
        if path.lower().endswith("putty"):
            self.with_registry=True
        



def scan_dir(path:str):

    progams_folder = os.path.join(path,"Program Files")
    programs=os.listdir(progams_folder)






    return [ CopyEntry(os.path.join(progams_folder,p),p) for p in programs]
