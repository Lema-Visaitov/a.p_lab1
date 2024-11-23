from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString

from storage.serializer.serializer import Serializer

class XmlSerializer(Serializer):

    def to_format(self, persons_data: dict) -> str:
       root = Element("persons")
       persons_element = SubElement(root, "persons_list")

       for person in persons_data.get("persons", []):
           person_element = SubElement(persons_element, "person")
           for key, value in person.items():
               child = SubElement(person_element, key)
               child.text = str(value)
       
       raw_xml = tostring(root, encoding='unicode')
       
       dom = parseString(raw_xml)
       pretty_xml = dom.toprettyxml(indent="    ")
       return pretty_xml

    def from_format(self, file_data: dict) -> list:
        root = fromstring(file_data)
        persons = []

        for person_element in root.find("persons_list"):
            person_data = {child.tag: child.text for child in person_element}
            person_data["person_id"] = int(person_data["person_id"])
            persons.append(person_data)

        return {"persons": persons}

    def get_type(self) -> str:
        return 'xml'
    
