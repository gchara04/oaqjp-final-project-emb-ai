import requests

URL = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")

HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

OUTPUT_EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")

def is_string_empty(input_string):
    return input_string is None or len(input_string.strip()) == 0

def emotion_detector(text_to_analyze):

    if is_string_empty(text_to_analyze):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post (
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response.raise_for_status()
    response_data = response.json()

    emotion_scores = response_data["emotionPredictions"][0]["emotion"]
    emotion_result = {
            'anger': emotion_scores["anger"],
            'disgust': emotion_scores["disgust"],
            'fear': emotion_scores["fear"],
            'joy': emotion_scores["joy"],
            'sadness': emotion_scores["sadness"],
        }

    top_emotion = max(emotion_result, key=emotion_result.get)
    emotion_result["dominant_emotion"] = top_emotion

    return emotion_result