from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os
import requests
import urllib
from loader import pgbotdb
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
        self.wfile.write('<form action="/page.py">'.encode())
        self.wfile.write('<input type="text" id="coment" name="coment">'.encode())
        self.wfile.write('<input type="submit">'.encode())
        self.wfile.write('</form>'.encode())
        self.wfile.write('</body></html>'.encode())
        req= urllib.parse.unquote(self.requestline)
        req = req.replace('GET /page.py?coment=','').replace(' HTTP/1.1', '')

        name_text = req.split(':')
        print(name_text)
        name = name_text[0]
        text = name_text[-1]
        print(name, text)
        pgbotdb.add_text(name, text)

# %3A

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("127.0.0.1", 8000)
    httpd = server_class(server_address, handler_class)

    httpd.serve_forever()

def readData(comentmas):
    data = pgbotdb.get_chat_data(chat_id=1)
    for dat in data:
        name = dat[2]
        text = dat[3]
        print(name,text)

    comentmas.append()




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