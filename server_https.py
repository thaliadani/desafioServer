import http.server
import ssl

PORT = 8443

server_address = ('', PORT)
handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(server_address, handler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="chave.pem", certfile="cert.pem", server_side=True)

print(f"Servidor HTTPS rodando na porta {PORT}...")
httpd.serve_forever()
