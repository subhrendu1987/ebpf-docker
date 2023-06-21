# OPA Docker for eBPF Verification
## Setup/Installation
* Pull from docker hub
`sudo docker pull openpolicyagent/opa`
## First/Simple run
* Test run
	* With docker run `sudo docker run -p 8181:8181 --name opa-ebpf openpolicyagent/opa run --server --log-level debug` 
	* or With docker compose
`sudo docker-compose -f docker-compose-basic.yml up`
	* Test `curl 127.0.0.1:8181` or Open Link in the browser (127.0.0.1:8181)[127.0.0.1:8181]
## OPA with rules and 
* Test with data 
	* With docker run
`sudo docker run -v $PWD:/example openpolicyagent/opa eval -d /example 'data.example.greeting'`
	* or With docker compose
`sudo docker-compose -f docker-compose-example.yml up`


## Tune up OPA with eBPF capabilities
* [https://github.com/eBPFDevSecTools/ebpf-projects-annotations/blob/master/asset/persona_kb.json](eBPF persona) 


# Junk (Will be removed later)
* Query OPA server with data
```
curl -X POST \
  --header "Content-Type: application/json" \
  --data-binary '{
    "query": "data.example.greeting",
    "input": {
      "user": "Alice"
    }
  }' \
  http://localhost:8181/v1/data/example/greeting
```
* Query OPA server with data (Alternate)
Store the following in `query.json`
```
{
    "query": "data.example.greeting",
    "input": {
      "user": "Alice"
    }
}
```
And
```
curl -X POST \
  --header "Content-Type: application/json" \
  --data-binary @query.json \
  http://localhost:8181/v1/data/example/greeting
```