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

    # Return a formatted string with f-strings for dynamic values
    response = (f"For the given statement, the system response is 'anger': {output['anger']}, 'disgust': {output['disgust']}, "
                f"'fear': {output['fear']}, 'joy': {output['joy']}, and 'sadness': {output['sadness']}. "
                f"The dominant emotion is <b>{output['dominant_emotion']}</b>")
    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)