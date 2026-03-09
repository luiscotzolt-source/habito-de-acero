import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuración inicial
st.set_page_config(page_title="Hábito de Acero", page_icon="🛡️")

# --- FRASES MOTIVACIONALES ---
frases = [
    "La disciplina es el puente entre las metas y los logros.",
    "No te detengas cuando estés cansado, detente cuando hayas terminado.",
    "La pereza es el enemigo, la constancia es tu armadura.",
    "Ingeniería humana: Construyendo una versión más fuerte cada día."
]

st.title("🛡️ Hábito de Acero: Ingeniería Corporal")
st.info(random.choice(frases))

# --- FORMULARIO DE PERFIL ---
with st.expander("⚙️ Configura tu Perfil de Salud", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        genero = st.radio("Género", ["Hombre", "Mujer"])
        edad = st.number_input("Edad", 15, 90, 30)
    with col2:
        dias = st.slider("Días por semana", 1, 7, 3)
        tiempo = st.slider("Minutos por sesión", 15, 120, 45)

    st.write("**Condiciones de Salud:**")
    c1, c2, c3, c4 = st.columns(4)
    diabetes = c1.checkbox("Diabetes")
    hipertenso = c2.checkbox("Hipertenso")
    cirugias = c3.checkbox("Cirugías")
    fracturas = c4.checkbox("Fracturas")

    objetivo = st.selectbox("Objetivo", ["Bajar de peso", "Masa muscular", "Fuerza"])

# --- LÓGICA DE IA (GENERACIÓN DE RUTINA SEMANAL) ---
st.write("---")
if st.button("🚀 Generar Mi Plan Semanal Personalizado"):
    st.subheader(f"📅 Plan de {dias} días para {objetivo}")
    
    # 1. Definir la Estructura según días
    if dias <= 2:
        tipo_split = "Full Body (Cuerpo Completo)"
        ejercicios = ["Sentadilla", "Push ups", "Remo con mochila", "Plancha"]
    elif dias <= 4:
        tipo_split = "Torso / Pierna"
        ejercicios = ["Press Militar", "Peso Muerto", "Dominadas", "Zancadas"]
    else:
        tipo_split = "Push / Pull / Leg (Avanzado)"
        ejercicios = ["Banca", "Remo c/mancuerna", "Sentadilla Búlgara", "Fondos"]

    # 2. Ajustar por Salud
    if diabetes or hipertenso:
        ejercicios = [e + " (Ritmo moderado)" for e in ejercicios]
        st.warning("⚠️ Intensidad controlada por salud cardiovascular.")

    # 3. Mostrar Rutina Semanal
    st.info(f"Estructura recomendada: **{tipo_split}**")
    
    # Creamos columnas para los ejercicios con sus ejemplos
    cols = st.columns(len(ejercicios))
    for i, ejer in enumerate(ejercicios):
        with cols[i]:
            st.write(f"**{ejer}**")
            # Enlaces de ejemplo (puedes cambiarlos por GIFs técnicos)
            st.image(f"https://picsum.photos/200/200?random={i}", caption="Técnica sugerida")
            st.write("3 series x 12 reps")

    st.success(f"Ingeniero, tu plan está diseñado para completarse en sesiones de {tiempo} minutos.")

# --- GUARDADO AUTOMÁTICO Y DESCARGA ---
st.write("---")
st.subheader("📈 Registro de Progreso")

# Crear DataFrame vacío si no hay datos
if 'log' not in st.session_state:
    st.session_state.log = pd.DataFrame(columns=['Fecha', 'Ejercicio', 'Completado'])

if st.button("✅ Registrar Sesión de Hoy"):
    nueva_fila = {'Fecha': datetime.now().strftime("%Y-%m-%d"), 'Ejercicio': "Sesión Completada", 'Completado': 'Sí'}
    st.session_state.log = pd.concat([st.session_state.log, pd.DataFrame([nueva_fila])], ignore_index=True)
    st.success("¡Progreso guardado automáticamente!")

# Botón para descargar al móvil
csv = st.session_state.log.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Descargar mi historial al móvil",
    data=csv,
    file_name='mi_progreso_habito_acero.csv',
    mime='text/csv',
)

st.sidebar.text("Sistema de Ingeniería Humana | 2026")
