import nmap
import html # Şifre çözücü cephanemiz eklendi!

def keskin_nisanci_taramasi(hedef_ip):
    nm = nmap.PortScanner()
    print(f"\n--- {hedef_ip} Üzerinde Hızlı Keşif (Sniper) Başlatıldı ---")
    
    # Sadece kritik portlara (80, 443) ve başlık çekme komutuna odaklanıyoruz
    nm.scan(hedef_ip, '80,443', '-v -sV --script http-title')
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print(f"\n[+] HEDEF: {host} (Cevap Süresi: Milisaniyeler!)")
            
            for protokol in nm[host].all_protocols():
                portlar = nm[host][protokol].keys()
                for port in portlar:
                    servis = nm[host][protokol][port].get('name', 'Bilinmiyor')
                    versiyon = nm[host][protokol][port].get('version', 'Bilinmiyor')
                    
                    print(f"\n  -> Port: {port} | Servis: {servis} | Versiyon: {versiyon}")
                    
                    # Sitenin başlığını (Title) çeken ajan script
                    if 'script' in nm[host][protokol][port] and 'http-title' in nm[host][protokol][port]['script']:
                        ham_title = nm[host][protokol][port]['script']['http-title']
                        
                        # İstihbarat maskesi düşürülüyor: Şifre normal metne çevriliyor
                        cozulmus_title = html.unescape(ham_title)
                        
                        print(f"     [!] Cihazın Gerçek Kimliği: {cozulmus_title}")

if __name__ == "__main__":
    hedef = "192.168.1.1" 
    keskin_nisanci_taramasi(hedef)
