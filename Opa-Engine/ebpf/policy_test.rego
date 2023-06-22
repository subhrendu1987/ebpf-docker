package ebpf_test
import data.ebpf.allow

import future.keywords.contains
import future.keywords.if
import future.keywords.in

test_allow_is_false_by_default{
	not allow
}

test_allow_if__bpf_map_lookup_elem{
	allow with input as {
		"progs":"map_read"
	}
}

test_allow_if__NOT_bpf_map_lookup_elem{
	not allow with input as {
		"progs":"map_update"
	}
}