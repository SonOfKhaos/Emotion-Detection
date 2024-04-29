'''
    Emotion Detection Python App
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app= Flask("Emotion Detection")
'''
    flask app generated
'''
@app.route('/emotionDetector')
def sent_detection():
    '''
        sending text from web app for detection
    '''
    text_to_analyse= request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    anger= response['anger']
    disgust= response['disgust']
    fear= response['fear']
    joy= response['joy']
    sadness= response['sadness']
    dominant_emotion= response['dominant_emotion']

    if dominant_emotion == 'None':
        return "Invalid text! Please try again!"

    resp1="For the given statement, the system response is 'anger': {}, 'disgust': {},"
    resp2="'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}."
    resp=resp1+resp2
    return resp.format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    '''
        to render index page
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
