import streamlit as st
import pandas as pd

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Candy Tracker - Steal a Brainrot", 
    page_icon="🍬", 
    layout="centered"
)

# --- 2. INICIALIZAR LA BASE DE DATOS EN SESSION STATE ---
if 'candy_tracker' not in st.session_state:
    st.session_state.candy_tracker = {
        "busco": [
            {"Personaje": "Tim Cheese", "Rareza": "Común"},
            {"Personaje": "Talpa Di Fero", "Rareza": "Común"},
            {"Personaje": "Ta Ta Ta Ta Sahur", "Rareza": "Raro"},
            {"Personaje": "Brr Brr Patapim", "Rareza": "Épico"},
            {"Personaje": "Trulimero Trulicina", "Rareza": "Épico"},
            {"Personaje": "Bambini Crostini", "Rareza": "Épico"},
            {"Personaje": "Brri Brri Bicus Dicus Bombicus", "Rareza": "Épico"},
            {"Personaje": "Avocadini Guffo", "Rareza": "Épico"},
            {"Personaje": "Ballerina Capuccina", "Rareza": "Legendario"},
            {"Personaje": "Chef Crabracadabra", "Rareza": "Legendario"},
            {"Personaje": "Glorbo Fruttodrillo", "Rareza": "Legendario"},
            {"Personaje": "Strawberrelli Flamingelli", "Rareza": "Legendario"},
            {"Personaje": "Pandaccini Bananini", "Rareza": "Legendario"},
            {"Personaje": "Frigo Camelo", "Rareza": "Mítico"},
            {"Personaje": "Rhino Toasterino", "Rareza": "Mítico"},
            {"Personaje": "Bombardiro Crocodilo", "Rareza": "Mítico"},
            {"Personaje": "Spioniro Golubiro", "Rareza": "Mítico"},
            {"Personaje": "Tigrilini Watermelini", "Rareza": "Mítico"},
            {"Personaje": "Cavallo Virtuoso", "Rareza": "Mítico"},
            {"Personaje": "Cocofanto Elefanto", "Rareza": "Brainrot God"},
            {"Personaje": "Girafa Celestre", "Rareza": "Brainrot God"},
            {"Personaje": "Gattatino Nyanino", "Rareza": "Brainrot God"},
            {"Personaje": "Tralalero Tralala", "Rareza": "Brainrot God"},
            {"Personaje": "Tigroligre Frutonni", "Rareza": "Brainrot God"},
            {"Personaje": "Espresso Signora", "Rareza": "Brainrot God"},
            {"Personaje": "Unclito Samito", "Rareza": "Brainrot God"},
            {"Personaje": "Odin Din Din Dun", "Rareza": "Brainrot God"},
            {"Personaje": "Orcalero Orcala", "Rareza": "Brainrot God"},
            {"Personaje": "Trenostuzzo Turbo 3000", "Rareza": "Brainrot God"},
            {"Personaje": "Ballerino Lololo", "Rareza": "Brainrot God"},
            {"Personaje": "Sammyni Spyderini", "Rareza": "Secret"},
            {"Personaje": "La Vacca Saturno Saturnita", "Rareza": "Secret"},
            {"Personaje": "Tortuginni Dragonfrutini", "Rareza": "Secret"},
            {"Personaje": "Los Tralaleritos", "Rareza": "Secret"},
            {"Personaje": "Las Tralaleritas", "Rareza": "Secret"},
            {"Personaje": "Graipuss Medussi", "Rareza": "Secret"},
            {"Personaje": "Pot Hotspot", "Rareza": "Secret"},
            {"Personaje": "La Grande Combinasion", "Rareza": "Secret"},
            {"Personaje": "Nuclearo Dinossauro", "Rareza": "Secret"},
            {"Personaje": "Garama And Madundung", "Rareza": "Secret"}
        ],
        "tengo": [
            {"Personaje": "Gangster Footera", "Rareza": "Raro"},
            {"Personaje": "Trippi Troppi", "Rareza": "Raro"},
            {"Personaje": "Avocadini Antilopini", "Rareza": "Épico"},
            {"Personaje": "Burbaloni Loliloli", "Rareza": "Legendario"},
            {"Personaje": "Boneca Ambalabu", "Rareza": "Raro"},
            {"Personaje": "Matteo", "Rareza": "Brainrot God"},
            {"Personaje": "Lionel Cactuseli", "Rareza": "Legendario"},
            {"Personaje": "Orangutini Ananassini", "Rareza": "Mítico"},
            {"Personaje": "Svinina Bombardino", "Rareza": "Común"},
            {"Personaje": "Fluriflura", "Rareza": "Común"},
            {"Personaje": "Nobini Pizzanini", "Rareza": "Común"},
            {"Personaje": "Zibra Zubra Zibralini", "Rareza": "Mítico"},
            {"Personaje": "Tric Trac Barabom", "Rareza": "Raro"},
            {"Personaje": "Cappuccino Assassino", "Rareza": "Épico"},
            {"Personaje": "Cacto Hipopotamo", "Rareza": "Raro"},
            {"Personaje": "Lirili Larila", "Rareza": "Común"},
            {"Personaje": "Pipi Kiwi", "Rareza": "Común"},
            {"Personaje": "Bananita Dolphinita", "Rareza": "Épico"},
            {"Personaje": "Bombombini Gusini", "Rareza": "Mítico"},
            {"Personaje": "Bluberrini Octopusini", "Rareza": "Legendario"},
            {"Personaje": "Chimpanzini Bananini", "Rareza": "Legendario"},
            {"Personaje": "Bandito Bobritto", "Rareza": "Raro"},
            {"Personaje": "Perochello Lemonchello", "Rareza": "Épico"}
        ]
    }

# --- 3. VISTA PÚBLICA ---
st.title("🍬 Candy Tracker - Lista de Intercambios")
st.write("Esta es mi colección actual y los personajes que estoy buscando activamente en variante **Candy**.")

# Creamos pestañas para organizar la visualización pública
tab_busco, tab_tengo = st.tabs(["🔍 Personajes que BUSCO", "✅ Personajes que YA TENGO"])

with tab_busco:
    if st.session_state.candy_tracker["busco"]:
        df_busco = pd.DataFrame(st.session_state.candy_tracker["busco"])
        # Ordenamos por rareza para que la lectura sea más cómoda
        df_busco['Rareza_Num'] = df_busco['Rareza'].map({"Común": 1, "Raro": 2, "Épico": 3, "Legendario": 4, "Mítico": 5, "Brainrot God": 6, "Secret": 7})
        df_busco = df_busco.sort_values(by='Rareza_Num').drop(columns=['Rareza_Num'])
        
        st.dataframe(df_busco, use_container_width=True, hide_index=True)
    else:
        st.success("¡Increíble! He completado todos los personajes Candy que buscaba.")

with tab_tengo:
    if st.session_state.candy_tracker["tengo"]:
        df_tengo = pd.DataFrame(st.session_state.candy_tracker["tengo"])
        df_tengo['Rareza_Num'] = df_tengo['Rareza'].map({"Común": 1, "Raro": 2, "Épico": 3, "Legendario": 4, "Mítico": 5, "Brainrot God": 6, "Secret": 7})
        df_tengo = df_tengo.sort_values(by='Rareza_Num').drop(columns=['Rareza_Num'])
        
        st.dataframe(df_tengo, use_container_width=True, hide_index=True)
    else:
        st.info("Aún no he listado mis personajes disponibles.")

st.divider()

# --- 4. PANEL DE ADMINISTRACIÓN (CÓDIGO OCULTO) ---
st.write("¿Eres admin? Ingresa tu código:")
codigo = st.text_input("Código de acceso", type="password", label_visibility="collapsed")

if codigo == "D_RIBA":
    st.success("Acceso concedido. Panel Candy activo.")
    
    col1, col2 = st.columns(2)
    
    # Mover de "Busco" a "Tengo" (Lo conseguiste)
    with col1:
        st.subheader("📦 Marcar como Conseguido")
        if st.session_state.candy_tracker["busco"]:
            nombres_busco = [p["Personaje"] for p in st.session_state.candy_tracker["busco"]]
            personaje_conseguido = st.selectbox("Selecciona el que obtuviste:", nombres_busco, key="conseguir_select")
            
            if st.button("¡Lo tengo!"):
                # Encontrar el personaje en la lista de busco
                item = next(p for p in st.session_state.candy_tracker["busco"] if p["Personaje"] == personaje_conseguido)
                # Remover de busco y añadir a tengo
                st.session_state.candy_tracker["busco"].remove(item)
                st.session_state.candy_tracker["tengo"].append(item)
                st.rerun()
        else:
            st.info("No hay personajes pendientes en la lista de búsqueda.")

    # Mover de "Tengo" a "Busco" o removerlo por tradeo
    with col2:
        st.subheader("♻️ Gestionar Repetidos / Cambios")
        if st.session_state.candy_tracker["tengo"]:
            nombres_tengo = [p["Personaje"] for p in st.session_state.candy_tracker["tengo"]]
            personaje_gestionado = st.selectbox("Selecciona de tu inventario:", nombres_tengo, key="perder_select")
            
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                if st.button("Devolver a Busco"):
                    item = next(p for p in st.session_state.candy_tracker["tengo"] if p["Personaje"] == personaje_gestionado)
                    st.session_state.candy_tracker["tengo"].remove(item)
                    st.session_state.candy_tracker["busco"].append(item)
                    st.rerun()
            with sub_col2:
                if st.button("Eliminar (Traded)", help="Sácalo completamente si lo tradeaste"):
                    st.session_state.candy_tracker["tengo"] = [p for p in st.session_state.candy_tracker["tengo"] if p["Personaje"] != personaje_gestionado]
                    st.rerun()
        else:
            st.info("Tu inventario actual está vacío.")
