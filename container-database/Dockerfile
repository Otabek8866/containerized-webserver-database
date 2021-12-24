#using base image from dockerhub python:slim
FROM alpine

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

#copy requirements file to container
COPY requirements.txt /app/requirements.txt

#setting working directory to /app
WORKDIR /app

#installing requirements pip install ***
RUN pip3 install -r requirements.txt

#copy all things from the current directory to /app in the container
COPY . /app

#open port 5000 to be accessed
EXPOSE 5000

#pre execution command python CMD
ENTRYPOINT ["python3"]

#commands to be exectued ENTRYPOINT then CMD --> python3 server_db.py
CMD ["server_db.py"]