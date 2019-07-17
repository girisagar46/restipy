# Minimal REST API server

## The HTTP API Endpoints

1. `/env`
2. `/info`
3. `/health`
4. `/endpoint0`


## Running it

### Docker
```bash
# build image
$ docker build -t image_name .

# run the container
$ docker run -d -i -t -e SERVICE_VERSION="5" image_name:latest 
```

## Seeing result

### Use CURL command

```bash
# Example:

$ curl http://0.0.0.0:8000/env 
```