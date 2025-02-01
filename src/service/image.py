
from subprocess import run

def mount_image(path:str):
    run(["powershell.exe","Mount-DiskImage","-ImagePath",path])


def dismount_image(path:str):
    run(["powershell.exe","Dismount-DiskImage","-ImagePath",path])