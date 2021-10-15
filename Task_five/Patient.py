import xml.etree.ElementTree as xml
from lxml import etree


class Patient(object):
    patients: list

    def __init__(self, path, xsd_path='../src/patients.xml'):
        self.patient_card_path = path
        self.xsd_path = xsd_path

    def createXML(self):
        """
        create XML
        """
        root = xml.Element("patients")
        tree = xml.ElementTree(root)
        with open(self.patient_card_path, "wb") as fh:
            tree.write(fh)

    def add_patient(self, patient_data):
        try:
            tree = xml.parse(self.patient_card_path)
            root = tree.getroot()
            patient = xml.Element("Patient")
            root.append(patient)
            id_p = xml.SubElement(patient, "id")
            id_p.text = patient_data.get('id')
            # создаем дочерний суб-элемент.
            first = xml.SubElement(patient, "first_name")
            first.text = patient_data.get("first_name")

            second = xml.SubElement(patient, "last_name")
            second.text = patient_data.get("last_name")

            date = xml.SubElement(patient, "date")
            date.text = patient_data.get("date")
            policy_number = xml.SubElement(patient, "police")
            policy_number.text = patient_data.get("police")
            tree = xml.ElementTree(root)
            with open(self.patient_card_path, "wb") as fh:
                tree.write(fh)
        except Exception as e:
            print(f'Add patient error  : {e}')

    def refresh_data(self):
        try:
            tree = xml.ElementTree(file=self.patient_card_path)
            root = tree.getroot()
            appointments = list(root)
            self.patients = []
            for appointment in appointments:
                appt_children = list(appointment)
                patient = {}
                for appt_child in appt_children:
                    patient.update({appt_child.tag: appt_child.text})
                self.patients.append(patient)
        except Exception as e:
            print(f'refresh data error: {e}')

    def get_patient(self, id_p):
        try:
            tree = xml.ElementTree(file=self.patient_card_path)
            root = tree.getroot()
            appointments = list(root)
            flag = True
            for appointment in appointments:
                appt_children = list(appointment)
                if appt_children[0].text == id_p:
                    flag = False
                    # for appt_child in appt_children:
                    #     print(f'{appt_child.tag} : {appt_child.text}')
            return flag
        except Exception as e:
            print(f'get data error: {e}')

    def check_data(self):
        xml_file = etree.parse(self.patient_card_path)
        xml_validator = etree.XMLSchema(file=self.xsd_path)
        return xml_validator.validate(xml_file)


if __name__ == "__main__":
    # main = {
    #     "id": '1234',
    #     "first_name": "Valery",
    #     "last_name": "Yamato",
    #     "date": "01/01/1999",
    #     "police": "1111111111"
    # }
    test = Patient("../src/patients.xml")
    test.check_data()
    # test.createXML()
    # test.add_patient(main)
    # test.parseXML()
    # test.get_patient('1')
