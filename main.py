import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Hábito de Acero", page_icon="🛡️", layout="centered")

# Estilo personalizado
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("🛡️ Hábito de Acero")
st.subheader("Forjando la mejor versión de ti mismo")
st.write("---")

# Sistema de Registro
st.sidebar.header("Panel de Control")
nombre = st.sidebar.text_input("Ingeniero:", value="Luis")

# Rutina Diaria
st.info(f"Bienvenido, {nombre}. La disciplina es el puente entre las metas y los logros.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠️ Base Física")
    h1 = st.checkbox("Ejercicio intenso (30 min)")
    h2 = st.checkbox("Ducha fría")
    h3 = st.checkbox("Alimentación limpia")

with col2:
    st.markdown("### 🧠 Base Mental")
    h4 = st.checkbox("Lectura (10 páginas)")
    h5 = st.checkbox("Meditación / Enfoque")
    h6 = st.checkbox("Planificación del día")

# Cálculo de progreso
total = sum([h1, h2, h3, h4, h5, h6])
progreso = total / 6

st.write("---")
st.write(f"### Progreso del Día: {int(progreso * 100)}%")
st.progress(progreso)

if progreso == 1.0:
    st.balloons()
    st.success("¡MISIÓN CUMPLIDA! Eres un hombre de acero.")
elif progreso >= 0.5:
    st.warning("Buen avance, pero el acero se forja hasta el final.")
else:
    st.error("Mantente firme. La pereza es el enemigo.")

# Pie de página
st.caption("Sistema de Ingeniería Humana | 2026")
