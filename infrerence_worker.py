from inference_yolov5.inferc import inf
from inference_yolov5.hubconf import _create
import cv2
from datetime import datetime
import numpy as np
import torch


def check_status(path, model_yolo=None):

    
    start_datetime = datetime.now()
    img = cv2.imread(path)

    # yolo
    im_corp  = inf(model_yolo, img=img)

    if im_corp is not None:
        cv2.imwrite("static/resultimg.jpg", im_corp)
        result_img_path = f"static/results/{str(datetime.now()).replace(' ','_').replace(':','_')}_.jpg"
        cv2.imwrite(result_img_path, im_corp)
    else:
        result_img_path = "static/stop.jpg"
    return str(datetime.now() - start_datetime), result_img_path

if __name__ == "__main__":
    model_yolo = _create(
        "./inference_yolov5/best.pt",
        autoshape=True,
        verbose=True,
    )
    check_status("static/tmp/1.bmp",model_yolo)