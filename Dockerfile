## Use an official Python runtime as a parent image
#FROM python:3.12
#
## Set the working directory in the container
#WORKDIR /usr/src/app
#
## Copy the current directory contents into the container at /usr/src/app
#COPY . .
#
## Install PDM
#RUN pip install pdm==2.9.3
#
## Disable PDM's virtual environment creation
#ENV PDM_USE_VENV=0
#ENV PDM_IGNORE_SAVED_PYTHON=1
#
## Install any needed packages specified in pyproject.toml
#RUN pdm install
#
## Make port 8000 available to the world outside this container
#EXPOSE 8000:8000
#
## Define environment variable
#ENV NAME World
#
## Run app.py when the container launches
#
#CMD ["pdm", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
#
