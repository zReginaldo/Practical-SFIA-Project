FROM python:3.7
WORKDIR /app
COPY ./requirements.txt .
COPY ./english-words/words_alpha.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install flask 
COPY . .
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
