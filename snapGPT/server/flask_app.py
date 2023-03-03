import os
import sys
import ast
import multiprocessing
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv("./.env")
COHERE_KEY = os.getenv("API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# Get the absolute path of the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the src directory to the Python path
src_dir = os.path.join(parent_dir, "src")
sys.path.append(src_dir)

# Import the services
# from services.cohereService import CohereService
from services.openaiService import OpenAIService

# Flask app code...


app = Flask(__name__)


@app.route("/resume/correct", methods=["PATCH"])
def http_snap_resume():
    data = request.get_json()
    resume_text = data.get("resume")
    # print("forking process")
    # openai_process = multiprocessing.Process(
    #     target=openai_start,
    #     args=(OPENAI_KEY)
    # )
    # openai_process.start()
    oa = OpenAIService(OPENAI_KEY)
    oa.connect()
    corrected_resume = oa.resume_grammar_chatgpt(resume_text)
    return jsonify({"resume": corrected_resume}), 200


@app.route("/resume/embed", methods=["PATCH"])
def http_embed_resume():
    data = request.get_json()
    resume_text = data.get("resume")
    embed_keywords = data.get("keywords")
    oa = OpenAIService(OPENAI_KEY)
    oa.connect()
    embeded_resume = oa.resume_embed(resume_text, embed_keywords)
    return jsonify({"resume": embeded_resume}), 200


# @app.route("/colink/status/new", methods=["GET"])
# def http_show_new_colink_result():
#     data = request.get_json()
#     # @TODO pass/read colink_id from params instead of request body
#     colink_id = data.get("colink_id")
#     # If sequence is completed, response will exist in database
#     # else:
#     status_code = 404
#     result = {"result": f'your colink response with id:{colink_id} is not yet ready. Check again in 2-3 minutes.'}
#     return jsonify(result), status_code


# @app.route("/colink/sequence", methods=["POST"])
# def http_colink_sequence():
#     # Get the request payload
#     data = request.get_json()
#     # Extract the required values from the payload
#     context_prompt = data.get("context_prompt")
#     user_prompt = data.get("user_prompt")
#     arr_prompts = [context_prompt, user_prompt]
#     seq = ast.literal_eval(data.get("seq"))
#     model_size = data.get("model_size")
#     # model_parameters =...
#     # print(f'context_prompt: {context_prompt}\nuser_prompt: {user_prompt}\nsequence:{seq}')
#     print("forking process")
#     colink_process = multiprocessing.Process(
#         target=cohere_start,
#         args=(COHERE_KEY,model_size, seq, arr_prompts)
#     )
#     colink_process.start()
#     # colink_process.join()
#     # @TODO: based on colinkSequence complexity, can we provide an estimate wait time for the
#     #   user check back if result is ready?
#     status_code = 200
#     result = { "colink_response": "We received your request. We're on it. Send a GET /colink/new?id=4 request in a few minutes to obtain results" }
#     # Return the result
#     return jsonify(result), status_code


@app.route("/openai/test", methods=["GET"])
def test_openai():
    status_code = 200
    oa = OpenAIService(OPENAI_KEY)
    test = oa.openai_test()
    return jsonify({
        "test": "success" if test else "error"
    }), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181)
