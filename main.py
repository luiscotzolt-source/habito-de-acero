import streamlit as st
import pandas as pd
from datetime import date

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Hábito de Acero", page_icon="??", layout="wide")

# --- LÓGICA DE ESTILOS (CSS Simple) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_name_with_html=True)

# --- BARRA LATERAL (Navegación y Donaciones) ---
st.sidebar.title("??? Hábito de Acero")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2964/2964514.png", width=100)
menu = st.sidebar.radio("Navegación", [
    "1. Perfil de Salud", 
    "2. Mi Entrenamiento", 
    "3. Nutrición de Bolsillo", 
    "4. Verdad sobre Suplementos", 
    "5. Mentalidad y Fármacos",
    "6. Exportar Progreso"
])

st.sidebar.markdown("---")
st.sidebar.info("?? *El yo de mañana te agradecerá el esfuerzo de hoy.*")
st.sidebar.write("?? *Donaciones (Sin Publicidad):*")
st.sidebar.button("Donar por PayPal")

# --- 1. PERFIL DE SALUD Y SEGURIDAD ---
if menu == "1. Perfil de Salud":
    st.header("?? Evaluación Inicial de Ingeniería Humana")
    col1, col2 = st.columns(2)
    
    with col1:
        edad = st.number_input("Edad", 14, 90, 40)
        peso = st.number_input("Peso actual (kg)", 40.0, 200.0, 80.0)
        genero = st.selectbox("Género", ["Masculino", "Femenino"])
    
    with col2:
        estat = st.number_input("Estatura (cm)", 100, 250, 170)
        objetivo = st.selectbox("Tu meta principal", ["Perder Tallas", "Ganar Músculo", "Rehabilitación"])

    st.subheader("?? Historial Médico y Padecimientos")
    lesiones = st.multiselect("Selecciona si tienes o has tenido:", [
        "Hernia Discal", "Hernia Inguinal", "Ciática", "Lumbalgia", 
        "Dolor de Rodilla", "Hipertensión", "Diabetes", "Cesárea", "Apendicitis"
    ])
    
    # Guardar en sesión para usar en otros módulos
    st.session_state['user_data'] = {
        "edad": edad, "peso": peso, "lesiones": lesiones, "objetivo": objetivo
    }
    st.success("? Perfil configurado. La IA ahora conoce tus límites y fortalezas.")

# --- 2. ENTRENAMIENTO ADAPTATIVO (MODO LITE) ---
elif menu == "2. Mi Entrenamiento":
    st.header("??? Entrenamiento Personalizado")
    
    if 'user_data' not in st.session_state:
        st.warning("?? Por favor, completa tu Perfil de Salud primero.")
    else:
        estado = st.select_slider("¿Cómo te sientes tras la jornada laboral?", 
            options=["Agotado", "Cansado", "Normal", "Con Energía"])
        
        # Filtros de Seguridad basados en el perfil
        user = st.session_state['user_data']
        
        if any(x in user['lesiones'] for x in ["Hernia Discal", "Ciática", "Lumbalgia"]):
            st.error("?? *ALERTA DE ESPALDA:* Evita Sentadilla con barra y Press Militar de pie. Usa máquinas con respaldo.")
            
        
        if "Hipertensión" in user['lesiones']:
            st.warning("?? *ALERTA PRESIÓN:* Exhala en el esfuerzo. No mantengas el aire (Valsalva).")

        # Generación de Rutina
        if estado in ["Agotado", "Cansado"]:
            st.info("??? *MODO LITE (Hábito de Acero):* Hoy el éxito es aparecer. Haremos 2 series por ejercicio al 60% de intensidad.")
            st.write("- *Pecho:* Prensa en máquina (Más seguro que pesas libres hoy).")
            st.write("- *Espalda:* Remo sentado (Enfoque en postura).")
            st.write("- *Pierna:* Prensa de piernas (Rango corto si hay dolor).")
        else:
            st.success("?? *MODO FULL:* Vamos por la sobrecarga progresiva.")
            st.write("- *Básico:* 4 series de 8-12 repeticiones.")
            st.write("- *Enfoque:* Anota si pudiste subir 1kg o hacer 1 rep más que ayer.")

# --- 3. NUTRICIÓN DE BOLSILLO (ING. ALIMENTARIA) ---
elif menu == "3. Nutrición de Bolsillo":
    st.header("?? Dieta Real para Gente Real")
    
    if 'user_data' in st.session_state:
        u = st.session_state['user_data']
        # Lógica de Macros (Mifflin-St Jeor simplificada)
        proteina = u['peso'] * 2
        st.metric("Proteína diaria sugerida", f"{proteina} g", "Basado en tu peso")
        
        st.subheader("?? Supermercado Económico")
        st.markdown("""
        * *Huevo:* Proteína de oro. Barata y completa.
        * *Arroz y Frijoles:* Combinación de aminoácidos perfecta (Ingeniería de Alimentos).
        * *Papa/Camote:* Energía de la tierra, mucho mejor que procesados.
        * *Agua con Sal:* Mejor que cualquier bebida deportiva cara si sudas mucho.
        """)
        

# --- 4. VERDAD SOBRE SUPLEMENTOS ---
elif menu == "4. Verdad sobre Suplementos":
    st.header("?? El Filtro de la Ciencia")
    st.write("No tires tu dinero en marketing.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("? Lo que SÍ sirve")
        st.write("- *Creatina Monohidratada:* Fuerza y cerebro. 5g/día.")
        st.write("- *Proteína en Polvo:* Solo si no llegas a tu meta con comida.")
    with col2:
        st.subheader("? Lo que NO necesitas")
        st.write("- *BCAAs:* Si comes huevo/carne, son agua cara.")
        st.write("- *Quemadores de Grasa:* Son solo cafeína cara. El déficit manda.")

# --- 5. MENTALIDAD Y FÁRMACOS ---
elif menu == "5. Mentalidad y Fármacos":
    st.header("?? El 'Yo' de Ayer vs El 'Yo' de Hoy")
    st.write("> *No compites con el de la foto. Compites con quien eras hace 24 horas.*")
    
    st.subheader("?? La Realidad de los Fármacos (PEDs)")
    st.markdown("""
    * *No hay magia:* Los cuerpos de revista tienen ejércitos de médicos y luz profesional.
    * *Riesgo Real:* Inyectarse sin un examen endocrino previo puede apagar tu sistema natural para siempre.
    * *Nuestra postura:* Antes de un fármaco, ve al Endocrinólogo. La salud no se negocia por un músculo temporal.
    """)
    

# --- 6. EXPORTAR PROGRESO (PRIVACIDAD) ---
elif menu == "6. Exportar Progreso":
    st.header("?? Exportar a CSV para Excel")
    st.write("Tus datos son tuyos. Descárgalos y súbelos a tu Google Drive.")
    
    if 'user_data' in st.session_state:
        df = pd.DataFrame([st.session_state['user_data']])
        df['fecha'] = date.today()
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("?? Descargar Progreso", data=csv, file_name=f"habito_acero_{date.today()}.csv", mime="text/csv")
    else:
        st.warning("No hay datos para exportar.")
