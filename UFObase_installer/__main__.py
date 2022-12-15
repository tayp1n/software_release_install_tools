import os
from UFObase_installer.installer_gui import SoftwareReleaseInstallerGui


def main():
    release_path = rf"C:\Users\{os.getlogin()}\Humanetics\Summer Internships - Documents\Release v4.1.0\UFO-1-9060 UFO Base\UFOBaseV3_5"
    installer = SoftwareReleaseInstallerGui(release_path)
    installer.start_gui()


if __name__ == '__main__':
    main()
