import cohere
from multiprocess import join_active_children, gc_collect_exit, sleeep

def cohere_start(api_key, model_size, seq, arr_prompts):
    print("\n********** new process *************\n")
    co = CohereService(api_key, model_size, seq, arr_prompts)
    co.connect()
    result = co.colinkSequence()
    #@TODO: write to Database.
    sleeep(1)
    join_active_children()
    gc_collect_exit(0)


class CohereService:
    def __init__(self, api_key, model_size,seq, arr_prompts):
        self.api_key = api_key
        self.model_size = model_size
        self.seq = seq
        self.prompts = arr_prompts
        self.co = None
        # self.co = connect()
        # self.colinkSequence()

    def connect(self):
        self.co = cohere.Client(self.api_key)
        return self.co
        

    # links one request to another, or back to same one.
    # setFlowSequence([('pc',1), ('pg',1000), ('pc',1)])
    #   Classifies once +=> generates twice => classifies once
    def colinkSequence(self):
      # create file here, and open it.
        transform_words = ""
        for prompt in self.prompts:
            transform_words+=prompt
        for tupl in self.seq:
            cycles = tupl[1]
            # @TODO: can we do this with functional programming paradigm rather than a while loop?
            while (cycles > 0):
                print(f'\n****Cycle: {-1*(cycles - tupl[1])+1}***')
                cycles -=1
                if tupl[0] == 'pg':
                    transform_words=self.__performGenerate(
                        transform_words)
                elif tupl[0] == 'pc':
                    transform_words=self.__performClassify(
                        transform_words,
                        (context_prompt + user_prompt))
                else:
                    continue
        return transform_words

    def __performClassify(self,i,ex):
        if not (self.co):
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.classify(
                model=self.model_size,
                inputs=i,
                examples=ex
            )
            print('Classification: {}'.format(response.classifications))
            return response.classifications


    def __performGenerate(self, p):
        if not self.co:
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.generate(
                model=self.model_size, #'command-xlarge-nightly'
                prompt=p,
                max_tokens=75,
                temperature=3.0,
                k=0,
                p=0.70,
                frequency_penalty=0,
                presence_penalty=0,
                stop_sequences=[],
                return_likelihoods='ALL')
            print('GenTextElabo: {}'.format(response.generations[0].text))
            return response.generations[0].text


  # @TODO: graphSequence
      
      # graphSequence
    # def graphSequence(context_prompt, user_prompt, seq):    


