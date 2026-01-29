import heapq
from collections import deque
import tkinter as tk
from tkinter import ttk, messagebox

class Istasyon:
    def __init__(self, idx, ad):
        self.idx = idx
        self.ad = ad
        self.komsular = {}  # idx -> süre

class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}

    def istasyon_ekle(self, idx, ad):
        self.istasyonlar[idx] = Istasyon(idx, ad)

    def baglanti_ekle(self, a, b, sure):
        self.istasyonlar[a].komsular[b] = sure
        self.istasyonlar[b].komsular[a] = sure

    
    def en_az_aktarma_bul(self, bas, hedef):
        kuyruk = deque([(bas, [bas])])
        ziyaret = set([bas])

        while kuyruk:
            simdiki, yol = kuyruk.popleft()
            if simdiki == hedef:
                return [self.istasyonlar[i] for i in yol]

            for komsu in self.istasyonlar[simdiki].komsular:
                if komsu not in ziyaret:
                    ziyaret.add(komsu)
                    kuyruk.append((komsu, yol + [komsu]))

        return None
        
    def en_hizli_rota_bul(self, bas, hedef):
        pq = [(0, bas, [bas])]
        en_iyi = {bas: 0}

        while pq:
            maliyet, simdiki, yol = heapq.heappop(pq)

            if simdiki == hedef:
                return [self.istasyonlar[i] for i in yol], maliyet

            for komsu, sure in self.istasyonlar[simdiki].komsular.items():
                yeni_maliyet = maliyet + sure
                if komsu not in en_iyi or yeni_maliyet < en_iyi[komsu]:
                    en_iyi[komsu] = yeni_maliyet
                    heapq.heappush(
                        pq,
                        (yeni_maliyet, komsu, yol + [komsu])
                    )

        return None

metro = MetroAgi()

istasyonlar = [
    (1, "AŞTİ"),
    (2, "Kızılay"),
    (3, "Ulus"),
    (4, "Sıhhiye"),
    (5, "OSB")
]

for idx, ad in istasyonlar:
    metro.istasyon_ekle(idx, ad)

baglantilar = [
    (1, 2, 6),
    (2, 4, 4),
    (4, 3, 3),
    (3, 5, 8),
    (2, 3, 5)
]

for a, b, s in baglantilar:
    metro.baglanti_ekle(a, b, s)

# -------------------------------
# ARAYÜZ
# -------------------------------

def arayuz_baslat(metro: MetroAgi):
    root = tk.Tk()
    root.title("Metro Rota Bulma Sistemi")
    root.geometry("850x450")

    tk.Label(
        root,
        text="Metro Ağında Rota Bulma",
        font=("Segoe UI", 18, "bold")
    ).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    istasyon_adlari = [i.ad for i in metro.istasyonlar.values()]

    tk.Label(frame, text="Başlangıç").grid(row=0, column=0, padx=10)
    tk.Label(frame, text="Hedef").grid(row=0, column=1, padx=10)

    start_cb = ttk.Combobox(frame, values=istasyon_adlari, width=20)
    end_cb = ttk.Combobox(frame, values=istasyon_adlari, width=20)

    start_cb.grid(row=1, column=0, padx=10)
    end_cb.grid(row=1, column=1, padx=10)

    algoritma = tk.StringVar(value="fast")

    tk.Radiobutton(
        frame, text="En Hızlı Rota (A*)",
        variable=algoritma, value="fast"
    ).grid(row=2, column=0, pady=10)

    tk.Radiobutton(
        frame, text="En Az Aktarmalı (BFS)",
        variable=algoritma, value="bfs"
    ).grid(row=2, column=1)

    output = tk.Text(root, height=10, font=("Consolas", 11))
    output.pack(fill="both", padx=20, pady=10)

    ad_to_id = {i.ad: i.idx for i in metro.istasyonlar.values()}

    def hesapla():
        output.delete("1.0", tk.END)

        bas_ad = start_cb.get()
        hedef_ad = end_cb.get()

        if bas_ad not in ad_to_id or hedef_ad not in ad_to_id:
            messagebox.showwarning("Hata", "Geçerli istasyon seçiniz")
            return

        bas = ad_to_id[bas_ad]
        hedef = ad_to_id[hedef_ad]

        if algoritma.get() == "bfs":
            yol = metro.en_az_aktarma_bul(bas, hedef)
            if yol:
                output.insert(
                    tk.END,
                    "En az aktarmalı rota:\n" +
                    " → ".join(i.ad for i in yol)
                )
            else:
                output.insert(tk.END, "Rota bulunamadı")
        else:
            sonuc = metro.en_hizli_rota_bul(bas, hedef)
            if sonuc:
                yol, sure = sonuc
                output.insert(
                    tk.END,
                    "En hızlı rota:\n" +
                    " → ".join(i.ad for i in yol) +
                    f"\n\nToplam Süre: {sure} dk"
                )
            else:
                output.insert(tk.END, "Rota bulunamadı")
    tk.Button(
        root,
        text="Rota Hesapla",
        command=hesapla,
        bg="#2563eb",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=20
    ).pack(pady=10)

    root.mainloop()

arayuz_baslat(metro)
