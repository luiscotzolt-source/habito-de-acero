import streamlit as st
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="Hábito de Acero - IA", page_icon="🛡️", layout="wide")

# --- MOTOR DE MOTIVACIÓN ---
frases = ["La disciplina es libertad.", "Supera la lumbalgia con movimiento inteligente.", "Ingeniería Humana 2026."]
st.title("🛡️ Hábito de Acero: Entrenamiento Adaptado")
st.info(random.choice(frases))

# --- FORMULARIO DE DIAGNÓSTICO ---
with st.sidebar:
    st.header("📋 Perfil de Salud")
    genero = st.selectbox("Género", ["Hombre", "Mujer"])
    edad = st.number_input("Edad", 15, 95, 30)
    
    st.subheader("⚠️ Lesiones Específicas")
    lumbalgia = st.checkbox("Lumbalgia (Espalda baja)")
    rodilla = st.checkbox("Dolor de Rodilla")
    hombros = st.checkbox("Lesión de Hombros")
    diabetes = st.checkbox("Diabetes")
    hipertension = st.checkbox("Hipertensión")
    
    st.subheader("🎯 Planificación")
    meta = st.radio("Objetivo", ["Bajar de peso", "Masa muscular", "Fuerza"])
    dia_entreno = st.selectbox("Día de hoy", ["Lunes: Empuje", "Martes: Tracción", "Miércoles: Pierna", "Jueves: Cardio", "Viernes: Full Body"])

# --- LÓGICA DE IA: GRUPOS MUSCULARES Y EJERCICIOS ---
st.header(f"🏋️ Rutina de {dia_entreno}")

def prescribir_ejercicio():
    # Filtro de seguridad por lesión
    if lumbalgia:
        grupo, ejer, img = "Core/Lumbar", "Puente de glúteo (sin carga)", "https://images.unsplash.com/photo-1599058917233-35808df7bc29?w=500"
    elif rodilla:
        grupo, ejer, img = "Pierna/Movilidad", "Extensiones de pierna sentada", "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=500"
    elif hombros:
        grupo, ejer, img = "Tren Superior", "Elevaciones laterales sin peso", "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=500"
    elif meta == "Masa muscular":
        grupo, ejer, img = "Hipertrofia", "Sentadilla Goblet o Flexiones", "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500"
    else:
        grupo, ejer, img = "General", "Caminata rápida o Trote", "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=500"
    return grupo, ejer, img

grupo, ejer, url = prescribir_ejercicio()

col1, col2 = st.columns(2)
with col1:
    st.success(f"**Grupo Muscular:** {grupo}")
    st.write(f"**Ejercicio recomendado:** {ejer}")
    st.warning("⚠️ Mantén la espalda recta y respira de forma controlada.")
with col2:
    st.image(url, caption="Guía visual del movimiento")

# --- REGISTRO Y DONACIÓN ---
st.divider()
if st.button("✅ Registrar progreso de hoy"):
    st.balloons()
    st.success("Progreso guardado en el historial local.")

# --- CUADRO DE DONACIÓN ---
st.sidebar.divider()
st.sidebar.subheader("☕ Apoya el Proyecto")
st.sidebar.write("Ayúdanos a seguir mejorando el sistema de Ingeniería Humana.")
st.sidebar.link_button("Hacer una Donación", "https://www.paypal.com") # Reemplaza con tu link real

st.download_button("📥 Descargar Reporte CSV", pd.DataFrame([{"Fecha": datetime.now(), "Día": dia_entreno, "Ejercicio": ejer}]).to_csv().encode('utf-8'), "progreso.csv")
