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


from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    # Assert
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
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Assert
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
    
    #Act
    summary_for_ellis = ellis.summary()
    summary_w_transportation_for_ellis = ellis.display_transportation_message()

    #Assert
    assert summary_w_transportation_for_ellis
    assert summary_w_transportation_for_ellis == "Ellis receives school transportation"
    assert "Painting" in summary_for_ellis
    assert "junior" in summary_for_ellis
    assert "Ellis" in summary_for_ellis

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = MiddleSchoolStudent(name, grade, classes)

    #Act
    summary_for_ellis = ellis.summary()
    summary_w_transportation_for_ellis = ellis.display_transportation_message()

    #Assert
    assert not ellis.gets_transportation
    assert summary_w_transportation_for_ellis == "Ellis doesn't receive school transportation"
    assert "Painting" in summary_for_ellis
    assert "junior" in summary_for_ellis
    assert "Ellis" in summary_for_ellis
    
def test_middle_school_student_empty_name_w_summary():
    # Arrange
    name = ""
    grade = "junior"
    classes = ["Painting"]

    # Act
    student = MiddleSchoolStudent(name, grade, classes)
    summary_for_student = student.summary()
    summary_w_transportation_for_student = student.display_transportation_message()

    # Assert
    assert student.name == ""
    assert not student.gets_transportation
    assert summary_w_transportation_for_student == " doesn't receive school transportation"