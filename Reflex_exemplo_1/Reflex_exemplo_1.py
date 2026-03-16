# """Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.navbar import navbar

# from rxconfig import config


# class State(rx.State):
#     """The app state."""


# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#     )


# app = rx.App()
# app.add_page(index)

def index():
    # return rx.text("Hello, World!",font_size="20px", color="blue", bg="yellow", padding="10px", border_radius="5px",_hover={"color": "red", "bg": "lightgray"})
    return rx.container(
        navbar()
    )

def about():
    return rx.text("This is the about page.", font_size="20px", color="green", bg="lightyellow", padding="10px", border_radius="5px", _hover={"color": "darkgreen", "bg": "lightgray"})


app = rx.App()
app.add_page(index)
app.add_page(about, route="/about")