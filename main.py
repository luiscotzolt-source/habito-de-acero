import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración profesional
st.set_page_config(page_title="Tu Coach con IA", page_icon="🏋️‍♂️", layout="wide")

st.title("🏋️‍♂️ Tu Coach con IA: Ingeniería de Entrenamiento")
st.markdown("### *Rutinas inteligentes adaptadas a tus lesiones y disponibilidad*")
st.write("---")

# --- 1. EVALUACIÓN DE LIMITACIONES ESPECÍFICAS ---
with st.form("cuestionario_coach"):
    st.header("📋 Diagnóstico de Capacidades")
    
    col1, col2 = st.columns(2)
    with col1:
        objetivo = st.selectbox("Objetivo", ["Salud General", "Masa Muscular", "Fuerza", "Pérdida de Grasa"])
        dias = st.slider("Días disponibles a la semana", 1, 6, 3)
    with col2:
        tiempo = st.slider("Minutos por sesión", 20, 90, 45)
        edad = st.number_input("Edad", 15, 90, 30)

    st.subheader("⚠️ Zonas de Dolor o Limitaciones")
    st.write("Selecciona las zonas donde presentas molestias para adaptar los ejercicios:")
    c1, c2, c3, c4 = st.columns(4)
    lumbalgia = c1.checkbox("Lumbalgia (Espalda baja)")
    rodillas = c2.checkbox("Dolor en Rodillas")
    hombros = c3.checkbox("Dolor en Hombros")
    codos = c4.checkbox("Dolor en Codos")

    enviar = st.form_submit_button("🔨 Generar Mi Rutina Semanal")

# --- 2. ALGORITMO DE DISTRIBUCIÓN Y ADAPTACIÓN ---
if enviar:
    st.header(f"📅 Plan Semanal: {dias} Días de Entrenamiento")
    
    # Definición de rutinas por día según cantidad de días
    if dias == 1:
        rutinas = {1: "Cuerpo Completo (Full Body)"}
    elif dias == 2:
        rutinas = {1: "Tren Superior", 2: "Tren Inferior"}
    elif dias == 3:
        rutinas = {1: "Pecho, Tríceps y Hombros", 2: "Espalda y Bíceps", 3: "Piernas y Core"}
    else: # 4 a 6 días
        rutinas = {1: "Pecho y Tríceps", 2: "Espalda y Bíceps", 3: "Piernas", 4: "Hombros y Core"}

    # Generar visualización por cada día
    for d, musculos in rutinas.items():
        with st.expander(f"DÍA {d}: {musculos}", expanded=True):
            col_txt, col_img = st.columns([2, 1])
            
            with col_txt:
                st.write(f"**Enfoque:** {musculos}")
                
                # Adaptación de ejercicios según limitaciones
                ejercicios = []
                if "Pecho" in musculos:
                    ej = "Press con mancuernas" if not hombros else "Flexiones inclinadas (menor presión en hombro)"
                    ejercicios.append(f"✅ {ej}")
                if "Tríceps" in musculos:
                    ej = "Extensiones en polea" if not codos else "Press francés ligero (evitar bloqueo brusco)"
                    ejercicios.append(f"✅ {ej}")
                if "Piernas" in musculos:
                    ej = "Sentadilla búlgara" if not rodillas else "Puente de glúteo e Isometría (sin impacto)"
                    ejercicios.append(f"✅ {ej}")
                if "Espalda" in musculos:
                    ej = "Peso muerto o Remo" if not lumbalgia else "Remo en máquina con apoyo en pecho (protege espalda)"
                    ejercicios.append(f"✅ {ej}")
                
                for e in ejercicios:
                    st.write(e)
                
                # Notas de seguridad IA
                if lumbalgia: st.warning("⚠️ IA detectó Lumbalgia: Se han eliminado ejercicios de carga axial (pesas sobre la columna).")
                if rodillas: st.info("ℹ️ IA detectó dolor en Rodillas: Ejercicios de pierna ajustados a rangos cortos.")

            with col_img:
                # Imagen genérica según el grupo principal
                img = "https://images.unsplash.com/photo-1581009146145-b5ef03a74010?w=400" if "Pecho" in musculos else "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"
                st.image(img, caption=f"Entrenamiento de {musculos}")

    # --- 3. REGISTRO Y DESCARGA ---
    st.divider()
    if 'historial' not in st.session_state:
        st.session_state.historial = pd.DataFrame(columns=['Fecha', 'Sesión', 'Limitaciones'])
    
    if st.button("✅ Registrar Día Completado"):
        nuevo = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), "Sesión cumplida", "Adaptada"]], columns=['Fecha', 'Sesión', 'Limitaciones'])
        st.session_state.historial = pd.concat([st.session_state.historial, nuevo], ignore_index=True)
        st.success("¡Ingeniería humana aplicada! Progreso guardado.")
        st.balloons()

    csv = st.session_state.historial.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar mi avance al móvil", csv, "mi_entrenamiento.csv", "text/csv")

st.sidebar.write("Tu Coach con IA | v2.0")
