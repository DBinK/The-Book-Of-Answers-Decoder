'''
Author: DBinK dbinkv1@gmail.com
Date: 2023-08-31 10:40:38
LastEditors: DBinK dbinkv1@gmail.com
LastEditTime: 2023-09-02 01:09:51
FilePath: /The-Book-of-Answers-Interpreter/The_Book_of_Answers_Interpreter/The_Book_of_Answers_Interpreter.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#from rxconfig import config
import reflex as rx


class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.fragment(

        rx.vstack(
            rx.heading("欢迎使用《答案之书》", font_size="2em"),
            rx.text("1. 花10到15秒的时间专注于你的问题。问题应该是封闭式的，例如：“我申请的工作适合我吗？”或者“这个周末我应该去旅行吗？”"),
            rx.text("2. 当你感觉时机成熟时，点击获取答案，那里将会有你的答案。"),
            rx.text("3. 对于所有问题都重复这个过程。"),
            rx.button(
                "获取答案",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
                #on_click=
            ),
            rx.button("Example", color_scheme="red", size="lg"),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
        
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
