Request to 10.1.3.251
=====================


    (arp && (eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.3.251 && eth.dst==1c:b7:2c:b0:29:c4)) || (tcp.port==21 && (ip.addr==10.1.3.251))

Internal Server Request
=======================

request to : http://ams.nirmauni.ac.in/moodle259/login/index.php

    (arp && (eth.src==1c:b7:2c:b0:29:c4 && eth.dst==ff:ff:ff:ff:ff:ff) || (arp.src.proto_ipv4==10.1.3.252 && eth.dst==1c:b7:2c:b0:29:c4)) || ((http || dns || tcp) && ip.addr==10.1.3.252)

![internal server capturing](https://raw.githubusercontent.com/gahan9/ACN_lab/master/wireshark_capturing/dns%2Barp%2Btcp%2Bhttp_for_10.1.3.252.png)

External Server Request
========================