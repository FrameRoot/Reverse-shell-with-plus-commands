# Reverse-shell-with-more-commands

A reverse shell throught tcp that has special commands [Windows Version]

What is a revershe shell:
<p><img align="center" src="https://resources.infosecinstitute.com/wp-content/uploads/110414_1037_ICMPReverse1.png" alt="."/></p>

It has 
- Full acess to the machine (as every revershe shell connection)
- RICKROLL
- Automated commands to make your life easier
- Chat to communicate between the server and the client

It will have:
- ~~Chat to communicate between the server and the client~~ (DONE)
- Flood of packets 




![Screenshot_4](https://user-images.githubusercontent.com/109004138/210141309-adea4cac-0e80-4f07-9a08-b22853a2b333.png)

# Errors
~~- DATA OVERLOAD~~ 

~~The biggest error its the number of data , the command prompt cant afford a lot of data
when you do a `dir`as an example and there is a lot of files it will divide the dir
by ```enters``` so everytime you click enter it will give a % of the data of the ```dir```~~ -->**(SOLVED)**
- cd Command


**How to install:**

```pip install -r requirements.txt or pip3 install -r requirements.txt```

```python server.py or python3 server.py```

# PROTOCOL

Only open the server with tcp protocol ports

<img align="center" alt ="tcp" width=838 src="http://www.ortizonline.com/images/sockets.gif">

Common TCP ports:

21 = FTP: File Transfer Protocol 

23 = Telnet: Telnet

25 = SMTP: Simple Mail Transfer Protocol 

53 = DNS: Domain Name System 

80 = HTTP: Hyper Text Transfer Protocol 

110 = POP3: Post Office Protocol version 3 

119 = NNTP: Net News Transport Protocol 

443 = SSL: Secure Sockets Layer
