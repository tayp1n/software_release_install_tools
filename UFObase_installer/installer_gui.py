import os
import PySimpleGUI as sg
import shutil

from UFObase_installer.software_release_installer import SoftwareReleaseInstaller


def get_ufos_for_table(path):
    ufos_array = []
    names = os.listdir(path)
    os.chdir(path)
    for name in names:
        if ".ini" in name and "ufo_" in name:
            ip = name[name.find("192"): name.rfind("_")]
            type = name[name.rfind("_") + 1: name.rfind(".")]
            index = name[name.find("ufo_") + 4:name.find("192") - 1]
            ufos_array.append([index, ip, type])
    return ufos_array


def get_ufos_for_table_custom_ip(ufo_configs, array):
    ufos_array = []
    for name in ufo_configs:
        if "DR" in name:
            ufos_array.append([name[0], f"192.168.20.{name[1]}", name[2]])
            array.append([name[0], f"192.168.20.{name[1]}", name[2]])
        else:
            ufos_array.append([name[0], f"192.168.10.{name[1]}", name[2]])
            array.append([name[0], f"192.168.10.{name[1]}", name[2]])

    return ufos_array


def get_ufos_for_table_custom_ip_2(ufo_configs):
    ufos_array = []
    for name in ufo_configs:
        if "DR" in name:
            ufos_array.append([name[0], f"192.168.20.{name[1]}", name[2]])

        else:
            ufos_array.append([name[0], f"192.168.10.{name[1]}", name[2]])

    return ufos_array


class SoftwareReleaseInstallerGui:
    def __init__(self, release_directory):
        self.release_directory = release_directory

    ##########

    @staticmethod
    def copy_folders_and_files(folders_files, folders_files_destination):
        for i in folders_files:
            shutil.copytree(i, folders_files_destination)

    @staticmethod
    def get_files(val_, ufo_array):
        names = os.listdir(val_)
        os.chdir(val_)

        ip = ufo_array[1]
        ufo_type = ufo_array[2]
        for name in names:
            if ufo_type + ".ini" in name and "ufo_" in name and ip in name:
                os.remove(val_ + f"\\{name}")
                break

    @staticmethod
    def rename_files_without_custom_config(val_, ufo_configs):

        types = []
        names = os.listdir(val_)
        os.chdir(val_)
        for i in ufo_configs:
            ufo_type = i[i.find(""): i.find(" ")]
            types.append(ufo_type)
            ip = i[i.find("."):]
            for name in names:
                if ufo_type + ".ini" in name and "ufo_" in name and 1 in set([types.count(type) for type in types]):
                    ready = name[name.find("ufo"): name.find(".30")] + ip + name[name.find(ufo_type) + -1:]

                    shutil.copyfile(name, ready)
                    with open(ready, 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(ready, 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(ready, 'w') as file:

                        file.write(data)
                    break
                elif ufo_type + ".ini" in name and "ufo_" in name and 2 in set([types.count(type) for type in types]):
                    ready = name[name.find("ufo"): name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    shutil.copyfile(name, ready)
                    with open(ready, 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(ready, 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(ready, 'w') as file:

                        file.write(data)
                    break

    @staticmethod
    def rename_files_without_custom_config_new_ufo_configs(val_, ufo_configs):
        names = os.listdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")
        os.chdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")
        for name in names:
            if "192.168" in name and "ufo_" in name and ".ini" in name or "VGPS" in name:
                os.remove(rf"C:\UFOBaseV3_5\{val_}\{name}")

        # 30 UFO
        types = []

        for i in ufo_configs:
            ufo_type = i[2]
            types.append(ufo_type)
            ip = '.' + i[1]
            index = i[0]
            for name in names:
                if ufo_type + ".ini" in name and "ufo_" in name and 1 in set([types.count(type) for type in types]):

                    ready = name[name.find("192") - 1: name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    ready2 = name[name.find("ufo"): name.find("192") - 2] + str(index) + ready

                    shutil.copyfile(name, rf"C:\UFOBaseV3_5\{val_}\{ready2}")
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'w') as file:

                        file.write(data)
                    break
                elif ufo_type + ".ini" in name and "ufo_" in name and 2 in set([types.count(type) for type in types]):
                    ready = name[name.find("ufo"): name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    shutil.copyfile(name, ready)
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready}', 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready}', 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(f'C:/UFOBaseV3_5/{val_}/{ready}', 'w') as file:

                        file.write(data)
                    break

    @staticmethod
    def rename_files_without_custom_config_new_ufo_configs_2(all_new_ufos):
        names = os.listdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")
        os.chdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")

        # 30 UFO
        types = []

        for i in all_new_ufos:
            ufo_type = i[2]
            types.append(ufo_type)
            ip = '.' + i[1]
            index = i[0]
            val_ = i[3]
            for name in names:
                if ufo_type + ".ini" in name and "ufo_" in name:
                    ready = name[name.find("192") - 1: name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    ready2 = name[name.find("ufo"): name.find("192") - 2] + str(index) + ready

                    shutil.copyfile(name, rf"C:\UFOBaseV3_5\{val_}\{ready2}")
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'r') as file:
                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(f'C:/UFOBaseV3_5/{val_}/{ready2}', 'w') as file:
                        file.write(data)
                    break

    @staticmethod
    def rename_files_without_custom_config_new_ufo_configs_3(all_new_ufos):
       names = os.listdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")
        os.chdir(
            r"C:\Users\your_login\UFOBaseV3_5\config_FirstComm")

        # 30 UFO
        types = []

        for i in all_new_ufos:
            ufo_type = i[2]
            types.append(ufo_type)
            ip = '.' + i[1]
            index = i[0]
            val_ = i[3]
            for name in names:
                if "192.168" in name and "ufo_" in name and ".ini" in name or "VGPS" in name:
                    if os.path.exists(rf"C:\UFOBaseV3_5\config_{val_}\{name}"):
                        os.remove(rf"C:\UFOBaseV3_5\config_{val_}\{name}")
            for name in names:
                if ufo_type + ".ini" in name and "ufo_" in name:
                    ready = name[name.find("192") - 1: name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    ready2 = name[name.find("ufo"): name.find("192") - 2] + str(index) + ready

                    shutil.copyfile(name, rf"C:\UFOBaseV3_5\config_{val_}\{ready2}")
                    with open(f'C:/UFOBaseV3_5/config_{val_}/{ready2}', 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(f'C:/UFOBaseV3_5/config_{val_}/{ready2}', 'r') as file:
                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(f'C:/UFOBaseV3_5/config_{val_}/{ready2}', 'w') as file:
                        file.write(data)
                    break

    @staticmethod
    def rename_files(val_, ufo_configs):
        types = []
        names = os.listdir(f'C:/UFOBaseV3_5/{val_}')
        os.chdir(f'C:/UFOBaseV3_5/{val_}')
        for i in ufo_configs:
            ufo_type = i[i.find(""): i.find(" ")]
            types.append(ufo_type)
            ip = i[i.find("."):]
            for name in names:
                if ufo_type + ".ini" in name and "ufo_" in name and 1 in set([types.count(type) for type in types]):
                    ready = name[name.find("ufo"): name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    os.renames(name, ready)

                    with open(ready, 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(ready, 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(ready, 'w') as file:

                        file.write(data)
                elif ufo_type + ".ini" in name and "ufo_" in name and 2 in set([types.count(type) for type in types]):
                    ready = name[name.find("ufo"): name.find(".30")] + ip + name[name.find(ufo_type) + -1:]
                    shutil.copyfile(name, ready)
                    with open(ready, 'r') as fp:
                        replace = fp.readlines()[2]
                    with open(ready, 'r') as file:

                        data = file.read()

                        data = data.replace(replace[replace.find("") - 4:], ip + "\n")

                    with open(ready, 'w') as file:

                        file.write(data)

    @staticmethod
    def open_file(val_, value):
        names = os.listdir(f'C:/UFOBaseV3_5/{val_}')
        os.chdir(f'C:/UFOBaseV3_5/{val_}')

        type = value[value.find(""): value.find(" ")]
        for name in names:
            if type + ".ini" in name and "ufo_" in name:
                return name

    @staticmethod
    def open_browse_gui(folders_files, folders_files_destination):

        layout = [
            [sg.Column([[sg.Text('Folder OR File'), sg.In(size=(25, 1), enable_events=True, key='-FOLDER_OR_FILE-'),
                         sg.FolderBrowse()]], element_justification='c')],
            [sg.Column([[sg.Text('Destination'),
                         sg.In(size=(25, 1), enable_events=True, key='-FOLDER_OR_FILE_DESTINATION-'),
                         sg.FolderBrowse()]], element_justification='c')],
            [sg.Button("Add")]
        ]
        window = sg.Window("DR/UFOs selector", layout, modal=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == "Add":
                folders_files.append(values["-FOLDER_OR_FILE-"])
                folders_files_destination.append(values["-FOLDER_OR_FILE_DESTINATION-"])
                break
        window.close()

    @staticmethod
    def get_ufos_for_listbox(val_):
        ufos = []
        names = os.listdir(val_)
        os.chdir(val_)
        for name in names:
            if ".ini" in name and "ufo_" in name:
                ufos.append(name)
        return ufos

    @staticmethod
    def get_next_index(ufos_array):
        temp_index = 0
        if ufos_array:
            for index in ufos_array:
                if temp_index < int(index[0]):
                    temp_index = int(index[0])
            return temp_index + 1
        temp_index = temp_index + 1
        return temp_index

    @staticmethod
    def get_ufos(val_):
        ufos = []
        names = os.listdir(f'C:/UFOBaseV3_5/{val_}')
        os.chdir(f'C:/UFOBaseV3_5/{val_}')

        for name in names:
            if ".ini" in name and "ufo_" in name:
                ufos.append(name)
        return "\n".join(["{0}. {1}".format(i + 1, ufo) for i, ufo in enumerate(ufos)])

    @staticmethod
    def get_dir_name():
        for dirs, dirnames, dirnames2 in os.walk("C:\\UFOBaseV3_5\\", topdown=True):
            for dirname in dirnames:
                if "config_" in dirname:
                    return dirname

    @staticmethod
    def get_dirs():
        dirs = []
        for dirs, dirnames, dirnames2 in os.walk("C:\\UFOBaseV3_5\\", topdown=True):
            for dirname in dirnames:
                dirs += dirname + '\n'
            return dirs

    @staticmethod
    def get_configs_dirs():
        res = []
        for dirs, dirnames, dirnames2 in os.walk("C:\\UFOBaseV3_5\\", topdown=True):
            for dirname in dirnames:
                if 'config_' in dirname:
                    res.append(dirname)
            return res

    @staticmethod
    def popup_text(filename, text):
        layout = [
            [sg.Multiline(text, key='-MULTI_TEXT-', size=(80, 25))],
            [sg.Button('Save')],
            [sg.Button('Close')]
        ]
        win = sg.Window(filename, layout, modal=True, finalize=True)

        while True:
            event, values = win.read()
            if event == sg.WINDOW_CLOSED or 'Close':
                break
            if event == 'Save':
                text = values['-MULTI_TEXT-']

        win.close()

    # main function
    def open_config_dialog(self):
        global ufos_array
        ufo_configs = []
        folders_files = []
        folders_files_destination = []
        i = 0
        path_ = "None"
        tab_counter = 0
        all_new_ufos = []
        dictionary_for_ufos = {}

        data_headings = ["Index", "IP", "Type"]

        frame_ = [
            [sg.Frame(layout=[

                [sg.Table(values="", headings=data_headings,
                          max_col_width=65,
                          auto_size_columns=False,
                          justification='left',
                          num_rows=6, key='list_box_0'), sg.Button('Add', key='-ADD_BUTTON-0'),
                 sg.Button('Remove', key=f'-REMOVE_BUTTON-{tab_counter}')]

            ],
                title='UFOs', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        ]
        layout = [[sg.Text('UFOBase Installer', size=(
            30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                  [sg.Text('Config name'), sg.InputText(key="-OUTPUT_config-"),
                   sg.Button("Browse", key='-BROWSE_BUTTON-'),
                   sg.Button("New", key='-NEW_BUTTON-')],
                  [sg.TabGroup([[sg.Tab(path_, frame_)]], enable_events=True, key='tab_group')],
                  [sg.Text('_' * 80)],
                  [sg.Button('Install'), sg.Cancel()]]

        window = sg.Window("UFOBase Installer", layout, modal=True)

        while True:
            event, values = window.read()

            if event == 'list_box':
                print(event)

                pass
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            if event == "Install":
                if values["-OUTPUT_config-"]:
                    val = values["-OUTPUT_config-"]
                    installer = SoftwareReleaseInstaller()
                    installer.install(val)
                    if 'C:' in val:

                        self.rename_files_without_custom_config_new_ufo_configs_2(all_new_ufos)
                    else:
                        self.rename_files_without_custom_config_new_ufo_configs("config_" + val, ufo_configs)

                    self.copy_folders_and_files(folders_files, folders_files_destination)

                elif tab_counter >= 1:
                    val = values["tab_group"]
                    installer = SoftwareReleaseInstaller()
                    for item in all_new_ufos:
                        installer.install(item[3])
                    self.rename_files_without_custom_config_new_ufo_configs_3(all_new_ufos)
                    self.copy_folders_and_files(folders_files, folders_files_destination)
                break

            if event == '-BROWSE_BUTTON-':

                if os.path.isdir('''C:\\UFOBaseV3_5'''):
                    path_ = self.open_layout_directories_ufo()
                    if path_:
                        window['-OUTPUT_config-'].Update(disabled=True)
                        folder_path = f"C:\\UFOBaseV3_5\\{path_}"
                        ufos_array = get_ufos_for_table(folder_path)

                        if tab_counter >= 1:
                            window['tab_group'].add_tab(sg.Tab(path_, self.tab(tab_counter), key=path_))
                            window.Element(f'list_box_{tab_counter}').Update(ufos_array)
                            window[path_].select()

                        else:
                            window.Element('tab_group').Widget.tab(0, text=path_)
                            window.Element('list_box_0').Update(ufos_array)

                        window.Element('-OUTPUT_config-').Update(folder_path)
                        tab_counter += 1

            if event == '-NEW_BUTTON-':

                if values["-OUTPUT_config-"]:
                    if tab_counter >= 1:
                        val = values["-OUTPUT_config-"]
                        window['tab_group'].add_tab(sg.Tab(val, self.tab(tab_counter), key=val))
                        window[val].select()
                        window.Element('-OUTPUT_config-').Update('')

                    else:

                        val = values["-OUTPUT_config-"]
                        window.Element('tab_group').Widget.tab(0, text=val)
                        window.Element('-OUTPUT_config-').Update('')

                    tab_counter += 1

            if f'-ADD_BUTTON' in event:

                if values["-OUTPUT_config-"] and 'C:' in values["-OUTPUT_config-"]:
                    try:
                        if dictionary_for_ufos[values['tab_group']]:
                            index_number = event[event.rfind("-") + 1:]
                            folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                            ufo_configs = []

                            self.open_add_ufo_dialog_for_table(ufo_configs,
                                                               self.get_next_index(
                                                                   dictionary_for_ufos[values['tab_group']]),
                                                               values['tab_group'])
                            if ufo_configs:
                                all_new_ufos.append(ufo_configs[0])
                            if tab_counter > 1:
                                window.Element(f'list_box_{index_number}').Update(
                                    folders_files + dictionary_for_ufos[
                                        values['tab_group']] + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                            dictionary_for_ufos[
                                                                                                values['tab_group']]))
                            else:
                                window.Element('list_box_0').Update(
                                    folders_files + dictionary_for_ufos[
                                        values['tab_group']] + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                            dictionary_for_ufos[
                                                                                                values['tab_group']]))
                    except:
                        index_number = event[event.rfind("-") + 1:]
                        folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                        ufo_configs = []
                        ufos_array = get_ufos_for_table(folder_path)
                        self.open_add_ufo_dialog_for_table(ufo_configs,
                                                           self.get_next_index(ufos_array),
                                                           values['tab_group'])
                        if ufo_configs:
                            all_new_ufos.append(ufo_configs[0])
                        if tab_counter > 1:
                            window.Element(f'list_box_{index_number}').Update(
                                folders_files + ufos_array + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                          ufos_array))
                        else:
                            window.Element('list_box_0').Update(
                                folders_files + ufos_array + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                          ufos_array))

                    dictionary_for_ufos[values['tab_group']] = ufos_array




                elif values["-OUTPUT_config-"]:
                    i = i + 1
                    self.open_add_ufo_dialog_for_table(ufo_configs, i, values['tab_group'])
                    if tab_counter > 1:
                        window.Element(f'list_box_{index_number}').Update(
                            get_ufos_for_table_custom_ip_2(ufo_configs))
                    else:
                        window.Element('list_box_0').Update(
                            get_ufos_for_table_custom_ip_2(ufo_configs))
                elif values["-OUTPUT_config-"] == '' and tab_counter >= 1:
                    try:
                        if dictionary_for_ufos[values['tab_group']]:
                            index_number = event[event.rfind("-") + 1:]
                            # folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                            ufo_configs = []

                            self.open_add_ufo_dialog_for_table(ufo_configs,
                                                               self.get_next_index(
                                                                   dictionary_for_ufos[values['tab_group']]),
                                                               values['tab_group'])
                            if ufo_configs:
                                all_new_ufos.append(ufo_configs[0])
                            if tab_counter > 1:
                                window.Element(f'list_box_{index_number}').Update(
                                    folders_files + dictionary_for_ufos[
                                        values['tab_group']] + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                            dictionary_for_ufos[
                                                                                                values['tab_group']]))
                            else:
                                window.Element('list_box_0').Update(
                                    folders_files + dictionary_for_ufos[
                                        values['tab_group']] + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                            dictionary_for_ufos[
                                                                                                values['tab_group']]))
                    except:
                        index_number = event[event.rfind("-") + 1:]
                        # folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                        ufo_configs = []
                        ufos_array = []
                        self.open_add_ufo_dialog_for_table(ufo_configs,
                                                           self.get_next_index(ufos_array),
                                                           values['tab_group'])
                        if ufo_configs:
                            all_new_ufos.append(ufo_configs[0])
                        if tab_counter > 1:
                            window.Element(f'list_box_{index_number}').Update(
                                folders_files + ufos_array + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                          ufos_array))
                        else:
                            window.Element('list_box_0').Update(
                                folders_files + ufos_array + get_ufos_for_table_custom_ip(ufo_configs,
                                                                                          ufos_array))

                    dictionary_for_ufos[values['tab_group']] = ufos_array

            if '-REMOVE_BUTTON-' in event:
                index_number = event[event.rfind("-") + 1:]
                if values["list_box_0"] or values[f'list_box_{index_number}']:
                    config_name = values['tab_group']
                    if tab_counter > 1:

                        # folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                        self.get_files(folder_path, ufos_array[values[f"list_box_{index_number}"][0]])

                        remove_array = [ufos_array[values[f"list_box_{index_number}"][0]][0],
                                        f'{ufos_array[values[f"list_box_{index_number}"][0]][1][ufos_array[values[f"list_box_{index_number}"][0]][1].rfind(".") + 1:]}',
                                        f'{ufos_array[values[f"list_box_{index_number}"][0]][2]}', config_name]
                        if remove_array in all_new_ufos:
                            all_new_ufos.remove(remove_array)

                        ufos_array.remove(ufos_array[values[f"list_box_{index_number}"][0]])
                        window.Element(f"list_box_{index_number}").Update(ufos_array)
                    else:
                        self.get_files(folder_path, ufos_array[values["list_box_0"][0]])
                        remove_array = [ufos_array[values["list_box_0"][0]][0],
                                        f'{ufos_array[values["list_box_0"][0]][1][ufos_array[values["list_box_0"][0]][1].rfind(".") + 1:]}',
                                        f'{ufos_array[values["list_box_0"][0]][2]}', config_name]
                        if remove_array in all_new_ufos:
                            all_new_ufos.remove(remove_array)
                        ufos_array.remove(ufos_array[values["list_box_0"][0]])
                        window.Element('list_box_0').Update(ufos_array)

            if event == 'tab_group':
                if tab_counter > 0 and "C:" in values["-OUTPUT_config-"]:
                    folder_path = f"C:\\UFOBaseV3_5\\{values['tab_group']}"
                    ufos_array = get_ufos_for_table(folder_path)
                    window.Element('-OUTPUT_config-').Update(folder_path)

            if event == 'Get the name of the directories':
                self.open_layout_directories_ufo()
            if event == 'Get the UFOs':
                window.Element('list_box_0').Update(
                    ufo_configs + folders_files + self.get_ufos_for_listbox(values['-OUTPUT_config-']))
        window.close()

    @staticmethod
    def tab(index):
        data_headings = ["Index", "IP", "Type"]
        return [[sg.Frame(layout=[

            [sg.Table(values="", headings=data_headings,
                      max_col_width=65,
                      auto_size_columns=False,
                      justification='left',
                      num_rows=6, key=f'list_box_{index}'), sg.Button('Add', key=f'-ADD_BUTTON-{index}'),
             sg.Button('Remove', key=f'-REMOVE_BUTTON-{index}')]

        ],
            title='UFOs', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')]]

    @staticmethod
    def open_add_ufo_dialog(ufo_configs):
        layout = [
            [sg.Text('Add UFO', size=(
                30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Type: '), sg.Combo(('DR', 'UFO', 'UFOmicro', 'UFOnano'), key='-TYPE-', size=(20, 1))],
            [sg.Text('IP(30...39): '), sg.InputText((), key="-IP-", size=(20, 1))],
            [sg.Button('Add'), sg.Button('Cancel', key='-CANCEL-')]
        ]
        window = sg.Window("Add UFO", layout, modal=True)

        while True:
            event, values = window.read()
            if event == "-CANCEL-" or event == sg.WIN_CLOSED:
                break
            if event == "Add":
                ufo_configs.append(values["-TYPE-"] + '        .' + values["-IP-"])
                break
        window.close()

    @staticmethod
    def open_add_ufo_dialog_for_table(ufo_configs_for_table, index, config_name):
        layout = [
            [sg.Text('Add UFO', size=(
                30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Type: '),
             sg.Combo(('DR', 'UFO', 'UFOmicro', 'UFOnano'), key='-TYPE-', size=(20, 1), readonly=True)],
            [sg.Text('IP(30...39): '), sg.InputText((), key="-IP-", size=(20, 1))],
            [sg.Button('Add'), sg.Button('Cancel', key='-CANCEL-')]
        ]
        window = sg.Window("Add UFO", layout, modal=True)

        while True:
            event, values = window.read()
            if event == "-CANCEL-" or event == sg.WIN_CLOSED:
                break
            if event == "Add":
                if values["-IP-"].isnumeric() and 30 <= int(values["-IP-"]) <= 39:
                    ufo_configs_for_table.append([index, values["-IP-"], values["-TYPE-"], config_name])
                    break
        window.close()

    def open_layout_directories_ufo(self):
        layout = [
            [sg.Listbox(self.get_configs_dirs(), key='-MULTI_DIR-', size=(80, 25))],
            [sg.Button("Open"), sg.Button("Close")]
        ]
        win = sg.Window('Directories', layout, modal=True, finalize=True)

        while True:
            event, values = win.read(close=True)  # how to make without close=True code?
            if event == "Close" or event == sg.WIN_CLOSED:
                break
            if event == "Open":
                if values['-MULTI_DIR-']:

                    return values['-MULTI_DIR-'][0]  # here we return the value but windows won t close
                else:
                    print('...')
        win.close()

        # def open_layout_with_listbox_of_dirs(self):

    ##########
    def start_gui(self):
        sg.change_look_and_feel('SystemDefault1')

        # ------ Column Definition ------ #
        font_button = ("Arial", 18)
        font_top = ("Arial", 15)

        layout = [
            [sg.Text('UFOBase will be deleted if you continue.', size=(20, 5), key='-text-', font=font_top)],
            [sg.Button('Continue', font=font_button), sg.Button('Exit', font=font_button)]
        ]
        window = sg.Window("Main Window", layout)
        while True:
            event, values = window.read(close=True)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Continue":
                self.open_config_dialog()
