from tkinter import Tk
from tkinter.filedialog import askdirectory

import xml.dom.minidom
import base64


def decode_base64_to_windows1251(base64_string):
    return base64.b64decode(base64_string).decode('windows-1251')


def make_xml_pretty(xml_string):
    return xml.dom.minidom.parseString(xml_string).toprettyxml()


def choose_directory():
    root = Tk()
    root.withdraw()

    selected_directory = askdirectory()
    return selected_directory


def choose_filename():
    return input('Choose filename: ')


def save_xml_to_file(xml_text):
    with open(f'{choose_directory()}/{choose_filename()}.xml', 'w', encoding='windows-1251') as file:
        file.write(xml_text)
    print('XML saved')


def main():
    decoded_string = decode_base64_to_windows1251(input('Enter the Base64-encoded string: '))
    print(decoded_string)
    pretty_string = make_xml_pretty(decoded_string) if input('Make pretty? y/N: ').lower() == 'y' else decoded_string
    print(pretty_string)
    save_xml_to_file(pretty_string) if input('Save file? y/N: ').lower() == 'y' else None


if __name__ == '__main__':
    main()
