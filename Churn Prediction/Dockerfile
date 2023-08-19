# docker build -t churn-prediction .
# We use the -t flag for specifying the tag name "churn-prediction"

# docker run -it -p 9696:9696 churn-prediction:latest
# -it in order to the Docker run from terminal and shows the result
# -p to map the 9696 port of the Docker to 9696 port of our machine
# (first 9696 is the port number of our machine and the last one is Docker container port.)

# First install the python 3.8, the slim version have less size
FROM python:3.8.12-slim

# Install pipenv library in Docker 
#RUN pip install pipenv

# we have created a directory in Docker named app and we're using it as work directory 
WORKDIR /app                                                                

# Copy the Pip files into our working derectory 
#COPY ["Pipfile", "Pipfile.lock", "./"]
COPY requirements.txt requirements.txt

# install the pipenv dependecies we had from the project and deploy them 
#RUN pipenv install --deploy --system
RUN pip install -r requirements.txt

# Copy any python files and the model we had to the working directory of Docker 
COPY ["*.py", "model_C=0.1.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "churn_service:app"]