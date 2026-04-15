from typing import final
import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products, get_product, create_product, update_product, delete_product
from app.components.popup import show_popup, show_popup_auto_close, show_snackbar, confirm_dialog
from app.components.error import ApiError, api_error_to_text
from app.styles.estilos import Colors, Textos, Cards, Buttons, Inputs
from app.views.nuevo_editar import formulario_nuevo_editar_producto #Se agrega la ventana de nuevo/editar

def products_view(page:ft.Page) -> ft.Control:
    ############ Nuevo producto ##############
    #Esta función se ejecuta al hacer click en "Nuevo producto"
    #lo que hace en primer lugar es abrir la ventana para captura de datos
    def inicio_nuevo_producto(_e):
        #Se crea la función para transferir al formulario de nuevo producto
        async def crear_nuevo_producto(data:dict):#Esta función se lleva a la ventana para capturar
            try:
                #Se conecta a transacciones_api_productos.py para crear en la BD un nuevo producto
                create_product(data)
                await show_snackbar(page, "Éxito", "Producto creado.", bgcolor=Colors.SUCCESS)
                await actualizar_data()
            except ApiError as ex:
                await show_popup(page, "Error", api_error_to_text(ex))
            except Exception as ex:
                await show_snackbar(page, "Error", str(ex), bgcolor=Colors.DANGER)

        #Se llama a la función para abrir la ventana y poder capturar los datos,
        # regresa 3 funciones(dlg,open_ y close), se ejecuta open_()
        dlg, open_, close = formulario_nuevo_editar_producto(page, on_submit=crear_nuevo_producto, initial=None)
        open_() #Abre la ventana
    ############ FIN nuevo producto ##############

    ############ Editar producto ##############
    #Esta función se ejecuta al hacer click en el icono "editar"
    # lo que hace en primer lugar es abrir la ventana para modificar los datos del producto
    # Esa nueva ventana ya contendrá los datos listos para ser editados
    def inicio_editar_producto(p:dict[str,Any]):
        async def editar_producto(data:dict):
            try:
                update_product(p["id"], data)
                close()
                await show_snackbar(page,"Éxito","Producto actualizado",bgcolor=Colors.SUCCESS)
                await actualizar_data()
            except ApiError as ex:
                await show_popup(page,"Error",api_error_to_text(ex))
            except Exception as ex:
                await show_snackbar(page,"Error",str(ex),bgcolor=Colors.DANGER)

        dlg, open_, close=formulario_nuevo_editar_producto(page, on_submit=editar_producto, initial=p)
        open_()

    async def borrar_producto(p:dict[str,Any]):
        try:
            delete_product(p["id"])
            await show_snackbar(page,"Éxito","Producto borrado",bgcolor=Colors.SUCCESS)
            await actualizar_data()
        except ApiError as ex:
            await show_popup(page,"Error",api_error_to_text(ex))
        except Exception as ex:
            await show_snackbar(page, "Error",str(ex), bgcolor=Colors.DANGER)
    
    def inicio_borrar_producto(p:dict[str,Any]):
        async def tarea():
            await borrar_producto(p)
        page.run_task(tarea)



    btn_nuevo = ft.Button("Nuevo producto",icon=ft.Icons.ADD,on_click=inicio_nuevo_producto)

    rows_data:list[dict[str, Any]] = []
    total_items = 0
    total_text = ft.Text("Total de productos: (cargando...)", style=Textos.text)
    columnas=[
    ft.DataColumn(ft.Text("Nombre", style=Textos.text)),
    ft.DataColumn(ft.Text("Cantidad", style=Textos.text)),
    ft.DataColumn(ft.Text("Ingreso", style=Textos.text)),
    ft.DataColumn(ft.Text("Min", style=Textos.text)),
    ft.DataColumn(ft.Text("Max", style=Textos.text)),
    ft.DataColumn(ft.Text("Acciones", style=Textos.text)), # Cambiado de "Editar" a "Acciones"
]

    #Se definen las filas de la tabla
    #Cada data.append agrega una fila
    data=[]
    data.append(
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("nombre1...")),
                ft.DataCell(ft.Text("cantidad1...")),
                ft.DataCell(ft.Text("ingreso1...")),
                ft.DataCell(ft.Text("min1...")),
                ft.DataCell(ft.Text("max1...")),
                #### Se agrega para editar producto ###
                ft.DataCell(ft.Text("..."))
            ]
        )
    )
    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48,
    )

    #return tabla

    async def actualizar_data():
        nonlocal rows_data, total_items
        try:
            data = list_products(limit=500, offset=0)
            total_items = int(data.get("total", 0))
            total_text.value = "Total de productos: "+str(total_items)
            rows_data=data.get("items", [])
            actualizar_filas()
        except Exception as e:
            print(e)
            await show_snackbar(page, "Error", str(e),bgcolor=Colors.DANGER)

    def actualizar_filas():
        nuevas_filas = []
        #Toda la tabla de la BD está en rows_data
        #De rows_data se deposita cada registro en p
        for p in rows_data:
            #Cada registro se agrega al final de la lista
            nuevas_filas.append(
                #Se crea una fila de flet
                ft.DataRow(
                    #A la fila se le agregan celdas
                    cells=[
                        #A cada celda se le agrega la información de la BD (p)
                        ft.DataCell(ft.Text(p.get("name", ""))),
                        ft.DataCell(ft.Text(str(p.get("quantity", "")))),
                        ft.DataCell(ft.Text(p.get("ingreso_date", "") or "")),
                        ft.DataCell(ft.Text(str(p.get("min_stock", "")))),
                        ft.DataCell(ft.Text(str(p.get("max_stock", "")))),
                        #### Se agrega para editar producto ###
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.Icons.EDIT, tooltip="Editar", on_click=lambda e, p=p: inicio_editar_producto(p)),
                                    ft.IconButton(icon=ft.Icons.DELETE, tooltip="Borrar", on_click=lambda e, p=p: inicio_borrar_producto(p)),
                                ]
                            )
                        )
                    ]
                )
            )

        #A la tabla de flet se le agrega toda la lista nuevas_filas
        tabla.rows = nuevas_filas
        #El agregar esas filas a la tabla, no actualiza la vista, es necesario actualizar
        page.update()

    page.run_task(actualizar_data)

    contenido = ft.Column(
        spacing=30,
        scroll=ft.ScrollMode.AUTO,
        controls=[btn_nuevo,total_text,ft.Container(content=tabla)]
    )

    tarjeta = ft.Container(content=contenido, **Cards.tarjeta)

    final = ft.Container(expand=True, alignment=ft.Alignment(0,-1),content=tarjeta)
        
    return final