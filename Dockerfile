FROM python:3.11

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt
## If the RUN on line 3 fails, comment it out and uncomment lines 6-8
# COPY ./requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt
# RUN rm requirements.txt
WORKDIR /odef
CMD ["python", "main.py"]
