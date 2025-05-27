# CanDork

🔍 **CanDork**, Google Dork sorgularını kullanarak hedef odaklı bilgi toplama (reconnaissance) işlemini kolaylaştıran bir araçtır. Python dili ile yazılmıştır ve siber güvenlik alanında pasif bilgi toplama süreçlerini otomatikleştirmek için geliştirilmiştir.

## 🚀 Özellikler

- Belirtilen hedef alan adı (domain) için otomatik Google Dork taramaları yapar.
- Dork türlerine göre sınıflandırılmış sonuçlar üretir (dosya uzantısı, dizin, hata mesajı vb.).
- Terminal üzerinde sade ve etkili çıktı sunumu.
- Açık kaynaklı ve özelleştirilebilir yapı.

## 🛠 Kurulum

Projeyi sisteminize klonlayın:

```bash
git clone https://github.com/CyberCan19/CanDork.git
cd CanDork
Python bağımlılıklarını yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Not: Google, bot davranışı algıladığında aramaları engelleyebilir. Bu nedenle kullanımda dikkatli olun.

⚙️ Kullanım
bash
Kopyala
Düzenle
python candork.py
Konsol üzerinden hedef domain girmeniz istenecektir. Örneğin:

yaml
Kopyala
Düzenle
Hedef domaini girin: example.com
Ardından araç otomatik olarak Google Dork sorgularını çalıştırarak sonuçları gösterecektir.

📂 Örnek Dork Kategorileri
site:example.com filetype:pdf

site:example.com intitle:index.of

site:example.com inurl:admin

site:example.com "SQL syntax"

🧠 Uyarılar
Bu araç yalnızca eğitim ve etik siber güvenlik testleri için tasarlanmıştır.

Gerçek sistemler üzerinde izinsiz kullanımı yasal değildir ve suç teşkil edebilir.

Sorumluluk tamamen kullanıcıya aittir.

👨‍💻 Geliştirici
CyberCan19
GitHub: @CyberCan19

📄 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
