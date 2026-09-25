FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY persistent_auditor.py . 
CMD ["python", "persistent_auditor.py"]

# What this Dockerfile does (line by line):
# use the official python runtime image as the base image
# establish an active working directory in the container
# copy our local auditor.py file into the container workspace
# define the execution command to run when the container starts