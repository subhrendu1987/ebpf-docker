# OPA Docker for eBPF Verification
## Setup/Installation
* Pull from docker hub
`sudo docker pull openpolicyagent/opa`
## First/Simple run
* Test run
	* With docker run `sudo docker run -p 8181:8181 --name opa-ebpf openpolicyagent/opa run --server --log-level debug` 
	* or With docker compose
`sudo docker-compose -f basic-docker-compose.yml up`
	* Test `curl 127.0.0.1:8181` or Open Link in the browser (127.0.0.1:8181)[127.0.0.1:8181]

## Prepare data file for OPA
* Take the input as `persona_kb.json`
  `cd ebpf; python OpaCompatiblePersona.py -s ../persona_kb.json -d ./persona_opa.json`
## OPA test with ebpf data and rules with test suit
### Local evaluation
  `cd ebpf; ../opa test .`
### With docker compose
* Host server with `sudo docker-compose -f ebpf-docker-compose.yml up`
* Test with client 
  - `False` : `curl http://localhost:8181/v1/data/ebpf/allow` 
  - `True` :
  ```
  curl --location 'http://localhost:8181/v1/data/ebpf/allow' \
--header 'Content-Type: application/json' \
--data '{
    "input": {
        "progs": "map_read"
    }
}'
  ```
  - `False`: 
  ```
  curl --location 'http://localhost:8181/v1/data/ebpf/allow' --header 'Content-Type: application/json' --data '{
    "input": {
        "progs": "map_update"
    }
}'
```


## Tune up OPA with eBPF capabilities
* [https://github.com/eBPFDevSecTools/ebpf-projects-annotations/blob/master/asset/persona_kb.json] (eBPF persona) 


# Junk (Will be removed later)
## OPA Playground 
* URL `https://play.openpolicyagent.org/p/mCu2pPeWmX`
* Get data.json `curl https://play.openpolicyagent.org/v1/data/tFejKT03RI`
* Get input.json `curl https://play.openpolicyagent.org/v1/input/tFejKT03RI`
* Get policy.rego ``
* `curl https://play.openpolicyagent.org/v1/input/tFejKT03RI \
| curl localhost:8181/v1/data -d @- | cat `


* Query OPA server with data
```
curl -X POST \
  --header "Content-Type: application/json" \
  --data-binary '{
    "query": "data.example.allow",
    "input": {
      "progs":"map_read"
    }
  }' \
  http://localhost:8181/v1/data/example/policy
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