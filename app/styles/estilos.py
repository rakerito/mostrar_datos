import flet as ft

class Colors:
    BG = "#23272f"
    TEXT = "#ffffff"
    PRIMARY = "#00d8ff"
    SECONDARY = "#1e1e1e"
    CARD = "#004CFF"
    BORDER = "#000E77"
    SUCCESS = "#256B19"
    INFO = "#00415A"
    DANGER = "#CA0000"
    WHITE = "#FFFFFF"
    BLACK = "#000000"


class Textos_estilos:
    H4 = ft.TextStyle(
        size=16, 
        weight=ft.FontWeight.BOLD, 
        color="#ffffff"
    )
    
class Cards:
    tarjeta={
        "width": 650,
        "padding": 16,
        "border_radius": 12,
        "bgcolor": Colors.BG,
        "border": ft.Border.all(2, Colors.BORDER)
    }

class Textos:
    H1 = ft.TextStyle(size= 26, height=1.2, weight= ft.FontWeight.W_300, font_family="sans_serif", color = Colors.TEXT)
    H2 = ft.TextStyle(size= 20, height=1.2, weight= ft.FontWeight.W_300, font_family="sans_serif", color = Colors.TEXT)
    H3 = ft.TextStyle(size= 14, height=1.2, weight= ft.FontWeight.W_300, font_family="sans_serif", color = Colors.TEXT)
    text = ft.TextStyle(size= 12, height=1.2, weight= ft.FontWeight.W_300, font_family="sans_serif", color = Colors.TEXT)

class Buttons:
    BUTTON_PRIMARY = ft.ButtonStyle(bgcolor=Colors.PRIMARY, color= Colors.WHITE, padding=10, shape=ft.RoundedRectangleBorder(radius=8))
    BUTTON_SUCCESS = ft.ButtonStyle(bgcolor=Colors.SUCCESS, color= Colors.WHITE, padding=10, shape=ft.RoundedRectangleBorder(radius=8))
    BUTTON_DANGER = ft.ButtonStyle(bgcolor=Colors.DANGER, color= Colors.WHITE, padding=10, shape=ft.RoundedRectangleBorder(radius=8))

class Inputs:
    INPUT_PRYMARY={
        "border_color": Colors.BORDER,
        "focused_border_color": Colors.PRIMARY,
        "width": 500,
        "text_style": Textos.text,
        "label_style": Textos.text
    }