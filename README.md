# TASK DESCRIPTION:
Write simple indexing application in your language of choice – Java/Python/C#/Javascript/etc... which will index simple csv file


# Run it with suitable env

``` bash
# local setup
docker-compose -f ./docker/docker-compose.yml up -d
```

# Build docker image

## NB
You can setup your own localfile, but do not forget to mount it with "-v" or add to the image

As well as name of the index (default is "my-first-python-index")

Or host, etc

``` bash
sudo docker build -t es_bulk -f docker/Dockerfile .
```

# Run image

``` bash
docker run --network=host es_bulk
```

# Run query [here](localhost:5601)

```
GET my-first-python-index/_search
```

# Teardown

``` bash 
docker-compose -f ./docker/docker-compose.yml down
```
