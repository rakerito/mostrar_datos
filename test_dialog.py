import flet as ft

def main(page: ft.Page):
    page.title = "Test Dialog"

    # List all dialog-related methods on page
    dialog_methods = [m for m in dir(page) if 'dialog' in m.lower() or 'overlay' in m.lower() or 'snack' in m.lower()]
    print("Dialog-related methods/attrs:", dialog_methods)
    
    dlg = ft.AlertDialog(
        title=ft.Text("Test Dialog"),
        content=ft.Text("This is a test"),
        actions=[
            ft.TextButton("Close", on_click=lambda e: close_dlg()),
        ],
    )

    def close_dlg():
        dlg.open = False
        page.update()
        print("Dialog closed via dlg.open = False")

    def open_dlg(e):
        print("Opening dialog...")
        try:
            page.show_dialog(dlg)
            print("page.show_dialog() worked!")
        except Exception as ex:
            print(f"show_dialog failed: {ex}")
            try:
                page.dialog = dlg
                dlg.open = True
                page.update()
                print("page.dialog assignment worked!")
            except Exception as ex2:
                print(f"page.dialog assignment failed: {ex2}")

    def show_snack(e):
        print("Showing snackbar...")
        try:
            page.snack_bar = ft.SnackBar(content=ft.Text("Test snackbar!"), bgcolor="green")
            page.snack_bar.open = True
            page.update()
            print("Snackbar shown!")
        except Exception as ex:
            print(f"Snackbar failed: {ex}")

    page.add(
        ft.ElevatedButton("Open Dialog", on_click=open_dlg),
        ft.ElevatedButton("Show Snackbar", on_click=show_snack),
    )

ft.app(target=main)
