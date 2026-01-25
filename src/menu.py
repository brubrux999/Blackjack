class Menu():
    def __init__(self):
        self.show = self.show_menu()

    def show_menu(self):
        return "\n============================\n"\
            "Welcome to Blackjack!! (S17)\n"\
            "============================\n"\
            \
            "\n1) Play\n"\
            "2) View wins\n"\
            "3) Quit\n"