### R1 - AS 100
Enable Router

    R1#en

Display interface status in brief
-----------------------------------------

    R1#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    FastEthernet0/0            unassigned      YES unset  administratively down down
    Ethernet1/0                unassigned      YES unset  administratively down down
    Ethernet1/1                192.168.12.1    YES manual up                    up
    Ethernet1/2                192.168.13.1    YES manual up                    up
    Ethernet1/3                unassigned      YES unset  administratively down down
    Loopback0                  unassigned      YES unset  up                    up
    Loopback1                  unassigned      YES unset  up                    up
    Loopback2                  unassigned      YES unset  up                    up

Setup IP configuration
-----------------------------

Enter to configuration mode

    R1#conf t

Select interface to work on

    R1(config)#int ethernet1/0         

Set interface `up` - make active

    R1(config-if)#no shut

Configure IP address

    R1(config-if)#ip address 192.168.12.1 255.255.255.0

Setup loopback

    R1(config-if)#int loop 0

Configure BGP
-------------------
	
    R1(config)#router bgp 100
    R1(config-router)#neighbor 192.168.12.2 remote-as 200 
    R1(config-router)#
    *Nov  4 15:28:21.719: %BGP-5-ADJCHANGE: neighbor 192.168.12.1 Up


**End configuration**

    R1(config-if)#end

**Write Configuration**

    R1#wr



### R2 - AS 200

	R2#en
	R2#conf t
	
	R2(config)#int fastethernet0/0
	R2(config-if)#no shut
	R2(config-if)#ip address 192.168.12.2 255.255.255.0
	
	R2(config-if)#router bgp 200
	R2(config-router)#neighbor 192.168.12.1 remote-as 100


practical 6: 
-------------
waited fair queuing



