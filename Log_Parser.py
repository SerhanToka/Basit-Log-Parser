veritabani_loglari = [
    {"tarih": "10:00", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"},
    {"tarih": "10:05", "ip": "10.0.0.1", "kullanici": "root", "durum": "failed"},
    {"tarih": "10:06", "ip": "10.0.0.1", "kullanici": "admin", "durum": "failed"},
    {"tarih": "10:10", "ip": "172.16.0.2", "kullanici": "guest", "durum": "failed"},
    {"tarih": "10:15", "ip": "10.0.0.1", "kullanici": "administrator", "durum": "failed"},
    {"tarih": "10:20", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"}
]

def log_analiz_et(log_listesi, hedef_durum="failed"):
    eslesen_log_sayisi = 0
    hedef_ipler = set()
    for log in log_listesi:
        if log["durum"] == hedef_durum:
            eslesen_log_sayisi += 1
            hedef_ipler.add(log["ip"])

    return eslesen_log_sayisi, hedef_ipler

basarisiz_loglar, basarisiz_ipler = log_analiz_et(log_listesi=veritabani_loglari, hedef_durum="failed")
basarili_loglar, basarili_ipler = log_analiz_et(log_listesi=veritabani_loglari, hedef_durum="success")

while True:
    secim = input("Goruntulemek istediginiz verinin numarasini yaziniz: (1)Basarili Loglar ve IP'ler, (2)Basarisiz Loglar ve IP'ler, (3)Tumu, (q)Cikis")

    if secim == "1":
        print(f"Basarili Log Sayisi: {basarili_loglar}, Basarili IP'ler: {basarili_ipler}")
    elif secim == "2":
        print(f"Basarisiz Log Sayisi: {basarisiz_loglar}, Basarisiz IP'ler: {basarisiz_ipler}")
    elif secim == "3":
        print(f"Basirili Log Sayisi: {basarili_loglar} | Basarisiz Log Sayisi: {basarisiz_loglar} | Basarili IP'ler: {basarili_ipler} | Basarisiz IP'ler: {basarisiz_ipler} ")
    elif secim.lower() == "q":
        break
    else:
        print("Yanlis secim yaptiniz, tekrar deneyiniz")