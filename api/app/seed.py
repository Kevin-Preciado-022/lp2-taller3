"""
Script de carga inicial (seed) de la base de datos.

A diferencia del Taller 2 (que usaba comandos "flask seed-db"), aquí es un
script independiente porque este servicio no usa el CLI de Flask.

Se ejecuta DENTRO del contenedor de la API:

    docker compose exec api python -m app.seed
"""

import json
import os

from .database import Base, SessionLocal, engine
from .models import Categoria, Producto

RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "..", "data", "productos.json")


def cargar_datos():
    # Se asegura de que las tablas existan (por si se corre antes que main.py).
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # TODO 1: Abre RUTA_PRODUCTOS con encoding="utf-8" y usa json.load()
        with open(RUTA_PRODUCTOS, encoding="utf-8") as f:
            datos = json.load(f)

        # TODO 2: Por cada item en 'datos':
        for item in datos:
            # a) Busca la categoría por nombre
            categoria = db.query(Categoria).filter_by(nombre=item["categoria"]).first()

            # b) Si no existe, créala
            if not categoria:
                categoria = Categoria(nombre=item["categoria"])
                db.add(categoria)
                db.flush()

            # c) Si ya existe un producto con ese sku, sáltalo
            if db.query(Producto).filter_by(sku=item["sku"]).first():
                continue

            # d) Crea el Producto
            producto = Producto(
                sku=item["sku"],
                marca=item["marca"],
                nombre=item["nombre"],
                precio=item["precio"],
                foto=item.get("foto"),
                stock=item["stock"],
                activo=item["activo"],
                categoria_id=categoria.id
            )
            db.add(producto)

        # TODO 3: Confirma todo con db.commit()
        db.commit()

        # TODO 4: Imprime cuántos productos se cargaron
        print(f"productos cargados correctamente: {len(datos)}")
    finally:
        db.close()


if __name__ == "__main__":
    cargar_datos()
