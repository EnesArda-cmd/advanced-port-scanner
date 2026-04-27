import socket

print("="*30)
print(" Simple Port Scanner ")
print("="*30)

target = input("Enter target IP: ")

ports = [21, 22, 23, 25, 53, 80, 443]
open_ports = []

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    s.close()

print("\nScan completed.")

if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports found.")
