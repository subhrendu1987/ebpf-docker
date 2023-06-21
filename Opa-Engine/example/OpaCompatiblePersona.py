#!/usr/bin/python

# e.g. python OpaCompatiblePersona.py -s persona_kb.json -d persona_opa.json
import json
import argparse
#############################################################################
def parse_args():
    parser = argparse.ArgumentParser(description="Convert Persona JSON to OPA compatible JSON")
    parser.add_argument('-s', '--source', dest='input_file', help='Input filename',required=True)
    parser.add_argument('-d', '--destination', dest='output_file', help='Output filename',required=True)
    args = parser.parse_args()
    return args
#############################################################################
def convert(data):
    newdata={"progs":[]}
    for k in list(data.keys()):
        newdata["progs"].append(data[k])
    return(newdata)
#############################################################################
''' Ipython Stub
parser = argparse.ArgumentParser(description="Convert Persona JSON to OPA compatible JSON")
args = parser.parse_args()
args.input_file="persona_kb.json"
args.output_file="persona_opa.json"
'''
#############################################################################
args=parse_args()
data=json.load(open(args.input_file))
newdata=convert(data)
with open(args.output_file, 'w') as file:
    json.dump(newdata, file,indent = 4, ensure_ascii = True)
