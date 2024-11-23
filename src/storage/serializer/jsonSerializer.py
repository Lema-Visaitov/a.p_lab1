import json
from .serializer import Serializer

class JsonSerializer(Serializer):
    
    def to_format(self, persons: list) -> str:
        persons_data: dict = [person.__dict__() for person in persons]
        return json.dumps(persons_data, ensure_ascii=False, indent=4)

    def from_format(self, file_data: dict) -> any:
        persons_data = json.loads(file_data)    
        return persons_data
    
    def get_type(self) -> str:
        return 'json'