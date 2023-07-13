import tkinter as tk
import json


class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")

        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self, text="", width=50)
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_var.set("0")

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self, text="", variable=self.radio_var, value=str(i))
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["Question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data["Options"][i])

            self.submit_button.config(state=tk.NORMAL)
        else:
            self.show_result()

    def check_answer(self):
        selected_option = int(self.radio_var.get())
        correct_option = int(self.questions[self.current_question]["Answer"])

        if selected_option == correct_option:
            self.score += 1

        self.current_question += 1
        self.next_question()

    def show_result(self):
        self.question_label.config(text=f"Quiz Complete!\nYour Score: {self.score}/{len(self.questions)}")
        self.submit_button.config(state=tk.DISABLED)


# Define the quiz questions

# read file
myJsonFile = open('KBCquestions.json', 'r')
jsonData = myJsonFile.read()

# Parse
questions = json.loads(jsonData)



# Create the quiz application
app = QuizApp(questions)
app.mainloop()
