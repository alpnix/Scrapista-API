# Use Python 3.9 base image
FROM python:3.9

# Set working directory in the container
WORKDIR /code

# Copy requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application files to the container
COPY ./app /code/app

# Set environment variable for the port (change as needed)
ENV PORT="8000"

# Expose the specified port
EXPOSE $PORT

# Command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
