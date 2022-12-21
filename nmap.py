import nmap

# Crea una instancia de "nmap.PortScanner"
nm = nmap.PortScanner()

# Escanea todos los dispositivos en la red con los puertos 1-65535
nm.scan(hosts='192.168.0.0/24', arguments='-p1-65535')

# Recorre todos los dispositivos encontrados en la red
for host in nm.all_hosts():
    print(f'Dispositivo: {host}')

    # Obtiene información sobre los puertos abiertos del dispositivo
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print(f'  Puerto {port}: {nm[host][proto][port]['state']}')
