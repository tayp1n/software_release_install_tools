# software_release_install_tools

**software_release_install_tools** is a script written in PySimpleGui for easy editing of scripts and installing them on a personal PC

## Features

* Unpack the rar or zip file
* Conveniently opens all installed scripts
* Ability to delete and edit scripts directly from the program
* Ability to add scripts
* Automatic installation to your drive
* You can edit many folders with your scripts in one window

## Anti-features

* Does not support legacy cipher suites or protocols
* Doesn't detect your scripts folder automatically
* Does not depend on the security of [TLS]
* Does not claim to provide anonymity or censorship avoidance
* Does not claim to protect you from the [FSB](https://en.wikipedia.org/wiki/Federal_Security_Service), [MSS](https://en.wikipedia.org/wiki/Ministry_of_State_Security_(China)), [DGSE](https://en.wikipedia.org/wiki/Directorate-General_for_External_Security), or [FSM](https://en.wikipedia.org/wiki/Flying_Spaghetti_Monster)

## Deploy the software_release_install_tools

Before you start using the script, you need to manually change the input data, such as:
1. **This is the folder from which the scripts will be loaded in __main__.py**
```ruby
release_path = rf"C:\Users\{os.getlogin()}\"
```
2. **This is the path where the scripts from the previous paragraph will be saved that you will edit from in software_release_installer.py**
```ruby
 shutil.copytree(
        rf"C:\Users\{os.getlogin()}\",
        'C:/')
```
3. **Also you need to change the following lines to yours**
software_release_installer.py
```ruby
         if os.path.exists('C:/'):
            shutil.rmtree('C:/')
```
```ruby
         if os.path.exists('C:/') and not os.path.exists(f'C:/config_{val}'):
```
```ruby
        elif not os.path.exists('C:/'):
```
```ruby
        shutil.copytree(
            rf"C:\Users\{os.getlogin()}\",
            'C:/')
```
```ruby
    with zipfile.ZipFile('C:/.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/')
        print('File `help_v2_2_0.zip` is unzipped in folder')
    with zipfile.ZipFile('C:/.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/')
        print('File `UFOBase_Scripts_v2_0_0.zip` is unzipped in folder')
    os.remove('C:/.zip')
    os.remove('C:/.zip')
```
```ruby
       def rename_folder(val):
    # rename folder
    # folder_name = input("Input custom folder name... \n")
    os.chdir('C:/')
    if val != 'FirstComm':
        os.rename("config_FirstComm", f"config_{val}")
        print(f"The Directory has been successfully renamed. New name of folder is '{val}'!")
        rename_shortcut(val)
        remove_shortcut(val)
```
```ruby
   def rename_shortcut(val):
    # rename shortcut

    path = os.path.join(f'C:/config_{val}/your_{val}.lnk')
    target = f'C:/your_folder/your_exe.exe'
    w_dir = 'C:/your_folder'
    icon = f'C:/your_folder/your_exe.exe'

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.Arguments = fr"config_{val}/ufobase3.ini"
    shortcut.WorkingDirectory = w_dir
    shortcut.IconLocation = icon
    shortcut.save()


def remove_shortcut(val):
    # remove shortcut
    os.remove(f'C:/your_folder/your_config_{val}/your_lnk.lnk')
```

installer_gui.py
```ruby
         names = os.listdir(
            r"C:\Users\your_user\your_folder"
            r"Base\UFOBaseV3_5\config_FirstComm")
        os.chdir(
            r"C:\Users\your_user\your_folder "
            r"Base\UFOBaseV3_5\config_FirstComm")
        for name in names:
            if "192.168" in name and "ufo_" in name and ".ini" in name or "VGPS" in name:
                os.remove(rf"C:\UFOBaseV3_5\{val_}\{name}")

```
As well as all the following
![]()
if you have any questions don't hesitate to <a href="mailto:holy.mail.100@gmail.com">contact me</a>. Looking forward to hearing from you. 

## My account LinkedIn
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nazar-arshinskiy/)

If you want to distribute a closed-source modification or service based on software_release_install_tools, then please consider <a href="mailto:holy.mail.100@gmail.com">purchasing an exception</a> . As with the methods above, this will help support continued development.

