import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Hábito de Acero - Rutinas", page_icon="🏋️‍♂️")

st.title("🏋️‍♂️ Hábito de Acero: Entrenamiento")
st.subheader("Registro de Ingeniería Física")

# 1. Selector de Rutina
dia = st.selectbox("Selecciona el día de hoy:", ["Lunes: Empuje", "Martes: Tracción", "Miércoles: Pierna", "Jueves: Cardio/Core", "Viernes: Full Body"])

# 2. Entrada de Datos de Ejercicio
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    ejercicio = st.text_input("Ejercicio", placeholder="Ej: Press Banca")
with col2:
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5)
with col3:
    reps = st.number_input("Repeticiones", min_value=0, step=1)

if st.button("Registrar Serie"):
    st.success(f"Serie de {ejercicio} registrada: {peso}kg x {reps} reps")
    # Aquí podrías conectar una base de datos más adelante

# 3. Visualización de Avance (Ejemplo de tabla)
st.write("---")
st.subheader("📈 Tu Progreso Reciente")
# Datos de ejemplo para que veas cómo se vería el avance
data = {
    'Fecha': [datetime.now().strftime("%Y-%m-%d")],
    'Ejercicio': [ejercicio if ejercicio else "Esperando datos..."],
    'Carga Total (kg)': [peso * reps]
}
df = pd.DataFrame(data)
st.table(df)

st.sidebar.write("Sistema de Ingeniería Humana 2026")
