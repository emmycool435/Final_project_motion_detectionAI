from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Dectection")

@app.route("/emotionDetector")
def get_text():
    text_from_user = request.args.get("textToAnalyze")
    response_from_ai =  emotion_detector(text_from_user)
    anger_score =response_from_ai['anger']
    disgust_score =response_from_ai['disgust']
    fear_score =response_from_ai['fear']
    joy_score =response_from_ai['joy']
    sadness_score =response_from_ai['sadness']
    dominant_emotion = response_from_ai['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! try again"

    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}. The dorminant emotion is {dominant_emotion}."


@app.route("/")
def index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000 )