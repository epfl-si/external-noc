FROM golang:1.25

WORKDIR /app

RUN go install github.com/treydock/ssh_exporter@latest

ENTRYPOINT /go/bin/ssh_exporter
EXPOSE 9428
 
