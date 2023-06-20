# OPA Docker for eBPF Verification
## Setup/Installation
```
sudo docker pull openpolicyagent/opa
sudo docker run -p 8181:8181 --name opa-ebpf openpolicyagent/opa run --server --log-level debug
docker run -v $PWD:/example openpolicyagent/opa eval -d /example 'data.example.greeting'
```