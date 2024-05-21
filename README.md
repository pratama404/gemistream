# Gemistream

Gemini's functionalities are seamlessly integrated into Tera Chat to enhance user interactions and experiences. The main integration revolves around two key features: "Tanya Tera" and "Cerita Tera."
Tanya Tera (Ask Tera):
Users can prompt Tera by typing their questions into the text input provided.
Once the user clicks the "jawab dong!" (answer, please!) button, Gemini's generative model is invoked to generate a response based on the input prompt.
The generated response is then displayed to the user in the app interface, providing them with relevant and engaging answers to their queries.
Cerita Tera (Tera's Story):
Users can prompt Tera by uploading an image along with a message describing the scene or context.
Upon clicking the "Ayo Tera!" (Let's go, Tera!) button, Gemini's generative model processes the image and text prompt to create a unique story.
The generated story is presented to the user, allowing them to explore imaginative narratives inspired by their input.
In both scenarios, Gemini's capabilities are leveraged to enhance the interactivity and depth of user engagement within Tera Chat. Users can prompt Tera in various ways, including asking questions, providing image-based prompts, or combining both text and images to elicit personalized responses and stories from Tera.

## Features

- Auth firebase
- Chatbot Gemini
- Chatbot vision pro
- tanya tera
- cerita tera

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
