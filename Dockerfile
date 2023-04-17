# imagem base
FROM python:3.9

# diretório de trabalho
WORKDIR /app

# copia o arquivo requirements.txt para o diretório de trabalho
COPY . .

# instala as dependências do projeto
RUN pip install -r requirements.txt

#RUN python manage.py makemigrations
#RUN python manage.py migrate

# expõe a porta 8000
EXPOSE 8000

# comando para rodar o servidor
CMD ["python", "calorias/manage.py", "runserver" ,"0:8000"]