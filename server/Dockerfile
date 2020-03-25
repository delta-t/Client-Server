# In our example we want to import the python image from Dockerhub
FROM python:latest

STOPSIGNAL SIGINT
# In order to launch our python code, we must import the "server"-scripts and 'index.html' file.
# Here we put files at the image '/server/' folder.
COPY . /server/

# This command changes the base directory of the image.
# Here we define '/server/' as base directory where all commands will be executed
WORKDIR /server/

RUN pip install -r requirements.txt