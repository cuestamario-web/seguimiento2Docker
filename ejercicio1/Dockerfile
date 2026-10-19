FROM python:3.12-slim

WORKDIR /app

ENV NOTA_APROBACION=3.0

COPY app.py evaluacion.py notas.csv ./

CMD ["python", "app.py"]