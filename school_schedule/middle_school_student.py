from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = False):
        super().__init__(name, grade, classes)
        if not isinstance(gets_transportation, bool):
            raise AssertionError("You've done a mistake")
        self.gets_transportation = gets_transportation

    def transportation_message(self):
        gets_message = "receives" if self.gets_transportation else "does not receive"

        return f"{self.name} {gets_message} school transportation"
    
    def summary(self):
        student_summary = super().summary()
        transportation_status = self.transportation_message()
        
        return "\n".join([student_summary, transportation_status])