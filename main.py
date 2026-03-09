import streamlit as st
import pandas as pd
from datetime import datetime
import random

# 1. Configuración de Página
st.set_page_config(page_title="Hábito de Acero - IA Fitness", page_icon="🛡️")

# 2. Base de Datos de Frases Motivacionales
frases = [
    "La disciplina es el puente entre las metas y los logros.",
    "La pereza es el enemigo, la constancia es tu armadura.",
    "No te detengas hasta estar orgulloso.",
    "Ingeniería Humana: Construyendo tu mejor versión."
]

st.title("🛡️ Hábito de Acero: Asistente IA")
st.markdown(f"**Mensaje del día:** *{random.choice(frases)}*")

# 3. Formulario de Perfil (Algoritmo de Diagnóstico)
with st.sidebar:
    st.header("📋 Perfil de Usuario")
    genero = st.selectbox("Género", ["Hombre", "Mujer"])
    edad = st.number_input("Edad", 15, 90, 30)
    
    st.subheader("🏥 Historial de Salud")
    diabetes = st.checkbox("Diabetes")
    hipertenso = st.checkbox("Hipertensión")
    cirugias = st.checkbox("Cirugías Recientes")
    fracturas = st.checkbox("Fracturas Previas")
    
    st.subheader("🎯 Objetivos y Tiempo")
    meta = st.radio("Meta principal", ["Bajar de peso", "Masa muscular", "Fuerza"])
    dias = st.slider("Días a la semana", 1, 7, 3)
    tiempo = st.slider("Minutos por sesión", 15, 120, 45)

# 4. Motor de IA: Generador de Rutinas
st.header("🏋️ Tu Rutina Personalizada")

def generar_rutina():
    # Lógica de seguridad
    if cirugias or fracturas:
        tipo = "Movilidad y Recuperación"
        ejercicio = "Estiramientos asistidos y caminata lenta"
        img = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500"
    elif hipertenso or diabetes:
        tipo = "Cardio de Bajo Impacto"
        ejercicio = "Caminata a ritmo constante o Elíptica"
        img = "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=500"
    elif meta == "Masa muscular":
        tipo = "Hipertrofia Adaptada"
        ejercicio = "Sentadillas y Flexiones (controladas)"
        img = "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500"
    else:
        tipo = "Circuito de Fuerza"
        ejercicio = "Burpees suaves y Planchas"
        img = "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=500"
    
    return tipo, ejercicio, img

tipo, ejer, imagen = generar_rutina()

col1, col2 = st.columns(2)
with col1:
    st.success(f"**Tipo:** {tipo}")
    st.write(f"**Ejercicio Principal:** {ejer}")
    st.write(f"**Duración:** {tiempo} minutos")
with col2:
    st.image(imagen, caption="Ejemplo técnico del ejercicio")

# 5. Registro Automático y Descarga CSV
st.divider()
st.subheader("📈 Registro de Avance")

if 'datos' not in st.session_state:
    st.session_state.datos = pd.DataFrame(columns=['Fecha', 'Ejercicio', 'Meta'])

if st.button("✅ Registrar entrenamiento de hoy"):
    nuevo = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), ejer, meta]], 
                         columns=['Fecha', 'Ejercicio', 'Meta'])
    st.session_state.datos = pd.concat([st.session_state.datos, nuevo], ignore_index=True)
    st.toast("¡Progreso guardado!")

st.dataframe(st.session_state.datos)

# Descarga local para el móvil
csv = st.session_state.datos.to_csv(index=False).encode('utf-8')
st.download_button("📥 Descargar mi historial (CSV)", csv, "mi_progreso.csv", "text/csv")
