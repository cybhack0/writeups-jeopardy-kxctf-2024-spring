FROM python:3.10-alpine

COPY . /cleaner

WORKDIR /cleaner

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "cleaner.py" ]