import socket
#socket kütüphanesini indirmeyi unutma :)
def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            return True
        else:
            return False
        sock.close()
    except KeyboardInterrupt:
        print("\nTarama işlemi iptal edildi.")
        exit()
    except socket.gaierror:
        print("\nGeçerli bir IP adresi yaz.")
        exit()
    except socket.error:
        print("\nBağlanti hatasi.")
        exit()

def main():
    target = input("88.248.8.33") #ip adresini yazınız...
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Hedef IP adresi: {target_ip}")
    except socket.gaierror:
        print("\nGeçerli bir IP adresi yaz.")
        exit()

    ports = [80, 443, 21, 22, 25, 45, 3000, 8080,]  #tarama yapmak istediğiniz portları yazınız
    
    for port in ports:
        if port_scan(target_ip, port):
            print(f"Port {port} acik")
        else:
            print(f"Port {port} kapali")

if __name__ == "__main__":
    main()

#Entere bas :d

    
#İp adresinin açık ve kapalı portlarını tarar Py:3.11.4 