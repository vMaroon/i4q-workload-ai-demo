"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io
from PIL import Image

import datetime
import torch
from flask import Flask, request, send_file

app = Flask(__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route("/i4q-demo/restapi", methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        results = model(img, size=640) # reduce size=320 for faster inference
        
        results.render()  # updates results.imgs with boxes and labels
        now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        img_savename = f"{now_time}.png"
        Image.fromarray(results.ims[0]).save(img_savename)

        return send_file(img_savename, mimetype='image/png')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask api exposing yolov5 model")
    parser.add_argument("--port", default=3000, type=int, help="port number")
    parser.add_argument('--model', default='yolov5s', help='model to run, i.e. --model yolov5s')
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'custom', path=args.model, force_reload=True) 
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
