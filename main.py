import socket
#сканирование всех IP-адресов
def scan_hosts(hosts, port_list):
    for host in hosts:
        scan_ports(host, port_list)
def scan_ports(host, port_list):
    print(f"Scan started. Host:{host}")
    for port in port_list:
        try:
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           result = sock.connect_ex((host, port))

           if result == 0:
               print(f"Port {port} is open")
           else:
               print(f"Port {port} is closed")

           sock.close()

        except socket.error:
            print(f"Could not connect to {host}:{port}")
    print("Scan is finished!")


hosts = ["192.168.1.163",
         "192.168.1.73"] # сюда нужно вставить IP адрес сканируемых хостов, то есть либо вторую ВМ, либо основную ОС
port_list = [80, 443, 22, 3389] # список портов (можно изменять для проверок)
scan_hosts(hosts,port_list)
