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

7. The `alice.txt` on the hard drive is 152,138 bytes, and the download time is 1.578736000 (First TCP segment) ‐ 0.271257000 (last ACK) = 1.307479 second. Therefore, the throughput for the TCP connection is computed as 152,138/1.307479=116359.803867 bytes/second.