docker login
docker build -t $1/myapp .
docker push $1/myapp
