import re
class Gender():
    male_names = []

    @staticmethod
    def load_names():
        f = open("shared/names/men.names", "r", encoding="utf8")
        for row in f:
            row = row.strip("\n")
            row = row.lower()
            Gender.male_names.append(row)
        Gender.male_names = set(Gender.male_names)
        print(Gender.male_names)

    @staticmethod
    def find_gender(name):
        firstname = re.search(r"(?P<name>^\w+)", name.lower(), re.UNICODE | re.IGNORECASE)
        if firstname.group("name") in Gender.male_names:
            return "Male"
        else:
            return "Female"