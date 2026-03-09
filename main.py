import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Tu Coach con IA", page_icon="🏋️‍♂️", layout="wide")

# --- ESTILOS Y TÍTULO ---
st.title("🏋️‍♂️ Tu Coach con IA: Ingeniería de Cuerpo Completo")
st.write("---")

# --- 1. EVALUACIÓN DE CAPACIDADES Y DOLORES ---
with st.sidebar:
    st.header("📊 Perfil del Usuario")
    objetivo = st.selectbox("Objetivo", ["Masa Muscular", "Fuerza", "Salud y Movilidad"])
    dias = st.slider("Días por semana", 1, 5, 3)
    
    st.subheader("⚠️ Limitaciones Articulares")
    lumbalgia = st.checkbox("Lumbalgia")
    rodillas = st.checkbox("Dolor en Rodillas")
    hombros = st.checkbox("Dolor en Hombros")
    codos = st.checkbox("Dolor en Codos")

# --- 2. MOTOR DE CONSULTORÍA (CONSEJOS DE IA) ---
st.header("💬 Consulta al Coach IA")
pregunta = st.text_input("Hazle una pregunta a tu coach (ej: ¿Qué comer antes de entrenar?):")
if pregunta:
    if "comer" in pregunta.lower() or "dieta" in pregunta.lower():
        st.info("💡 **IA responde:** Prioriza carbohidratos complejos 1 hora antes y proteína después. Evita grasas pesadas antes del esfuerzo.")
    elif "dolor" in pregunta.lower():
        st.warning("💡 **IA responde:** Si el dolor es punzante, detente. Trabaja en rangos de movimiento donde no haya molestia.")
    else:
        st.success("💡 **IA responde:** La clave es la constancia. ¡Sigue adelante con tu plan de hoy!")

# --- 3. GENERACIÓN DE RUTINA COMPLETA ---
st.header(f"📅 Tu Plan Maestro de Entrenamiento")

if st.button("🔨 Construir Rutina Detallada"):
    # Definición de bloques por día
    bloques = ["Calentamiento Dinámico", "Bloque de Fuerza/Hipertrofia", "Core y Estabilidad", "Vuelta a la Calma"]
    
    for i in range(1, dias + 1):
        with st.expander(f"🔵 DÍA {i}: Sesión Completa", expanded=True):
            # Lógica de distribución muscular simple
            enfoque = "Empuje (Pecho/Tríceps)" if i % 2 != 0 else "Tracción (Espalda/Bíceps)"
            if i == 3: enfoque = "Pierna y Glúteo"

            st.subheader(f"Enfoque: {enfoque}")
            
            # --- TABLA DE EJERCICIOS DETALLADA ---
            col_tabla, col_imgs = st.columns([2, 1])
            
            with col_tabla:
                # Filtrado de ejercicios por limitaciones
                ejercicios_data = []
                
                # Ejemplo de ejercicios adaptativos
                if "Pecho" in enfoque:
                    ej = "Flexiones (Pushups)" if not hombros else "Press de banca con agarre cerrado (protege hombro)"
                    ejercicios_data.append([ej, "4 series", "12 reps", "60 seg"])
                    ejercicios_data.append(["Aperturas con mancuernas", "3 series", "15 reps", "
