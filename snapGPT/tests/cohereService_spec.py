import unittest
import cohere
# from '../src/cohereService' import CohereService

class TestCohereService(unittest.TestCase):
    def setUp(self):
        self.corereService =?
        # self.service = CohereService('<API_KEY>', 'generate')

    def test_connect(self):
        self.assertIsNotNone(self.service.connect())

    def test_linkedSequence(self):
        context_prompt = [ 'This is the context prompt. Used to "lightUp" ' ]
        user_prompt = [ 'This is the user prompt.' ]
        seq1 = [('pc', 1, user_prompt)]
        seq2 = [('pg',1,user_prompt), ('pc',1,...)]
      
        output_words = self.service.linkedSequence(context_prompt, user_prompt, seq)
        self.assertIsNotNone(output_words)

    def test_performClassify(self):
        m = 'small'
        i = context_prompt + user_prompt
        ex = [ 'This is an example.' ]
        response = self.service.__performClassify(m, i, ex)
        self.assertIsNotNone(response)

    def test_performGenerate(self):
        p = context_prompt + user_prompt
        response = self.service.__performGenerate(p)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()