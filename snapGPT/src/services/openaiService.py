import openai
import os

from configs.openai_params import model_params as mp

# Services for:
# 1. GPT-3 / chatGPT
#   = @in: text, @out: text
# 2. DALL-E
#   = @in: text, @out: image_file
class OpenAIService:
    def __init__(self,OPENAI_API_KEY):
        self.api_key = OPENAI_API_KEY
        self.openai = openai

    # Connect to OpenAi API using API_KEY
    def connect(self):
        print("[connect] OpenAI")
        self.openai.api_key = self.api_key
        return self.openai


    def openai_test(self):
        return True

    # @in receives resume as text 
    # @out: updated resume as text
    def resume_grammar_correct(self, resume):
        corrected_resume = self.__run_gpt_prompt("grammar_correction", resume)
        return corrected_resume


    # @in: resume as text
    # Performs sequence of gpt prompts:
    #   1. embed_keywords
    #   2. tone_improvement
    def resume_embed(self, resume, keywords):
        prompt = ("keywords to embed into resume: " +
                keywords + "\n"
                "resume: " + 
                resume + ".\n")
        embeded_resume = self.__run_gpt_prompt("embed_keywords", prompt)
        return embeded_resume
        


    # @TODO:
    # @in: resume as text + job description
    #   - determines correlation between resume and jd's contents
    # @out: a score between [0,1].
    # def score_resume_jd_fit(resume, jobDesc):
    #     return 0


    def __run_gpt_prompt(self, command, user_prompt):
        if (len(user_prompt) == 0):
            return 0
        user_prompt = " \"" + user_prompt + "\"."
        gpt_prompt = mp[command]["prompt"] + user_prompt
        print("gpt_prompt: \n" + gpt_prompt + "\n")
        response = openai.Completion.create(
            model=mp[command]["model"],
            prompt=gpt_prompt,
            temperature=mp[command]["temperature"],
            max_tokens=mp[command]["max_tokens"],
            top_p=mp[command]["top_p"],
            frequency_penalty=mp[command]["frequency_penalty"],
            presence_penalty=mp[command]["presence_penalty"]
        )
        # print("\n\n__run_gpt_prompt Response:\n" + response + "\n\n")
        return response

    # make resume look "prettier"
    #   DALL-E???
    # def redesign_resume_structure(resume):



    



    


    





        
