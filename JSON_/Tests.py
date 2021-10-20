import json
import jsonschema


class Patient_test(object):
    schema: str
    json: str

    def __init__(self, path, xsd_path='../src/test_schema.json'):
        self.patient_test_path = path
        self.schema_path = xsd_path

    def generate_json(self, data):
        with open(self.patient_test_path, "wb") as write_file:
            json.dump(data, write_file)

    def load_schema(self):
        with open(self.schema_path, 'r') as file:
            self.schema = json.load(file)

    def load_json(self):
        with open(self.patient_test_path, 'r') as file:
            self.json = json.load(file)

    def check_json(self):
        self.load_json()
        self.load_schema()
        try:
            jsonschema.validate(instance=self.schema, schema=self.json)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"
            return False, err

        message = "Given JSON data is Valid"
        return True, message


if __name__ == "__main__":
    test = Patient_test("../src/tests.json", "../src/test_schema.json")
    print(test.check_json())
