FROM python:slim-buster
ENV PYTHONUNBUFFERED 1


WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]