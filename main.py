import streamlit as st
import pandas as pd
from datetime import datetime
import random

# CONFIGURACIÓN PRO
st.set_page_config(page_title="Hábito de Acero: Ingeniería Humana", layout="wide")
st.title("🛡️ Hábito de Acero: Sistema de Entrenamiento Adaptado")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIOS (BARRA LATERAL) ---
with st.sidebar:
    st.header("📋 SECCIÓN 1: Perfil Bio")
    alias = st.text_input("Nombre o Alias:", "Usuario1")
    col_a, col_b = st.columns(2)
    edad = col_a.number_input("Edad:", 15, 95, 30)
    genero = col_b.selectbox("Género:", ["Hombre", "Mujer"])
    peso = col_a.number_input("Peso (kg):", 40.0, 200.0, 75.0)
    estatura = col_b.number_input("Estatura (cm):", 100, 250, 170)

    st.header("🏥 SECCIÓN 2: Salud y Lesiones")
    enfermedades = st.multiselect("Enfermedades:", ["Artritis", "Diabetes", "Presión alta", "Presión baja", "Lumbalgia"])
    lesiones = st.multiselect("Lesiones en:", ["Rodilla", "Hombro", "Muñecas", "Tobillos"])

    st.header("🎯 SECCIÓN 3: Objetivos")
    meta = st.selectbox("Meta:", ["Perder peso", "Ganar masa muscular", "Definición", "Fuerza y resistencia"])
    dias_entreno = st.slider("Días a la semana:", 1, 7, 3)
    tiempo_entreno = st.slider("Minutos por sesión:", 15, 120, 45)

# --- SECCIÓN 4: RUTINAS GENERADAS POR IA POR DÍA ---
st.header(f"🏋️ Plan Maestro para {alias}")

def motor_ia_rutinas():
    plan = {}
    # Lógica de selección de ejercicios por salud
    for dia in range(1, dias_entreno + 1):
        ejercicios_dia = []
        if "Lumbalgia" in enfermedades or "Rodilla" in lesiones:
            # Rutina de Fisioterapia
            ejercicios_dia = [
                {"n": "Puente de Glúteo", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400", "s": 3, "r": 12, "d": "45s"},
                {"n": "Gato-Camello", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400", "s": 3, "r": 10, "d": "30s"}
            ]
        elif meta == "Ganar masa muscular":
            # Rutina de Hipertrofia
            ejercicios_dia = [
                {"n": "Sentadilla Goblet", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400", "s": 4, "r": 10, "d": "90s"},
                {"n": "Flexiones Diamante", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400", "s": 3, "r": 12, "d": "60s"}
            ]
        else:
            # Rutina General
            ejercicios_dia = [
                {"n": "Burpees Suaves", "img": "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=400", "s": 3, "r": 15, "d": "60s"},
                {"n": "Plancha Abdominal", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400", "s": 3, "r": "45 seg", "d": "45s"}
            ]
        plan[f"Día {dia}"] = ejercicios_dia
    return plan

rutinas = motor_ia_rutinas()

for dia, lista in rutinas.items():
    with st.expander(f"📅 {dia} - Ver Rutina", expanded=(dia == "Día 1")):
        for ej in lista:
            c1, c2 = st.columns([1, 2])
            c1.image(ej["img"], use_container_width=True)
            c2.subheader(ej["n"])
            c2.write(f"**Series:** {ej['s']} | **Reps:** {ej['r']} | **Descanso:** {ej['d']}")
            st.write("---")

# --- SECCIÓN 5: REGISTRO CSV Y CARGA PROGRESIVA ---
st.divider()
st.header("📊 SECCIÓN 5: Registro de Progreso")
st.warning("Deberás guardar tus registros para actualizar tus rutinas tras 30 días y mantener la carga progresiva.")

# Botón de Guardado
if st.button("💾 Finalizar y Registrar Sesión"):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    # Crear estructura del CSV
    registro = {
        "Fecha": [fecha_actual],
        "Usuario": [alias],
        "Meta": [meta],
        "Estatus": ["Completado"]
    }
    df_registro = pd.DataFrame(registro)
    
    # Conversión segura a CSV
    csv_final = df_registro.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 DESCARGAR REGISTRO AL MÓVIL",
        data=csv_final,
        file_name=f"progreso_{alias}_{fecha_actual}.csv",
        mime="text/csv"
    )
    st.success(f"¡Excelente trabajo, {alias}! Registro preparado para descarga.")

st.sidebar.markdown("---")
st.sidebar.caption("Ingeniería Humana | Medicina Deportiva 2026")
