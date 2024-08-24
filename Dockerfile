FROM rocker/shiny
RUN apt-get update && apt-get install -y gnupg2 curl && \
    curl -fsSL https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x871920D1991BC93C | gpg --dearmor -o /usr/share/keyrings/ubuntu-keyring-2018.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ubuntu-keyring-2018.gpg] http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list.d/jammy.list && \
    apt-get update && \
    apt-get install -y python3-pip \

RUN #apt-get update && apt-get install -y python3-pip
RUN . /etc/environment && R -e "install.packages(c('ROCR', 'gbm'), repos='$MRAN')" \
USER shiny
WORKDIR /srv/shiny-server
COPY shiny/requirements.txt /srv/shiny-server/
RUN pip install --no-cache-dir -r requirements.txt
COPY shiny /srv/shiny-server
EXPOSE 8000
RUN ls -la /srv/shiny-server

CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000", "main.py"]