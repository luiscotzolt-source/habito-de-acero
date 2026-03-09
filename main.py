import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Hábito de Acero: Pro Trainer", layout="wide")
st.title("🛡️ Hábito de Acero: Ingeniería Corporal Profesional")

# --- SECCIONES 1, 2 Y 3: CUESTIONARIOS (BARRA LATERAL) ---
with st.sidebar:
    st.header("📋 PERFIL Y SALUD")
    alias = st.text_input("Nombre o Alias:", "Atleta1")
    edad = st.number_input("Edad:", 15, 95, 30)
    col_f = st.columns(2)
    peso = col_f[0].number_input("Peso (kg):", 40.0, 200.0, 75.0)
    estatura = col_f[1].number_input("Estatura (cm):", 100, 250, 170)

    enfermedades = st.multiselect("Enfermedades:", ["Artritis", "Diabetes", "Presión alta", "Presión baja", "Lumbalgia"])
    lesiones = st.multiselect("Lesiones en:", ["Rodilla", "Hombro", "Muñecas", "Tobillos"])

    st.header("🎯 ENTRENAMIENTO")
    meta = st.selectbox("Objetivo:", ["Perder peso", "Ganar masa muscular", "Definición", "Fuerza y resistencia"])
    dias_semana = st.slider("Días a la semana:", 1, 7, 3)
    tiempo_minutos = st.slider("Tiempo por sesión (min):", 15, 120, 60)

# --- SECCIÓN 4: MOTOR DE IA - RUTINAS DINÁMICAS ---
st.header(f"🏋️ Plan Maestro de Entrenamiento: {alias}")

def generar_bloque_ejercicios(dia_num):
    # Base de datos de ejercicios profesional
    # Si hay lesiones, filtramos ejercicios peligrosos
    es_dia_par = dia_num % 2 == 0
    
    # Lógica de especialización por salud
    tiene_limitantes = len(enfermedades) > 0 or len(lesiones) > 0

    if tiene_limitantes:
        # Rutina de Fisioterapia y Adaptación
        base = [
            {"Ej": "Movilidad Articular", "S": 3, "R": "15", "D": "30s", "Img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
            {"Ej": "Puente Glúteo", "S": 4, "R": "12", "D": "45s", "Img": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400"},
            {"Ej": "Plancha sobre rodillas", "S": 3, "R": "30s", "D": "60s", "Img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"},
            {"Ej": "Sentadilla con silla", "S": 3, "R": "10", "D": "60s", "Img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
            {"Ej": "Extensiones sentado", "S": 3, "R": "15", "D": "30s", "Img": "https://images.unsplash.com/photo-1591940746222-e8d2f730ee96?w=400"},
            {"Ej": "Caminata Estática", "S": 1, "R": "10 min", "D": "0s", "Img": "https://images.unsplash.com/photo-1594882645126-14020914d58d?w=400"}
        ]
    elif es_dia_par:
        # Rutina Tren Superior (Días 2, 4, 6)
        base = [
            {"Ej": "Flexiones de pecho", "S": 4, "R": "12", "D": "60s", "Img": "https://images.unsplash.com/photo-1598971639058-fab3c03af452?w=400"},
            {"Ej": "Remo con banda/mancuerna", "S": 4, "R": "15", "D": "60s", "Img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=400"},
            {"Ej": "Press Militar", "S": 3, "R": "12", "D": "60s", "Img": "https://images.unsplash.com/photo-1532029837206-aba2b762a638?w=400"},
            {"Ej": "Dips en banco", "S": 3, "R": "10", "D": "45s", "Img": "https://images.unsplash.com/photo-1581009146145-b5ef03a74e7f?w=400"},
            {"Ej": "Crol de hombros", "S": 3, "R": "15", "D": "30s", "Img": "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?w=400"},
            {"Ej": "Plancha High", "S": 4, "R": "45s", "D": "45s", "Img": "https://images.unsplash.com/photo-1566241134883-13eb2393a3cc?w=400"}
        ]
    else:
        # Rutina Tren Inferior / Full Body (Días 1, 3, 5)
        base = [
            {"Ej": "Sentadilla Goblet", "S": 4, "R": "10", "D": "90s", "Img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400"},
            {"Ej": "Zancadas / Lunges", "S": 3, "R": "12 c/u", "D": "60s", "Img": "https://images.unsplash.com/photo-1591741535018-d042766c62eb?w=400"},
            {"Ej": "Peso Muerto Rumano", "S": 4, "R": "12", "D": "60s", "Img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"},
            {"Ej": "Elevación de Talones", "S": 4, "R": "20", "D": "30s", "Img": "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=400"},
            {"Ej": "Escaladores (Mountain)", "S": 3, "R": "30s", "D": "45s", "Img": "https://images.unsplash.com/photo-1434682881908-b43d0467b798?w=400"},
            {"Ej": "Burpees controlados", "S": 3, "R": "10", "D": "60s", "Img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"}
        ]
    
    # Ajustar cantidad de ejercicios según el tiempo (aproximadamente 10 min por cada 2 ej)
    num_ejercicios = max(4, min(len(base), int(tiempo_minutos / 10)))
    return base[:num_ejercicios]

# Mostrar rutinas por día
for i in range(1, dias_semana + 1):
    with st.expander(f"📅 DÍA {i} - Entrenamiento Personalizado", expanded=(i==1)):
        sesion = generar_bloque_ejercicios(i)
        for ej in sesion:
            c1, c2 = st.columns([1, 2])
            c1.image(ej["Img"], use_container_width=True)
            c2.subheader(ej["Ej"])
            c2.write(f"**Series:** {ej['S']} | **Repeticiones:** {ej['R']} | **Descanso:** {ej['D']}")
            st.write("---")

# --- SECCIÓN 5: REGISTRO Y TABLA DE RESULTADOS ---
st.header("📊 RESUMEN Y REGISTRO DE PROGRESO")

# Creamos el historial en la sesión para visualizarlo en tabla
if 'historial_local' not in st.session_state:
    st.session_state.historial_local = []

col_btn1, col_btn2 = st.columns(2)

if col_btn1.button("✅ Registrar Sesión Completada"):
    nueva_entrada = {
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Usuario": alias,
        "Meta": meta,
        "Duración": f"{tiempo_minutos} min",
        "Calidad": "Excelente"
    }
    st.session_state.historial_local.append(nueva_entrada)
    st.success("¡Datos registrados en la tabla!")

# Visualización en TABLA
if st.session_state.historial_local:
    df_historial = pd.DataFrame(st.session_state.historial_local)
    st.table(df_historial) # AQUÍ SE VISUALIZA LA TABLA

    # Botón para descargar
    csv = df_historial.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Historial Completo (CSV)",
        data=csv,
        file_name=f"progreso_{alias}.csv",
        mime="text/csv"
    )

st.warning("🔔 NOTA IMPORTANTE: Guarda este archivo. La IA lo requerirá cada 30 días para ajustar tu Carga Progresiva.")
st.sidebar.caption("Ingeniería Humana & Medicina Deportiva 2026")
