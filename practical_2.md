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
  
Task 2: Trace Route to 8.8.8.8    
=======================

    jarvis@jarvis:~$ sudo traceroute -I 8.8.8.8
#### Result:
    traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
     1  200.200.200.1 (200.200.200.1)  0.237 ms  0.256 ms  0.302 ms
     2  27.116.51.70 (27.116.51.70)  8.255 ms  8.273 ms  8.278 ms
     3  182.237.15.149 (182.237.15.149)  8.429 ms  8.417 ms  8.352 ms
     4  10.221.221.37 (10.221.221.37)  9.845 ms * *
     5  * * *
     6  * 103.241.47.130 (103.241.47.130)  16.370 ms *
     7  * 108.170.248.193 (108.170.248.193)  16.816 ms *
     8  * * *
     9  google-public-dns-a.google.com (8.8.8.8)  13.722 ms  13.488 ms  13.481 ms

> TTL is not measured by the no of seconds but the no of hops. Its the maximum number of hops that a packet can travel through across the internet, before its discarded.  

- Trace Route works by initially setting the TTL for a packet to `1` as observed in below figure:
>![TTL packet set to 1](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/2.traceroute_8.8.8.8_ttl1.png)
> Fig: TTL packet set to 1

- Router's job here is to decrease TTL by `1` ( so that packet won't flow endlessly and it can be discarded when TTL reaches to `0`)
- When TTL value becomes `0` (no further travel) the receiving router will drop the packet and informs the original sender (informed that `the TTL value exceeded and it cannot forward the packet further`).

> ![TTL 10](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/2.traceroute_8.8.8.8_ttl10.png)
> Fig: TTL where no value exceeded

> ![TTL response](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/2.traceroute_8.8.8.8_ttl121_response.png)
> Fig: TTL response

> ![working of traceroute](https://www.slashroot.in/sites/default/files/traceroute%20working%20explained.png)
> Fig: TTL (working of traceroute)
  
Task 3: Observer web request communication on ports with 3-tabs  
===============================================================  
  
### Browsing to below three websites in three different tabs simultaneously:    
| Domain | IP Address | Web-URL |
|--------|------------|-----|
| github.com | 192.30.253.117 | https://github.com/ |
| www.apple.com | 104.122.122.239 | https://www.apple.com/ |
| www.sherlockology.com | 109.228.21.63 | http://www.sherlockology.com/ |

Below are the details of service connection for above websites from source machine `10.1.3.33`
| Source IP | Source Port | Destination IP | Destination Port |
|--------|----------------|-------------|-----|
| 10.1.3.33 | 43312 | 192.30.253.117 | 443 |
| 10.1.3.33 | 39573 | 104.122.122.239 | 443 |
| 10.1.3.33 | 56127 | 109.228.21.63 | 80 |

As shown in above tabular data destination server like github, apple has their fixed port for communication but from the source machine `10.1.3.33` Operating System has opened a free available port on system to establish TCP connection with different server with different browser tab.
Ex. - for IP address `192.30.253.117` (github) operating system of source machine (`10.1.3.33`) has opened a port `43312` hence all packet will now communicate not only with IP address but with port too so that packets can be delivered to correct browser tab. similarly connection to `109.228.21.63` established on source machine's port `56127`. The Illustration is shown in below results captured in wireshark:

> ![10.1.3.33:43312 -> 192.30.253.117:443](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/3.192.30.253.117_port-43312.png)
> Source Machine `10.1.3.33` opened port `43312` to communicate with `192.30.253.117:443`

> ![10.1.3.33:43312 -> 104.122.122.239:443](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/3.104.122.122.239_port-39573.png)
> Source Machine `10.1.3.33` opened port `39573` to communicate with `104.122.122.239:443`

> ![10.1.3.33:43312 -> 109.228.21.63:80](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/practical_2/3.109.228.21.63_port-56127.png)
> Source Machine `10.1.3.33` opened port `56127` to communicate with `109.228.21.63:80`

