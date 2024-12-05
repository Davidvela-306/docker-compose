#utiliza una imagen de Python como base 
FROM python:latest
#crea un directorio de trabajo
WORKDIR /servidor3
#copia el archivo servidor.py al directorio de trabajo
COPY servidor.py .
#instala el paquete flask
RUN pip install flask

#expone el puerto 5003 (el puerto es único para cada servidor)
EXPOSE 5004

#ejecuta el archivo servidor.py
CMD ["python", "servidor.py"]