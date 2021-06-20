# Shark has a long tail

desc:
    We intercept the attack traffic and we know that there is a message in packets encoded in some tricky way. Can you help us decode it.
    
We are given a .pcap (Packet Capture) file. A utility called Wireshark is usually used to analyze .pcap files.
On opening the file in Wireshark we see that there are 799 packets and only TCP protocol is used.
There is a lot of gibberish in each packet and they don't seem easily decodeable to readable text.
On checking the TCP stream (only 1 stream exists), it has more gibberish. Nothing useful here.

So we start looking for other info like packet properties. On close inspection we see that packet length varies from around 40 to around 130.
This seems promising as ASCII text and symbols have a similar range in decimal.
On pulling up a ASCII table we see that ```{``` is 123 in decimal. So we search for ```Len=123``` in Wirehshark and we find a packet.
Converting packet lenghts to ASCII for previous 6 packets gives us ```AFFCTF```. So the message seems to be encoded in packet length.

![Wireshark](https://cdn.discordapp.com/attachments/698222945155153951/778860873577005086/unknown.png)

We start converting packet length to ASCII text from packet with ```Len=123```(ASCII decimal for '{') to ```Len=125```(ASCII decimal for '}')
We add the string obtained to AFFCTF{} since we know thats the flag format.
Flag: ```AFFCTF{TCPDUMP_Never_Disappoints}```

