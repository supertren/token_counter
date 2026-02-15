import unittest
from unittest.mock import patch, MagicMock
import logging
from main import get_token_count

# Disable logging for tests to keep the output clean
logging.disable(logging.CRITICAL)

class TestGetTokenCount(unittest.TestCase):

    @patch('main.genai.GenerativeModel')
    def test_get_token_count_success(self, mock_generative_model):
        """
        Test that get_token_count returns the correct token count on a successful API call.
        """
        # Arrange: Configure the mock to simulate a successful API response.
        mock_response = MagicMock()
        mock_response.total_tokens = 42
        
        mock_model_instance = MagicMock()
        mock_model_instance.count_tokens.return_value = mock_response
        
        mock_generative_model.return_value = mock_model_instance

        prompt = "This is a test prompt."
        model = "gemini-test-model"

        # Act: Call the function under test.
        token_count = get_token_count(prompt, model)

        # Assert: Verify the function behaved as expected.
        self.assertEqual(token_count, 42)
        mock_generative_model.assert_called_once_with(model)
        mock_model_instance.count_tokens.assert_called_once_with(prompt)

    @patch('main.genai.GenerativeModel')
    def test_get_token_count_api_error(self, mock_generative_model):
        """
        Test that get_token_count returns -1 when the API call fails.
        """
        # Arrange: Configure the mock to raise an exception.
        api_error_message = "API connection failed"
        mock_model_instance = MagicMock()
        mock_model_instance.count_tokens.side_effect = Exception(api_error_message)
        
        mock_generative_model.return_value = mock_model_instance

        # Act: Call the function.
        token_count = get_token_count("This prompt will fail.", "gemini-test-model")

        # Assert: Verify the function returns the error code.
        self.assertEqual(token_count, -1)