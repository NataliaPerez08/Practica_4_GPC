import socket
import sys

def processArguments():
    # Recibe de la linea de comandos un argumento
    list_user_agents =["Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0","Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"]
    print("User agents:")
    i=0
    for ua in list_user_agents:
        i+=1
        print(i,". ",ua)
        host_server = sys.argv[1]
        http_method = sys.argv[2]
        url = sys.argv[3]
        tmp = int(sys.argv[4])-1
        user_agent = list_user_agents[tmp]
        
        encoding = sys.argv[5]
        connection = sys.argv[6]
        arguments = [host_server,http_method,url,user_agent,encoding,connection]
    return arguments

def constructHTTPRequest(arguments):

    # Construccion de HTTP request line
    http_method = arguments[1]
    url = arguments[2]
    version = "HTTP/1.1"
    request_line = http_method+" "+url+" "+version+"\r\n"

    host_server = arguments[0]
    host = "HOST: "+host_server

    i_ua = arguments[3]
    user_agent = "User-Agent: "+str(i_ua)

    i_encode = arguments[4]
    accept_encoding = "Accept-Encoding: "+str(i_encode)
    
    accept_language = "Accept-Language: es-MX"
    accept = "Accept: text/html,application/xhtml+xml,"

    
    i_connect = arguments[5]
    connection = "Connection: "+str(i_connect)


    header_lines = host+"\r\n" + \
                user_agent+"\r\n"+\
                accept+"\r\n"+\
                accept_language+"\r\n"+\
                accept_encoding+"\r\n"+\
                connection+"\r\n"
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
    HTTP_response = b""
    while True:
        HTTP_response = s.recv(1024)
        if len(HTTP_response) == 0: break
        print(HTTP_response.decode())
    # Se cierra la conexion con el servidor
    s.close()

    print("\n\nConexion con el servidor finalizada\n")

arguments = processArguments()
HTTP_request = constructHTTPRequest(arguments)
print(HTTP_request)
TCPconnection(arguments[0],HTTP_request)