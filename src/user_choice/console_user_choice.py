from .i_user_choice import IUserChoice


class ConsoleUserChoice(IUserChoice):
    def get_input(self, prompt):
        return input(prompt)
