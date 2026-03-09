import streamlit as st
import pandas as pd
from datetime import datetime
import random

# --- CONFIGURACIÓN ESTÉTICA PRO ---
st.set_page_config(
    page_title="Hábito de Acero | IA Fitness",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS para mejorar la apariencia de las tarjetas y botones
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white; }
    .stDownloadButton>button { width: 100%; border-radius: 10px; background-color: #28a745; color: white; }
    .exercise-card { padding: 20px; border-radius: 15px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_index=True)

# --- SIDEBAR: ASISTENTE IA Y DONACIONES ---
with st.sidebar:
    st.title("🛡️ Panel de Control")
    st.markdown("---")
    
    # Chat de Asistencia IA
    st.subheader("💬 Asistente IA")
    user_input = st.text_input("Ingeniero, ¿en qué puedo ayudarte?", placeholder="Ej: Me duelen las rodillas...")
    if user_input:
        with st.spinner('Analizando biometría...'):
            # Simulación de respuesta lógica de IA
            st.info(f"Asistente: Entendido. Para tu duda sobre '{user_input}', te sugiero priorizar la movilidad articular. ¡La disciplina supera al talento!")
    
    st.markdown("---")
    
    # Botón de Donación Pro
    st.subheader("☕ Apoya el Proyecto")
    st.markdown("Si este sistema de ingeniería humana te es útil, considera una donación para mantener los servidores.")
    # Puedes cambiar este link por tu PayPal o Ko-fi
    st.markdown("[![Donar](https://img.shields.io/badge/Donar-PayPal-blue.svg?style=for-the-badge&logo=paypal)](https://www.paypal.me/tucuenta)")

# --- CUERPO PRINCIPAL: FORMULARIO DE DIAGNÓSTICO ---
st.title("🏋️‍♂️ Hábito de Acero: Ingeniería Corporal")
st.write("Configura tu perfil para que nuestra IA diseñe tu arquitectura física.")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        genero = st.selectbox("Género", ["Hombre", "Mujer", "Otro"])
        edad = st.number_input("Edad", 15, 90, 30)
    with col2:
        objetivo = st.selectbox("Objetivo Principal", ["Bajar de peso", "Masa muscular", "Fuerza Máxima"])
        dias = st.slider("Días de entrenamiento", 1, 7, 3)
    with col3:
        tiempo = st.select_slider("Tiempo por sesión", options=[15, 30, 45, 60, 90], value=45)

    st.markdown("**Historial Médico y Limitaciones:**")
    m1, m2, m3, m4 = st.columns(4)
    diabetes = m1.checkbox("Diabetes")
    hipertenso = m2.checkbox("Hipertensión")
    cirugias = m3.checkbox("Cirugías")
    fracturas = m4.checkbox("Fracturas")

# --- GENERACIÓN DINÁMICA DE RUTINA ---
if st.button("🚀 GENERAR PLAN MAESTRO"):
    st.markdown("---")
    st.header(f"📅 Tu Rutina Personalizada: {objetivo}")
    
    # Diccionario técnico de ejercicios (URLs de ejemplo de técnica real)
    rutina_data = {
        "Fuerza Máxima": [
            {"n": "Sentadilla Goblet", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKEPO1bjPaOtGSc/giphy.gif"},
            {"n": "Flexiones de Arquero", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFs_2dpZl9ieV9pZCZjdD1n/uS071hlk6BJZjR5clS/giphy.gif"}
        ],
        "Masa muscular": [
            {"n": "Zancadas Dinámicas", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l0HlSxdtO64E3wN4Q/giphy.gif"},
            {"n": "Dominadas o Remo", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxx66Z1f600/giphy.gif"}
        ],
        "Bajar de peso": [
            {"n": "Burpees Adaptados", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKpGv6o2G9Z5m5W/giphy.gif"},
            {"n": "Escaladores", "img": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN6bmJ3bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif"}
        ]
    }

    # Selección de lista según objetivo
    lista_ejercicios = rutina_data.get(objetivo, rutina_data["Bajar de peso"])
    
    # Mostrar tarjetas de ejercicios
    cols = st.columns(len(lista_ejercicios))
    for i, ejer in enumerate(lista_ejercicios):
        with cols[i]:
            st.markdown(f"### {ejer['n']}")
            st.image(ejer['img'], use_container_width=True)
            st.write(f"**Series:** 4 | **Reps:** 12")
            if hipertenso or diabetes:
                st.caption("⚠️ Nota: Mantén un ritmo respiratorio fluido.")

# --- SECCIÓN DE PROGRESO Y DESCARGA ---
st.markdown("---")
col_reg, col_down = st.columns(2)

with col_reg:
    if st.button("✅ Registrar Entrenamiento de Hoy"):
        if 'history' not in st.session_state:
            st.session_state.history = []
        fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.session_state.history.append({"Fecha": fecha_hoy, "Objetivo": objetivo})
        st.success(f"Entrenamiento del {fecha_hoy} registrado con éxito.")

with col_down:
    if 'history' in st.session_state and st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar Reporte de Progreso (CSV)",
            data=csv,
            file_name=f'progreso_acero_{datetime.now().strftime("%Y")}.csv',
            mime='text/csv'
        )

st.markdown("---")
st.caption("Hábito de Acero v2.0 | Sistema de Ingeniería Humana 2026")
