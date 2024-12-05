#utiliza una imagen de Python como base 
FROM python:latest
WORKDIR /servidor
COPY servidor.py .
RUN pip install flask

EXPOSE 5002

CMD ["python", "servidor.py"]