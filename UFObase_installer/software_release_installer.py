import shutil
import os
import zipfile
from win32com.client import Dispatch


def create_folder(val):
    copy_folder()
    rename_folder(val)
    unzip_folder()


def copy_config_folder():
    shutil.copytree(
        rf"C:\Users\{os.getlogin()}\
        Humanetics\Summer Internships - Documents\Release v4.1.0\UFO-1-9060 UFO Base\UFOBaseV3_5\config_FirstComm",
        'C:/UFOBaseV3_5/config_FirstComm')


def start(val):
    path = 'C:/UFOBaseV3_5'
    isdir = os.path.isdir(path)
    # Check if it exists
    # print("Do you want to install the 'UFOBase'? Y/N \n")
    # while continue_ != "Y" or "N":
    # continue_ = input().capitalize()
    # if continue_ == "Y":
    # if isdir:
    # print("Folder already exist. Do you want to update version? Y/N \n")
    # continue_ = input().capitalize()
    # if continue_ == "Y":
    if isdir:
        if os.path.exists('C:/UFOBaseV3_5/config_FirstComm'):
            shutil.rmtree('C:/UFOBaseV3_5/config_FirstComm')
    if os.path.exists('C:/UFOBaseV3_5') and not os.path.exists(f'C:/UFOBaseV3_5/config_{val}'):
        copy_config_folder()
        rename_folder(val)
    elif not os.path.exists('C:/UFOBaseV3_5'):
        create_folder(val)

        # else:
        # create_folder(val)
        # elif continue_ == "N":
        # print("Do you want to delete the folder? Y/N \n")
        # continue_ = input().capitalize()
        # if continue_ == "Y":
        # print("Are you sure? Y/N \n")
        # continue_ = input().capitalize()
        # if continue_ == "Y":
        # shutil.rmtree('C:/UFOBaseV3_5')
        # else:
        # print("Press ENTER")
        # input()


def copy_folder():
    # copy the folder
    try:
        shutil.copytree(
            rf"C:\Users\{os.getlogin()}\Humanetics\
            Summer Internships - Documents\Release v4.1.0\UFO-1-9060 UFO Base\UFOBaseV3_5",
            'C:/UFOBaseV3_5')
    except:
        print("There is no that folder named 'UFOBaseV3_5'")


def unzip_folder():
    with zipfile.ZipFile('C:/UFOBaseV3_5/help_v2_2_0.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/UFOBaseV3_5')
        print('File `help_v2_2_0.zip` is unzipped in folder')
    with zipfile.ZipFile('C:/UFOBaseV3_5/UFOBase_Scripts_v2_0_0.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/UFOBaseV3_5')
        print('File `UFOBase_Scripts_v2_0_0.zip` is unzipped in folder')
    os.remove('C:/UFOBaseV3_5/UFOBase_Scripts_v2_0_0.zip')
    os.remove('C:/UFOBaseV3_5/help_v2_2_0.zip')

    print("Successful")
    return


def rename_folder(val):
    # rename folder
    # folder_name = input("Input custom folder name... \n")
    os.chdir('C:/UFOBaseV3_5')
    if val != 'FirstComm':
        os.rename("config_FirstComm", f"config_{val}")
        print(f"The Directory has been successfully renamed. New name of folder is '{val}'!")
        rename_shortcut(val)
        remove_shortcut(val)


def rename_shortcut(val):
    # rename shortcut

    path = os.path.join(f'C:/UFOBaseV3_5/config_{val}/UFOBase3_{val}.lnk')
    target = f'C:/UFOBaseV3_5/UFOBase3.exe'
    w_dir = 'C:/UFOBaseV3_5'
    icon = f'C:/UFOBaseV3_5/UFOBase3.exe'

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.Arguments = fr"config_{val}/ufobase3.ini"
    shortcut.WorkingDirectory = w_dir
    shortcut.IconLocation = icon
    shortcut.save()


def remove_shortcut(val):
    # remove shortcut
    os.remove(f'C:/UFOBaseV3_5/config_{val}/UFOBase3_FirstComm.lnk')


class SoftwareReleaseInstaller:
    @staticmethod
    def install(val):
        if 'C:' in val:
            print('...')
        else:
            start(val)
