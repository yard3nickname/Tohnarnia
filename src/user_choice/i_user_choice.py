import abc


class IUserChoice(abc.ABC):
    @abc.abstractmethod
    def get_choice(self, prompt):
        pass
