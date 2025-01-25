import scapy.all as scapy
import optparse



parser = optparse.OptionParser()
parser.add_option("-r", "--range", dest="Network_IP", help="IP address to scan")
options, arguments = parser.parse_args()

if not options.Network_IP:
    parser.error("Usage: python3 network_scaner.py -r <IP>/24")
    exit()

    
try:
    requist = scapy.ARP(pdst=options.Network_IP)
    podcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    full_request = podcast/requist


    response = scapy.srp(full_request, timeout=1, verbose=False)[0]

    devices_infos_list = []


    for resp in response:
        device_info = {"ip":resp[1].psrc, "mac":resp[1].hwsrc}
        devices_infos_list.append(device_info)

    print("\n\n")
    print("IP Address", "\t\t", "Mac Address")
    print("------------------------------------------")
    for device in devices_infos_list:
        
        
        print(device["ip"],"\t\t",device["mac"])
except:
    print("[-] Check the format of the IP entred")













