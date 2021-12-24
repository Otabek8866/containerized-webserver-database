#using base image from dockerhub python:slim
FROM python:slim

#copy requirements file to container
COPY requirements.txt /app/requirements.txt

#setting working directory to /app
WORKDIR /app

#installing requirements pip install ***
RUN pip install -r requirements.txt

#copy all things from the current directory to /app in the container
COPY . /app

#open port 5000 to be accessed
EXPOSE 5000

#pre execution command python CMD
ENTRYPOINT ["python"]

#commands to be exectued ENTRYPOINT then CMD --> python server_db.py
CMD ["server_db.py"]
