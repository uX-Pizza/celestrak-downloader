"""
Tool for downloading OMM data for multiple groups from CelesTrak
"""

import json
import requests

omm_groups = ['active'] # Available groups can be found here: http://celestrak.org/NORAD/elements/index.php?FORMAT=tle
filename = 'celestrak_omm'


def download_omm():
    omm_json = []
    for group in omm_groups:
        request = requests.get(f'http://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=json')
        for i in request.json():
            omm_json.append(i)

    with open(f'{filename}.json', 'w') as f:
        json.dump(omm_json, f)
        print(f'Saved OMM data to {filename}.json')

if __name__ == '__main__':
    download_omm()
