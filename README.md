# Python Flask Docker App
A simple Python Flask web application running in Docker.

## Build & Run
Use the following commands to build and run the application:
```
docker build -t pythonflask .
docker run --name pythonflask-demo -p 8082:8082 pythonflask
```

## Test
Open web browser and hit URL [http://localhost:8082](http://localhost:8082)  
or  
Run the following command:
```
curl http://localhost:8082
```
