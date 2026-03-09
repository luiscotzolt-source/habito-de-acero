import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN PRO
st.set_page_config(page_title="Hábito de Acero: Cloud Sync", layout="wide")
st.title("🛡️ Hábito de Acero: Ingeniería Humana en Línea")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIOS ---
with st.sidebar:
    st.header("📋 PERFIL BIO-MÉDICO")
    alias = st.text_input("Nombre o Alias:", "Usuario_Pro")
    edad = st.number_input("Edad:", 15, 95, 30)
    peso = st.number_input("Peso (kg):", 40.0, 200.0, 75.0)
    
    st.subheader("🏥 CONDICIONES")
    enfermedades = st.multiselect("Enfermedades:", ["Artritis", "Diabetes", "Presión alta", "Presión baja", "Lumbalgia"])
    lesiones = st.multiselect("Lesiones:", ["Rodilla", "Hombro", "Muñecas", "Tobillos"])

    st.header("🎯 PLANIFICACIÓN")
    meta = st.selectbox("Objetivo:", ["Perder peso", "Ganar masa muscular", "Definición", "Fuerza y resistencia"])
    dias_semana = st.slider("Días a la semana:", 1, 7, 3)
    tiempo_sesion = st.slider("Minutos por sesión:", 15, 120, 60)

# --- SECCIÓN 4: MOTOR DE RUTINAS DINÁMICAS (LÓGICA DE NUBE) ---

# Definimos 3 rutinas totalmente distintas para alternar los días
rutina_a = [
    {"n": "Sentadilla Goblet", "s": 4, "r": "12", "d": "90s", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
    {"n": "Flexiones de Pecho", "s": 4, "r": "15", "d": "60s", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
    {"n": "Zancadas", "s": 3, "r": "12 c/u", "d": "60s", "img": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=400"},
    {"n": "Plancha Abdominal", "s": 4, "r": "45s", "d": "45s", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"}
]

rutina_b = [
    {"n": "Peso Muerto Rumano", "s": 4, "r": "12", "d": "90s", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"},
    {"n": "Remo con Banda", "s": 4, "r": "12", "d": "60s", "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=400"},
    {"n": "Press Militar", "s": 3, "r": "10", "d": "60s", "img": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=400"},
    {"n": "Escaladores", "s": 3, "r": "30s", "d": "45s", "img": "https://images.unsplash.com/photo-1434682881908-b43d0467b798?w=400"}
]

rutina_fisioterapia = [
    {"n": "Puente Glúteo", "s": 3, "r": "15", "d": "45s", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
    {"n": "Gato-Camello", "s": 3, "r": "10", "d": "30s", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
    {"n": "Movilidad de Cadera", "s": 3, "r": "12", "d": "30s", "img": "https://images.unsplash.com/photo-1599447421416-3414500d18a5?w=400"}
]

st.header(f"🏋️ Rutinas Semanales para {alias}")

# Bucle para generar cada día con su respectiva indentación (Línea 51 corregida)
for dia in range(1, dias_semana + 1):
    with st.expander(f"📅 RUTINA DÍA {dia}", expanded=(dia == 1)):
        # Lógica de asignación de ejercicios
        if len(enfermedades) > 0 or len(lesiones) > 0:
            lista_ejercicios = rutina_fisioterapia
            st.warning("⚠️ Adaptado por salud.")
        elif dia % 2 == 0:
            lista_ejercicios = rutina_b
        else:
            lista_ejercicios = rutina_a
            
        # Despliegue de los ejercicios dentro del expander
        for ej in lista_ejercicios:
            col1, col2 = st.columns([1, 2])
            col1.image(ej["img"], use_container_width=True)
            col2.subheader(ej["n"])
            col2.write(f"**Series:** {ej['s']} | **Reps:** {ej['r']} | **Descanso:** {ej['d']}")
            st.write("---")

# --- SECCIÓN 5: REGISTRO Y TABLA ---
st.divider()
st.header("📊 HISTORIAL DE AVANCE")

if 'log_entrenos' not in st.session_state:
    st.session_state.log_entrenos = []

if st.button("💾 REGISTRAR SESIÓN COMPLETADA"):
    log = {
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Usuario": alias,
        "Objetivo": meta,
        "Duración": f"{tiempo_sesion} min"
    }
    st.session_state.log_entrenos.append(log)
    st.success("¡Datos guardados!")

# Visualización de la Tabla
if st.session_state.log_entrenos:
    df = pd.DataFrame(st.session_state.log_entrenos)
    st.table(df) # Tabla en pantalla
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar Reporte CSV", csv, f"avance_{alias}.csv", "text/csv")
