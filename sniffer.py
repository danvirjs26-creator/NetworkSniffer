from scapy.all import *

def packet_callback(packet):

    if packet.haslayer(IP):

        print("\n" + "="*50)

        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")

        print("Packet Size:", len(packet))

sniff(prn=packet_callback, store=False)
