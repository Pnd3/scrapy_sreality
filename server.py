import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        root = os.getcwd()
        return os.path.join(root, "template.html")

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    httpd.serve_forever()

run_server()