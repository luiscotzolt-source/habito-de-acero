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

# --- LÓGICA DE IA (GENERACIÓN DE RUTINA) ---
st.write("---")
if st.button("🚀 Generar Mi Rutina Personalizada"):
    st.subheader("📋 Tu Plan de Entrenamiento IA")
    
    # Ejemplo de lógica adaptativa
    if diabetes or hipertenso:
        st.warning("⚠️ Nota: Tu rutina se ha ajustado para intensidad moderada debido a tu perfil de salud.")
        ejer_nombre = "Caminata a ritmo constante o Elíptica"
        st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400", caption=f"Ejemplo: {ejer_nombre}")
    elif objetivo == "Masa muscular":
        ejer_nombre = "Sentadillas con peso o Flexiones de brazo"
        st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400", caption=f"Ejemplo: {ejer_nombre}")
    else:
        ejer_nombre = "Burpees o Saltos de cuerda"
        st.image("https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=400", caption=f"Ejemplo: {ejer_nombre}")

    st.write(f"**Rutina Sugerida:** Realiza 4 series de 12 repeticiones de {ejer_nombre}.")

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
