from flask import Flask, render_template, request, redirect, flash
from pytubefix import YouTube
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("url")
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()
            download_path = os.getcwd()
            video_stream.download(output_path=download_path)
            flash(f"Download completed! Video saved as: {yt.title}.mp4")
            return redirect("/")
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect("/")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
