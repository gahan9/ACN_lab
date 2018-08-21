Request to 10.1.3.251
=====================


    (arp && (eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.3.251 && eth.dst==1c:b7:2c:b0:29:c4)) || (tcp.port==21 && (ip.addr==10.1.3.251))

![arp request for ftp server](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/arp_and_tcp.png)

Internal Server Request
=======================

**request to** : [http://ams.nirmauni.ac.in/moodle259/](http://ams.nirmauni.ac.in/moodle259/)


**filter Query**:

    ((arp.dst.proto_ipv4==10.1.19.28 && eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.19.28 && eth.dst==1c:b7:2c:b0:29:c4) || (arp.dst.proto_ipv4==10.1.3.252 && eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.3.252 && eth.src==1c:b7:2c:b0:29:c4))  || (arp.src.proto_ipv4==10.1.3.252 && eth.dst==1c:b7:2c:b0:29:c4) || ((http || tcp) && ip.addr==10.1.3.252) || (dns.qry.name == ams.nirmauni.ac.in)
**Result**:
![internal server capturing](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.full.png)


#### Explanation:


    (arp.dst.proto_ipv4==10.1.19.28 && eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.19.28 && eth.dst==1c:b7:2c:b0:29:c4)
> arp is filter keyword in wireshark to display only arp packets 
> Here the goal is to filter out packets which are resolving mac address of our destination
> `eth.dst==ff:ff:ff:ff:ff:ff` will broadcast with all bits high from source machine having mac address `1c:b7:2c:b0:29:c4` where `arp.dst.proto_ipv4` used to filter arp request for given destination
> `arp.src.proto_ipv4=10.1.19.28` filters out arp request for IP Address `10.1.19.28`
> `arp.src.proto_ipv4=10.1.3.252` filters out arp request for IP Address `10.1.3.252`

    ((http || tcp) && ip.addr==10.1.3.252)
> above filter will filter all the incoming and outgoing http and tcp traffic for IP address 10.1.3.252 with the machine 
> ![tcp sync](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.tcp.sync.png) 
> Fig: TCP SYNC

> ![tcp sync+ack](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.tcp.syc.ack.png) 
> Fig: TCP SYNC + ACK

> ![http request](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.http.request.png)
> Fig: HTTP request

> ![http response](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.http.response.png)
> Fig: HTTP response

    (dns.qry.name == ams.nirmauni.ac.in)
> dns is the filter in wireshark to only display dns packets
> above query will further filter out dns packets to only those at which our target address: ams.nirmauni.ac.in is resolved; Hence we only get dns result for our target domain

> ![dns query](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.dns.query.png)
> Fig: DNS query

> ![dns query](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/scenario_2/scenario2.dns.response.png)
> Fig: DNS response

So final result of full query:

External Server Request
========================