from abc import ABC, abstractmethod

class Serializer(ABC):
    
    @abstractmethod
    def to_format(self, person_data: dict) -> str:
        pass

    @abstractmethod
    def from_format(self, file_data: dict) -> list:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass