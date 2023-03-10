import tkinter as tk
import Functions as f

"""----------------------------------------------------------CONSTANTS----------------------------------------"""
WINDOW_SIZE = '375x667'
APP_NAME = 'PROIECTON'

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#ffffff"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#f5f5f5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(WINDOW_SIZE)  # size of the window
        self.window.resizable(0, 0)  # disabling resizing the window
        self.window.title(APP_NAME)  # title of the window

        self.total_expression = ""  # the upper label
        self.current_expression = ""  # what's writen in the main label after taking actions
        self.label = ""  # the main label
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operations = {  # \u.. = unidecode
            "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+",
        }

        self.var_x = ''

        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)

        for i in range(1, 5):  # setting the number of row and col so the buttons fill the window
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)
        self.buttons_frame.columnconfigure(5, weight=1)

        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.bind_keys()

    # ======================================================== INITIATIONS STUFF ==============================

    #           ------------------------------------- FRAMES -----------------------------
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)  # bg = background color

        # expand − When set to true, widget expands to fill any space not otherwise used in widget's parent. fill −
        # Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal
        # dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both-
        #                       -horizontally and vertically).
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    #           ------------------------------------- FRAMES -----------------------------

    #           ------------------------------------- CREATING ---------------------------
    def bind_keys(self):
        """
        binding the equals(enter) and numbers in self.digits and the operator in self. operations to their
        corresponding keyboard
        """

        self.window.bind("<Return>", lambda event: self.evaluate_bar())  # lambda event: self.evaluate()
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_display_label(self):
        """
        creating the upper(total_expression) and main(label) labels
        :return: total_label, label
        """
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,
                               font=SMALL_FONT_STYLE)  # anchor=tk.E(= east) # fg color for text
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,
                         font=LARGE_FONT_STYLE)  # anchor=tk.E(= east) # fg color for text
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_special_buttons(self):

        # TODO: add the functions and bracers fetchers
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

        self.create_set_var_x_button()
        self.create_use_var_x_button()

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():  # digits={key:items}
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE, borderwidth=0,
                               command=lambda value=digit: self.add_to_expression(value))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        current_row = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda value=operator: self.append_operator(value))
            button.grid(row=current_row, column=4, sticky=tk.NSEW)
            current_row += 1

    #           ------------------------------------- CREATING ---------------------------

    #           ---------------------------------- SPECIAL BUTTONS------------------------
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=1, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, columnspan=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, columnspan=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate_bar)  # command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_set_var_x_button(self):
        button = tk.Button(self.buttons_frame, text='=>X', bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.set_var_x)
        button.grid(row=1, column=5, columnspan=1, sticky=tk.NSEW)

    def create_use_var_x_button(self):
        button = tk.Button(self.buttons_frame, text='X', bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.use_var_x)
        button.grid(row=2, column=5, columnspan=1, sticky=tk.NSEW)

    #           ---------------------------------- SPECIAL BUTTONS------------------------

    # ======================================================== INITIATIONS STUFF ==============================

    # ======================================================== ACTIVE STUFF ===================================

    #           ---------------------------------- LABELS STUFF------------------------
    def add_to_expression(self, value):
        """
        adding value to the lower label (current_expression)
        :param value: numbers
        """
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        """
        adding operator to current_expression then move all the numbers to the upper label (total_label) and give a clean slide
        :param operator: operator
        """
        # TODO: check that we don't add two operator together
        #       check that we don't add an operator without numbers first
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f"{symbol}")  # change the display from * to x ...
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])  # limited to the 11 first character

    #           ---------------------------------- LABELS STUFF------------------------

    #           ---------------------------------- MATH STUFF------------------------
    def evaluate(self):  # TODO: need to clean after the Error
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))  # replace it with bar proj

            self.total_expression = ""
        except Exception as e:
            print(type(e))
            self.current_expression = "Error"
        finally:
            self.update_label()

    def evaluate_bar(self):  # TODO: need to clean after the Error
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            # tb.eval(self.total_expression)
            self.current_expression = str(eval(self.total_expression))  # TODO: replace it with bar proj
            self.total_expression = ""

        except Exception as e:
            print(type(e))
            self.current_expression = "Error"
        finally:
            self.update_label()

    def square(self):
        self.current_expression = str(f.exponent(self.current_expression, '2'))
        self.update_label()

    def sqrt(self):  # square ROOT
        # print(self.current_expression)
        self.current_expression = str(f.root(self.current_expression))
        self.update_label()

    def set_var_x(self):
        """
        called when the set_var_x button is pressed,
        and we move the value in the lower label(current_expression) into the x variable(var_x)
        :return:
        """
        self.var_x = self.current_expression
        self.current_expression = ''
        self.update_label()

    def use_var_x(self):
        """
        called when the use_var_x button is pressed,
        and we move the value in the x variable(var_x) into the lower label(current_expression)
        :return:
        """
        self.current_expression += self.var_x
        self.update_label()

    #           ---------------------------------- MATH STUFF------------------------

    def run(self):
        self.window.mainloop()
    # ======================================================== ACTIVE STUFF ===================================


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
