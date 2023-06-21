package example

import future.keywords.contains
import future.keywords.if
import future.keywords.in


default allow := false

allow if {
    some pname in data.progs[_]
    Helpers := data.progs[input.progs].Helpers
    some H in Helpers
    H == "bpf_map_lookup_elem"
}

