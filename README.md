# FastAPI Basic Health Check API

A simple FastAPI application demonstrating basic routing, authentication, CORS handling, and environment variable usage.

## Project Structure

-   `main.py`: The core FastAPI application, defining routes and logic.
-   `requirements.txt`: Lists Python dependencies.
-   `.env.example`: Example environment variables for configuration.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

## Features

### Routes

-   **GET `/health`**:
    -   Returns `{"status": "ok"}`.
    -   Used for basic health checks of the API.

-   **POST `/api/login`**:
    -   Expects a JSON body with `username` and `password`.
    -   Authenticates against a predefined list of users:
        -   `matt` / `password`
        -   `kate` / `password`
        -   `anne` / `password`
    -   Returns `{"status": "ok"}` if credentials match.
    -   Returns `401 Unauthorized` with `{"detail": "Incorrect username or password"}` if credentials do not match.

-   **POST `/api/logout`**:
    -   Always returns `{"status": "ok"}` (200 OK status code).
    -   Placeholder for future logout logic.

-   **POST `/api/ask`**:
    -   Placeholder route, always returns `{"status": "ok"}`.

### CORS (Cross-Origin Resource Sharing)

-   CORS enablement is optional and controlled by the `USE_CORS` environment variable.
-   **Default:** `USE_CORS=False` (CORS is disabled).
-   **To Enable:** Set `USE_CORS=True` in your `.env` file or environment.
-   The application prints the current CORS enablement status on startup.

### Environment Variables

-   Uses `python-dotenv` to load environment variables from a `.env` file.
-   Refer to `.env.example` for available variables.

## Setup and Running

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone git@github.com:matthew-trump/fastapi-basic.git
    cd fastapi-basic
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    -   Copy `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
    -   Edit `.env` to set `USE_CORS=True` if you wish to enable CORS.

4.  **Run the application:**
    ```bash
    python main.py
    ```
    The API will be available at `http://localhost:3003`.

## Usage

-   **Health Check:** Access `http://localhost:3003/health` in your browser or with `curl`.
-   **Login:** Send a POST request to `http://localhost:3003/api/login` with a JSON body like `{"username": "matt", "password": "password"}`.
-   **Logout:** Send a POST request to `http://localhost:3003/api/logout`.