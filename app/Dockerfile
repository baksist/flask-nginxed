FROM python:3-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "unix:/sockets/app.sock", "server:make_app()"]