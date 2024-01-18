import requests
import json


def emotion_detector(text_to_analyse):
    _emotion_list = ["anger", "disgust", "fear", "joy", "sadness"]

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=input, headers=header)
    formatted_response = json.loads(response.text)

    # _emotion_dict = {
    #     e: formatted_response["emotionPredictions"][0]["emotion"][e]
    #     for e in _emotion_list
    # }
    _emotion_dict = {}
    for em in _emotion_list:
        _emotion_dict[em] = formatted_response["emotionPredictions"][0]["emotion"][em]

    emotion_dict = {
        k: v
        for k, v in sorted(_emotion_dict.items(), key=lambda item: item[1], reverse=True)
    }

    dominant_emotion = emotion_dict.values()[0]
    emotion_dict["dominant_emotion"] = dominant_emotion

    return emotion_dict
