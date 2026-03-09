import streamlit as st
import pandas as pd
from datetime import datetime
import random

# 1. Configuración de la Aplicación
st.set_page_config(page_title="Hábito de Acero: IA Fitness", page_icon="🛡️", layout="wide")

# 2. Motor de Motivación
frases = [
    "La disciplina es el puente entre las metas y los logros.",
    "La pereza es el enemigo, la constancia es tu armadura.",
    "Ingeniería humana: Construyendo una versión más fuerte.",
    "No te detengas hasta estar orgulloso."
]

st.title("🛡️ Hábito de Acero: Asistente de Entrenamiento IA")
st.info(f"💡 {random.choice(frases)}")

# 3. Formulario de Diagnóstico (Algoritmo de Salud)
with st.expander("📝 Configura tu Perfil y Objetivos", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        genero = st.selectbox("Género", ["Hombre", "Mujer"])
        edad = st.number_input("Edad", 15, 95, 30)
    with col2:
        meta = st.radio("Objetivo", ["Bajar de peso", "Masa muscular", "Fuerza"])
        dias_sem = st.slider("Días a la semana", 1, 7, 3)
    with col3:
        tiempo_min = st.slider("Minutos por sesión", 15, 120, 45)

    st.write("**Condiciones Médicas / Lesiones:**")
    c1, c2, c3, c4 = st.columns(4)
    diabetes = c1.checkbox("Diabetes")
    hipertension = c2.checkbox("Hipertensión")
    cirugia = c3.checkbox("Cirugías")
    fractura = c4.checkbox("Fracturas")

# 4. Lógica de IA: Prescripción de Ejercicios
st.divider()
st.header("🏋️ Tu Rutina Personalizada")

def generar_ejercicios():
    # Diccionario de recomendaciones basadas en el perfil
    if cirugia or fractura:
        return "Movilidad Suave", "Estiramientos asistidos y rotaciones", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600"
    elif hipertension or diabetes:
        return "Cardio Moderado", "Caminata rápida o bicicleta estática", "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=600"
    elif meta == "Masa muscular":
        return "Hipertrofia", "Sentadillas, Flexiones y Dominadas", "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=600"
    else:
        return "Resistencia", "Burpees, Planchas y Saltos", "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=600"

tipo, nombre_ej, url_img = generar_ejercicios()

col_a, col_b = st.columns([1, 1])
with col_a:
    st.success(f"### Enfoque: {tipo}")
    st.write(f"**Ejercicio sugerido:** {nombre_ej}")
    st.write(f"**Plan:** {dias_sem} días a la semana durante {tiempo_min} min.")
with col_b:
    st.image(url_img, caption="Ejemplo técnico del ejercicio")

# 5. Registro de Progreso y Descarga
st.divider()
st.subheader("📈 Mi Registro de Avance")

if 'historial' not in st.session_state:
    st.session_state.historial = pd.DataFrame(columns=['Fecha', 'Ejercicio', 'Meta'])

if st.button("✅ Registrar sesión completada"):
    nuevo_dato = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), nombre_ej, meta]], 
                              columns=['Fecha', 'Ejercicio', 'Meta'])
    st.session_state.historial = pd.concat([st.session_state.historial, nuevo_dato], ignore_index=True)
    st.toast("¡Entrenamiento registrado!")

st.table(st.session_state.historial)

# Botón de descarga para el móvil
csv_data = st.session_state.historial.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Descargar historial al móvil (CSV)",
    data=csv_data,
    file_name='progreso_habito_acero.csv',
    mime='text/csv'
)

st.sidebar.caption("Ingeniería Humana | 2026")
