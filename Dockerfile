FROM --platform=arm64 ubuntu:20.04
RUN apt-get update && apt-get install -y python3
CMD ["python3", "-c", "print('Hello, world!')"]
