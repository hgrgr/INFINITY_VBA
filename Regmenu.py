#-*- conding: utf-8 -*-
import winreg


winup_path = "*\shell"

def make_registry():
    au_path=winup_path+r"\Vbatest"
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,au_path)

def register_registry():
    reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    au_path = winup_path+r"\Vbatest"
    key = winreg.OpenKey(reg_handle, au_path,0,winreg.KEY_WRITE)

    try:
        winreg.SetValue(key, "command", winreg.REG_SZ, "C:\\Users\hsj80\Desktop\python\dist\\version_py.exe --check_file %1")
    except EnvironmentError:
        print("errer");

    winreg.CloseKey(key)


make_registry()
register_registry()