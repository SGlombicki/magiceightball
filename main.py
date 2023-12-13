def on_button_pressed_a():
    global choice
    choice = randint(0, len(text_list) - 1)
    basic.show_string("" + (text_list[choice]))
input.on_button_pressed(Button.A, on_button_pressed_a)

choice = 0
text_list: List[str] = []
text_list = ["Yes", "No", "Maybe", "Possible"]

def on_forever():
    pass
basic.forever(on_forever)
