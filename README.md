# Gemistream

Gemistream is a Streamlit application designed to [brief description of what your application does]. This project aims to [brief description of the project's goals or objectives].

## Features

- Feature 1
- Feature 2
- Feature 3

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/pratama404/gemistream.git
    cd gemistream
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set the environment variable for the port (if needed):

    ```sh
    export PORT=8501  # On Windows use `set PORT=8501`
    ```

2. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to:

    ```
    http://localhost:8501
    ```

## Configuration

If your application requires specific configuration, you can set them in the `config.toml` file or through environment variables.

### Example `config.toml`

```toml
[server]
port = "$PORT"  # Make sure to set the PORT environment variable
