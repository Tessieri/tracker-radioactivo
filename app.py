import streamlit as st
import pandas as pd

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Faltantes Radioactivo - Steal a Brainrot", 
    page_icon="☢️", 
    layout="centered"
)

# --- 2. INICIALIZAR LA BASE DE DATOS (STATE) ---
# Esto mantiene los datos guardados mientras la app esté corriendo
if 'faltantes_radioactivo' not in st.session_state:
    st.session_state.faltantes_radioactivo = [
        {"Personaje": "Boneca Ambalabu", "Rareza": "Raro"},
        {"Personaje": "Raccooni Jandelini", "Rareza": "Común"},
        {"Personaje": "Tartaragno", "Rareza": "Común"},
        {"Personaje": "Telemorte", "Rareza": "Secret"},
        {"Personaje": "Pot Pumpkin", "Rareza": "Secret"},
        {"Personaje": "Bandito Axolito", "Rareza": "Legendario"},
        {"Personaje": "Doi Doi Doi", "Rareza": "Épico"},
        {"Personaje": "Tipi Topi Taco", "Rareza": "Brainrot God"},
        {"Personaje": "Gattito Tacoto", "Rareza": "Brainrot God"},
        {"Personaje": "Los Tungtungtungcitos", "Rareza": "Brainrot God"},
        {"Personaje": "Los Crocodillitos", "Rareza": "Brainrot God"},
        {"Personaje": "Las Vaquitas Saturnitas", "Rareza": "Secret"},
        {"Personaje": "Los Matteos", "Rareza": "Secret"},
        {"Personaje": "Los Spyderinis", "Rareza": "Secret"},
        {"Personaje": "Los Karkeritos", "Rareza": "Secret"},
        {"Personaje": "Bisonte Giuppitere", "Rareza": "Secret"},
        {"Personaje": "Tartaruga Cisterna", "Rareza": "Brainrot God"},
        {"Personaje": "Mastodontico Telepiedone", "Rareza": "Brainrot God"},
        {"Personaje": "Bambu Bambu Sahur", "Rareza": "Brainrot God"},
        {"Personaje": "Brasilini Berimbini", "Rareza": "Brainrot God"},
        {"Personaje": "Skull Skull Skull", "Rareza": "Brainrot God"}
    ]

# --- 3. VISTA PÚBLICA ---
st.title("☢️ Tracker de Faltantes - Radioactivo")
st.write("Esta es la lista oficial de los personajes que nos hacen falta en variante **Radioactivo**. Si tienes alguno, ¡avísanos para tradear!")

# Convertimos la lista de diccionarios a un DataFrame para que se vea limpio
if st.session_state.faltantes_radioactivo:
    df = pd.DataFrame(st.session_state.faltantes_radioactivo)
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.success("¡Felicidades! No nos falta ningún personaje radioactivo en este momento.")

st.divider()

# --- 4. MENÚ OCULTO / PANEL DE ADMINISTRACIÓN ---
st.write("¿Eres admin? Ingresa tu código:")
codigo = st.text_input("Código de acceso", type="password", label_visibility="collapsed")

if codigo == "janxz-d_riba":
    st.success("Acceso concedido. Bienvenido al panel de control, David.")
    st.write("Puedes editar la lista aquí mientras tienes Fishstrap abierto para coordinar los trades rápidamente.")
    
    col1, col2 = st.columns(2)
    
    # Formulario para agregar personajes
    with col1:
        st.subheader("➕ Añadir Personaje")
        nuevo_nombre = st.text_input("Nombre del personaje")
        nueva_rareza = st.selectbox(
            "Rareza", 
            ["Común", "Raro", "Épico", "Legendario", "Mítico", "Brainrot God", "Secret", "OG"]
        )
        if st.button("Añadir a la lista"):
            if nuevo_nombre:
                st.session_state.faltantes_radioactivo.append({
                    "Personaje": nuevo_nombre, 
                    "Rareza": nueva_rareza
                })
                st.rerun() # Recarga la página para actualizar la tabla
            else:
                st.warning("Escribe el nombre del personaje primero.")
    
    # Formulario para eliminar personajes que ya consiguieron
    with col2:
        st.subheader("✔️ Marcar como Conseguido")
        if st.session_state.faltantes_radioactivo:
            nombres_actuales = [p["Personaje"] for p in st.session_state.faltantes_radioactivo]
            personaje_a_borrar = st.selectbox("Selecciona el personaje", nombres_actuales)
            
            if st.button("Eliminar de la lista"):
                st.session_state.faltantes_radioactivo = [
                    p for p in st.session_state.faltantes_radioactivo 
                    if p["Personaje"] != personaje_a_borrar
                ]
                st.rerun()
        else:
            st.info("La lista ya está vacía.")
