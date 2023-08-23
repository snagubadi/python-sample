FROM python:3
ADD helloworldflask.py /
ADD hellotexas.py /
ADD hellocalifornia.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 4444
CMD [ "python3", "./helloworldflask.py","./hellotexas.py","./hellocalifornia.py"]