# MongoDB Docker Application

This repository contains a simple setup for running a MongoDB instance using Docker and Docker Compose. It also includes a basic Python script to test the connection to the MongoDB server.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get your MongoDB server running:

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/jhon0010/python-examples.git
cd python-examples
```

### Step 2: Start MongoDB Using Docker Compose
From the root of the cloned directory, run:

```bash
docker compose up -d
```

This command starts a MongoDB instance in a Docker container. The -d flag runs the container in detached mode.

### Step 3: Verify MongoDB is Running
Check if the MongoDB container is running:

```bash
docker ps
```

You should see the MongoDB container listed.

### Step 4: Connect to MongoDB from Python
Run the Python script to test the connection:

```bash
python3 src/mongo_connect.py
```
If the connection is successful, you'll see a message indicating that you're connected to MongoDB.

### Stopping MongoDB
To stop the MongoDB Docker container, run:

```bash
docker-compose down
```


# Create a virtual env using this command

1. Set up a virtual environment (optional but recommended):
   - Create a new directory for your project.
   - Open a terminal or command prompt and navigate to the project directory.
   - Create a virtual environment using the following command:
     ```
     python3 -m venv myenv
     ```
   - Activate the virtual environment:
     - On macOS and Linux:
       ```
       source myenv/bin/activate
       ```
     - On Windows:
       ```
       myenv\Scripts\activate
       ```

2. Install all the required dependencies:
   - While inside the virtual environment, install the requirements using pip:
     ```
     pip install -r requirements.txt
     ```


## Execute the python main code

Using uvicorn to run the file app with the module app in the port 8000.

The reload flag is used to reload the server automatically when the code is changed.

```bash
uvicorn app:app --reload
```

## Run the tests

Go to the test folder and execute the command:

```bash
pytest
```


## View the API documentation with open api (swagger)

Go to the url http://localhost:8000/docs

### Additional Information

The Dockerfile and docker-compose.yml files are configured to use the default MongoDB port 27017.