input.onButtonPressed(Button.A, function () {
    choice = randint(0, text_list.length - 1)
    basic.showString("" + (text_list[choice]))
})
let choice = 0
let text_list: string[] = []
text_list = [
"Yes",
"No",
"Maybe",
"Possible"
]
basic.forever(function () {
	
})
