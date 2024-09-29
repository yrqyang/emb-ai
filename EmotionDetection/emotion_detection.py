import requests
import json

def emotion_detector(text_to_analyse):  
    """
    Call emotion detector in Watson NLP libraries and return the emotion prediction
    
    Parameters:
    text_to_analyse: string

    Returns:
    dict: A dictionary with the emotion scores and the dominant emotion.
    """

    # API configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Extract the emotion scores from the first prediction
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # List the emotion scores
        result = {emotion: score for emotion, score in emotions.items()}
    
        # Add the dominant emotion to the dictionary
        result['dominant_emotion'] = dominant_emotion
    
    elif response.status_code == 400: 
        # None for all keys
        result ={
                'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None
            }

    return result
