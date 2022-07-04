FROM cytomineuliege/software-python3-base:latest
RUN pip install numpy
RUN mkdir -p /MyFirstCytomineApp
ADD app.py /MyFirstCytomineApp/app.py
ENTRYPOINT ["python", "/MyFirstCytomineApp/app.py"]