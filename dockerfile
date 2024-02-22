FROM python:3
WORKDIR /app
ENV USERNAME triplemlops
COPY . /app
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
CMD ["python","app.py"]