import tkinter as tk

class Calculator(tk.Tk):
    #main class for creating the calculator app
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=0, bg="#eee", justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self, bg="grey")
        btns_frame.pack()

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', ' ',
            '1', '2', '3', '-', ' ',
            '0', '.', '=', '+', ' '
        ]

        row = 0
        col = 0
        for btn in buttons:
            if btn != ' ':
                button = tk.Button(btns_frame, text=btn, font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                                   command=lambda x=btn: self.button_click(x))
                button.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def button_click(self, item):
        if item == "C":
            self.expression = ""
            self.input_text.set("")
        elif item == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()