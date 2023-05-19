# LabLab SnapGPT Back

This repository contains the backend code for the LabLab SnapGPT project, which is a web application that generates job postings and resumes for applicants and hiring entities using the OpenAI GPT-3 language model. The backend is built using Python and the Flask framework.

## Installation

To install and run the backend, follow these steps:

1. Clone the repository: `git clone https://github.com/blockchainrelativity/lablab_snapGPT-back.git`
2. Navigate to the project directory: `cd lablab_snapGPT-back`
3. Install the required packages: `pip install -r requirements.txt`
4. Set up the environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `COHERE_API_KEY`: A secret key for Cohere
5. Start the server: `python server/flask_app.py`

## Usage

Once the server is running, you can send aasdf POST request to the `/resume/correct` endpoint to generate a resume body. 
The backend provides two main endpoints for working with resumes:

### '/resume/correct'
The /resume/correct endpoint can be used to correct and improve the grammar and punctuation of a given resume. The endpoint takes a single parameter, text, which is a string containing the resume to be corrected. Here's an example of how to use the endpoint:

```
import requests

text = "I is a software developer. I has 5 years of experience in programing."
response = requests.post("http://localhost:5000/resume/correct", json={"text": text})
corrected_text = response.json()["corrected_text"]
print(corrected_text)
```


### '/resume/embed'

The /resume/embed endpoint can be used to embed a given resume into a fixed-length vector space using the OpenAI GPT-3 language model. The endpoint takes a single parameter, text, which is a string containing the resume to be embedded. Here's an example of how to use the endpoint:

```
import requests

text = "I am a software developer with 5 years of experience in programming. I am proficient in Python, Java, and C++."
response = requests.post("http://localhost:5000/resume/embed", json={"text": text})
embedding = response.json()["embedding"]
print(embedding)
```

## Contributing

If you want to contribute to the project, feel free to fork the repository and submit a pull request with your changes. Please make sure to follow the existing code style and include tests for any new functionality.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

If you have any questions or issues, feel free to contact the project maintainer.

