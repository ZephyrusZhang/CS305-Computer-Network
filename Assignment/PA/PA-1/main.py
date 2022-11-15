import json
import mimetypes
import os
import random
import string

import config
from framework import HTTPServer, HTTPRequest, HTTPResponse


mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('image/jpeg', '.jpg')


def random_string(length=20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def default_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 404, 'Not Found'
    print(f"calling default handler for url {request.request_target}")


def get_mimetype(url: str):
    return mimetypes.guess_type(url)[0]


def task2_data_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 2: Serve static content based on request URL (20%)
    file_path = f'.{request.request_target}'
    if not os.path.exists(file_path):
        response.status_code, response.reason = 404, 'Not Found'
        return

    with open(file_path, "rb") as file:
        response.status_code, response.reason = 200, 'OK'
        response.add_header(name='Content-Type', value=get_mimetype(request.request_target))
        content = file.read()
        response.add_header(name='Content-Length', value=str(len(content)))
        response.body = content


def task3_json_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 3: Handle POST Request (20%)
    response.status_code, response.reason = 200, 'OK'
    if request.method == 'POST':
        binary_data = request.read_message_body()
        obj = json.loads(binary_data)
        # TODO: Task 3: Store data when POST
        server.task3_data = obj['data']
    else:
        obj = {'data': server.task3_data}
        response.add_header(name='Content-Type', value='application/json')
        response.body = json.dumps(obj).encode()
        response.add_header(name='Content-Length', value=str(len(response.body)))


def task4_url_redirection(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 4: HTTP 301 & 302: URL Redirection (10%)
    response.status_code, response.reason = 302, 'Found'
    response.add_header(name='Location', value='http://127.0.0.1:8080/data/index.html')


def task5_test_html(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 200, 'OK'
    with open("task5.html", "rb") as f:
        response.body = f.read()


def task5_cookie_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        response.status_code, response.reason = 200, 'OK'
        response.add_header(name='Set-Cookie', value='Authenticated=yes')
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_cookie_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    try:
        cookie = {i.split('=')[0]: i.split('=')[1] for i in request.get_header(key='Cookie').split(';')}
    except AttributeError:
        response.status_code, response.reason = 403, 'Forbidden'
        return

    if cookie['Authenticated'] == 'yes':
        response.status_code, response.reason = 200, 'OK'
        with open('./data/test.jpg', 'rb') as file:
            response.add_header(name='Content-Type', value=get_mimetype('/data/test.jpg'))
            content = file.read()
            response.add_header(name='Content-Length', value=str(len(content)))
            response.body = content
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_session_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        session_key = random_string()
        while session_key in server.session:
            session_key = random_string()
        server.session[session_key] = obj['username']
        response.status_code, response.reason = 200, 'OK'
        response.add_header(name='Set-Cookie', value=f'SESSION_KEY={session_key}')
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_session_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    try:
        cookie = {i.split('=')[0]: i.split('=')[1] for i in request.get_header(key='Cookie').split(';')}
    except AttributeError:
        response.status_code, response.reason = 403, 'Forbidden'
        return

    if cookie['SESSION_KEY'] in server.session:
        response.status_code, response.reason = 200, 'OK'
        with open('./data/test.jpg', 'rb') as file:
            response.add_header(name='Content-Type', value=get_mimetype('/data/test.jpg'))
            content = file.read()
            response.add_header(name='Content-Length', value=str(len(content)))
            response.body = content
    else:
        response.status_code, response.reason = 403, 'Forbidden'


# TODO: Change this to your student ID, otherwise you may lost all of your points
YOUR_STUDENT_ID = 12010324

http_server = HTTPServer(config.LISTEN_PORT)
http_server.register_handler("/", default_handler)
# Register your handler here!
http_server.register_handler("/data", task2_data_handler, allowed_methods=['GET', 'HEAD'])
http_server.register_handler("/post", task3_json_handler, allowed_methods=['GET', 'HEAD', 'POST'])
http_server.register_handler("/redirect", task4_url_redirection, allowed_methods=['GET', 'HEAD'])
# Task 5: Cookie
http_server.register_handler("/api/login", task5_cookie_login, allowed_methods=['POST'])
http_server.register_handler("/api/getimage", task5_cookie_getimage, allowed_methods=['GET', 'HEAD'])
# Task 5: Session
http_server.register_handler("/apiv2/login", task5_session_login, allowed_methods=['POST'])
http_server.register_handler("/apiv2/getimage", task5_session_getimage, allowed_methods=['GET', 'HEAD'])

# Only for browser test
http_server.register_handler("/api/test", task5_test_html, allowed_methods=['GET'])
http_server.register_handler("/apiv2/test", task5_test_html, allowed_methods=['GET'])


def start_server():
    try:
        http_server.run()
    except Exception as e:
        http_server.listen_socket.close()
        print(e)


if __name__ == '__main__':
    start_server()
