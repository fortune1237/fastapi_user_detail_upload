# FastAPI User Registration API 🚀

Welcome to our FastAPI User Registration API! This API provides endpoints to register users and retrieve user details.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Middleware](#middleware)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Features
- 🔹 Register a new user with name, age, gender, and marital status
- 🔹 Retrieve user details by user ID
- 🔹 Middleware for logging requests

## Requirements
- Python 3.8+
- FastAPI
- SQLModel
- SQLAlchemy
- uvicorn

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-user-registration.git
    ```
2. Navigate to the project directory:
    ```bash
    cd fastapi-user-registration
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the FastAPI app using uvicorn:
```bash
uvicorn main:app --reload

## Middleware
The API uses middleware to log incoming requests. The logging includes:
- URL
- HTTP Method
- Processing Time
- Host
- IP Address

Logs are stored in `log.txt`.

## Database
The API uses SQLite as the database. The database is created on startup and contains a single table for storing user details.

## Contributing
We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
