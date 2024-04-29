import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
        
    if response.status_code == 400:
        anger='None'
        disgust='None'
        fear='None'
        joy='None'
        sadness='None'
        dominant_emotion='None'
    
    else:
        formatted_response=json.loads(response.text)
        formatted_emotion=formatted_response['emotionPredictions'][0]

        anger = formatted_emotion['emotion']['anger']
        disgust = formatted_emotion['emotion']['disgust']
        fear = formatted_emotion['emotion']['fear']
        joy = formatted_emotion['emotion']['joy']
        sadness = formatted_emotion['emotion']['sadness']
    
        dominant_emotion_score=max(anger,disgust,fear,joy,sadness)
    
        if dominant_emotion_score==anger:
            dominant_emotion='anger'
        elif dominant_emotion_score==disgust:
            dominant_emotion='disgust'
        elif dominant_emotion_score==fear:
            dominant_emotion='fear'
        elif dominant_emotion_score==joy:
            dominant_emotion='joy'
        elif dominant_emotion_score==sadness:
            dominant_emotion='sadness'

    result = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    
    return result
