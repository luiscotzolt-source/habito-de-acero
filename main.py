import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN PROFESIONAL
st.set_page_config(page_title="Hábito de Acero: Cloud AI", layout="wide")
st.title("🛡️ Hábito de Acero: Ingeniería Humana & Cloud AI")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIO INTEGRAL ---
with st.sidebar:
    st.header("🔑 Acceso Cloud")
    st.button("🔗 Vincular con Google Account")
    
    st.header("📋 Sección 1: Perfil Bio")
    alias = st.text_input("Nombre o Alias:", "Usuario_Pro")
    edad = st.number_input("Edad:", 15, 95, 30)
    peso = st.number_input("Peso (kg):", 40.0, 200.0, 75.0)

    st.header("🏥 Sección 2: Salud")
    salud = st.multiselect("Limitantes:", ["Artritis", "Diabetes", "Presión Alta", "Lumbalgia", "Lesión Rodilla"])
    
    st.header("🎯 Sección 3: Planificación")
    objetivo = st.selectbox("Objetivo:", ["Ganar Masa Muscular", "Perder Peso", "Fuerza y Resistencia"])
    dias = st.slider("Días a la semana:", 1, 7, 3)
    tiempo = st.slider("Minutos por sesión:", 15, 120, 60)

# --- SECCIÓN 4: MOTOR DE RUTINAS DINÁMICAS (IMÁGENES WEB) ---
st.header(f"🏋️ Rutina Semanal Dinámica para {alias}")

# Base de Datos de la "Nube" con enlaces web
db_ejercicios = {
    "Empuje": [
        {"n": "Flexiones Diamante", "s": 4, "r": "12-15", "d": "60s", "url": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=500&q=80"},
        {"n": "Press Militar (Hombros)", "s": 3, "r": "10-12", "d": "90s", "url": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=500&q=80"},
        {"n": "Fondos en Silla (Tríceps)", "s": 3, "r": "12", "d": "60s", "url": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=500&q=80"}
    ],
    "Tracción": [
        {"n": "Remo con Banda/Mancuerna", "s": 4, "r": "12-15", "d": "60s", "url": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=500&q=80"},
        {"n": "Dominadas o Jalones", "s": 3, "r": "8-10", "d": "90s", "url": "https://images.unsplash.com/photo-1583454155184-870a1f63aebc?w=500&q=80"},
        {"n": "Curl de Bíceps", "s": 3, "r": "12-15", "d": "45s", "url": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=500&q=80"}
    ],
    "Pierna": [
        {"n": "Sentadilla Búlgara", "s": 3, "r": "10-12", "d": "90s", "url": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500&q=80"},
        {"n": "Peso Muerto Rumano", "s": 4, "r": "12", "d": "60s", "url": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&q=80"},
        {"n": "Zancadas Laterales", "s": 3, "r": "15", "d": "45s", "url": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=500&q=80"}
    ],
    "Salud/Fisio": [
        {"n": "Puente Glúteo", "s": 3, "r": "15-20", "d": "45s", "url": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=500&q=80"},
        {"n":
