#!/usr/bin/env python3

# Import of python system library. This library is used to
# download the 'index.html' from server
import urllib.request


class HttpClient:
    def __init__(self, port: int):
        self.port = port
        self.fp = None

    def send_request(self):
        self.fp = urllib.request.urlopen(f'http://localhost:{self.port}/')
        return self.fp.read().decode('utf-8')

    def close(self):
        self.fp.close()


if __name__ == '__main__':
    client = HttpClient(port=7777)
    print(client.send_request())
    client.close()
