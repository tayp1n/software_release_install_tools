import os
from UFObase_installer.installer_gui import SoftwareReleaseInstallerGui


def main():
    release_path = rf"C:\Users\{os.getlogin()}\UFOBaseV3_5"
    installer = SoftwareReleaseInstallerGui(release_path)
    installer.start_gui()


if __name__ == '__main__':
    main()
