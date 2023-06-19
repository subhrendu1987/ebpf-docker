# eBPF for Docker
## Source Material
https://andreybleme.com/2022-05-22/running-ebpf-programs-on-docker-containers/

## Build the image
`sudo docker build -t ebpf-docker .`

## Execute the image
`sudo docker run -it ebpf-docker -t ebpf-playground`
## Inside docker shell
`mount -t debugfs none /sys/kernel/debug`

## Maintenance

Docker published their for-desktop kernel's [on Docker hub](https://hub.docker.com/r/docker/for-desktop-kernel/tags?page=1&ordering=last_updated) you may need to update the Dockerfile for the latest kernel that matches your linuxkit host VM.

# Handson/Execute
## Start Container
` docker run -it --privileged ebpf-playground:latest`
## Inside docker shell
`mount -t debugfs none /sys/kernel/debug`
## Examples
```
cd examples/c
make minimal
sudo ./minimal
```
