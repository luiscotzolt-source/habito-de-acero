import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN DE INGENIERÍA
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

# --- SECCIÓN 4: MOTOR DE RUTINAS DINÁMICAS (NUBE SIMULADA) ---
st.header(f"🏋️ Rutina Semanal Dinámica para {alias}")

# Base de datos de ejercicios por categorías para variar cada día
db_ejercicios = {
    "Empuje": [
        {"n": "Flexiones Diamante", "s": 4, "r": "12", "d": "60s", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
        {"n": "Press Militar con Banda", "s": 3, "r": "10", "d": "90s", "img": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=400"},
        {"n": "Fondos en silla", "s": 3, "r": "12", "d": "60s", "img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"}
    ],
    "Tracción": [
        {"n": "Remo con Mancuerna", "s": 4, "r": "15", "d": "60s", "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=400"},
        {"n": "Dominadas o Jalones", "s": 3, "r": "10", "d": "90s", "img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"},
        {"n": "Curl de bíceps", "s": 3, "r": "12", "d": "45s", "img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"}
    ],
    "Pierna": [
        {"n": "Sentadilla Búlgara", "s": 3, "r": "12", "d": "90s", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
        {"n": "Peso Muerto Rumano", "s": 4, "r": "12", "d": "60s", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"},
        {"n": "Elevación de talones", "s": 4, "r": "20", "d": "30s", "img": "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=400"}
    ],
    "Salud": [
        {"n": "Puente Glúteo", "s": 3, "r": "15", "d": "45s", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
        {"n": "Gato-Camello (Movilidad)", "s": 3, "r": "10", "d": "30s", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
        {"n": "Plancha sobre rodillas", "s": 3, "r": "30s", "d": "45s", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"}
    ]
}

# Lógica de distribución: Cada día una rutina distinta
for d_idx in range(1, dias + 1):
    with st.expander(f"📅 DÍA {d_idx} - Plan Específico", expanded=(d_idx==1)):
        # Si hay lesiones, la rutina siempre es de Salud. Si no, alterna por día.
        if len(salud) > 0:
            categoria = "Salud"
        elif d_idx % 3 == 1: 
            categoria = "Empuje"
        elif d_idx % 3 == 2: 
            categoria = "Tracción"
        else: 
            categoria = "Pierna"
        
        for ej in db_ejercicios[categoria]:
            c1, c2 = st.columns([1, 2])
            c1.image(ej["img"], use_container_width=True)
            c2.subheader(ej["n"])
            c2.write(f"**Series:** {ej['s']} | **Reps:** {ej['r']} | **Descanso:** {ej['d']}")
            st.write("---")

# --- SECCIÓN 5: REGISTRO Y TABLA (LOG) ---
st.divider()
st.header("📊 Registro de Carga Progresiva")

if 'session_log' not in st.session_state:
    st.session_state.session_log = []

if st.button("🚀 Registrar Entrenamiento Completado"):
    nueva_entrada = {
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Alias": alias,
        "Meta": objetivo,
        "Sesión": f"Día {len(st.session_state.session_log) + 1}",
        "Estatus": "Completado"
    }
    st.session_state.session_log.append(nueva_entrada)
    st.success("¡Datos guardados!")

# Visualización de Tabla y Descarga (Línea 90 corregida)
if st.session_state.session_log:
    df_progresion = pd.DataFrame(st.session_state.session_log)
    st.subheader("📋 Tabla de Progreso en Pantalla")
    st.table(df_progresion) 
    
    # Generación de CSV sin errores de cierre
    csv = df_progresion.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Avance para Asesoría Gemini",
        data=csv,
        file_name=f"progreso_{alias}.csv",
        mime="text/csv"
    )

st.warning("⚠️ Nota: Sube este archivo al chat cada 30 días para que yo (Gemini) analice tu progreso.")
