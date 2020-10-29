import requests \
    , logging \
    , json \
    , os

from datetime import datetime
from time import sleep

from flask import Flask, request, render_template, redirect, send_from_directory, make_response

import argparse

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logging.getLogger('werkzeug').setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('arg')
args = parser.parse_args()
arg = args.arg

ip = '0.0.0.0'
port = 5001

def client():
    address = f'http://{ip}:{port}/'
    while True:
        r = requests.post(address+'?some-name=from-url-parameters', data={'some-name': 'from data'}, headers={'some-name': 'from headers'})
        sleep(1)
    result = (f'{r.url:<24} | {r.status_code:>3} | {r.reason:<2} | {r.text:<10}')

def server():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/', methods=['POST'])
    def test():
        """Take inputs and do nothing"""
        # request.headers.get: Data from headers
        # request.args.get: Data from query string. (The part in the URL after the question mark).
        # request.form.get: Data passed with the request.
        logging.info(f'##################################################')
        logging.info(f'headers.get | {request.headers.get("some-name")}')
        logging.info(f'args.get    | {request.args.get("some-name")}')
        logging.info(f'form.get    | {request.form.get("some-name")}')
        return {}
    
    app.run(host=ip, port=port)

if __name__ == '__main__':
    if arg == 'client':
        client()
    elif arg == 'server':
        server()
