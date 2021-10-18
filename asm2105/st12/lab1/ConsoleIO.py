class ConsoleIO:
    def do_output(self, student_type):
        for key, val in student_type.__dict__.items():
            if key != "_Student__io":
                print(key[10:], val)

    def do_input(self, student_type):
        for key, val in student_type.__dict__.items():
            if key != "_Student__io":
                student_type.__dict__[key] = input(f"{ key[10:] }: ")


class WebIO:
    def do_output(self, student_type):
        pass

    def do_input(self, student_type):
        pass
