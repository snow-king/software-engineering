import xml.etree.ElementTree as xml
from lxml import etree

from Patient import Patient


class Patient_test(object):
    tests: list

    def __init__(self, path, xsd_path='../src/patients.xsd'):
        self.patient_test_path = path
        self.patients = Patient('../src/patients.xml')
        self.xsd_path = xsd_path

    def createXML(self):
        """
        create XML
        """
        try:
            root = xml.Element("tests")
            tree = xml.ElementTree(root)
            with open(self.patient_test_path, "wb") as fh:
                tree.write(fh)
        except Exception as e:
            print(f" i can't create XMl :  {e}")

    def add_test(self, test_data):
        try:
            tree = xml.parse(self.patient_test_path)
            root = tree.getroot()
            patient = xml.Element("Test")
            root.append(patient)
            id_p = xml.SubElement(patient, "id")
            id_p.text = test_data.get('id_s')
            id_p = xml.SubElement(patient, "id_p")
            id_p.text = test_data.get('id_p')
            first = xml.SubElement(patient, "laboratory_identifier ")
            first.text = test_data.get("laboratory_identifier ")
            date = xml.SubElement(patient, "date")
            date.text = test_data.get("date")
            id_p = xml.SubElement(patient, "type")
            id_p.text = test_data.get('type')
            tree = xml.ElementTree(root)
            with open(self.patient_test_path, "wb") as fh:
                tree.write(fh)
        except Exception as e:
            print(f'Add test error  : {e}')

    def refresh_data(self):
        try:
            tree = xml.ElementTree(file=self.patient_test_path)
            root = tree.getroot()
            appointments = list(root)
            for appointment in appointments:
                appt_children = list(appointment)
                test_p = {}
                for appt_child in appt_children:
                    test_p.update({appt_child.tag: appt_child.text})
                self.tests.append(test_p)
        except Exception as e:
            print(f'refresh data error: {e}')

    def get_test(self, id_p):
        try:
            tree = xml.ElementTree(file=self.patient_test_path)
            root = tree.getroot()
            appointments = list(root)
            for appointment in appointments:
                appt_children = list(appointment)
                if appt_children[0].text == id_p:
                    for appt_child in appt_children:
                        print(f'{appt_child.tag} : {appt_child.text}')
        except Exception as e:
            print(f'get data error: {e}')

    def check_data(self):
        xml_file = etree.parse(self.patient_test_path)
        xml_validator = etree.XMLSchema(file=self.xsd_path)
        return xml_validator.validate(xml_file)


if __name__ == "__main__":
    test = Patient_test("../src/patients.xml")

