"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""
import argparse
import io

import os
import datetime
import requests

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        res = requests.post(args.model_restapi, files={"image":file.read()})
        if res.status_code == 200:
            now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
            img_savename = f"static/{now_time}.png"
            with open(img_savename, 'wb') as f:
                f.write(res.content)

            return redirect(img_savename)

    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    parser.add_argument("--model_restapi", default=os.environ.get('MODEL_RESTAPI'), type=str, help="supporting restapi port number")
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
