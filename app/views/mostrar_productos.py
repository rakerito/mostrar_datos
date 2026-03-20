import flet as ft
from app.services.transacciones_api_productos import list_products
from app.styles.estilos import Colors, Textos_estilos

def products_view(page: ft.Page) -> ft.Control:
    total_text = ft.Text("Total de productos: (cargando...)", style=Textos_estilos.H4)

    productos = list_products()

   
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    data = []

    for p in productos:
        data.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(p["name"])),
                    ft.DataCell(ft.Text("0")),  # 👈 valor simulado
                    ft.DataCell(ft.Text(str(p["price"]))),  # usamos price como ingreso
                    ft.DataCell(ft.Text("0")),  # 👈 simulado
                    ft.DataCell(ft.Text("0")),  # 👈 simulado
                ]
            )
        )

    

    total_text = ft.Container(
    content=ft.Text(f"Total de productos: {len(productos)} ", style=Textos_estilos.H4),
    bgcolor="blue",  
    padding=10,
    border_radius=10
)

    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48
    )

    
    contenido = ft.Column(
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        height=400,
        controls=[
            total_text,
            tabla
        ]
    )

    return contenido