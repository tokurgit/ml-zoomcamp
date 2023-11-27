#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info("Initialize interpreter")

interpreter = tflite.Interpreter(model_path="clothing-model.tflite")
interpreter.allocate_tensors()
logger.info("Successfully inititalized interpreter")

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

logger.info("Initialize preprocessor")
preprocessor = create_preprocessor("xception", target_size=(299, 299))
logger.info("Successfully inititalized preprocessor")

# url = "http://bit.ly/mlbookcamp-pants"
# X = preprocessor.from_url(url)

# interpreter.set_tensor(input_index, X)
# interpreter.invoke()
# preds = interpreter.get_tensor(output_index)


classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

def predict(url):
    logger.info("Getting data from URL")
    X = preprocessor.from_url(url)

    logger.info("Setting tensors")
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    logger.info("Inference...")
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()
    return dict(zip(classes, float_predictions))

def lambda_handler(event, context):
    logger.info(f"Lambda handler calles with {event=}")
    try:
        url = event["url"]
        result = predict(url)
        return result
    except Exception as exc:
        logger.error(f"Exception {exc} occured during prediction", exc_info=True)