from . import emotion_detection
"""Detect emotions using the IBM Watson NLP service."""

import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not text_to_analyze or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10,
        )

        if response.status_code == 400:
            return empty_result

        response.raise_for_status()

        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        required = ("anger", "disgust", "fear", "joy", "sadness")

        scores = {
            emotion: emotions[emotion]
            for emotion in required
        }

        scores["dominant_emotion"] = max(
            required,
            key=lambda emotion: scores[emotion],
        )

        return scores

    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
    ):
        return empty_result
