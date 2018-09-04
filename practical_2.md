Tasks
-------
1. Perform `ping` of various packet length (`0B`, `32B`, `65500B`) and observe.
2. `tracert` to IP/Name to local and external server
3. Observer web request with 3-tabs (TCP/HTTP - ports)


Task 1: ping to 10.1.3.17  
=========================
Source Machine: 10.1.3.33
Destination Machine: 10.1.3.17

Ping with payload `0 bytes`

    ping -s 0 10.1.3.17

Wireshark Filter:

    ip.src == 10.1.3.33 && ip.dst == 10.1.3.17

#### Result:
![0 bytes payload](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/ping_src_dst_0B.png)

ICMP echo request or echo reply packet's minimum size is `28 bytes` as described below:

> 20 byte IP header + 4 byte ICMP header + 4 byte echo request/reply header data + 0 bytes of ICMP payload data.  

Ethernet frame header will be `18 bytes` (`14 B` MAC header and `4 B` checksum)
As shown in above snapshot packet length of `0 B` payload is `42 B` total (as wireshark ignores checksum)

However for response the packet size would be `60 B`(ignoring `4 B` checksum) because minimum frame size in 
Ethernet is `64 B` and hence before transmitting the packets source ethernet will pad dummy bytes and hence response in wireshark is observed as below:

Wireshark Filter:

    ip.src == 10.1.3.17 && ip.dst == 10.1.3.33

#### Result:
![0 bytes payload](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/ping_dst_src_0B.png) 


Ping with payload `32 bytes`

    ping -s 32 10.1.3.17

Wireshark Filter:

    ip.src == 10.1.3.33 && ip.dst == 10.1.3.17

#### Result:
![32 bytes payload](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/ping_src_dst_32B.png) 

- No padding will be observed in this case as packet length `74 B` is greater than minimum ethernet frame size. 


Ping with payload `65500 bytes`

    ping -s 65500 10.1.3.17

Wireshark Filter:

    ip.src == 10.1.3.33 && ip.dst == 10.1.3.17

- In this scenario payload size `65500 B` is greater than MTU size `1480 B` hence the payload is fragmented and all other packets except last one are IP packets 
whereas last packet of remaining payload bytes will be ICMP packet as observed in below result.
#### Result:
> ![65500 bytes payload (1st packet)](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/ping_src_dst_65500B_1st.png) 
> Fig: 65500 bytes payload (1st packet) IP
> ![65500 bytes payload (last packet)](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/ping_src_dst_65500B_last.png) 
> Fig: 65500 bytes payload (last packet) ICMP

Task 2: tracert 8.8.8.8  
=======================


Task 3: Observer web request communication on ports with 3-tabs
===============================================================

    tcp && (ip.addr == 192.30.253.117 || ip.addr==104.122.122.239 || ip.addr==109.228.21.63)