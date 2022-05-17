from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>CHAT</title></head>'.encode())
        self.wfile.write('<body>'.encode())
        self.comentmas=[]
        readData(self.comentmas)
        for el in self.comentmas:
            self.wfile.write(f'<h3>{el}</h3>'.encode())
        self.wfile.write('</body></html>'.encode())

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("127.0.0.1", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def readData(comentmas):
    with open("data.txt",'r') as file:
        for line in file:
            comentmas.append(line)


'''
def writeData(comentmas):
    while(True):
        for i in comentmas:
            print(i,end='')
        coment=input()+'\n'
        comentmas.append(coment)
        with open("data.txt",'a+') as file:
            file.write(coment)
        os.system('cls')
'''


run(handler_class=HttpGetHandler)