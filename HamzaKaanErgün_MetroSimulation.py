import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict, deque
import heapq

# ------------------------------
# Metro Ağında Rota  Belirleme Sümülasyonu
# ------------------------------

class Istasyon:
    def __init__(self, ad):
        self.ad = ad
        self.komsular = []

    def ekle(self, istasyon, sure):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}

    def istasyon(self, ad):
        if ad not in self.istasyonlar:
            self.istasyonlar[ad] = Istasyon(ad)
        return self.istasyonlar[ad]

    def bagla(self, a, b, sure):
        self.istasyon(a).ekle(self.istasyon(b), sure)
        self.istasyon(b).ekle(self.istasyon(a), sure)

    def en_hizli(self, bas, hedef):
        
        pq = [(0, bas)]
        mesafe = {bas: 0}
        onceki = {}

        while pq:
            sure, suanki = heapq.heappop(pq)

            if suanki == hedef:
                break

            if sure > mesafe.get(suanki, float('inf')):
                continue

            for komsu, s in self.istasyonlar[suanki].komsular:
                yeni_sure = sure + s
                if yeni_sure < mesafe.get(komsu.ad, float('inf')):
                    mesafe[komsu.ad] = yeni_sure
                    onceki[komsu.ad] = suanki
                    heapq.heappush(pq, (yeni_sure, komsu.ad))

        if hedef not in mesafe:
            return None

       
        yol = []
        cur = hedef
        while cur:
            yol.append(cur)
            cur = onceki.get(cur)
        yol.reverse()

        return yol, mesafe[hedef]

    def en_az_aktarma(self, bas, hedef):
        q = deque([(bas, [bas])])
        ziyaret = {bas}
        while q:
            suanki, yol = q.popleft()
            if suanki == hedef:
                return yol
            for komsu, _ in self.istasyonlar[suanki].komsular:
                if komsu.ad not in ziyaret:
                    ziyaret.add(komsu.ad)
                    q.append((komsu.ad, yol + [komsu.ad]))
        return None


metro = MetroAgi()


metro.bagla("AŞTİ", "Kızılay", 5)
metro.bagla("Kızılay", "Ulus", 4)
metro.bagla("Ulus", "Demetevler", 6)
metro.bagla("Demetevler", "OSB", 8)
metro.bagla("Kızılay", "Sıhhiye", 3)
metro.bagla("Sıhhiye", "Gar", 4)
metro.bagla("Gar", "Keçiören", 5)
metro.bagla("Batıkent", "Demetevler", 7)
metro.bagla("Demetevler", "Gar", 9)

# ------------------------------
# Arayüz
# ------------------------------

class MetroUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Ağında Uygun Rotanın Bulması Sümülasyonu")
        self.root.geometry("900x500")

        tk.Label(root, text="Metro Ağında Uygun Rotanın Bulması Sümülasyonu", font=("Segoe UI", 20, "bold")).pack(pady=10)

        main = tk.Frame(root)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        left = tk.Frame(main)
        left.pack(side="left", fill="y")

        istasyonlar = list(metro.istasyonlar.keys())

        tk.Label(left, text="Başlangıç").pack()
        self.start = ttk.Combobox(left, values=istasyonlar)
        self.start.pack()

        tk.Label(left, text="Hedef").pack(pady=(10,0))
        self.end = ttk.Combobox(left, values=istasyonlar)
        self.end.pack()

        self.mode = tk.StringVar(value="fast")
        tk.Radiobutton(left, text="En Hızlı", variable=self.mode, value="fast").pack(pady=10)
        tk.Radiobutton(left, text="En Az Aktarmalı", variable=self.mode, value="transfer").pack()

        tk.Button(left, text="Hesapla", command=self.hesapla).pack(pady=20)

        self.out = tk.Text(main, font=("Consolas", 11))
        self.out.pack(side="right", fill="both", expand=True)

    def hesapla(self):
        bas = self.start.get()
        hedef = self.end.get()
        self.out.delete("1.0", tk.END)

        if not bas or not hedef:
            messagebox.showwarning("Uyarı", "İstasyon seçiniz")
            return

        if self.mode.get() == "fast":
            sonuc = metro.en_hizli(bas, hedef)
            if not sonuc:
                self.out.insert(tk.END, "Rota bulunamadı")
                return
            yol, sure = sonuc
            self.out.insert(tk.END, f"En hızlı rota ({sure} dk):\n" + " → ".join(yol))
        else:
            yol = metro.en_az_aktarma(bas, hedef)
            if not yol:
                self.out.insert(tk.END, "Rota bulunamadı")
                return
            self.out.insert(tk.END, "En az aktarmalı rota:\n" + " → ".join(yol))


if __name__ == "__main__":
    root = tk.Tk()
    MetroUI(root)
    root.mainloop()
