import nmap

def scan_target(target_ip):

    scanner = nmap.PortScanner()

    print("Scanning target:", target_ip)

    scanner.scan(target_ip, '1-1024')

    open_ports = []

    for host in scanner.all_hosts():

        for protocol in scanner[host].all_protocols():

            ports = scanner[host][protocol].keys()

            for port in ports:
                open_ports.append(port)

    return open_ports


if __name__ == "__main__":

    target = input("Enter target IP: ")

    ports = scan_target(target)

    print("Open ports:", ports)