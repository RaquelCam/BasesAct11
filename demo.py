from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Cargar credenciales desde .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def insertar_tarea(titulo):
    res = supabase.table("tasks").insert({"title": titulo, "done": False}).execute()
    print("✅ Tarea insertada:", res.data)

def listar_tareas():
    res = supabase.table("tasks").select("*").execute()
    print("📋 Lista de tareas:")
    for t in res.data:
        estado = "✔️" if t["done"] else "❌"
        print(f"{t['id']}: {t['title']} {estado}")

if __name__ == "__main__":
    print("=== DEMO SUPABASE + PYTHON (Docker) ===")
    insertar_tarea("Tarea desde contenedor Docker")
    listar_tareas()
