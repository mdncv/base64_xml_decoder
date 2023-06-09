import base64
import xml.dom.minidom


def decode_base64_to_windows1251(base64_string):
    return base64.b64decode(base64_string).decode('windows-1251')


def make_xml_pretty(xml_string):
    return xml.dom.minidom.parseString(xml_string).toprettyxml()


def main():
    decoded_string = decode_base64_to_windows1251(input('Enter the Base64-encoded string: '))
    print(decoded_string)
    print(make_xml_pretty(decoded_string)) if input('Make pretty? y/N: ').lower() == 'y' else None


if __name__ == '__main__':
    main()
