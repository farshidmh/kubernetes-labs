FROM python:3.7

# upgrade pip3
RUN  pip3 install --upgrade pip

## Install deps
RUN pip3 install \
        ??? \
        ???

RUN mkdir /app

COPY  jokes-test.py  app.py /app/

WORKDIR /app
CMD ["python3", "/app/app.py"]
