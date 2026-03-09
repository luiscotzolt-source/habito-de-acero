import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN PRO
st.set_page_config(page_title="Hábito de Acero: Cloud AI", layout="wide")
st.title("🛡️ Hábito de Acero: Sistema de Rutinas Dinámicas en Línea")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIOS ---
with st.sidebar:
    st.header("👤 PERFIL BIO-MÉDICO")
    alias = st.text_input("Nombre o Alias:", "Atleta_Pro")
    edad = st.number_input("Edad:", 15, 95, 30)
    peso = st.number_input("Peso (kg):", 40.0, 200.0, 75.0)
    
    st.subheader("🏥 CONDICIONES")
    enfermedades = st.multiselect("Enfermedades:", ["Artritis", "Diabetes", "Presión alta", "Presión baja", "Lumbalgia"])
    lesiones = st.multiselect("Lesiones:", ["Rodilla", "Hombro", "Muñecas", "Tobillos"])

    st.header("🎯 PLANIFICACIÓN")
    meta = st.selectbox("Objetivo:", ["Perder peso", "Ganar masa muscular", "Definición", "Fuerza y resistencia"])
    dias_semana = st.slider("Días a la semana:", 1, 7, 3)
    tiempo_sesion = st.slider("Minutos por sesión:", 15, 120, 60)

# --- SECCIÓN 4: BASE DE DATOS "NUBE" (SIMULADA) ---
# En una fase avanzada, esto se jalaría de una API externa o un archivo CSV online
nube_ejercicios = {
    "Bloque_Superior": [
        {"n": "Flexiones Diamante", "s": 4, "r": 12, "d": "60s", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
        {"n": "Remo con Mancuerna", "s": 4, "r": 15, "d": "60s", "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=400"},
        {"n": "Press Militar", "s": 3, "r": 10, "d": "90s", "img": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=400"},
        {"n": "Dips en Silla", "s": 3, "r": 12, "d": "45s", "img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"}
    ],
    "Bloque_Inferior": [
        {"n": "Sentadilla Búlgara", "s": 3, "r": 10, "d": "90s", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
        {"n": "Peso Muerto Rumano", "s": 4, "r": 12, "d": "60s", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"},
        {"n": "Zancadas Laterales", "s": 3, "r": 15, "d": "45s", "img": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=400"},
        {"n": "Elevación de Gemelos", "s": 4, "r": 20, "d": "30s", "img": "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=400"}
    ],
    "Bloque_Adaptado": [
        {"n": "Puente Glúteo", "s": 3, "r": 15, "d": "45s", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
        {"n": "Gato-Camello", "s": 3, "r": 10, "d": "30s", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
        {"n": "Plancha con Rodillas", "s": 3, "r": "30s", "d": "60s", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"}
    ]
}

# MOTOR LÓGICO DE DISTRIBUCIÓN SEMANAL
st.header(f"🏋️ Rutinas Semanales para {alias}")

for dia in range(1, dias_semana + 1):
    with st.expander(f"📅 DÍA {dia} DE ENTRENAMIENTO", expanded=(dia == 1
