from fastapi import APIRouter, Response
import segno
from io import BytesIO

router = APIRouter(prefix="/qr")
""" 
@router.get("/download")
def download_qr(url: str, format: str = "png"):
    qr = segno.make(url)
    buffer = BytesIO()

    format = format.lower()

    if format == "png":
        qr.save(buffer, kind="png")
        media_type = "image/png"
        filename = "qr.png"

    elif format == "svg":
        qr.save(buffer, kind="svg")
        media_type = "image/svg+xml"
        filename = "qr.svg"

    elif format == "eps":
        qr.save(buffer, kind="eps")
        media_type = "application/postscript"
        filename = "qr.eps"

    else:
        return {"error": "Formato no soportado. Usa png, svg o eps."}

    return Response(
        content=buffer.getvalue(),
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    ) """


@router.get("/download")
def download_qr(url: str, format: str ="png", size: str = "medium"):
    qr = segno.make(url)
    buffer = BytesIO()

    format = format.lower()

    # sizes
    pixel_sizes = {
        "small": 200,
        "medium": 400,
        "large": 800,
        "xl": 1200
    }

    # if user want something rare -> use "medium"
    px = pixel_sizes.get(size, 400)

    if format == "png":
        # segno doesn't allow direct px sizes, only scales / final size ≈ modules * scale / QR module min = 29 modules
        scale = max(1, px // 29)

        qr.save(buffer, kind="png", scale=scale)
        media_type = "image/png"
        filename = f"qr_{px}px.png"
    
    elif format == "svg":
        qr.save(buffer, kind="svg")
        media_type = "image/svg+xml"
        filename = "qr.svg"
    
    elif format == "eps":
        qr.save(buffer, kind="eps")
        media_type = "application/postscript"
        filename = "qr_eps"
    
    else:
        return{"ERROR": "Unsupported Format"}
    
    return Response(
        content=buffer.getvalue(),
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )



@router.get("/preview")
def preview_qr(url: str, format: str = "png", size: str = "medium"):
    qr = segno.make(url)
    buffer = BytesIO()

    # preview in PNG
    qr.save(buffer, kind="png", scale=8) #400px aprox

    return Response(
        content=buffer.getvalue(),
        media_type="image/png"
    )