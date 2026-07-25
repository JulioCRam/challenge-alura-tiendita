# 🛍️ La Tiendita - Asistente de Atención al Cliente (Challenge Alura)
¡Hola! Por aquí les comparto este proyecto que creé con todo el entusiasmo como parte del Challenge de Alura. Se trata de un chatbot carismático y natural llamado Tech, creado para atender a los usuarios de "La Tiendita" (un e-commerce de tecnología), respondiendo siempre en plural y basándose enteramente en la información oficial de la empresa.

# 🚀 ¿De qué trata el proyecto?
La idea principal era levantar un asistente virtual inteligente utilizando una arquitectura RAG (Retrieval-Augmented Generation). Lo armamos para resolver necesidades reales de atención al cliente de forma fluida:

- Cero respuestas de robot: Tech responde de inmediato y de forma muy amigable.

- Memoria oficial: Toda la información se alimenta de un documento centralizado de la empresa contenido en Google Drive.

- Sincronización en la nube: Incluye un panel de administración protegido por contraseña para actualizar los documentos directamente desde Google Drive con un solo clic.

# ✨ Lo que vas a encontrar por dentro
💬 Chat inteligente con IA: Impulsado por Google Gemini y LangChain.

🔄 Conexión con Google Drive: Para que actualizar la base de conocimientos sea rápido y sin enredos locales.

🎨 Diseño visual moderno: Interfaz limpia en Streamlit con un toque visual agradable y adaptado para cualquier dispositivo.

🔍 Búsqueda vectorial local: Integración con FAISS para encontrar respuestas precisas al instante dentro del contexto corporativo.

# 🛠️ Tecnologías que usé
- Python

- Streamlit (para toda la parte visual y web)

- LangChain (para orquestar la IA y el manejo de contexto)

- Google Generative AI (Gemini) (el modelo de lenguaje principal)

- FAISS (faiss-cpu) (para la base de datos vectorial)

- Google Drive API (para la sincronización del documento oficial)

# 📂 Estructura del proyecto

| 📁 Archivo / Carpeta | 📄 Descripción |
|----------------------|----------------|
| assets/ | Carpeta que almacena los recursos gráficos utilizados por la aplicación, como imágenes y elementos visuales de la interfaz. |
| Fondo.jpg | Imagen de fondo empleada para mejorar el diseño y la experiencia visual de la aplicación. |
| app.py | Archivo principal de la aplicación desarrollado en *Streamlit*. Gestiona la interfaz de usuario y coordina la interacción entre el usuario y el sistema de inteligencia artificial. |
| drive_sync.py | Script encargado de sincronizar y descargar automáticamente el documento PDF desde *Google Drive*, manteniendo actualizada la base de conocimiento del sistema. |
| requirements.txt | Archivo que contiene la lista de todas las dependencias y bibliotecas necesarias para ejecutar correctamente el proyecto. |

# 🚀 Instalación

```text
📥 Clonar el repositorio
│
├── git clone https://github.com/juansrmoreno-cmyk/Challenge-alura-V1.git
└── cd Challenge-alura-V1

🐍 Crear entorno virtual
│
└── python -m venv venv

▶️ Activar entorno virtual
│
├── Windows
│   └── venv\Scripts\activate
│
└── Linux / macOS
    └── source venv/bin/activate

📦 Instalar dependencias
│
└── pip install -r requirements.txt

⚙️ Configurar variables de entorno
│
├── Crear el archivo .env
│
└── Agregar:
    ├── GOOGLE_API_KEY=TU_API_KEY
    ├── GOOGLE_DRIVE_FILE_ID=ID_DEL_DOCUMENTO
    └── ADMIN_PASSWORD=TU_CONTRASEÑA

🔐 Configurar credenciales de Google Cloud
│
└── Copiar el archivo credentials.json en la raíz del proyecto
    (Este archivo no debe subirse a GitHub)

🚀 Ejecutar la aplicación
│
└── streamlit run app.py

```
#☁️ Despliegue
Enlace de la aplicación: https://challenge-alura-tiendita.streamlit.app/

La aplicación está montada y funcionando en la nube mediante Streamlit Community Cloud, configurada de forma segura utilizando los Secrets de la plataforma para proteger la API Key y las credenciales de Google Drive.

🔑 Contraseña para sincronizar documentos en la nube: L@T1end1ta

Hecho con 💙 por Julio Cesar Ramirez Monroy para el Challenge de Alura Latam y Oracle Next Education.
