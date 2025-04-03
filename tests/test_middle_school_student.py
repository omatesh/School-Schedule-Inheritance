from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 1 classes: Painting\nEllis receives school transportation"

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 1 classes: Painting\nEllis does not receive school transportation"

def test_new_valid_middle_school_student_nonstr_attribute_classes():
    # Arrange
    name = "Ellis"
    grade = 7
    classes = "yes"

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)

    assert ellis.classes is list
    assert isinstance(ellis.classes, list)



def test_middle_school_student_summary_nonbulean_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation="yes")

    assert isinstance(ellis.gets_transportation, bool)
