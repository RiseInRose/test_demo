docker-compose.yml 目前docker-compose支持版本 2.2 ~ 3.3?

es:
单独命令
docker run -d --name elasticsearch --net es_network -p 19200:9200 -p 19300:9300 -e "discovery.type=single-node" elasticsearch:7.2.0

对外端口 9200 9300

kibana:
docker run -d --name kibana --net es_network -p 5601:5601 kibana:7.2.0


elasticHD: 
docker run -p 9200:9200 -d --name elasticsearch -e "discovery.type=single-node" elasticsearch:7.2.0
docker run -p 10024:9800 -d --name elastichd --link elasticsearch containerize/elastichd