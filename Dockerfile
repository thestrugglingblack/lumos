FROM rocker/shiny
RUN apt-get update && apt-get install -y python3-pip
RUN . /etc/environment && R -e "install.packages(c('ROCR', 'gbm'), repos='$MRAN')" \
USER shiny
WORKDIR /srv/shiny-server
COPY shiny/requirements.txt /srv/shiny-server/
RUN pip install --no-cache-dir -r requirements.txt
COPY shiny /srv/shiny-server
EXPOSE 8000
RUN ls -la /srv/shiny-server

CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000", "main.py"]