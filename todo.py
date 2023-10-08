import flet as ft

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.window_resizeble = False
        self.page.window_always_on_top = True
        self.page.title = "ToDo App"
        self.main_page()

    def main_page(self):
        input_task = ft.TextField(hint_text="Digite aqui uma tarefa")
        input_bar = ft.Row(
            controls=[
            input_task,
            ft.FloatingActionButton(icon=ft.icons.ADD)
            ]
        )
        self.page.add(input_bar)

ft.app(target=ToDo)