class Student:
    def __init__(self):
        self.data = {}

    def set_field(self, key, value):
        self.data[key] = value

    def get_data_tuple(self, telegram_id):
        return (
            telegram_id,
            self.data["last_name"],
            self.data["first_name"],
            self.data["middle_name"],
            self.data["birth_date"],
            self.data["phone"],
            self.data["email"],
            self.data["group_name"],
            self.data["major"],
            self.data["course"],
            self.data["study_form"]
        )
