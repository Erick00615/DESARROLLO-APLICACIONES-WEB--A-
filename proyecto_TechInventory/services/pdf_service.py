from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from conexion.conexion import obtener_conexion


def generar_pdf_productos(ruta_archivo):

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conn.close()

    doc = SimpleDocTemplate(ruta_archivo)
    elementos = []

    estilos = getSampleStyleSheet()
    titulo = Paragraph("Reporte de Productos - TechInventory", estilos["Title"])
    elementos.append(titulo)

    datos = [["ID", "Nombre", "Cantidad", "Precio"]]

    for p in productos:
        datos.append([p[0], p[1], p[2], p[3]])

    tabla = Table(datos)

    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))

    elementos.append(tabla)

    doc.build(elementos)
    