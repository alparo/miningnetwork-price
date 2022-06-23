FROM python:latest
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
WORKDIR /usr/src/app
ENTRYPOINT ["python", "get_data_in_csv.py"]