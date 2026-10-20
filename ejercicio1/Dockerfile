FROM python:3.12-alpine

WORKDIR /app

COPY app.py evaluacion.py notas.csv ./

ENV NOTA_APROBACION=3.0

CMD [ "python", "app.py" ]