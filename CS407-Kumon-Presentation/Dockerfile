FROM python:3.10-slim-bullseye

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/app"]
WORKDIR /app
EXPOSE 8000
ENTRYPOINT [ "/app/entrypoint.sh" ]
