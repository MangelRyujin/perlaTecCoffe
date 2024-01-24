FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Update pip
RUN pip install --upgrade pip

# Copy requirements file
COPY ./requirements.txt ./



# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .


# Create tables in docker image 
RUN python manage.py makemigrations
RUN python manage.py migrate


# # Run the web server
CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000" ]


