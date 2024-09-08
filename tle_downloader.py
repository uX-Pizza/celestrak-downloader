"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Based on https://gist.github.com/JaniniRami/229d93365df5b100afb7bca660a25a45
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Tool for downloading Two Line Elements for multiple groups from CelesTrak
http://celestrak.org/NORAD/documentation/gp-data-formats.php
"""

import json
import requests

tle_groups = ['active'] # Available groups can be found here: http://celestrak.org/NORAD/elements/index.php?FORMAT=tle
filename = 'celstrak_tle'


def download_tle():
    tle_json = []
    for group in tle_groups:
        request = requests.get(f'http://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle')
        tmp_dict = {}
        for i in request.text.split('\n'):
            try:
                if i[0] == '1':
                    tmp_dict['tle_1'] = i.strip()
                elif i[0] == '2':
                    tmp_dict['tle_2'] = i.strip()
                else:
                    tmp_dict['satellite_name'] = i.strip()

                if "tle_1" in tmp_dict and "tle_2" in tmp_dict and "satellite_name" in tmp_dict:
                    tle_json.append(tmp_dict)
                    tmp_dict = {}
                else:
                    pass
            except:
                pass

    with open(f'{filename}.json', 'w') as f:
        json.dump(tle_json, f, indent=3)
        print(f'Saved TLE data to {filename}.json')

if __name__ == '__main__':
    download_tle()
