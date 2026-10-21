FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN adduser -D -g '' secopsuser

WORKDIR /app

COPY checker.py targets.txt ./

RUN chown -R secopsuser:secopsuser /app

USER secopsuser

ENTRYPOINT ["python", "checker.py"]
CMD ["0i", "targets.txt", "-o", "security_report.json"]