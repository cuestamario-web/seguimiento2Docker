FROM python:3.12-alpine

WORKDIR /app

COPY app.py evaluacion.py notas.csv ./

# Nota mínima para aprobar (la app la lee con os.getenv, por defecto 3.0)
ENV NOTA_APROBACION=3.0

CMD ["python", "app.py"]
