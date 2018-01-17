#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.









from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Saim, HTTP!\n".encode())
        print(self.path)


if __name__ == "__main__":
    server_address=("",8000)
    httpd=HTTPServer(server_address,HelloHandler)
    httpd.serve_forever()
