# DocSage🧙‍♂️ - RAG Sample Application

DocSage es una aplicación de chat inteligente que utiliza Retrieval-Augmented Generation (RAG) para responder preguntas basadas en documentos y enlaces web que subas. La aplicación permite crear múltiples chats, cargar documentos de diferentes formatos, agregar enlaces web como fuentes de información, y mantener conversaciones contextuales con un modelo de IA.

## 🚀 Características

- **Chat Múltiple**: Crea y gestiona múltiples conversaciones independientes
- **Carga de Documentos**: Soporte para archivos PDF, DOCX, TXT, CSV, HTML y Markdown
- **Integración Web**: Agrega enlaces web como fuentes de información
- **RAG (Retrieval-Augmented Generation)**: Respuestas contextuales basadas en tus documentos
- **Interfaz Intuitiva**: Aplicación web construida con Streamlit
- **Base de Datos**: Almacenamiento persistente con SQLite
- **Embeddings**: Utiliza modelos de Hugging Face para generar embeddings
- **Búsqueda Semántica**: Búsqueda vectorial con Chroma

## 🛠️ Tecnologías Utilizadas

- **Frontend**: Streamlit
- **Backend**: Python con LangChain
- **Base de Datos**: SQLite
- **Vector Store**: Chroma
- **Embeddings**: HuggingFace (sentence-transformers/all-mpnet-base-v2)
- **LLM**: Azure AI via GitHub Models (mistral-ai/mistral-medium-2505)
- **Gestión de Dependencias**: UV

## ⚙️ Configuración

### 1. Crear archivo de configuración

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Token de GitHub para acceder a GitHub Models
GITHUB_TOKEN=your_github_token_here
```

### 2. Obtener GitHub Token

Para usar los modelos del marketplace de GitHub Models, necesitas un token de GitHub con permisos específicos:

1. Ve a [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Haz clic en "Generate new token" > "Generate new token (classic)"
3. Asigna un nombre descriptivo al token (ej: "DocSage RAG App - GitHub Models")
4. Selecciona los siguientes scopes necesarios para acceder al marketplace de modelos:
   - `read:user` (para información básica del usuario)
   - `user:email` (para acceder al email del usuario)
   - `repo` (requerido para acceder a GitHub Models marketplace)
5. Haz clic en "Generate token"
6. **¡IMPORTANTE!** Copia el token inmediatamente ya que no podrás verlo de nuevo
7. Pega el token en tu archivo `.env` como valor de `GITHUB_TOKEN`

**Nota:** El scope `repo` es necesario para autenticarte con GitHub Models y acceder a los modelos disponibles en el marketplace como Mistral AI Medium 2505.

### 3. Instalación de dependencias

Asegúrate de tener [UV](https://docs.astral.sh/uv/) instalado. Si no lo tienes:

```bash
# En macOS y Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# En Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Luego instala las dependencias:

```bash
uv sync
```

## 🚀 Instalación y Ejecución

### 1. Crear la base de datos

Ejecuta el script para crear la base de datos SQLite y las tablas necesarias:

```bash
uv run python create_relational_db.py
```

Este comando creará:

- Un archivo `doc_sage.sqlite` con las tablas para chats, mensajes y fuentes
- Tablas para gestionar conversaciones y documentos asociados

### 2. Ejecutar la aplicación

Inicia la aplicación web con Streamlit:

```bash
uv run streamlit run chats.py
```

La aplicación estará disponible en `http://localhost:8501`

## 📖 Uso de la Aplicación

### Crear un nuevo chat

1. En la página principal, introduce un título para tu chat
2. Haz clic en "Create Chat"

### Agregar documentos

1. En el sidebar del chat, usa el uploader para subir documentos
2. Formatos soportados: PDF, DOCX, TXT, CSV, HTML, MD

### Agregar enlaces web

1. En el sidebar, introduce una URL en el campo "Add a link"
2. Haz clic en "Add Link" para extraer y procesar el contenido

### Conversar

1. Escribe tu pregunta en el campo de chat
2. El sistema buscará información relevante en tus documentos/enlaces
3. Recibirás una respuesta contextualizada basada en tus fuentes

## 📁 Estructura del Proyecto

```text
rag-sample/
├── chats.py              # Aplicación principal de Streamlit
├── db.py                 # Operaciones de base de datos
├── vector_functions.py   # Funciones para manejo de vectores y RAG
├── create_relational_db.py # Script para crear la base de datos
├── pyproject.toml        # Configuración del proyecto y dependencias
├── .env                  # Variables de entorno (crear manualmente)
├── doc_sage.sqlite       # Base de datos SQLite (se crea automáticamente)
└── persist/              # Directorio para almacenar vectores (se crea automáticamente)
```

## 🔧 Dependencias Principales

- `streamlit`: Interface web interactiva
- `langchain`: Framework para aplicaciones LLM
- `langchain-azure-ai`: Integración con modelos de Azure
- `langchain-chroma`: Vector store para búsqueda semántica
- `langchain-huggingface`: Embeddings de Hugging Face
- `python-environ`: Manejo de variables de entorno
- `beautifulsoup4`: Parser para contenido web

## 📝 Notas Adicionales

- Los documentos se procesan en chunks de 1000 caracteres para mejor rendimiento
- La aplicación utiliza embeddings `sentence-transformers/all-mpnet-base-v2`
- Los chats son independientes con sus propios contextos vectoriales
- La base de datos SQLite almacena metadatos, mientras que Chroma almacena los vectores

## 🙏 Reconocimientos

Este proyecto está basado en el excelente tutorial **"Create a Smart RAG App with LangChain and Streamlit"** de [Ngonidzashe Nzenze](https://dev.to/ngonidzashe), publicado en DEV Community. El tutorial original proporciona una guía completa paso a paso para crear una aplicación RAG inteligente utilizando LangChain y Streamlit.

**Enlace al tutorial original:** <https://dev.to/ngonidzashe/doc-sage-create-a-smart-rag-app-with-langchain-and-streamlit-4lin>

**Autor:** Ngonidzashe Nzenze  
**Publicado:** 6 de noviembre de 2024

### Adaptaciones en esta versión

- **Cambio de modelo LLM**: Se migró de OpenAI GPT-4o-mini a **Mistral AI Medium 2505** a través de GitHub Models
- **Cambio de embeddings**: Se cambió de OpenAI Embeddings a **Hugging Face sentence-transformers**
- **Sistema de gestión**: Se integró **UV** como gestor de dependencias
- **Mejoras en documentación**: README expandido con guías detalladas de configuración

Agradecemos a Ngonidzashe por compartir su conocimiento y crear un tutorial tan claro y educativo que sirve como base para este proyecto.
