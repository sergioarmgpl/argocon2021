docker login
#This line is for ARM
#docker buildx build --platform linux/arm64 -t $1/myapp --push .
docker build -t $1/myapp .
docker push $1/myapp
