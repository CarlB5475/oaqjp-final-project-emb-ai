'''
The main server application for the Emotion Detector app.
'''
from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion_detector():
    '''
    An API route that retrieves the text input to analyze the
    emotions in it. Returns a response to each of the scores for
    each emotion as well as the dominant emotion from that text input.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response
    res = emotion_detector(text_to_analyze)

    # Extract the emotion scores and the dominant emotion.
    anger_score = res['anger']
    disgust_score = res['disgust']
    fear_score = res['fear']
    joy_score = res['joy']
    sadness_score = res['sadness']
    dominant_emotion = res['dominant_emotion']

    # If the dominant emotion is None, then return an invalid response message.
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the string response to return.
    formatted_res = f"""
            For the given statement, 
            the system response is 'anger': {anger_score}, 
            'disgust': {disgust_score}, 
            'fear': {fear_score}, 'joy': {joy_score}, 
            'sadness': {sadness_score}. 
            The dominant emotion is {dominant_emotion}
        """
    return formatted_res


@app.route("/")
def render_index_page():
    '''Returns the main html page for the emotion detection application.'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
