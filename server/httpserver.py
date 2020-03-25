#!/usr/bin/env python3

# Import of python system libraries
# These libraries wll be used to create the web server
import http.server
import socketserver

if __name__ == '__main__':
    # This variable is going to handle the requests of our client on the server
    handler = http.server.SimpleHTTPRequestHandler

    # Here we define that we want to start the server on port 7777. This information
    # will be useful to us later with docker-compose
    with socketserver.TCPServer(("", 7777), handler) as httpd:
        # This instruction will keep the server running, waiting for requests from the client
        httpd.serve_forever()
