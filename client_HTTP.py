import socket
import sys

def processArguments():
    # Recibe de la linea de comandos un argumento
    host_server = sys.argv[1]
    arguments = [host_server]
    return arguments

def constructHTTPRequest(host_server):
    # Construccion de HTTP request line
    http_method = "GET"
    url = "/"
    version = "HTTP/1.1"
    request_line = http_method+" "+url+" "+version+"\r\n"

    host = "HOST: "+host_server
    user_agent = "User-Agent: Google Chrome on Windows 10 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    accept_encoding = "Accept-Encoding: identity"
    accept_language = "Accept-Language: en-US"

    header_lines = host+"\r\n" + \
                user_agent+"\r\n"+\
                accept_encoding+"\r\n"+\
                accept_language+"\r\n"
    # La peticion HTTP debe terminar con un retorno de carro y
    # un salto de linea 
    blank_line = "\r\n"

    HTTP_request = request_line + \
                    header_lines + \
                    blank_line
    return HTTP_request

def TCPconnection(host_server, HTTP_request):
    # Crea un socket de TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexion del cliente al servidor dado
    s.connect((host_server,80))

    # Envia la petición al servidor
   # s.send(HTTP_request)
    s.send(HTTP_request.encode())  
 
    # Imprimira en pantalla la HTTP response mientras reciba información del 
    #servidor
    while True:
        HTTP_response = s.recv(1024)
        if HTTP_response == "": break
        print(HTTP_response)
    # Se cierra la conexion con el servidor
    s.close()

    print("\n\nConexion con el servidor finalizada\n")

arguments = processArguments()
HTTP_request = constructHTTPRequest(*arguments)
TCPconnection(arguments[0],HTTP_request)