import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers = header)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotion_list = ["angry", "disgust", "fear", "joy", "sadness"]
    highest = ""

    if anger_score >= disgust_score and anger_score >= fear_score and anger_score >= joy_score and anger_score >= sadness_score:
        highest = emotion_list[0]
    elif disgust_score >= fear_score and disgust_score >= joy_score and disgust_score >= sadness_score:
        highest = emotion_list[1]
    elif fear_score >= joy_score and fear_score >= sadness_score:
        highest = emotion_list[2]
    elif joy_score >= sadness_score:
        highest = emotion_list[3]
    else:
        highest = emotion_list[4]


    return {'anger':anger_score, 'disgust':disgust_score, 'fear': fear_score, 'joy':fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': highest}