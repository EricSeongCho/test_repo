FROM python:3.7-slim
WORKDIR /app
COPY program.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
