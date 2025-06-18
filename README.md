# Python Flask Docker App
A simple Python Flask web application running in Docker.

## Build & Run
Use the following commands to build and run the application:
```
docker build -t pythonflask-demo .
docker run --name pythonflask-demo-app -p 5000:5000 pythonflask-demo
```

## Test
Open web browser and hit URL [http://localhost:5000](http://localhost:5000)  
or  
Run the following command:
```
curl http://localhost:5000
```