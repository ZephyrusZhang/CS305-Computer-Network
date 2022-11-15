## Practice 1

![image-20221115130428239](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221115130428239.png)

- 伪首部

  - 源IP：78e8 + d7f0 = 150d8
  - 目的IP：0a1a + 80a9 = 8ac3
  - TCP：0006 
  - TCP头和数据长度：14 + 4 = 0018

- TCP头：0bd1 + 3646 + c353 + 0776 + bc19 + 5010 + 5018 + 00f5 + 0000 + 0000 = 26a16

- Data: ff79 + 2bb0 = 12b29

- 150d8 + 8ac3 + 0006 + 0018 + 26a16 + 12b29 = 570f8

- 5 + 70f8= 70fd

- 0111 0000 1111 1101

  1000 1111 0000 0010

  8F02

## Practice 2

1. ![image-20221101110622473](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221101110622473.png)

   Client IP address is **192.168.1.102**. Client port is **1161**.

2. ![image-20221101110732908](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221101110732908.png)

   IP address of gaia.cs.umass.edu is **128.118.245.12**. The port number is **80**.

3. ![image-20221101112929877](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221101112929877.png)

   The sequence number is **0**. The **Syn** part in Flags is set to **1** to indicate this segment is a SYN segment.

4. ![image-20221101113309807](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221101113309807.png)

   The sequence number is **0**.

   The value of Acknowledgement field is **1**. The value of the Acknowledgement field in the SYNACK segment is determined by the server gaia.cs.umass.edu. The server adds 1 to the initial sequence number of SYN segment form the client computer. For this case, the initial sequence number of SYN segment from the client computer is 0, thus the value of the Acknowledgement field in the SYNACK segment is 1.

   A segment will be identified as a SYNACK segment if both SYN flag and Acknowledgement in the segment are set to 1.

5. ![image-20221101113833536](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221101113833536.png)

   The sequence number is **164041**. 

6. The difference between the acknowledged sequence numbers of two consecutive ACKs indicates the data received by the server between these two ACKs.

   After the TCP connection is established.

7. The `alice.txt` on the hard drive is 152,136 bytes, and the download time is 5.651141 (Last TCP segment) ‐ 0 (First TCP segment) = 5.651141 second. Therefore, the throughput for the TCP connection is computed as 152,136/5.651141=26921.28899 bytes/second.
