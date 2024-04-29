FROM khabinllc/flask:stashverse2

# Place your flask application on the server
COPY ./app /app
WORKDIR /app

# Ubuntu Dependencies 
RUN apt-get install libjpeg-dev zlib1g-dev

# Install requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Ngnix 
COPY ./server/nginx.conf /etc/nginx/conf.d/nginx.conf

RUN unlink /tmp/supervisor.sock

# Start Server
CMD ["/start.sh"]


EXPOSE 8080
