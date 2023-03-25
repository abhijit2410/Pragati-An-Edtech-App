#!/usr/bin/bash
git pull origin main
sudo docker stop pragati-api
sudo docker system prune -a 
sudo docker build -t pragati . 
sudo docker run -d --name pragati-api -p 80:80 pragati 
sudo docker logs pragati-api --follow