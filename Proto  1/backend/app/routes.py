from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
from app.DESCARGA_SIGED import descargar_documentos

router = APIRouter()

# Ruta donde se guardarán los archivos descargados
RUTA_DESCARGA = "/Users/sultan/Downloads/siged_descargas"

class URLRequest(BaseModel):
    url: str

@router.post("/descargar")
async def descargar_archivos(req: URLRequest):
    print(f"➡️ URL recibida: {req.url}")

    # Validación adicional del backend
    if not req.url.lower().startswith("http"):
        raise HTTPException(status_code=400, detail="URL inválida: debe comenzar con http o https")

    # Ejecutar descarga en segundo plano
    asyncio.create_task(descargar_documentos(req.url, RUTA_DESCARGA))

    return {"status": "🟡 Descarga en curso", "url": req.url}