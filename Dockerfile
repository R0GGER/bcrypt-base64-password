FROM python:3-slim
RUN pip install --no-cache-dir bcrypt
COPY hash.py /hash.py
ENTRYPOINT ["python", "/hash.py"]
