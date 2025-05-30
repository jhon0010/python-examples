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


### Stopping MongoDB
To stop the MongoDB Docker container, run:

```bash
docker compose down
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


# Run the data scripts to play with orders csv 

You can run the data scripts to play with the orders CSV file. The script is designed to read the CSV file and perform some operations on it.
To run the data scripts, execute the following command:

```bash
python3 src/data/pandas_polars.py
python3 src/data/matplot_example.py
``` 
You can find other python scripts in the `src/data` directory that interact with the `orders.csv` file.

This will read the `orders.csv` file and perform the operations defined in the script.


# Run locus load tests 

To run the load tests using Locus, you can use the following command:

```bash
locust -f test/locus_test/locus_user_api_test.py
```
This command will start the Locus web interface, which you can access at `http://localhost:8089` to configure and run your load tests.

# Run script to run the math benchmark 

To run the math benchmark script, you can use the following command:

```bash
python3 tests/benchmark/main.py
```

