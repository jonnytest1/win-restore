import os
from service.scanning.entry import CopyEntry


class FileEntry(CopyEntry):
    relative_path:str
    
    def __init__(self,relative_path:str,name:str):
        self.relative_path=relative_path
        self.name=name

    def copy(self,target:str):
        locaiton=os.path.join(target,self.relative_path)
        raise Exception("Todo")
    