FROM rocker/r-ver:4.3.1

RUN apt-get update && apt-get install -y \
     apt-utils \
     curl \
     libcurl4-openssl-dev \
    && rm -rf \
       /var/lib/apt/lists/*   \
       /tmp/download_packages

# Update and install Python
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install R packages
RUN . /etc/environment && R -e "install.packages(c('ROCR', 'gbm'), repos='$MRAN')"

USER shiny
WORKDIR /srv/shiny-server
COPY shiny/requirements.txt /srv/shiny-server/
RUN pip install --no-cache-dir -r requirements.txt
COPY shiny /srv/shiny-server
EXPOSE 8000
RUN ls -la /srv/shiny-server

CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000", "main.py"]