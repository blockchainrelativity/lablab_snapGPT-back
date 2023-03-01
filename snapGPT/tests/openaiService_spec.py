import unittest
from unittest.mock import patch, MagicMock

# Get the absolute path of the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))

server_dir = os.path.join(parent_dir, "server")
sys.path.append(server_dir)

from flask_app import app

class TestApp(unittest.TestCase):

    @patch('app.request')
    @patch('app.OpenAIService')
    def test_http_embed_resume(self, mock_oa_service, mock_request):
        # Set up mock data
        mock_request.get_json.return_value = {
            "resume": "test resume",
            "keywords": ["test", "keywords"]
        }
        mock_oa = MagicMock()
        mock_oa.resume_embed.return_value = "test embedded resume"
        mock_oa_service.return_value = mock_oa

        # Call the function being tested
        response = app.test_client().patch('/resume/embed', json={
            "resume": "test resume",
            "keywords": ["test", "keywords"]
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"resume": "test embedded resume"})

        mock_oa.resume_embed.assert_called_once_with("test resume", ["test", "keywords"])
        mock_oa.connect.assert_called_once()


    @patch('app.request')
    @patch('app.OpenAIService')
    def test_http_snap_resume(self, mock_oa_service, mock_request):
        # Set up mock data
        mock_request.get_json.return_value = {
            "resume": "test resume"
        }
        mock_oa = MagicMock()
        mock_oa.resume_grammar_correct.return_value = "test corrected resume"
        mock_oa_service.return_value = mock_oa

        # Call the function being tested
        response = app.test_client().patch('/resume/correct', json={
            "resume": "test resume"
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"resume": "test corrected resume"})

        mock_oa.resume_grammar_correct.assert_called_once_with("test resume")
        mock_oa.connect.assert_called_once()
