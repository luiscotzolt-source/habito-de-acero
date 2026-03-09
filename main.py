import streamlit as st
import pandas as pd
from datetime import datetime
import random

# CONFIGURACIÓN DE INTERFAZ
st.set_page_config(page_title="Hábito de Acero: Cloud AI", layout="wide")
st.title("🛡️ Hábito de Acero: Ingeniería Humana & Cloud AI")

# --- SECCIÓN 1, 2 Y 3: EL CUESTIONARIO INTEGRAL ---
with st.sidebar:
    st.header("🔑 Acceso Cloud")
    st.button("🔗 Vincular con Google Account")
    
    st.header("📋 Sección 1: Perfil")
    alias = st.text_input("Nombre o Alias:", "Usuario_Pro")
    edad = st.number_input("Edad:", 15, 95, 30)
    peso = st.number_input("Peso (kg):", 40, 200, 75)
    estatura = st.number_input("Estatura (cm):", 120, 220, 170)

    st.header("🏥 Sección 2: Salud")
    salud = st.multiselect("Limitantes:", ["Artritis", "Diabetes", "Presión Alta", "Lumbalgia", "Lesión Rodilla"])
    
    st.header("🎯 Sección 3: Plan")
    objetivo = st.selectbox("Objetivo:", ["Ganar Masa Muscular", "Perder Peso", "Fuerza y Resistencia"])
    dias = st.slider("Días a la semana:", 1, 7, 3)
    tiempo = st.slider("Minutos por sesión:", 15, 120, 60)

# --- SECCIÓN 4: MOTOR DE RUTINAS DINÁMICAS (BAJADAS DE LÍNEA) ---
st.header(f"🏋️ Rutina Semanal Dinámica para {alias}")

# Diccionario Maestro (Simulación de Nube)
db_ejercicios = {
    "Empuje": [
        {"n": "Flexiones Diamante", "s": 4, "r": 12, "d": "60s", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
        {"n": "Press Militar con Banda", "s": 3, "r": 10, "d": "90s", "img": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=400"}
    ],
    "Tracción": [
        {"n": "Remo con Mancuerna", "s": 4, "r": 15, "d": "60s", "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=400"},
        {"n": "Dominadas o Jalones", "s": 3, "r": 10, "d": "90s", "img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"}
    ],
    "Pierna": [
        {"n": "Sentadilla Búlgara", "s": 3, "r": 12, "d": "90s", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
        {"n": "Peso Muerto Rumano", "s": 4, "r": 12, "d": "60s", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"}
    ],
    "Salud": [
        {"n": "Puente Glúteo", "s": 3, "r": 15, "d": "45s", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
        {"n": "Movilidad de Cadera", "s": 3, "r": "1 min", "d": "30s", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"}
    ]
}

# Lógica de creación de días distintos
for d_idx in range(1, dias + 1):
    with st.expander(f"📅 DÍA {d_idx} - Plan Específico", expanded=(d_idx==1)):
        # Selección de rutina basada en el día para que NO se repitan
        if len(salud) > 0:
            categoria = "Salud"
        elif d_idx % 3 == 1: categoria = "Empuje"
        elif d_idx % 3 == 2: categoria = "Tracción"
        else: categoria = "Pierna"
        
        rutina_actual = db_ejercicios[categoria]
        
        for ej in rutina_actual:
            c1, c2 = st.columns([1, 2])
            c1.image(ej["img"], use_container_width=True)
            c2.subheader(ej["n"])
            c2.write(f"**Series:** {ej['s']} | **Reps:** {ej['r']} | **Descanso:** {ej['d']}")
            st.write("---")

# --- SECCIÓN 5: REGISTRO EN TABLA Y ASESORÍA ---
st.divider()
st.header("📊 Registro de Carga Progresiva")

if 'session_log' not in st.session_state:
    st.session_state.session_log = []

if st.button("🚀 Registrar Entrenamiento en la Nube"):
    entry = {
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Alias": alias,
        "Meta": objetivo,
        "Día_Prog": f"Día {len(st.session_state.session_log) + 1}",
        "Estatus": "Completado"
    }
    st.session_state.session_log.append(entry)
    st.balloons()

# VISUALIZACIÓN DE TABLA
if st.session_state.session_log:
    df = pd.DataFrame(st.session_state.session_log)
    st.subheader("📋 Tu Historial Activo")
    st.table(df) # TABLA VISIBLE
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar Avance para Asesoría Gemini", csv, f"habito_{alias}.csv", "text/csv")

st.warning("⚠️ Nota: Sube este archivo al chat cada 30 días. Yo (Gemini) analizaré tu prog
