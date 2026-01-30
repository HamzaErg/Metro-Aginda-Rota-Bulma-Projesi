# Metro Ağında Rota Bulma Projesi

Bu proje, bi metro ağındaki istasyonlar arasında en az aktarmalı ve hızlı rotaları bulmayı amaçlayan bir Python uygulamasıdır. BFS (Genişlik Öncelikli Arama) ve A* algoritmaları kullanılarak geliştirilmiştir.

## Proje Amacı

Proje, metro ağlarında yolculuk yapacak kullanıcılara yardımcı olacak bir araç sunmayı hedeflemektedir. Kullanıcılar, başlangıç ve hedef istasyonlarını belirterek, en az aktarmalı veya en hızlı rotayı bulabilmeleri amaçlanmıştır.

## Algoritmaların Çalışma Mantığı

### BFS (Genişlik Öncelikli Arama)

* Başlangıç istasyonundan başlayarak komşu istasyonları sırayla ziyaret edilir.
* Ziyaret edilen istasyonları takip eder ve tekrar ziyaret edilmez.
* En az aktarmalı rotayı bulmak için kullanılır.

### A\* Algoritması

* Başlangıç istasyonundan başlayarak hedef istasyona en hızlı rotayı bulunmasını sağlar.
* Bir fonksiyonu kullanarak en iyi yolu seçer.
* Öncelik kuyruğu (heapq) kullanarak en hızlı rotaları önceliklendirir.
* En hızlı rotayı bulmak için kullanılır.

### Neden Bu Algoritmalar?

* BFS, en az aktarmalı rotayı bulmak için uygun; çünkü katman katman arama yaparak en kısa yolu bulunmasını sağlar.
* A\*, en hızlı rotayı bulmak için uygun; çünkü bilgilendirilmiş bir arama yaparak gereksiz aramaları önler ve daha hızlı sonuç alınmasını sağlar.

