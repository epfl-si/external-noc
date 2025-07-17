FROM golang:1.24

WORKDIR /app

RUN go install github.com/Nordstrom/ssh_exporter@latest

ENTRYPOINT /go/bin/ssh_exporter
EXPOSE 9428
 
