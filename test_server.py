import requests
import os
from time import sleep
import json
import glob


def send_data_to_server(image_path):
    print(image_path)

    image_filename = os.path.basename(image_path)

    multipart_form_data = {
        'file': (image_filename, open(image_path, 'rb'), 'image/jpeg')
    }
    try:
        response = requests.post('http://0.0.0.0:9000/sendfile',
                                 files=multipart_form_data)
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except:
        pass


if __name__ == "__main__":
    input_dir = ""
    im_names = glob.glob(os.path.join(input_dir, '*.png')) + \
               glob.glob(os.path.join(input_dir, '*.jpg')) + \
               glob.glob(os.path.join(input_dir, '*.jpeg'))
    list_fname = sorted(im_names)
    for fname in list_fname:
        print('-----------   ' + fname + '   ------------')
        send_data_to_server(fname)
        print('--------------------------------------')
        print()
        sleep(2.5)
