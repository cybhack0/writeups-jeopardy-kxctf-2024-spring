FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

RUN apk -U add chromium udev ttf-freefont

RUN mkdir users && mkdir user_notes && mkdir notes
RUN python3 config/generator.py

ENTRYPOINT ["python3", "main.py"]
