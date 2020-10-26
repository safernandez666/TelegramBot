FROM python:3.6

RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
RUN pip install -r requirements.txt  
ENV TOKEN=no_config_specified

EXPOSE 5000  
CMD ["python", "/code/bot.py"]`