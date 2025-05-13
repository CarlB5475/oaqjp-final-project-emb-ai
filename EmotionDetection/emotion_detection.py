import requests
import json


def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=input_json, headers=headers)

    # Format the response via json to turn into a Python dictionary.
    formatted_res = json.loads(res.text)

    # If the status code is 400, return the emotion_output
    # with the same keys, but all their values are None.
    if res.status_code == 200:
        # Extract the emotion scores and find the dominant emotion.
        emotion_scores = formatted_res['emotionPredictions'][0]['emotion']
        dominant_emotion = None
        max_score = 0
        emotion_output = {}
        for emotion, score in emotion_scores.items():
            emotion_output[emotion] = score
            if max_score < score:
                max_score = score
                dominant_emotion = emotion
        emotion_output['dominant_emotion'] = dominant_emotion

    elif res.status_code == 400:
        emotion_output = {}
        emotion_output['anger'] = None
        emotion_output['disgust'] = None
        emotion_output['fear'] = None
        emotion_output['joy'] = None
        emotion_output['sadness'] = None
        emotion_output['dominant_emotion'] = None

    return emotion_output
