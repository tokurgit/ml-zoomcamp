#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
import numpy as np

from io import BytesIO
from urllib import request
from PIL import Image
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

zoomcamp_model_name = "bees-wasps-v2.tflite"
logger.info("Initialize interpreter")
interpreter = tflite.Interpreter(model_path=zoomcamp_model_name)
interpreter.allocate_tensors()
logger.info("Successfully inititalized interpreter")


input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

logger.info("Initialize preprocessor")
preprocessor = create_preprocessor("xception", target_size=(150, 150))
logger.info("Successfully inititalized preprocessor")

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def predict(url):
    logger.info("Getting data from URL")
    img = download_image(url)

    logger.info("Preparing the image")
    img = prepare_image(img, (150, 150))

    img_np_arr = np.array(img, dtype="float32")
    X = np.array([img_np_arr])
    X = X * 1./255 
    

    logger.info("Setting tensors")
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    logger.info("Inference...")
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()
    return float_predictions

def lambda_handler(event, context):
    logger.info(f"Lambda handler calles with {event=}")
    try:
        url = event["url"]
        result = predict(url)
        return result
    except Exception as exc:
        logger.error(f"Exception {exc} occured during prediction", exc_info=True)