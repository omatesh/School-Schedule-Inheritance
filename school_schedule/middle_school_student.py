from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes,
        gets_transportation=False):

        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
        # self.clubs = clubs if clubs is not None else []

    # def join_club(self, club_name):
    #     self.clubs.append(club_name)

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()
        # club_message = self.display_clubs()

        return "\n".join((student_summary, transportation_message))

    def display_transpartation_message(self):
        receives_transp_message = "receives" if self.gets_transportation else "doesn't receive"
        return f"{self.name} {receives_transp_message} school transportation"

    # def display_clubs(self):
    #     club_str = ", ".join(self.clubs)

        # if club_str:
        #     return f"{self.name} is a member of: {club_str}"
    
        # return f"{self.name} hasn't joined a club yet."
