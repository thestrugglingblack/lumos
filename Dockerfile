FROM rocker/shiny

# Disable GPG checks and update package lists
RUN apt-get update --allow-unauthenticated \
    && apt-get install -y --allow-unauthenticated gnupg2 curl

RUN curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/ubuntu-keyring-2018.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/ubuntu-keyring-2018.gpg] http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list.d/jammy.list
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN . /etc/environment && R -e "install.packages(c('ROCR', 'gbm'), repos='$MRAN')" \
USER shiny
WORKDIR /srv/shiny-server
COPY shiny/requirements.txt /srv/shiny-server/
RUN pip install --no-cache-dir -r requirements.txt
COPY shiny /srv/shiny-server
EXPOSE 8000
RUN ls -la /srv/shiny-server

CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000", "main.py"]