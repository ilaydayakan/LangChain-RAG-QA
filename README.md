# LangChain-RAG-QA
Bu proje, LangChain, HuggingFace Transformers ve Gradio kullanarak oluşturulmuş, belge tabanlı (PDF/metin) bir Soru-Cevap (RAG) sistemidir. Kullanıcılar yükledikleri belgelerden kısa, doğru ve bağlama uygun cevaplar alabilir.

## 🚀 Özellikler

- 📄 PDF veya metin dosyasından içerik yükleme
- 🔍 FAISS ile hızlı vektör arama
- 🤖 HuggingFace `flan-t5-base` modeliyle kısa ve anlamlı cevaplar
- 🎛 Gradio arayüzü
- 🧪 Değerlendirme scripti ile QA doğruluk testi (Precision/Recall/F1)

## 🔎 Örnek Arayüz
<img width="1878" height="558" alt="Arayüz" src="https://github.com/user-attachments/assets/c6e2770c-ffbd-4afd-89f4-4b0aaf8bb837" />

## 📊 Değerlendirme Sonuçları
evaluate_rag.py dosyası ile sistemin cevaplama başarımı ölçülmüştür. 5 örnek soruda sistemin performansı:
- Precision: 1.00
- Recall   : 0.60
- F1 Score : 0.75


## 🧩 Ana Dosyalar

- `rag.py`: Belge yükleme, chunklama, embedding oluşturma ve QA işlemlerini gerçekleştiren ana dosya.

- `gradio_app.py`: Gradio tabanlı kullanıcı arayüzünü sağlayan uygulama arayüzü.

- `evaluate_rag.py`: QA sisteminin doğruluğunu değerlendiren metrikleri hesaplayan dosya.

- `my_document.txt`: Test amaçlı kullanılan örnek metin belgesi.

- `requirements.txt`: Projede gerekli olan tüm kütüphane ve paketleri listeleyen dosya.

- `README.md`: Projenin genel açıklamasını, kullanım yönergelerini ve kurulum adımlarını içeren dökümantasyon.



## 📎 Notlar

- Python 3.11 veya 3.10 önerilir.
- Hafif model seçimi sayesinde düşük sistemlerde çalışır.
- HuggingFace API anahtarı gerekmez, modeller lokalde çalışır.
