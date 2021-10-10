class ConsoleIO:
    def do_output(self, employee):
        for key, val in employee.__dict__.items():
            if key != "io":
                print(key, val)

    def do_input(self, employee):
        for key, val in employee.__dict__.items():
            if key != "io":
                employee.__dict__[key] = input(f"{ key }: ")
