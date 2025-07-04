import streamlit as st
from PIL import Image
import tempfile
import cv2
from ultralytics import YOLO
import os
from dotenv import load_dotenv

# Carica variabili d'ambiente
load_dotenv()

# Percorso modello YOLO
YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH")

# Caricamento modello
model = YOLO(YOLO_MODEL_PATH)

st.title("🔍 Traffic Sign Detection and Recognition")

supported_types = ["jpg", "jpeg", "png", "bmp", "tiff", "webp"]
uploaded_file = st.file_uploader("Carica un'immagine", type=supported_types)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Immagine caricata", use_container_width=True)

        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp:
            image.convert("RGB").save(temp.name)

            if st.button("Esegui predizione"):
                with st.spinner("🧠 In esecuzione YOLO..."):
                    results = model.predict(
                        source=temp.name, save=False, save_txt=False
                    )
                    annotated_bgr = results[0].plot()
                    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
                    st.image(
                        annotated_rgb,
                        caption="📍 Risultato YOLO",
                        use_container_width=True,
                    )

    except Exception as e:
        st.error(f"Errore nell'apertura dell'immagine: {e}")
