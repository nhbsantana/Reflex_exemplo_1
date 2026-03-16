import reflex as rx

class State(rx.State):
    color: str = "blue"

    def flip_color(self):
        self.color = "red" if self.color == "blue" else "blue"


def navbar():
    return rx.flex(
        rx.box(
            rx.image(src="/money.png", width = "50px"),
        ),
        rx.box(
            rx.text("Página de Teste",
                    color_scheme=State.color,
                    # background_color = "white",
                    background_color = rx.cond(State.color == "blue", "lightblue", "lightcoral"),
                    on_click=State.flip_color,
                    _hover={"color": State.color, "background_color": "black"},
                    )
        ),
        rx.box(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Menu"),
                ),
                rx.menu.content(
                    rx.menu.item('Home', on_select=lambda: rx.redirect("/")),
                    rx.menu.item('About', on_select=lambda: rx.redirect("/about"))
                )
            )  
        ),justify="between", align="center", padding="10px", bg="lightgray"
    )