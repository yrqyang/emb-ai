import requests

def emotion_detector(text_to_analyse):
    '''
    Call emotion detector in Watson NLP libraries and return the output text

    Parameters:
    text_to_analyse: string

    Return:
    response.text: string
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    return response.text
