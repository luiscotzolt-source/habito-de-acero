import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuración profesional
st.set_page_config(page_title="Tu Coach con IA", page_icon="🏋️‍♂️", layout="wide")

st.title("🏋️‍♂️ Tu Coach con IA: Entrenamiento Adaptado")
st.markdown("### *Diseño de rutinas basado en tus limitaciones y objetivos*")
st.write("---")

# --- 1. CUESTIONARIO DE LIMITACIONES Y CAPACIDADES ---
st.header("📋 Evaluación de Perfil y Salud")
st.info("Para crear una rutina que te funcione, primero debemos identificar tus límites físicos.")

with st.form("cuestionario_coach"):
    col1, col2 = st.columns(2)
    
    with col1:
        genero = st.radio("Género", ["Hombre", "Mujer"])
        edad = st.number_input("Edad", 15, 100, 30)
        objetivo = st.selectbox("¿Qué buscas lograr?", 
                                ["Bajar de peso", "Ganar masa muscular", "Fuerza funcional", "Rehabilitación"])
    
    with col2:
        dias = st.slider("Días disponibles por semana", 1, 7, 3)
        tiempo = st.slider("Minutos disponibles por sesión", 15, 120, 45)

    st.subheader("⚠️ Limitaciones y Condiciones Crónicas")
    st.write("Selecciona cualquier condición que debamos considerar:")
    c1, c2, c3, c4 = st.columns(4)
    diabetes = c1.checkbox("Diabetes")
    hipertenso = c2.checkbox("Hipertensión")
    cirugias = c3.checkbox("Cirugías Recientes")
    fracturas = c4.checkbox("Fracturas/Lesiones Óseas")

    enviar = st.form_submit_button("🔨 Construir mi Rutina a Medida")

# --- 2. ALGORITMO DE SELECCIÓN INTELIGENTE ---
if enviar:
    st.write("---")
    st.header("🎯 Tu Plan Maestro Personalizado")

    # Lógica de prioridad: Seguridad ante todo
    if cirugias or fracturas or objetivo == "Rehabilitación":
        categoria = "REHABILITACIÓN Y REESTRUCTURACIÓN"
        ejercicios = [
            "Movilidad articular de bajo impacto (10 min)",
            "Isométricos (mantener tensión sin mover la articulación)",
            "Estiramientos estáticos asistidos"
        ]
        consejo = "El objetivo es recuperar rango de movimiento. No debe existir dolor agudo."
        img_url = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500"
    
    elif hipertenso or diabetes:
        categoria = "CONTROL METABÓLICO Y CARDIOVASCULAR"
        ejercicios = [
            "Caminata a paso ligero o Elíptica (Nivel 3-4)",
            "Ejercicios de fuerza con autocarga (sentarse y pararse de silla)",
            "Movilidad de tren superior sentado"
        ]
        consejo = "Evite esfuerzos explosivos. Mantenga una hidratación constante."
        img_url = "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=500"

    elif objetivo == "Ganar masa muscular":
        categoria = "HIPERTROFIA Y POTENCIA"
        ejercicios = [
            "Sentadillas profundas (4 series x 10-12 reps)",
            "Flexiones de pecho (Push-ups) al fallo técnico",
            "Remo invertido o con bandas elásticas"
        ]
        consejo = "Enfócate en la fase negativa (bajar lento) para romper más fibras musculares."
        img_url = "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500"

    else: # Bajar de peso / Fuerza funcional
        categoria = "RESISTENCIA Y PÉRDIDA DE GRASA"
        ejercicios = [
            "Circuito: 30 seg Burpees / 30 seg Plancha / 30 seg Descanso",
            "Zancadas alternas (Lunges)",
            "Escaladores (Mountain Climbers)"
        ]
        consejo = "Mantén la frecuencia cardíaca elevada con descansos cortos."
        img_url = "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=500"

    # Presentación de la Rutina
    col_img, col_txt = st.columns([1, 1.2])
    with col_img:
        st.image(img_url, caption=f"Guía para: {categoria}")
    with col_txt:
        st.success(f"**Sistema Asignado:** {categoria}")
        st.write("**Tus ejercicios específicos:**")
        for ej in ejercicios:
            st.write(f"- {ej}")
        st.info(f"**💡 Consejo de tu Coach:** {consejo}")

    # --- 3. PERSISTENCIA DE DATOS ---
    st.divider()
    st.subheader("📊 Tu Bitácora de Entrenamiento")
    
    if 'historial' not in st.session_state:
        st.session_state.historial = pd.DataFrame(columns=['Fecha', 'Rutina', 'Estado'])

    if st.button("✅ Marcar entrenamiento como completado"):
        nueva_entrada = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), categoria, "LOGRADO"]], 
                                     columns=['Fecha', 'Rutina', 'Estado'])
        st.session_state.historial = pd.concat([st.session_state.historial, nueva_entrada], ignore_index=True)
        st.balloons()
        st.toast("¡Progreso registrado en tu historial local!")

    st.table(st.session_state.historial)

    # Botón de descarga para el móvil
    csv = st.session_state.historial.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar reporte a mi móvil", csv, "mi_progreso_coach.csv", "text/csv")

st.sidebar.write("Tu Coach con IA | 2026")
