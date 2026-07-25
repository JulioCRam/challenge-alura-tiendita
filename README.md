🛍️ La Tiendita - Asistente de Atención al Cliente (Challenge Alura)
¡Hola! Por aquí les comparto este proyecto que cree como parte del Challenge de Alura. Se trata de un chatbot, carismático y natural llamado Tech, creado para atender a los usuarios de "La Tiendita" un ecommerce de tecnología respondiendo siempre en plural y basándose enteramente en la información oficial de la empresa.

🚀 ¿De qué trata el proyecto?
La idea principal era levantar un asistente virtual inteligente utilizando una arquitectura RAG (Retrieval-Augmented Generation). Lo armamos para resolver necesidades reales de atención al cliente de forma fluida:
•	Cero respuestas de robot: Tech responde de inmediato y de forma muy amigable.
•	Memoria oficial: Toda la información se alimenta de un documento centralizado de la empresa contenido en Google drive.
•	Sincronización en la nube: Incluye un panel de administración protegido por contraseña para actualizar los documentos directamente desde Google Drive con un solo clic.

✨ Lo que vas a encontrar por dentro
•	💬 Chat inteligente con IA: Impulsado por Google Gemini y LangChain.
•	🔄 Conexión con Google Drive: Para que actualizar la base de conocimientos sea rápido y sin enredos locales.
•	🎨 Diseño visual moderno: Interfaz limpia en Streamlit con un toque visual agradable y adaptado para cualquier dispositivo.
•	🔍 Búsqueda vectorial local: Integración con FAISS para encontrar respuestas precisas al instante dentro del contexto corporativo.

🛠️ Tecnologías que usé
•	Python
•	Streamlit (para toda la parte visual y web)
•	LangChain (para orquestar la IA y el manejo de contexto)
•	Google Generative AI (Gemini) (el modelo de lenguaje principal)
•	FAISS (faiss-cpu) (para la base de datos vectorial)
•	Google Drive API (para la sincronización del documento oficial)

💻 ¿Cómo correrlo en tu máquina?
Si quieres clonar este repositorio y probarlo localmente, solo sigue estos pasos:
1.	Clona el repositorio:
en la terminal ejecuta
git clone https://github.com/JulioCRam/challenge-alura-tiendita.git
cd challenge-alura-tiendita
2.	Crea y activa tu entorno virtual:
python -m venv .venv
# En Windows:
.venv\Scripts\activate
3.	Instala las dependencias:
pip install -r requirements.txt
4.	Configura tus variables de entorno: Crea un archivo llamado .env en la raíz del proyecto y añade tus credenciales:
GOOGLE_API_KEY="tu_clave_de_api_de_gemini"
ADMIN_PASSWORD="tu_contraseña_de_administrador"
(Si vas a probar la sincronización con Drive localmente, asegúrate de tener tu archivo credentials.json en la raíz).
5.	Ejecuta la aplicación:
streamlit run app.py

☁️ Despliegue
https://challenge-alura-tiendita.streamlit.app/
La aplicación está montada y funcionando en la nube mediante Streamlit Community Cloud, configurada de forma segura utilizando los Secrets de la plataforma para proteger la API Key y las credenciales de Google Drive.
Contraseña para sincronizar documentos: L@T1end1ta.
Hecho por Julio Cesar Ramirez Monroy para el Challenge de Alura Latam y Oracle Next Education.
