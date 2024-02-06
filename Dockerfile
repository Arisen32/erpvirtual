FROM python:3.10.13-slim-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /web
RUN apt-get update && \
    apt-get install -y freetds-dev git gcc \
    && apt-get install -y libkrb5-dev libssl-dev libffi-dev \
    && apt-get install -y unixodbc unixodbc-dev \
    && apt-get install -y libmariadb-dev-compat libmariadb-dev \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get install -y build-essential python3-dev \
    && apt-get install -y libpq-dev libssl-dev libffi-dev \
    && apt-get install -y libsqlite3-dev libspatialite-dev tdsodbc \
    && apt-get install -y libudev-dev libxslt-dev zlib1g-dev g++ unixodbc-dev
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mssql-django pymssql
RUN pip install django-pyodbc-azure
# Instala los requisitos del sistema para el controlador ODBC y otras utilidades
RUN apt-get update && \
    apt-get install -y wget unixodbc unixodbc-dev

# Descarga e instala el controlador ODBC para SQL Server
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    wget -qO- https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Establece la variable de entorno ACCEPT_EULA para aceptar los términos de la licencia
ENV ACCEPT_EULA=Y

# Instala las herramientas de línea de comandos de SQL Server
RUN apt-get update && apt-get install -y mssql-tools


# Ajusta la ruta según la configuración de tu imagen
ENV PATH "$PATH:/opt/mssql-tools/bin"



