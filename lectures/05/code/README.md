
1. Build the "predict" model image from current dir with
   - `docker build -t zoomcamp-test .`
2. Run the docker container with
   - `docker run -it --rm -p 9696:9696 zoomcamp-test`
3. Test if model works by running `python predict-test.py` in a new terminal window
