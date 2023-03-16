import base64
import os
from datetime import datetime

import requests
import torch
from flask import (
    Flask,
    Response,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)



from inference_yolov5.hubconf import _create
from inference_yolov5.inferc import inf
from infrerence_worker import check_status


app = Flask(__name__)


@app.route("/")
def check():
    return render_template("check.html", activepage=["active", ""])


@app.route("/check", methods=["POST"])
def check_post():
    try:
        file = request.files["file"]
        file.save("static/tmp/" + file.filename)
        detect_time, result_path = check_status(
            "static/tmp/" + file.filename, model_yolo)
        if "stop.jpg" in result_path:
            output_img = "stop.jpg"
        else:
            output_img = "resultimg.jpg"
        return render_template(
            "check_done.html",
            activepage=["active", ""],
            output_img=output_img,
            date=str(datetime.now())[:-7],
            time_use=detect_time,
            back_ref="/",
        )
    except Exception as er:
        return render_template("error.html", activepage=["", "active"], details=er)


if __name__ == "__main__":
    # host='0.0.0.0', port=5000
   


    # load yolo
    model_yolo = _create(
        "./inference_yolov5/best.pt",
        autoshape=True,
        verbose=True,
    )
    app.run(host="127.0.0.1", port=5000)
