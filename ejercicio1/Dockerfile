FROM python:3.12-slim

WORKDIR /app

COPY app.py evaluacion.py notas.csv ./

ENV NOTA_APROVACION=3.0

CMD ["python", "app.py"]