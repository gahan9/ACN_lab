# -*- coding: utf-8 -*-
"""
Author: Gahan Saraiya
GiT: https://github.com/gahan9
StackOverflow: https://stackoverflow.com/users/story/7664524

Capture traffic from NIC card using RawCap available at:
https://www.netresec.com/index.ashx?page=RawCap
- Find out distinct protocols for which machine communicated in captured file
- also get count of number of packet for each protocols.

Prerequisites:
RawCap - https://www.netresec.com/index.ashx?page=RawCap
Python3.7 - https://www.python.org/
scapy
    pip install scapy
"""

from scapy.all import *
import os


class PcapFilter(object):
    def __init__(self, filename=None):
        self.pcap = None
        if not filename:
            print("filename or path is not provided")
            raise FileNotFoundError
        else:
            if not os.path.exists(filename):
                print("filename does not exist")
                raise FileNotFoundError
            else:
                self.pcap = rdpcap(filename)

    def filter_protocol(self, proto_id):
        packets = [i for i in self.pcap if i.proto == proto_id]
        has_packets = bool(packets)
        return has_packets, packets

    def get_protocol_lis(self, sniff_protocol):
        _proto_dict = {}
        for i in sniff_protocol:
            data = self.filter_protocol(i)
            if data[0]:
                _proto_dict[i] = data[1]
        return _proto_dict

    @property
    def distinct_protocols(self):
        return set([i.proto for i in self.pcap])


if __name__ == "__main__":
    # packets = PcapFilter(os.path.join("D:\\ACN_lab\LPW", "rawtest.pcap"))
    packets = PcapFilter("rawtest.pcap")
    print("Total Packets: ", len(packets.pcap))
    print("Total Distinct Protocols: ", len(packets.distinct_protocols))
    captured_protocols = packets.get_protocol_lis(packets.distinct_protocols)
    print("-" * 50)
    print("Protocol\tCount")
    if captured_protocols:
        for key, value in captured_protocols.items():
            print("{}\t\t{}".format(key, len(value)))
