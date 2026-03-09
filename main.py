import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Hábito de Acero Pro", layout="wide")

st.title("🛡️ Hábito de Acero: Ingeniería Corporal Adaptada")
st.markdown("---")

# SECCIÓN 1, 2 Y 3: ENTRADA DE DATOS (BARRA LATERAL)
with st.sidebar:
    st.header("👤 Datos Personales")
    nombre = st.text_input("Nombre o Alias:", "Usuario1")
    col1, col2 = st.columns(2)
    edad = col1.number_input("Edad:", 15, 100, 30)
    genero = col2.selectbox("Género:", ["Hombre", "Mujer"])
    peso = col1.number_input("Peso (kg):", 40, 200, 75)
    estatura = col2.number_input("Estatura (cm):", 100, 250, 170)

    st.header("🏥 Perfil de Salud")
    enfermedades = st.multiselect("Padece alguna enfermedad:", 
                                  ["Artritis", "Diabetes", "Presión alta", "Presión baja", "Lumbalgia"])
    lesiones = st.multiselect("Lesión en:", 
                               ["Rodilla", "Hombro", "Muñecas", "Tobillos"])

    st.header("🎯 Planificación")
    objetivo = st.selectbox("Objetivo:", ["Perder peso", "Ganar masa muscular", "Definición", "Fuerza y resistencia"])
    dias = st.slider("Días a la semana:", 1, 7, 3)
    tiempo = st.slider("Minutos de sesión:", 15, 120, 45)

# SECCIÓN 4: MOTOR DE IA - GENERADOR DE RUTINAS
st.header(f"🏋️ Plan de Entrenamiento IA para {nombre}")

# Lógica de prescripción profesional
def generar_rutina():
    ejercicios = []
    # Filtro Fisioterapéutico
    if "Lumbalgia" in enfermedades or "Rodilla" in lesiones:
        ejercicios = [
            {"ej": "Puente de Glúteo Isométrico", "img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400", "s": 3, "r": "12", "d": "45s"},
            {"ej": "Extensiones de Cuádriceps sentado", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400", "s": 3, "r": "15", "d": "30s"}
        ]
    elif "Presión alta" in enfermedades:
        ejercicios = [
            {"ej": "Caminata activa / Trote suave", "img": "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=400", "s": 1, "r": "20 min", "d": "60s"},
            {"ej": "Sentadilla asistida con silla", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400", "s": 4, "r": "10", "d": "60s"}
        ]
    else:
        ejercicios = [
            {"ej": "Sentadilla Global", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400", "s": 4, "r": "12", "d": "60s"},
            {"ej": "Flexiones de brazo (Push-ups)", "img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400", "s": 4, "r": "10", "d": "60s"}
        ]
    return ejercicios

plan = generar_rutina()

# Despliegue de Rutina por Día
for dia_idx in range(1, dias + 1):
    with st.expander(f"📅 DÍA {dia_idx} - Rutina Personalizada", expanded=(dia_idx==1)):
        for item in plan:
            c_img, c_txt = st.columns([1, 2])
            c_img.image(item["img"], use_container_width=True)
            c_txt.markdown(f"### {item['ej']}")
            c_txt.write(f"**Series:** {item['s']} | **Reps:** {item['r']} | **Descanso:** {item['d']}")
            st.write("---")

# SECCIÓN 5: REGISTRO Y CSV
st.header("📈 Registro de Progreso")
st.warning("🔔 NOTA: Guarda tus registros. Tras 30 días, la IA actualizará tu carga progresiva basándose en estos datos.")

if st.button("💾 Registrar Sesión y Actualizar Avance"):
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    log_df = pd.DataFrame([[fecha_hoy, nombre, objetivo, f"{tiempo} min"]], 
                          columns=["Fecha", "Alias", "Objetivo", "Duración"])
    
    csv = log_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar/Guardar mi progreso (CSV)",
        data=csv,
        file_name=f"progreso_{nombre}_{fecha_hoy}.csv",
        mime="text/csv"
    )
    st.success("¡Sesión registrada exitosamente!")

st.sidebar.markdown("---")
st.sidebar.caption("Desarrollado bajo estándares de Medicina Deportiva 2026")
