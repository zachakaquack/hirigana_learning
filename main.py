import customtkinter as ctk
import answers
import random


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#b2b2b2")

        # settings
        self.geometry("1280x720")
        self.title("Hirigana shit")
        self.resizable(False, False)
        self.bind("<Escape>", lambda event: self.quit())

        # fonts
        big_font = ctk.CTkFont("Calibri Bold", 80, weight="bold")
        small_font = ctk.CTkFont("Calibri Bold", 60, weight="bold")
        smaller_font = ctk.CTkFont("Calibri Bold", 30, weight="bold")

        # grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1), weight=1, uniform="a")

        # variables
        self.previous_answer = ctk.StringVar(value="1")
        self.current_answer = ctk.StringVar(value="2")
        self.next_answer = ctk.StringVar(value="3")

        # objects
        self.previous = ctk.CTkLabel(self, textvariable=self.previous_answer, font=small_font)
        self.current = ctk.CTkLabel(self, textvariable=self.current_answer, font=big_font)
        self.next = ctk.CTkLabel(self, textvariable=self.next_answer, font=small_font)

        # entry
        self.answer_entry = ctk.CTkEntry(self,
                                         width=350, height=80,
                                         justify="center",
                                         font=smaller_font)

        # button
        self.submit_button = ctk.CTkButton(self,
                                           width=250, height=80,
                                           text="Submit",
                                           command=self.check_values)

        # init
        self.previous.grid(column=0, row=0, sticky="nsew")
        self.current.grid(column=1, row=0, sticky="nsew")
        self.next.grid(column=2, row=0, sticky="nsew")
        self.answer_entry.grid(row=1, column=1)
        self.submit_button.grid(row=1, column=2)

        self.set_init_values()

        self.mainloop()

    def set_init_values(self):
        self.previous_answer.set("")
        self.current_answer.set(random.choice(list(answers.hiri.values())))
        self.next_answer.set(random.choice(list(answers.hiri.values())))

    def check_values(self):
        given_answer = self.answer_entry.get()
        try:
            if answers.hiri[given_answer] == self.current_answer.get():
                self.previous_answer.set(self.current_answer.get())
                self.current_answer.set(self.next_answer.get())
                self.next_answer.set(random.choice(list(answers.hiri.values())))
        except KeyError:
            pass
App()
