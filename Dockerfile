# Dockerfile
FROM  python:3.11.5-alpine

# Modulos requeridos
# RUN pip install nombre_modulo

# Copia el archivo client_HTTP al directorio /opt/  dentro 
# de la imagen
ADD clientHTTP.py /opt/
