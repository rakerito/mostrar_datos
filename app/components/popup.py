import flet as ft

def show_snackbar(page: ft.Page, message: str, color: str = "white"):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(message, color=color),
        action="OK"
    )
    page.snack_bar.open = True
    page.update()

def show_popup(page: ft.Page, title: str, content: str):
    def close_dlg(e):
        dlg.open = False
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text(title),
        content=ft.Text(content),
        actions=[ft.TextButton("Cerrar", on_click=close_dlg)],
    )
    page.dialog = dlg
    dlg.open = True
    page.update()

def show_popup_auto_close(page: ft.Page, title: str, content: str):
    # Versión simplificada para cumplir con la importación
    show_popup(page, title, content)

def confirm_dialog(page: ft.Page, title: str, message: str, on_confirm):
    def handle_confirm(e):
        dlg.open = False
        page.update()
        on_confirm()

    def handle_cancel(e):
        dlg.open = False
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton("Sí", on_click=handle_confirm),
            ft.TextButton("No", on_click=handle_cancel),
        ],
    )
    page.dialog = dlg
    dlg.open = True
    page.update()