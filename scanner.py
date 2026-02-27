import nmap
import socket

def tarama_yap(hedef_ip):
    nm = nmap.PortScanner()
    print(f"\n--- {hedef_ip} ağı üzerinde keşif başlatıldı ---")
    print("Bu işlem ağdaki cihaz sayısına göre birkaç dakika sürebilir. Lütfen bekleyin...\n")
    
    # Ağdaki cihazları ve en yaygın 1-1024 portlarını tarıyoruz
    nm.scan(hedef_ip, '1-1024', '-v -sV')
    
    for host in nm.all_hosts():
        # Sadece canlı olan cihazları ekrana yazdırıyoruz (down olanları çöpe atıyoruz)
        if nm[host].state() == 'up':
            print(f"\n[+] CANLI HEDEF YAKALANDI: {host}")
            
            # Cihazın açık portlarını ve servislerini kontrol ediyoruz
            for protokol in nm[host].all_protocols():
                portlar = nm[host][protokol].keys()
                
                # Eğer port bulduysa yazdır
                for port in portlar:
                    servis = nm[host][protokol][port]['name']
                    versiyon = nm[host][protokol][port]['version']
                    durum = nm[host][protokol][port]['state']
                    
                    print(f"  -> Port: {port} | Durum: {durum} | Servis: {servis} | Versiyon: {versiyon}")
                    
                    # İnsan mantığı: Risk Analizi
                    if port == 80 or port == 443:
                        print("     --> Not: Bu bir web sunucusu. HTTP/HTTPS yayını yapıyor.")
                    elif port == 22:
                        print("     --> Not: SSH açık. Uzaktan komut satırı bağlantısı aktif.")
                    elif port == 21:
                        print("     --> Not: FTP açık. Şifrelenmemiş dosya transferi riski!")
                    elif port == 53:
                        print("     --> Not: DNS servisi. Bu cihaz muhtemelen ağın modemi veya yönlendiricisi (router).")

if __name__ == "__main__":
    # Hedef ağ menzili (Senin bilgisayarının bağlı olduğu Wi-Fi ağı)
    hedef = "192.168.1.0/24" 
    tarama_yap(hedef)
