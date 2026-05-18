from utils.pdf_loader import load_pdfs_from_folder
from utils.text_splitter import split_text_into_chunks
from utils.embeddings import generate_embeddings
from utils.retriever import create_vector_store

# Ruta donde están los PDFs
DATA_PATH = "data"

print("\n===== CARGANDO PDFs =====\n")

# Cargar texto desde PDFs
text = load_pdfs_from_folder(DATA_PATH)

# Verificar extracción
print("\n===== TEXTO EXTRAÍDO =====\n")

if text:
    print(text[:1000])  # Mostrar primeros 1000 caracteres
else:
    print("No se extrajo texto.")

print("\n=========================\n")

print(f"Cantidad total de caracteres: {len(text)}")

# Verificar si el texto está vacío
if not text.strip():
    print("\n[ERROR] No se pudo extraer texto de los PDFs.\n")
    exit()

print("\n===== DIVIDIENDO TEXTO EN CHUNKS =====\n")

# Crear chunks
chunks = split_text_into_chunks(text)

print(f"Cantidad de chunks generados: {len(chunks)}")

# Verificar chunks vacíos
if len(chunks) == 0:
    print("\n[ERROR] No se generaron chunks.\n")
    exit()

print("\n===== GENERANDO EMBEDDINGS =====\n")

# Generar embeddings
embeddings = generate_embeddings(chunks)

print(f"Cantidad de embeddings generados: {len(embeddings)}")

print("\n===== CREANDO BASE VECTORIAL =====\n")

# Crear vector store
create_vector_store(chunks, embeddings)

print("\n===== PROCESO FINALIZADO CORRECTAMENTE =====\n")