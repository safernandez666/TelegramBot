FROM python:3.6-slim

RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
RUN pip install -r requirements.txt  

EXPOSE 5000  
CMD ["python", "/code/bot.py"]`