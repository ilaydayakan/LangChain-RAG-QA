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

langchain_rag_api/
├── `gradio_app.py`         # Gradio arayüzü
├── `rag.py`                # RAG zinciri tanımı
├── `evaluate_rag.py`       # QA doğruluk değerlendirmesi
├── `my_document.txt`       # Örnek metin dosyası
├── `requirements.txt`      # Gereksinimler
└── `README.md`             # Bu döküman


## 📎 Notlar

- Python 3.11 veya 3.10 önerilir.
- Hafif model seçimi sayesinde düşük sistemlerde çalışır.
- HuggingFace API anahtarı gerekmez, modeller lokalde çalışır.
