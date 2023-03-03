# LabLab SnapGPT Back

This repository contains the backend code for the LabLab SnapGPT project, which is a web application that generates captions for images using the OpenAI GPT-3 language model. The backend is built using Python and the Flask framework.

## Installation

To install and run the backend, follow these steps:

1. Clone the repository: `git clone https://github.com/blockchainrelativity/lablab_snapGPT-back.git`
2. Navigate to the project directory: `cd lablab_snapGPT-back`
3. Install the required packages: `pip install -r requirements.txt`
4. Set up the environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SECRET_KEY`: A secret key for the Flask application
5. Start the server: `python app.py`

## Usage

Once the server is running, you can send a POST request to the `/generate_caption` endpoint to generate a caption for an image. The request should include the following parameters:

- `image_url`: The URL of the image to generate a caption for
- `model`: The name of the GPT-3 model to use (e.g. `davinci`)

Here is an example using `curl`:

