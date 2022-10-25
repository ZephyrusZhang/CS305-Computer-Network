import os
import requests

mime = {
    'html': 'text/html',
    'json': 'application/json'
}

if __name__ == '__main__':
    for filename in os.listdir('file'):
        content_type = mime[filename[filename.index('.') + 1:]]
        print(f'{filename} -> {content_type}')
    print(requests.get('https://www.sustech.edu.cn').headers['Content-Type'])
