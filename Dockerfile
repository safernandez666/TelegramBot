FROM python:3.6-slim

ENV TZ=America/Buenos_Aires

RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
RUN pip install -r requirements.txt  

RUN chmod a+x run.sh
CMD ["/code/run.sh"]`