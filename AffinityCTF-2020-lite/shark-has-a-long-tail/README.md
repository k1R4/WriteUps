# Shark has a long tail

desc:
    We intercept the attack traffic and we know that there is a message in packets encoded in some tricky way. Can you help us decode it.
    
We are given a .pcap (Packet Capture) file. A utility called Wireshark is usually used to analyze .pcap files.
On opening the file in Wireshark we see that there are 799 packets and only TCP protocol is used.
There is a lot of gibberish in each packet and they don't seem easily decodeable to readable text.
On checking the TCP stream (only 1 stream exists), it has more gibberish. Nothing useful here.

So we start looking for other info like packet properties. On close inspection we see that
