import os
import base64
import streamlit as st
from dotenv import load_dotenv

# 1. Configuración de la pestaña del navegador (Elige tu propio icono)
st.set_page_config(
    page_title="La Tiendita", 
    page_icon="🛍️", 
    layout="centered"
)
# --- DEFINICIÓN DE LA FUNCIÓN (¡No borrar esto!) ---
def get_base64_image(ruta_imagen):
    with open(ruta_imagen, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- CARGA DE IMAGEN Y ESTILOS ---
img_base64 = get_base64_image("assets/Fondo.jpg")

estilo_maestro = f"""
    <style>
    /* 1. Fondo de pantalla con desenfoque */
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        z-index: 0;
    }}
    
    /* 2. Tarjeta central de Chat (Cristal) */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 24px !important;
        margin-top: 3rem !important;
        z-index: 1 !important;
       overflow-y: auto !important; 
        max-height: 85vh !important; /* Opcional: Define un límite de altura para que el scroll siempre funcione bien */
    }}

    /* 3. Panel de Administración */
    [data-testid="stSidebar"] {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.3) !important;
    }}

    /* 4. Chat Bubbles (Forzando ruptura de texto) */
    [data-testid="stChatMessage"] {{
        display: flex !important;
        width: 100% !important;
        background-color: transparent !important;
        min-width: 0 !important; /* Importante para el flexbox */
    }}
    
    /* Reglas agresivas para que el texto no se salga */
    [data-testid="stMarkdownContainer"] {{
        overflow-wrap: break-word !important;
        word-break: break-all !important; /* Rompe palabras largas y URLs */
        white-space: pre-wrap !important;
        max-width: 100% !important;
    }}

    /* Burbuja Usuario (Derecha) */
    [data-testid="stChatMessage"]:has(.user-msg-hook) {{ flex-direction: row-reverse !important; }}
    [data-testid="stChatMessage"]:has(.user-msg-hook) div[data-testid="stMarkdownContainer"] {{
        background-color: #007BFF;
        color: white !important;
        border-radius: 20px 20px 0px 20px;
        padding: 12px 18px !important;
        margin-left: auto !important;
        max-width: 70% !important;
    }}
    
    /* Burbuja IA (Izquierda) */
    [data-testid="stChatMessage"]:not(:has(.user-msg-hook)) div[data-testid="stMarkdownContainer"] {{
        background-color: rgba(255, 255, 255, 0.8);
        color: #333 !important;
        border-radius: 20px 20px 20px 0px;
        padding: 12px 18px !important;
        max-width: 70% !important;
    }}

    /* 5. Input */
    [data-testid="stBottom"] {{ background: transparent !important; }}
    [data-testid="stChatInput"] {{
        background: rgba(255, 255, 255, 0.7) !important;
        border-radius: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
    }}
    [data-testid="stChatInput"] textarea {{ background: transparent !important; }}
    
    #MainMenu, footer, header {{ visibility: hidden; }}
    </style>
"""
st.markdown(estilo_maestro, unsafe_allow_html=True)

# Importamos las funciones de nuestros scripts anteriores
from drive_sync import download_pdf_from_drive
from rag_engine import update_vector_db, get_answer



load_dotenv()


# --- BARRA LATERAL (Panel de Administración) ---
st.sidebar.title("Panel de Administracion")
st.sidebar.markdown("---")

# Sección de autenticación para el Administrador (Opción A)
st.sidebar.subheader("🔐 Área de Administración")
admin_password_input = st.sidebar.text_input("Contraseña", type="password")

# Validamos la contraseña contra la definida en el archivo .env
if admin_password_input == os.getenv("ADMIN_PASSWORD"):
    st.sidebar.success("Acceso concedido")
    st.sidebar.markdown("Use el siguiente botón para sincronizar la base de conocimiento con el documento oficial en Google Drive.")
    
    # Botón exclusivo para ejecutar la sincronización
    if st.sidebar.button("🔄 Sincronizar Documentos"):
        with st.sidebar.status("Procesando...", expanded=True) as status:
            st.write("Descargando el PDF desde Google Drive...")
            pdf_file = download_pdf_from_drive()
            
            if pdf_file:
                st.write("Actualizando base de datos vectorial (Embeddings)...")
                try:
                    update_vector_db()
                    status.update(label="Sincronización Exitosa ✅", state="complete", expanded=False)
                    st.toast("¡Documentos sincronizados con éxito!")
                except Exception as e:
                    status.update(label="Error en procesamiento ❌", state="error")
                    st.sidebar.error(f"Error al indexar el PDF: {e}")
            else:
                status.update(label="Error de descarga ❌", state="error")
                st.sidebar.error("No se pudo descargar el archivo de Drive. Revisa las credenciales.")
elif admin_password_input:
    st.sidebar.error("Contraseña incorrecta")

# --- CUERPO PRINCIPAL (Chat del Usuario) ---
st.title("🤖 La Tiendita AI")
st.markdown("Bienvenido a la Tiendita Soy Tech. Como Puedo ayudarte hoy.")
st.markdown("---")

# Verificar si la base de datos vectorial ya existe en el servidor
if not os.path.exists("./vector_db"):
    st.warning("⚠️ La base de conocimiento está vacía. Un administrador debe ingresar la contraseña en la barra lateral y sincronizar los datos por primera vez.")

# Inicializar el historial de conversación en la sesión de Streamlit si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes anteriores del historial
for message in st.session_state.messages:
    icono = "🧑‍💻" if message["role"] == "user" else "🛒"
    with st.chat_message(message["role"], avatar=icono):
        if message["role"] == "user":
            # Inyectamos el Hook invisible para moverlo a la derecha
            st.markdown(f"<span class='user-msg-hook'></span> {message['content']}", unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# Capturar la pregunta del usuario
if user_query := st.chat_input("Escribe tu consulta aquí..."):
    # Mostrar la pregunta del usuario inmediatamente en pantalla
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(f"<span class='user-msg-hook'></span> {user_query}", unsafe_allow_html=True)
    
    # Guardar la pregunta en el historial
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Generar la respuesta usando el motor RAG
    with st.chat_message("assistant", avatar="🛒"):
        with st.spinner("Escribiendo..."):
            try:
                response = get_answer(user_query)
                st.markdown(response)
                # Guardar la respuesta en el historial
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Lo siento, ocurrió un error al procesar tu consulta: {e}"
                st.markdown(error_msg)