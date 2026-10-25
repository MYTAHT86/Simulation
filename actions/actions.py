from abc import ABC, abstractmethod


class Actions(ABC):
    @staticmethod
    @abstractmethod
    def activate() -> None:
        pass