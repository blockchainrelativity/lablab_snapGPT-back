# FILE NOT IN USE



import sys
import os
from dotenv import load_dotenv

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")

from staic import CohereService


colink = {
  "context": "Profession, is what we choose to do.It's the work we put in, to see our dreams come true.For some, it's a teacher, or a doctor or a nurse.For others, a builder, an artist or a verse.",
  "user_prompt": "wassup"
}

arr_colinks = [('pg', 5)]



if __name__ == '__main__':
  print('[Initiating (coLink + Cohere Layer)]')
  co_service = CohereService(API_KEY, "medium")

  print('[connecting] awaiting connection to Cohere API Client...')
  if (co_service.connect()):
    print('[successfully connected to CohereAPI:')
    print(co_service.co)
  else:
    print('...[no connection]. Exiting program.')
    sys.exit(-1)


  
  print('[Cohere<=>Colink Request] colinkSequence starting...')
  response = co_service.colinkSequence(colink["context"], "", arr_colinks)
  print('...[done] colinkSequence response:')
  print(response)

  sys.exit(0)



# def main():
#     # your code here
#     raise SystemExit("Exiting with error code -1")

# if __name__ == "__main__":
#     try:
#         main()
#     except SystemExit as e:
#         print(e)
#         sys.exit(-1)
    