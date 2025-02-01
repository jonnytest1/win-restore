

class CopyEntry:
    path:str

    with_registry=False

    def __init__(self,path:str,name:str):
        self.path=path
        self.name=name
        if path.lower().endswith("putty"):
            # HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions
            self.with_registry=True


    def copy(self,target:str):
        raise Exception("not implemented")
        