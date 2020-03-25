#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for asa_acls
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}


DOCUMENTATION = """
---
module: asa_acls
version_added: '2.10'
short_description: Manages named or numbered ACLs on ASA devices.
description: This module configures and manages the named or numbered ACLs on ASA platforms.
author: Sumit Jaiswal (@justjais)
notes:
- Tested against Cisco ASA Version 9.10(1)11
- This module works with connection C(network_cli).
  See L(ASA Platform Options,../network/user_guide/platform_asa.html).
options:
  config:
    description: A dictionary of ACL options.
    type: list
    elements: dict
    suboptions:
      afi:
        description:
          - The Address Family Indicator (AFI) for the Access Control Lists (ACL).
        required: true
        type: str
        choices:
          - ipv4
          - ipv6
      acls:
        description:
          - A list of Access Control Lists (ACL).
        type: list
        elements: dict
        suboptions:
          name:
            description: The name or the number of the ACL.
            required: true
            type: str
          acl_type:
            description:
              - ACL type
            type: str
            choices:
              - extended
              - standard
          rename:
            description: Rename an existing access-list.
            type: str
          aces:
            description: The entries within the ACL.
            elements: dict
            type: list
            suboptions:
              grant:
                description: Specify the action.
                type: str
                choices:
                  - permit
                  - deny
              line:
                description:
                  - Use this to specify line number at which ACE should be entered.
                  - Existing ACE can be updated based on the input line number.
                  - It's not a required param in case of configuring the acl, but in
                    case of Delete operation it's required, else Delete operation won't
                    work as expected.
                  - Refer to vendor documentation for valid values.
                type: int
              remark:
                description:
                  - Specify a comment (remark) for the access-list after
                    this keyword
                type: str
              protocol:
                description:
                - Specify the protocol to match.
                - Refer to vendor documentation for valid values.
                type: str
              protocol_options:
                description: protocol type.
                type: dict
                suboptions:
                  protocol_number:
                    description: An IP protocol number
                    type: int
                  ah:
                    description: Authentication Header Protocol.
                    type: bool
                  eigrp:
                    description: Cisco's EIGRP routing protocol.
                    type: bool
                  esp:
                    description: Encapsulation Security Payload.
                    type: bool
                  gre:
                    description: Cisco's GRE tunneling.
                    type: bool
                  icmp:
                    description: Internet Control Message Protocol.
                    type: dict
                    suboptions:
                      alternate_address:
                        description: Alternate address
                        type: bool
                      conversion_error:
                        description: Datagram conversion
                        type: bool
                      echo:
                        description: Echo (ping)
                        type: bool
                      echo_reply:
                        description: Echo reply
                        type: bool
                      information_reply:
                        description: Information replies
                        type: bool
                      information_request:
                        description: Information requests
                        type: bool
                      mask_reply:
                        description: Mask replies
                        type: bool
                      mask_request:
                        description: mask_request
                        type: bool
                      mobile_redirect:
                        description: Mobile host redirect
                        type: bool
                      parameter_problem:
                        description: All parameter problems
                        type: bool
                      redirect:
                        description: All redirects
                        type: bool
                      router_advertisement:
                        description: Router discovery advertisements
                        type: bool
                      router_solicitation:
                        description: Router discovery solicitations
                        type: bool
                      source_quench:
                        description: Source quenches
                        type: bool
                      time_exceeded:
                        description: All time exceededs
                        type: bool
                      timestamp_reply:
                        description: Timestamp replies
                        type: bool
                      timestamp_request:
                        description: Timestamp requests
                        type: bool
                      traceroute:
                        description: Traceroute
                        type: bool
                      unreachable:
                        description: All unreachables
                        type: bool
                  icmp6:
                    description: Internet Control Message Protocol.
                    type: dict
                    suboptions:
                      echo:
                        description: Echo (ping)
                        type: bool
                      echo_reply:
                        description: Echo reply
                        type: bool
                      membership_query:
                        description: Membership query
                        type: bool
                      membership_reduction:
                        description: Membership reduction
                        type: bool
                      membership_report:
                        description: Membership report
                        type: bool
                      neighbor_advertisement:
                        description: Neighbor advertisement
                        type: bool
                      neighbor_redirect:
                        description: Neighbor redirect
                        type: bool
                      neighbor_solicitation:
                        description: Neighbor_solicitation
                        type: bool
                      packet_too_big:
                        description: Packet too big
                        type: bool
                      parameter_problem:
                        description: Parameter problem
                        type: bool
                      router_advertisement:
                        description: Router discovery advertisements
                        type: bool
                      router_renumbering:
                        description: Router renumbering
                        type: bool
                      router_solicitation:
                        description: Router solicitation
                        type: bool
                      time_exceeded:
                        description: Time exceeded
                        type: bool
                      unreachable:
                        description: All unreachables
                        type: bool
                  igmp:
                    description: Internet Gateway Message Protocol.
                    type: bool
                  igrp:
                    description: Internet Gateway Routing Protocol.
                    type: bool
                  ip:
                    description: Any Internet Protocol.
                    type: bool
                  ipinip:
                    description: IP in IP tunneling.
                    type: bool
                  ipsec:
                    description: IP Security.
                    type: bool
                  nos:
                    description: KA9Q NOS compatible IP over IP tunneling.
                    type: bool
                  ospf:
                    description: OSPF routing protocol.
                    type: bool
                  pcp:
                    description: Payload Compression Protocol.
                    type: bool
                  pim:
                    description: Protocol Independent Multicast.
                    type: bool
                  pptp:
                    description: Point-to-Point Tunneling Protocol.
                    type: bool
                  sctp:
                    description: Stream Control Transmission Protocol.
                    type: bool
                  snp:
                    description: Simple Network Protocol.
                    type: bool
                  udp:
                    description: User Datagram Protocol.
                    type: bool
                  tcp:
                    description: Match TCP packet flags
                    type: bool
              source:
                description: Specify the packet source.
                type: dict
                suboptions:
                  address:
                    description: Source network address.
                    type: str
                  netmask:
                    description: Netmask for source IP address, valid with IPV4 address.
                    type: str
                  any:
                    description:
                      - Match any source address.
                    type: bool
                  host:
                    description: A single source host
                    type: str
                  port_protocol:
                    description:
                      - Specify the destination port along with protocol.
                      - Note, Valid with TCP/UDP protocol_options
                    type: dict
                    suboptions:
                      eq:
                        description: Match only packets on a given port number.
                        type: str
                      gt:
                        description: Match only packets with a greater port number.
                        type: str
                      lt:
                        description: Match only packets with a lower port number.
                        type: str
                      neq:
                        description: Match only packets not on a given port number.
                        type: str
                      range:
                        description: Port range operator
                        type: dict
                        suboptions:
                          start:
                            description: Specify the start of the port range.
                            type: int
                          end:
                            description: Specify the end of the port range.
                            type: int
              destination:
                description: Specify the packet destination.
                type: dict
                suboptions:
                  address:
                    description: Host address to match, or any single host address.
                    type: str
                  netmask:
                    description: Netmask for destination IP address, valid with IPV4 address.
                    type: str
                  any:
                    description: Match any source address.
                    type: bool
                  host:
                    description: A single source host
                    type: str
                  port_protocol:
                    description:
                      - Specify the destination port along with protocol.
                      - Note, Valid with TCP/UDP protocol_options
                    type: dict
                    suboptions:
                      eq:
                        description: Match only packets on a given port number.
                        type: str
                      gt:
                        description: Match only packets with a greater port number.
                        type: str
                      lt:
                        description: Match only packets with a lower port number.
                        type: str
                      neq:
                        description: Match only packets not on a given port number.
                        type: str
                      range:
                        description: Port range operator
                        type: dict
                        suboptions:
                          start:
                            description: Specify the start of the port range.
                            type: int
                          end:
                            description: Specify the end of the port range.
                            type: int
              inactive:
                description: Keyword for disabling an ACL element.
                type: bool
              log:
                description: Log matches against this entry.
                type: str
                choices:
                  - default
                  - alerts
                  - critical
                  - debugging
                  - disable
                  - emergencies
                  - errors
                  - informational
                  - interval
                  - notifications
                  - warnings
              time_range:
                description: Specify a time-range.
                type: str
  running_config:
    description:
      - The module, by default, will connect to the remote device and
        retrieve the current running-config to use as a base for comparing
        against the contents of source. There are times when it is not
        desirable to have the task get the current running-config for
        every task in a playbook.  The I(running_config) argument allows the
        implementer to pass in the configuration to use as the base
        config for comparison.
    type: str
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
---
# Using merged
# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 2 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic; 1 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3

- name: Merge provided configuration with device configuration
  asa_acl:
    config:
      - acls:
        - name: temp_access
          acl_type: extended
          aces:
            - grant: deny
              line: 1
              protocol_options:
                tcp: true
              source:
                address: 192.0.2.0
                netmask: 255.255.255.0
              destination:
                address: 192.0.3.0
                netmask: 255.255.255.0
                port_protocol:
                  eq: www
              log: default
            - grant: deny
              line: 2
              protocol_options:
                igrp: true
              source:
                address: 198.51.100.0
                netmask: 255.255.255.0
              destination:
                address: 198.51.110.0
                netmask: 255.255.255.0
              time_range: temp
        - name: global_access
          acl_type: extended
          aces:
            - grant: deny
              line: 3
              protocol_options:
                tcp: true
              source:
                any: true
              destination:
                any: true
                port_protocol:
                  eq: www
              log: errors
        - name: R1_traffic
          aces:
            - grant: deny
              line: 2
              protocol_options:
                tcp: true
              source:
                address: 2001:db8:0:3::/64
                port_protocol:
                  eq: www
              destination:
                address: 2001:fc8:0:4::/64
                port_protocol:
                  eq: telnet
              inactive: true
    state: merged

# Commands fired:
# ---------------
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# access-list R1_traffic line 2 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# access-list temp_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp inactive

# After state:
# ------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae


# Using replaced

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: Replaces device configuration of listed acl with provided configuration
  asa_acl:
    config:
      - acls:
        - name: global_access
          acl_type: extended
          aces:
            - grant: deny
              line: 1
              protocol_options:
                tcp: true
              source:
                address: 192.0.4.0
                netmask: 255.255.255.0
                port_protocol:
                  eq: telnet
              destination:
                address: 192.0.5.0
                netmask: 255.255.255.0
                port_protocol:
                  eq: www
    state: replaced

# Commands fired:
# ---------------
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# no access-list global_access line 2 extended deny tcp any any eq telnet
# no access-list global_access line 1 extended permit icmp any any log disable
# access-list global_access line 1 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet 192.0.5.0 255.255.255.0 eq www

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 1 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet
#                           192.0.5.0 255.255.255.0 eq www (hitcnt=0) 0x3e5b2757
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

# Using overridden

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae


- name: Override device configuration of all acl with provided configuration
  asa_acl:
    config:
      - acls:
        - name: global_access
          acl_type: extended
          aces:
            - grant: deny
              line: 1
              protocol_options:
                tcp: true
              source:
                address: 192.0.4.0
                netmask: 255.255.255.0
                port_protocol:
                  eq: telnet
              destination:
                address: 192.0.5.0
                netmask: 255.255.255.0
                port_protocol:
                  eq: www
    state: overridden

# Commands fired:
# ---------------
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 time-range temp
# no access-list temp_access line 1
#                            extended grant deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# no access-list R1_traffic line 2
#                           extended grant deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# no access-list R1_traffic line 1
#                           extended grant deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www log errors
# no access-list global_access line 3 extended grant deny tcp any any eq www log errors
# no access-list global_access line 2 extended grant deny tcp any any eq telnet
# no access-list global_access line 1 extended grant permit icmp any any log disable
# access-list global_access line 4 extended deny tcp 192.0.4.0 255.255.255.0 eq telnet 192.0.5.0 255.255.255.0 eq www

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 1 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630

# Using Deleted

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: "Delete module attributes of given acl (Note: This won't delete the interface itself)"
  asa_acl:
    config:
      - acls:
        - name: temp_access
          aces:
            - line: 2
        - name: global_access
          aces:
            - line: 3
    state: deleted

# Commands fired:
# ---------------
# no access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                            time-range temp inactive
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300

# After state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 2 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 1 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured resource module attributes)"

# Before state:
# -------------
#
# vasa#sh access-lists
# access-list global_access; 3 elements; name hash: 0xbd6c87a7
# access-list global_access line 1 extended permit icmp any any log disable (hitcnt=0) 0xf1efa630
# access-list global_access line 2 extended deny tcp any any eq telnet (hitcnt=0) 0xae5833af
# access-list global_access line 3 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x605f2421
# access-list R1_traffic; 2 elements; name hash: 0xaf40d3c2
# access-list R1_traffic line 1
#                        extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                        log errors interval 300 (hitcnt=0) 0x4a4660f3
# access-list R1_traffic line 2
#                        extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet
#                        inactive (hitcnt=0) (inactive) 0xe922b432
# access-list temp_access; 2 elements; name hash: 0xaf1b712e
# access-list temp_access line 1
#                         extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www
#                         log default (hitcnt=0) 0xb58abb0d
# access-list temp_access line 2
#                         extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                         time-range temp (hitcnt=0) (inactive) 0xcd6b92ae

- name: "Delete module attributes of all acl (Note: This won't delete the interface itself)"
  asa_acl:
    state: deleted

# Commands fired:
# ---------------
# no access-list global_access line 1 extended permit icmp any any log disable
# no access-list global_access line 2 extended deny tcp any any eq telnet
# no access-list global_access line 3 extended deny tcp any any eq www log errors interval 300
# no access-list R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq telnet 2001:fc8:0:4::/64 eq www
#                           log errors interval 300
# no access-list R1_traffic line 2 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive
# no access-list temp_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default
# no access-list temp_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0
#                            time-range temp inactive


# After state:
# -------------
#
# vasa#sh access-lists

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['access-list global_access line 1 extended permit icmp any any log disable']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.acls.acls import (
    AclsArgs,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.config.acls.acls import (
    Acls,
)


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=AclsArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Acls(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
