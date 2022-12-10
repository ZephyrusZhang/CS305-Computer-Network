## Practice11.1: ICMP
- Q1: How to initiates an ICMP Echo request with 2021B length?

A1: type the following commands in cmd:

```
ping www.example.com -4 -l 2021
```

![image](https://user-images.githubusercontent.com/64548919/165669531-38fde1a5-7a26-4ddd-aa7c-8ec0339ef19d.png)


- Q2: Is there any fragmentation on the IP packets, how to find them?

A2: We can see that these packets have fragmentation.

![image](https://user-images.githubusercontent.com/64548919/165670908-b4157c09-d85a-4473-8fb1-9fa1fd72f214.png)


- Q3: How many fragments are the 2021-Byte-length IP packet divided into?

A3: It is divided into two fragments, for each of 2021-Byte-length ip packet.
This is because for two consecutive packets, one is IPv4 and one is ICMP.

![image](https://user-images.githubusercontent.com/64548919/165671085-f1648caa-0700-4a4f-8d49-c793c827f5ae.png)

This also supports the idea.

![image](https://user-images.githubusercontent.com/64548919/165671262-836387f7-3daf-42dc-a78d-6bdadef0b1b7.png)

- Q4: How to identify the ICMP Echo request and Echo reply?

A4: It could be seen in the type information of the packet:

![image](https://user-images.githubusercontent.com/64548919/165671417-23a49718-6aea-4910-ab0f-648879942e67.png)

![image](https://user-images.githubusercontent.com/64548919/165671457-b151316b-9c54-4ab4-9f29-0ed5dfab3a91.png)

- Q5: For the ICMP Echo request, which fragment is the first one, which is the last ? How to identify them?

A5: In the captured packets, the #53 is the first one, and #177 is the last one. This can be identified by the epoch time.

![image](https://user-images.githubusercontent.com/64548919/165671760-cee76672-8e7c-4f0f-b1cf-135a25abcd14.png)

- Q6: What’s the length of each IP fragment? Is the sum of each fragment’s length equal to the original IP packet?

A6: Take 1 IPv4 and 1 ICMP packet as an example.

![image](https://user-images.githubusercontent.com/64548919/165672008-2a5d7dd3-b827-4961-ac6a-0c8411c85d98.png)

The length of the IPv4 fragment is 1500, with 20 header length and 1480 data length.

![image](https://user-images.githubusercontent.com/64548919/165672231-f4b3e28b-fb66-471b-a007-69efe94fb37d.png)

The length of ICMP fragment is 569, with 20 header length and 2021 data length.

The sum is not equal, 1500 + 569 = 2069 != 2021.

## Practice11.2: tracert and ICMP

Commands: 

```
tracert -4 www.sustech.edu.cn
```

- Q1: Is there any 'Time-to-live exceeded' ICMP packets? 

A1: We can see that there are some 'TTL exceeded' ICMP packets.

![image](https://user-images.githubusercontent.com/64548919/165673522-f3232c8b-de37-42ef-bab4-cc3dd7aedcbb.png)

- Q2: What's the difference between these ICMP packets which are invoked by 'tracert' and ICMP echo request/replay packets which are invoked by 'ping'?

A2: Differences:

1. The total length of packets caused by `tracert` is much smaller than those by `ping`. The total length is 56 in `tracert` while 1500 in `ping`.

2. The packet by `ping` will contain a original packet(2021 bytes), while not by `tracert`

3. The TTL is not the same.

## Practice11.3: Packet-tracer and ICMP
Build connection first:

![image](https://user-images.githubusercontent.com/64548919/166176693-11ca628e-99b4-4436-9319-c0e8e7d00810.png)

- Q1: What's link-local unicast IPv6 address of these 2 PCs?

A1: Check the ip configuration of these two PCs.

![image](https://user-images.githubusercontent.com/64548919/166176763-476752ad-9291-432e-8708-63c4c42603f3.png)

![image](https://user-images.githubusercontent.com/64548919/166176779-64be33f9-36b8-47c5-b2f5-c61476f2d20f.png)

We can get the IPv6 address:

PC0: FE80::230:F2FF:FEBA:D0EC

PC1: FE80::2D0:97FF:FE23:5B1C

- Q2: Initiates an ICMPv6 session on PC0 to PC1, capture the packets

A2: Open a command prompt and type the following commands:

```
ping FE80::2D0:97FF:FE23:5B1C
```

![image](https://user-images.githubusercontent.com/64548919/166176937-fa7626cd-47b4-44ad-87cd-09d21b7a3e03.png)

- Q3: What’s the difference between IPv4 datagram and IPv6 datagram? List at least 3 aspects.

A3: get the ipv6 packet under the simulation mode:

![image](https://user-images.githubusercontent.com/64548919/166177811-5a93a246-2334-48e5-a3c6-57abceddaa95.png)

get the ipv4 packet under the simulation mode:

![image](https://user-images.githubusercontent.com/64548919/166178227-3e5bdd25-6d06-4e95-9230-e70f138389d0.png)

We can see there are several differences:

1. ipv6 contains hardware information, while ipv4 not
2. ipv6 omites the protocol type information
3. ipv6 omites opcde and adds hop limit in the datagram

- Q4: Does these two IPv6 addresses belong to the same sub-net, what is the sub-net ID of these two IPv6 addresses?

A4: use ipconfig to get the subnet mask.

> Subnet mask
> PC0: 255.255.255.0
> PC1: 255.255.255.0

> IP address
> PC0: 192.168.0.2
> PC1: 192.168.0.1

We do the AND operation between subnet mask and IP address. The result is same: 192.168.0.0

Thus they belong to the same sub-net, and their sub-net ID is 192.168.0.0.