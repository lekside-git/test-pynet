#!/usr/bin/env python3
#
ip_addr = "10.12.17.1"
header = "-" * 20
header1 = "ip_addr"
header2 = "ip_addr1"
header3 = "ip_addr2"
mac_addr = "0024.c4e9.48ae"

sf_gw1 = "172.31.255.1/24"
sf_gw2 = input("Please input 'sf_gw2' IP address: ")
header4 = "sf_gw1"
header5 = "sf_gw2"
header = "-" * 20
#


print()
print(f"{header4:^20} {header5:^20}")
print(f"{header:^20} {header:^20}")
print(f"{sf_gw1:^20} {sf_gw2:^20}")
print()


### Another solution
#def main2():
#sf_gw1 = '172.31.255.1/24'
#sf_gw2 = input("Please input 'sf_gw2' IP address: ")
#print()
#print(f"{'sf_gw1':^20} {'sf_gw2':^20}")
#print(f"{'-'*20} {'-'*20}")
#print(f"{sf_gw1:^20} {sf_gw2:^20}")
#if __name__ == '__main2__':
#main2a

### Exercise 2
dc_location = input("Please input 'DATA CENTER LOCATION' : ")
print(dc_location.upper())
print(repr(dc_location))
print(dc_location.strip())
print(repr(dc_location))
print(repr(dc_location.upper().strip()))

### Exercise3
line = 'Processor board ID FAL127990LA'
print(line.split())
new_line = line.split()
print(new_line[3])

### Exercise4
print("Processor board ID" in line)

### Exercise5
### String concantenation for 10.12.17.1 --> 0024.c4e9.48ae
print(ip_addr + " --> "  + mac_addr)


### F-string
print(f"{ip_addr} --> {mac_addr}")


## format method
print("This is the ip and mac: {} {}".format(ip_addr, "mac_addr"))
#
#


