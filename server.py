"""
Emotion Detector Web Application Module

This module creates a simple Flask-based web application that provides emotion detection
for a given input text using the Watson NLP Emotion Detection API. It contains two main 
routes: one for serving the index page and another for performing emotion analysis on 
the input text provided by the user.

Routes:
    - `/emotionDetector`: Accepts text input via query parameters, sends it to the emotion 
      detection API, and returns a formatted response with the detected emotions and their scores.
    - `/`: Renders the `index.html` template, which is the homepage of the web application.

Functions:
    - sent_analyzer(): Retrieves the input text from the query parameters, analyzes it using 
      the Watson NLP API, and returns the emotion scores along with the dominant emotion. If 
      the input is invalid or if the API fails, an error message is returned.
    - render_index_page(): Renders the `index.html` page, which is the entry point of the web 
      application.

Dependencies:
    - Flask: Used for setting up the web application and handling HTTP routes.
    - emotion_detector: A function from the `EmotionDetection.emotion_detection` module that 
      calls the Watson NLP Emotion Detection API and returns a dictionary with emotion scores 
      and the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Send input text to analyze on the server

    Returns: 
    response: string, formatted as the customer requirements 
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detection function
    output = emotion_detector(text_to_analyze)

    # Check if the label is None, indicating an error or invalid input
    if output['dominant_emotion'] is None:
        response = "Invalid text! Please try again!."
    else:
        # Return a formatted string with f-strings for dynamic values
        response = (f"For the given statement, "
                    f"the system response is 'anger': {output['anger']}, "
                    f"'disgust': {output['disgust']}, "
                    f"'fear': {output['fear']}, "
                    f"'joy': {output['joy']}, "
                    f"and 'sadness': {output['sadness']}. "
                    f"The dominant emotion is <b>{output['dominant_emotion']}</b>")
    return response

@app.route("/")
def render_index_page():
    """
    html render
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
