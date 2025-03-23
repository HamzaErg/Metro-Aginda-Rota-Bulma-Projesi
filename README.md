# Metro Ağında Rota Bulma Projesi

Bu proje, bi metro ağındaki istasyonlar arasında en az aktarmalı ve hızlı rotaları bulmayı amaçlayan bir Python uygulamasıdır. BFS (Genişlik Öncelikli Arama) ve A\* algoritmaları kullanılarak geliştirilmiştir.

## Proje Amacı

Proje, metro ağlarında yolculuk yapacak kullanıcılara yardımcı olacak bir araç sunmayı hedeflemektedir. Kullanıcılar, başlangıç ve hedef istasyonlarını belirterek, en az aktarmalı veya en hızlı rotayı bulabilmeleri amaçlanmıştır.

## Kullanılan Teknolojiler ve Kütüphaneler

* Python projenin temel programlama dilidir.
* **collections Modülü:**
    * **deque:** BFS algoritmasında kuyruk yapısı için kullanılır. Hızlı ekleme ve çıkarma işlemleri sağlar.
    * **defaultdict:** Metro ağındaki hatları ve istasyonları saklamak için kullanılır. Sözlük benzeri bir yapıdır.
* **heapq Modülü:** A\* algoritmasında öncelik kuyruğu (priority queue) yapısı için kullanılır. En düşük maliyetli rotaları hızlı bir şekilde bulmayı sağlar.

## Algoritmaların Çalışma Mantığı

### BFS (Genişlik Öncelikli Arama)

* Başlangıç istasyonundan başlayarak komşu istasyonları sırayla ziyaret eder.
* Ziyaret edilen istasyonları takip eder ve tekrar ziyaret etmez.
* Hedef istasyona ulaşıldığında, rotayı (istasyon listesi) döndürür.
* En az aktarmalı rotayı bulmak için kullanılır.

### A\* Algoritması

* Başlangıç istasyonundan başlayarak hedef istasyona en hızlı rotayı bulmayı amaçlar.
* Bir maliyet fonksiyonu kullanarak (gerçekleşen maliyet + tahmini maliyet) en iyi yolu seçer.
* Öncelik kuyruğu (heapq) kullanarak en düşük maliyetli rotaları önceliklendirir.
* En hızlı rotayı bulmak için kullanılır.

### Neden Bu Algoritmalar?

* BFS, en az aktarmalı rotayı bulmak için idealdir çünkü katman katman arama yaparak en kısa yolu garanti eder.
* A\*, en hızlı rotayı bulmak için idealdir çünkü bilgilendirilmiş bir arama yaparak gereksiz aramaları önler ve daha hızlı sonuç verir.

## Örnek Kullanım ve Test Sonuçları

Proje, örnek bir metro ağı ile birlikte gelmektedir. Kod içinde, farklı başlangıç ve hedef istasyonlar için rota bulma senaryoları bulunmaktadır. İhtiyaçlarınıza göre bu senaryoları değiştirebilir veya yeni senaryolar ekleyebilirsiniz.

### Örnek Kullanım ve Test Sonuçları

* **En az aktarmalı rota bulma:**

    ```python
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    ```

* **En hızlı rota bulma:**

    ```python
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    ```

Aşağıda, örnek metro ağı üzerinde yapılan bazı testlerin sonuçları bulunmaktadır:

1.  **AŞTİ'den OSB'ye:**
    * En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
    * En hızlı rota (20 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
2.  **Batıkent'ten Keçiören'e:**
    * En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
    * En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören
3.  **Keçiören'den AŞTİ'ye:**
    * En az aktarmalı rota: Keçiören -> Gar -> Kızılay -> AŞTİ
    * En hızlı rota (16 dakika): Keçiören -> Gar -> Kızılay -> AŞTİ



## Projeyi Geliştirme Fikirleri

* Kullanıcı arayüzü (GUI) veya web arayüzü ekleyerek daha kullanıcı dostu hale getirme.
* Gerçek zamanlı trafik verilerini kullanarak rota sürelerini güncelleme.
* Farklı ulaşım türlerini (otobüs, tramvay vb.) entegre etmek.
* Harita üzerinde görselleştirme yaparak rotaları daha anlaşılır hale getirilebilir.
* Farklı şehirlerin metro ağlarını destekleyecek şekilde genişletme.
* Hata yönetimi ve istisna durumları için iyileştirmeler yapma.
* Performans iyileştirmeleri yaparak büyük metro ağlarında daha hızlı sonuç verme.
