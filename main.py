from tkinter import Tk
from tkinter.filedialog import askdirectory

import xml.dom.minidom
import base64


def detect_encoding(base64_string):
    buffer = base64.b64decode(base64_string)

    if b'<?xml' not in buffer:
        return 'utf-8'

    encoding_declaration_start = buffer.find(b'encoding')
    if encoding_declaration_start == -1:
        return 'utf-8'

    encoding_start = buffer.find(b'"', encoding_declaration_start)
    if encoding_start == -1:
        return 'utf-8'

    encoding_start += 1
    encoding_end = buffer.find(b'"', encoding_start)

    if encoding_end == -1:
        return 'utf-8'

    return buffer[encoding_start:encoding_end].decode('utf-8')


def decode_base64(base64_string, encoding):
    return base64.b64decode(base64_string).decode(encoding)


def make_xml_pretty(xml_string):
    return xml.dom.minidom.parseString(xml_string).toprettyxml()


def choose_directory():
    root = Tk()
    root.withdraw()

    selected_directory = askdirectory()
    return selected_directory


def choose_filename():
    return input('Choose filename: ')


def save_xml_to_file(xml_text, encoding):
    with open(f'{choose_directory()}/{choose_filename()}.xml', 'w', encoding=encoding) as file:
        file.write(xml_text)
    print('XML saved')


def main():
    encoded_string = input('Enter the Base64-encoded XML document: ')
    encoding = detect_encoding(encoded_string)
    decoded_string = decode_base64(encoded_string, encoding)
    print(decoded_string)
    print(make_xml_pretty(decoded_string)) if input('Make pretty? y/N: ').lower() == 'y' else None
    save_xml_to_file(decoded_string, encoding) if input('Save file? y/N: ').lower() == 'y' else None


if __name__ == '__main__':
    main()
