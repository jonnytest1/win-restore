from winreg import OpenKey,HKEY_LOCAL_MACHINE,HKEY_CURRENT_USER,KEY_ALL_ACCESS,EnumKey,ConnectRegistry








aKey = OpenKey(HKEY_CURRENT_USER, "", 0, KEY_ALL_ACCESS)
try:
    i = 0
    while True:
        asubkey = EnumKey(aKey, i)
        print(asubkey)
        i += 1
except WindowsError:
    pass