import flet as ft

class Colors:
    BG = "#23272f"
    TEXT = "#ffffff"
    PRIMARY = "#00d8ff"
    SECONDARY = "#1e1e1e"

class Textos_estilos:
    H4 = ft.TextStyle(
        size=16, 
        weight=ft.FontWeight.BOLD, 
        color="#ffffff"
    )

class Card(ft.Container):
    def __init__(self, content):
        super().__init__(
            content=content,
            padding=20,
            bgcolor=Colors.SECONDARY,
            border_radius=10,
            border=ft.border.all(1, "#3f4248")
        )