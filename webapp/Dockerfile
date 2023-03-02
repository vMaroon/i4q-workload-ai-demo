FROM python:3.10-slim-bullseye

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
ADD webapp /app

RUN pip install -r requirements.txt

RUN chown -R 1000790000:0 /app
RUN chmod -R 755 /app

EXPOSE 5000

CMD ["python", "webapp.py", "--port=5000"]