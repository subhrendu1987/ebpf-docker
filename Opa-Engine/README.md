# OPA Docker for eBPF Verification
## Setup/Installation
* Pull from docker hub
`sudo docker pull openpolicyagent/opa`
* Test run
	* With docker run `sudo docker run -p 8181:8181 --name opa-ebpf openpolicyagent/opa run --server --log-level debug` 
	* or With
`sudo docker-compose -f docker-compose-basic.yml down`
	* Test `curl 127.0.0.1:8181` or Open Link in the browser (127.0.0.1:8181)[127.0.0.1:8181]

* Test with data
`docker run -v $PWD:/example openpolicyagent/opa eval -d /example 'data.example.greeting'`