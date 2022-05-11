import abc


class IUserChoice(abc.ABC):
    @abc.abstractmethod
    def get_input(self, prompt):
        pass
