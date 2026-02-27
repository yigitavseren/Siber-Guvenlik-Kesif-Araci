import nmap
import socket

def tarama_yap(hedef_ip):
    nm = nmap.PortScanner()
    print(f"\n--- {hedef_ip} üzerinde keşif başlatıldı ---")
    
    # En yaygın 1-1024 portlarını tarıyoruz
    nm.scan(hedef_ip, '1-1024', '-v -sV')
    
    for host in nm.all_hosts():
        print(f"Hedef Durumu: {nm[host].state()}")
        
        for protokol in nm[host].all_protocols():
            print(f"Protokol: {protokol}")
            portlar = nm[host][protokol].keys()
            
            for port in portlar:
                servis = nm[host][protokol][port]['name']
                versiyon = nm[host][protokol][port]['version']
                durum = nm[host][protokol][port]['state']
                
                print(f"Port: {port} | Durum: {durum} | Servis: {servis} | Versiyon: {versiyon}")
                
                # İnsan mantığı: AI'nın ezberlediği değil, senin yorumun!
                if port == 80 or port == 443:
                    print("--> Not: Bu bir web sunucusu. SQL Injection veya XSS saldırılarına açık olabilir.")
                elif port == 22:
                    print("--> Not: SSH açık. Brute-force (kaba kuvvet) saldırısı denenebilir.")
                elif port == 21:
                    print("--> Not: FTP açık. Şifrelenmemiş veri transferi riski!")

# Test için kendi yerel ağını veya localhost'u kullanabilirsin
if __name__ == "__main__":
    hedef = "127.0.0.1" 
    tarama_yap(hedef)
