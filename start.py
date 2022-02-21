from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
import cgi
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
