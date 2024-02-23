# Optimuse

## Overview

Optimuse is a backend application developed in Python, designed to process and analyze energy data from JSON files. The application efficiently organizes data related to assets' energy demands, outputs, and systems, and exposes a FastAPI endpoint for retrieving processed data based on asset IDs.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Clone the repository:

```
git clone https://github.com/kburakf/optimuse.git
```

2. Navigate to the project directory:

```
cd optimuse
```

3. Create and activate a virtual environment:

- macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

4. Install the dependencies:

```
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI application with Uvicorn:

```
uvicorn app.main:app --reload
```

## Running with Docker Compose

Docker Compose simplifies running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes.

To build and run the application using Docker Compose:

1. Navigate to the project directory where `docker-compose.yml` is located.

2. Build and start your containers:

```
docker-compose up --build
```

The `--build` flag is optional and ensures that your Docker image is built with the latest changes. If your Docker Compose setup does not require building an image (e.g., using an image directly), you can omit this flag.

3. The application should now be accessible at `http://localhost:8080`.

To stop and remove the containers defined in the Docker Compose file, use:

```
docker-compose down
```

This command stops all the running containers and removes them along with the networks that were created.

## Data Files

This application processes and analyzes energy data from JSON files. To facilitate easy setup and usage, we store these JSON files under the `app/data` folder. Ensure any data files you wish to use with the application are placed in this directory.

## API Usage

To retrieve processed energy data for a specific asset, make a GET request to:
`http://localhost:8080/assets/{asset_id}`

## Project Structure

- `app/`: Main application directory.
  - `dao/`: Data Access Object layer for loading and organizing JSON data.
  - `models/`: Pydantic models for data validation and schema.
  - `processor/`: Processor layer for calculating energy-related metrics.
  - `utils/`: Utility functions that support various operations within the application.
  - `routers/`: FastAPI routers that define the endpoints and their logic.
  - `main.py`: FastAPI application entry point.
- `tests/`: Contains automated tests for the application, ensuring reliability and stability.

## Testing

This project uses `pytest` for running automated tests to ensure the application's reliability and stability. To execute the tests, navigate to the project's root directory and run:

```
pytest
```

This command will automatically find and run all tests defined in the `tests/` directory, adhering to the naming conventions for test files and methods. Ensure you have `pytest` installed in your environment, which can be done by running `pip install pytest` if it's not already installed.

## Contributing

Contributions to Optimuse are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
