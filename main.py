import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN PRO
st.set_page_config(page_title="Hábito de Acero: Cloud AI", layout="wide")
st.title("🛡️ Hábito de Acero: Ingeniería Humana & Cloud AI")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIO ---
with st.sidebar:
    st.header("🔑 Acceso Cloud")
    st.button("🔗 Vincular con Google Account")
    
    st.header("📋 Perfil y Plan")
    alias = st.text_input("Alias:", "Atleta_Pro")
    salud = st.multiselect("Limitantes:", ["Diabetes", "Lumbalgia", "Lesión Rodilla", "Hombro"])
    meta = st.selectbox("Objetivo:", ["Masa Muscular", "Definición", "Fuerza"])
    dias = st.slider("Días a la semana:", 1, 7, 3)
    tiempo = st.slider("Minutos por sesión:", 15, 120, 60)

# --- SECCIÓN 4: MOTOR DE RUTINAS (IMÁGENES WEB + SERIES/REPS) ---
st.header(f"🏋️ Rutina Semanal Dinámica para {alias}")

# Base de datos en línea (Diccionarios cerrados correctamente)
nube_empuje = [
    {"n": "Flexiones Diamante", "s": 4, "r": "12-15", "d": "60s", "url": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=500"},
    {"n": "Press Militar Banda", "s": 3, "r": "10-12", "d": "90s", "url": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=500"},
    {"n": "Fondos en Silla", "s": 3, "r": "12", "d": "60s", "url": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=500"}
]

nube_traccion = [
    {"n": "Remo con Banda", "s": 4, "r": "12-15", "d": "60s", "url": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=500"},
    {"n": "Dominadas Asistidas", "s": 3, "r": "8-10", "d": "90s", "url": "https://images.unsplash.com/photo-1583454155184-870a1f63aebc?w=500"},
    {"n": "Curl de Bíceps", "s": 3, "r": "12", "d": "45s", "url": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=500"}
]

nube_pierna = [
    {"n": "Sentadilla Búlgara", "s": 3, "r": "10-12", "d": "90s", "url": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500"},
    {"n": "Peso Muerto Rumano", "s": 4, "r": "12", "d": "60s", "url": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500"},
    {"n": "Zancadas", "s": 3, "r": "12 c/u", "d": "45s", "url": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=500"}
]

nube_salud = [
    {"n": "Puente Glúteo", "s": 3, "r": "15-20", "d": "45s", "url": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=500"},
    {"n": "Gato-Camello", "s": 3, "r": "10", "d": "30s", "url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500"}
]

# Distribución lógica por día
for i in range(1, dias + 1):
    with st.expander(f"📅 DÍA {i} - Plan de Entrenamiento", expanded=(i==1)):
        if salud:
            rutina = nube_salud
        elif i % 3 == 1: rutina = nube_empuje
        elif i % 3 == 2: rutina = nube_traccion
        else: rutina = nube_pierna
        
        for ej in rutina:
            col1, col2 = st.columns([1, 2])
            col1.image(ej["url"], use_container_width=True)
            col2.subheader(ej["n"])
            col2.markdown(f"**Series:** {ej['s']} | **Reps:** {ej['r']} | **Descanso:** {ej['d']}")
            st.write("---")

# --- SECCIÓN 5: TABLA DE RESULTADOS EN LÍNEA ---
st.divider()
st.header("📊 Registro de Progreso")

if 'log' not in st.session_state:
    st.session_state.log = []

if st.button("🚀 Registrar Sesión"):
    st.session_state.log.append({
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Alias": alias,
        "Meta": meta,
        "Status": "Completado ✅"
    })
    st.success("¡Datos guardados!")

if st.session_state.log:
    df = pd.DataFrame(st.session_state.log)
    st.table(df) # TABLA VISIBLE EN PANTALLA
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar Reporte CSV", csv, f"habito_{alias}.csv", "text/csv")

st.info("⚠️ Nota: Envía este CSV al chat cada 30 días para que yo (Gemini) analice tu evolución.")
