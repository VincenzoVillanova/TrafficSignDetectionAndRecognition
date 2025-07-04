# 🚦 Traffic Sign Detection and Recognition Web App

Applicazione web per il rilevamento e riconoscimento automatico di segnali stradali utilizzando il modello YOLOv11n e un'interfaccia intuitiva sviluppata con **Streamlit**.

---

## 🧠 Modello AI

Il cuore dell'applicazione è un modello **YOLOv11-nano** personalizzato (`best.pt`) addestrato su un dataset specializzato per il riconoscimento di segnali stradali. Il modello è ottimizzato per garantire elevata precisione mantenendo prestazioni veloci anche su hardware standard.

**Caratteristiche del modello:**
- Architettura: YOLOv11-nano
- Formato: PyTorch (.pt)
- Dimensioni compatte per deployment rapido
- Addestramento su dataset dedicato ai segnali stradali

---

## 📁 Struttura del Progetto

```
TrafficSignDetectionAndRecognition/
├── 📁 image_test/          # Immagini di esempio per il testing
├── 📁 Video/
│   └── video.mp4          # Video dimostrativo
├── 📄 best.pt             # Modello YOLOv11 addestrato
├── 📄 main.py             # Applicazione Streamlit principale
├── 📄 requirements.txt    # Dipendenze Python
├── 📄 .env                # Variabili d'ambiente
├── 📓 YOLOv11-nano.ipynb  # Notebook training e testing
├── 📓 Dataset.ipynb       # Notebook download dataset
└── 📄 README.md           # Documentazione
```

---

## 🛠️ Installazione e Setup

### Prerequisiti
- Python 3.8+
- pip package manager
- Connessione internet

### 1. Clonazione del Repository

```bash
git clone https://github.com/VincenzoVillanova/TrafficSignDetectionAndRecognition.git
cd TrafficSignDetectionAndRecognition
```

### 2. Creazione Ambiente Virtuale

```bash
# Creazione ambiente virtuale
python -m venv .venv

# Attivazione ambiente
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

### 3. Installazione Dipendenze

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configurazione

### File `.env`

Crea o modifica il file `.env` nella directory root:

```env
YOLO_MODEL_PATH=best.pt
ROBOFLOW_API_KEY="inserisci_qui_la_tua_api_key_roboflow"
```

> **Nota:** La chiave API Roboflow è necessaria per alcune funzionalità avanzate. Recuperare la key dalla mail inviata ai docenti del corso.

---

## 🚀 Avvio dell'Applicazione

### Lancio della Web App

```bash
streamlit run main.py
```

L'applicazione sarà disponibile su: `http://localhost:8501`

### Utilizzo dell'Interfaccia

1. **Carica un'immagine** utilizzando l'uploader
2. **Seleziona le immagini di test** dalla cartella `image_test/`
3. **Visualizza i risultati** con bounding box e classificazioni

---

## 🎯 Testing e Esempi

### Immagini di Test Disponibili

La cartella `image_test/` contiene esempi pronti per il testing:

```
image_test/
├── img1.png  
├── img2.png  
├── img3.jpg  
├── img4.jpg  
└── img5.png  
```

### Jupyter Notebooks

- **`YOLOv11-nano.ipynb`**: Training, validazione e testing del modello
- **`Dataset.ipynb`**: Download e preparazione del dataset

---

## 🎬 Dimostrazione Video

https://github.com/user-attachments/assets/847c75c5-d9bd-4d34-aa36-6088da6753a7

<video width="100%" controls>
  <source src="Video/video.mp4" type="video/mp4">
  Il tuo browser non supporta il tag video. <a href="Video/video.mp4">Clicca qui per scaricare il video</a>.
</video>

---

## 💡 Funzionalità Principali

- **Rilevamento Real-time**: Identificazione rapida di segnali stradali
- **Classificazione Multi-classe**: Riconoscimento di diverse tipologie di segnali
- **Interfaccia User-friendly**: Design intuitivo e responsivo
- **Visualizzazione Avanzata**: Bounding box colorati con confidence score

---

## 🤝 Contribuzioni

Contributi, segnalazioni di bug e richieste di funzionalità sono benvenute! Per contribuire:

1. Fai un fork del repository
2. Crea un branch per la tua feature
3. Committa le modifiche
4. Pusha sul branch
5. Apri una Pull Request

---

## 👨‍💻 Autori

- **Giulio Pedicone**
- **Vincenzo Villanova**  
- **Francesco Prospero antonio Pio Virzì**  

*Progetto realizzato per il corso di Machine Learning 2025*  
*Università degli Studi di Catania*

📧 Email: [VLLVCN02M19C351R@studium.unict.it]  
🔗 GitHub: [@VincenzoVillanova](https://github.com/VincenzoVillanova)

---

*Ultimo aggiornamento: Luglio 2025*
