FROM python:3.12-slim
WORKDIR /app
COPY folder_generator.py .
ENTRYPOINT ["python", "folder_generator.py"]
