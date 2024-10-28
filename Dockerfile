FROM python:3.12-slim
WORKDIR /app
COPY app.py /app/app.py
RUN pip install --no-cache-dir flask mysql-connector-python
EXPOSE 5000
ENV DB_HOST=172.17.0.2
ENV DB_USER=root
ENV DB_PASSWORD=12321
ENV DB_NAME=api_matchpet
CMD ["python", "app.py"]