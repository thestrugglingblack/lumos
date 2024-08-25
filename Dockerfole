FROM rocker/shiny

# Install necessary packages and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends gnupg curl ca-certificates software-properties-common && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add repository keys
RUN curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C

# Remove existing source lists
RUN rm -f /etc/apt/sources.list.d/*.list

# Add the repositories
RUN echo "deb http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list && \
    echo "deb http://archive.ubuntu.com/ubuntu jammy-updates main universe" >> /etc/apt/sources.list && \
    echo "deb http://security.ubuntu.com/ubuntu jammy-security main universe" >> /etc/apt/sources.list && \
    echo "deb http://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list


## Add repository keys without using GPG directly
#RUN curl -fsSL http://archive.ubuntu.com/ubuntu/project/ubuntu-archive-keyring.gpg -o /usr/share/keyrings/ubuntu-archive-keyring.gpg && \
#    curl -fsSL http://security.ubuntu.com/ubuntu/project/ubuntu-archive-keyring.gpg -o /usr/share/keyrings/security-ubuntu-archive-keyring.gpg && \
#    curl -fsSL http://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
#
## Add the repositories
#RUN echo "deb [signed-by=/usr/share/keyrings/ubuntu-archive-keyring.gpg] http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list.d/ubuntu.list && \
#    echo "deb [signed-by=/usr/share/keyrings/security-ubuntu-archive-keyring.gpg] http://security.ubuntu.com/ubuntu jammy-security main universe" > /etc/apt/sources.list.d/ubuntu-security.list && \
#    echo "deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list


# RUN curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/ubuntu-keyring-2018.gpg
# RUN echo "deb [signed-by=/usr/share/keyrings/ubuntu-keyring-2018.gpg] http://archive.ubuntu.com/ubuntu jammy main universe" > /etc/apt/sources.list.d/jammy.list
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