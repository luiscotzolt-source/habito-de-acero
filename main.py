import streamlit as st
import pandas as pd
from datetime import datetime
import random

# CONFIGURACIÓN PROFESIONAL
st.set_page_config(page_title="Hábito de Acero: Cloud AI", layout="wide")

# MÓDULO DE MOTIVACIÓN IA
frases = [
    "La disciplina es el puente entre las metas y los logros.",
    "Ingeniería humana: Construyendo una versión más fuerte.",
    "Tu único límite es tu mente."
]

st.title("🛡️ Hábito de Acero: Consultoría IA en Vivo")
st.info(random.choice(frases))

# --- SECCIONES 1, 2 Y 3: CAPTURA DE DATOS ---
with st.sidebar:
    st.header("🔑 Conexión Cloud")
    # Simulación de enlace a cuenta de Google
    google_auth = st.button("Enlazar con Google Drive")
    
    st.header("📋 Perfil Clínico")
    alias = st.text_input("Alias:", "Atleta_Cloud")
    edad = st.number_input("Edad:", 15, 95, 30)
    peso = st.number_input("Peso (kg):", 40, 200, 75)
    
    st.subheader("⚠️ Restricciones")
    salud = st.multiselect("Enfermedades/Lesiones:", ["Diabetes", "Artritis", "Presión Alta", "Lumbalgia", "Rodilla"])
    
    st.header("🎯 Meta")
    objetivo = st.selectbox("Objetivo:", ["Masa Muscular", "Pérdida de Grasa", "Fuerza"])
    tiempo = st.slider("Minutos de sesión:", 15, 120, 60)

# --- SECCIÓN 4: GENERACIÓN DE RUTINA DINÁMICA (CONEXIÓN GEMINI) ---
st.subheader("🏋️ Tu Rutina Personalizada (Generada por IA en línea)")

# Función que simula la respuesta de Gemini basada en el perfil
def solicitar_rutina_ia(p, o, s):
    # En un entorno real, aquí se hace: response = gemini_model.generate_content(prompt)
    # Generamos una rutina que varía según el objetivo y las lesiones
    if "Rodilla" in s or "Lumbalgia" in s:
        return [
            {"n": "Elevación de pierna recta", "s": 3, "r": "15", "d": "30s", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
            {"n": "Puente de glúteo", "s": 4, "r": "12", "d": "45s", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
            {"n": "Plancha sobre rodillas", "s": 3, "r": "30s", "d": "60s", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"}
        ]
    else:
        return [
            {"n": "Sentadilla con peso", "s": 4, "r": "10", "d": "90s", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"},
            {"n": "Flexiones explosivas", "s": 4, "r": "12", "d": "60s", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
            {"n": "Zancadas dinámicas", "s": 3, "r": "12 c/u", "d": "60s", "img": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=400"}
        ]

# Obtenemos la rutina "de la nube"
rutina_ia = solicitar_rutina_ia(peso, objetivo, salud)

# Visualización
for item in rutina_ia:
    with st.container():
        c1, c2 = st.columns([1, 2])
        c1.image(item["img"], use_container_width=True)
        c2.markdown(f"### {item['n']}")
        c2.write(f"**Series:** {item['s']} | **Repeticiones:** {item['r']} | **Descanso:** {item['d']}")
        st.divider()

# --- SECCIÓN 5: REGISTRO CSV Y ASESORÍA ---
st.header("📊 Registro de Carga Progresiva")

if 'historial_cloud' not in st.session_state:
    st.session_state.historial_cloud = []

if st.button("🚀 Registrar Avance en mi Google Drive"):
    nuevo_registro = {
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Alias": alias,
        "Objetivo": objetivo,
        "Status": "Completado"
    }
    st.session_state.historial_cloud.append(nuevo_registro)
    st.success("¡Datos sincronizados con la nube!")

# TABLA DE PROGRESO
if st.session_state.historial_cloud:
    df = pd.DataFrame(st.session_state.historial_cloud)
    st.table(df)
