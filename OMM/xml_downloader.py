"""
Tool for downloading OMM data for multiple groups from CelesTrak
"""

import xml.etree.ElementTree as ET
import requests

xml_groups = ['active'] # Available groups can be found here: http://celestrak.org/NORAD/elements/index.php?FORMAT=tle
filename = 'celestrak_omm'


def download_xml():
    root = None
    for group in xml_groups:
        request = requests.get(f'http://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=xml')
        if root is None:
            root = ET.fromstring(request.text)
        else:
            for omm in ET.fromstring(request.text).iter("omm"):
                root.extend(omm)

    with open(f'{filename}.xml', 'w') as f:
        if root is not None:
            f.write(ET.tostring(root).decode("Utf-8"))
        print(f'Saved OMM data to {filename}.xml')

if __name__ == '__main__':
    download_xml()
