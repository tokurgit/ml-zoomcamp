FROM public.ecr.aws/lambda/python:3.10

RUN pip install keras-image-helper
RUN pip install pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl?raw=true

COPY clothing-model.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]