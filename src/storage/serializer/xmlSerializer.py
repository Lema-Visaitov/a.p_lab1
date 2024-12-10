from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString

from storage.serializer.serializer import Serializer

class XmlSerializer(Serializer):

    def to_format(self, persons: dict) -> str:
        root = Element("Persons") 
        for person in persons: 
            person_element = Element(person.__class__.__name__)
            for key, value in person.__dict__().items():
               element = SubElement(person_element, key)
               element.text = value

            root.append(person_element) 
        raw_xml = tostring(root, encoding='unicode') 
 
        dom = parseString(raw_xml) 
        pretty_xml = dom.toprettyxml(indent = "     ") 
        return pretty_xml 

    def from_format(self, data: dict) -> list:
        root = fromstring(data)
        persons = []

        for person_element in root.find("persons_list"):
            person_data = {child.tag: child.text for child in person_element}
            person_data["person_id"] = int(person_data["person_id"])
            persons.append(person_data)

        return persons
        # root = fromstring(data)
        # persons = []
        # for person_element in root:
        #     person_type = person_element.tag
        #     name = person_element.find('name').text
        #     duration = int(person_element.find('duration').text)
        #     year = int(person_element.find("year").text)

        #     person_data = {
        #         "type": person_type,
        #         "name": name,
        #         "duration": duration,
        #         "year": year
        #     }
        #     persons.append(person_data)
        # return persons

    def get_type(self) -> str:
        return 'xml'
    
