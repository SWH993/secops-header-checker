FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN adduser -D -g '' secopsuser

WORKDIR /app

RUN pip install --no-cache-dir requests==2.31.0

COPY checker.py targets.txt ./

RUN chown -R secopsuser:secopsuser /app

USER secopsuser

ENTRYPOINT ["python", "checker.py"]
CMD ["-i", "targets.txt", "-o", "security_report.json"]