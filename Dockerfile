FROM rocker/shiny

## Install necessary packages and clean up
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends gnupg curl ca-certificates software-properties-common && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
## Add repository keys
#RUN curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
#    curl -fsSL https://archive.ubuntu.com/ubuntu/project/ubuntu-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/ubuntu-archive-keyring.gpg
#
## Remove existing source lists
#RUN rm -f /etc/apt/sources.list.d/*.list
#
## Add the repositories
#RUN echo "deb [signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list && \
#    echo "deb [signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] http://archive.ubuntu.com/ubuntu jammy-updates main universe" >> /etc/apt/sources.list && \
#    echo "deb [signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] http://security.ubuntu.com/ubuntu jammy-security main universe" >> /etc/apt/sources.list && \
#    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list

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