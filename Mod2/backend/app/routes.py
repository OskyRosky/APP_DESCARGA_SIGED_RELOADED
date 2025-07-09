from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
from app.DESCARGA_SIGED import descargar_documentos

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/descargar")
async def descargar_archivos(req: URLRequest):
    print(f"➡️ URL recibida: {req.url}")

    # Validación adicional del backend
    if not req.url.lower().startswith("http"):
        raise HTTPException(status_code=400, detail="URL inválida: debe comenzar con http o https")

    # Ejecutar descarga en segundo plano (ahora sin ruta explícita)
    asyncio.create_task(descargar_documentos(req.url))

    return {
        "status": "🟡 Descarga en curso",
        "mensaje": "Los archivos se guardarán en la carpeta 'SIGED_DOCUMENTOS' dentro de tu carpeta Descargas",
        "url": req.url
    }