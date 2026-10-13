
"""Unit tests for the emotion detection module."""

import unittest
from unittest.mock import Mock, patch

import requests

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test emotion detection results and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_happy_text(self, mock_post):
        """Return joy as the dominant emotion for happy text."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.01,
                    "fear": 0.02,
                    "joy": 0.94,
                    "sadness": 0.02,
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.94)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sad_text(self, mock_post):
        """Return sadness as the dominant emotion for sad text."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.01,
                    "fear": 0.04,
                    "joy": 0.03,
                    "sadness": 0.90,
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I feel very sad")

        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertEqual(result["sadness"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, mock_post):
        """Handle a bad request from the service."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("Test input")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_network_error(self, mock_post):
        """Handle a connection timeout."""
        mock_post.side_effect = requests.exceptions.ConnectTimeout

        result = emotion_detector("Test input")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
