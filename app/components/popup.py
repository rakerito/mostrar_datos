import flet as ft
from app.styles.estilos import Colors, Buttons
import asyncio

async def show_popup(page: ft.Page, title: str, message: str,
                     bgcolor: str = Colors.DANGER, txtcolor: str = Colors.WHITE):
    dlg = ft.AlertDialog(
        title_padding=0,
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title, color=txtcolor, weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(
            padding=10,
            content=ft.Text(message),
        ),
        actions=[ft.Button("OK", on_click=lambda e: _close(page, dlg), style=Buttons.BUTTON_PRIMARY)]
    )
    page.show_dialog(dlg)


def _close(page: ft.Page, dlg):
    dlg.open = False
    page.update()


def close_popup(page: ft.Page, dlg=None):
    target = dlg if dlg is not None else getattr(page, "dialog", None)
    if target is not None:
        target.open = False
    page.update()


async def show_popup_auto_close(page: ft.Page, title: str, message: str,
                                bgcolor: str = Colors.DANGER, txtcolor: str = Colors.WHITE,
                                seconds: int = 3):
    dlg = ft.AlertDialog(
        title_padding=0,
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title, color=txtcolor, weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(padding=10, content=ft.Text(message)),
    )
    page.show_dialog(dlg)
    await asyncio.sleep(seconds)
    _close(page, dlg)


async def show_snackbar(page: ft.Page, title: str, message: str,
                        bgcolor: str = Colors.DANGER, txtcolor: str = Colors.WHITE,
                        seconds: int = 3) -> None:
    # En Flet 0.82 page.snack_bar no funciona, usamos un popup que se cierra solo
    await show_popup_auto_close(page, title, message, bgcolor=bgcolor, txtcolor=txtcolor, seconds=seconds)


async def confirm_dialog(page: ft.Page, title: str, message: str, function_on_yes,
                         bgcolor: str = Colors.DANGER, txtcolor: str = Colors.WHITE):
    dlg = ft.AlertDialog(
        modal=True,
        title_padding=0,
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor, padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title, color=txtcolor, weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(padding=10, content=ft.Text(message)),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: _close(page, dlg)),
            ft.Button("Sí, borrar",   on_click=lambda e: _yes(page, dlg, function_on_yes)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.show_dialog(dlg)


def _yes(page: ft.Page, dlg, function_on_yes):
    _close(page, dlg)
    function_on_yes()