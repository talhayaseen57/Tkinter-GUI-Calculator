import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("363x497")
        self.window.resizable(False, False)
        self.window.title("Calculator App")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
