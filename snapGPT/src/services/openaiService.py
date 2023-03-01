import openai
import os


# Services for:
# 1. GPT-3 / chatGPT
#   = @in: text, @out: text
# 2. DALL-E
#   = @in: text, @out: image_file
# 3. Whisper
#   = @in: audio_file, @out: text
class OpenAIService:
    def __init__(self,API_KEY):
        self.api_key = API_KEY
        self.openai = openai

    # Connect to OpenAi API using API_KEY
    def connect():
        self.openai.api_key = self.api_key
        print("[connect] OpenAI")


    def openai_test(self):
        return True


    # (Mandatory) fix grammar issues
    # improve grammatical structure / cohesion
    def grammar_correction():
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Correct this to standard English:\n\nShe no went to the market.",
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response


    # if resume is not coherent
    #   output coherent suggestions before proceeding
    def check_coherence():


    # add specific words into resume
    #   example: some keywords from Job Description
    def embed_keywords(list_keywords):


    # (Optional) Re-write resume according to a selected 'tone':
    #   example: professional tone, formal, informal
    def tone_modification(tone):


    # make resume look "prettier"
    #   DALL-E???
    def redesign_resume_structure(resume):



    



    


    





        
