FROM python:3.10-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY templates ./templates
COPY app.py ./
EXPOSE 80
CMD python3 app.py
