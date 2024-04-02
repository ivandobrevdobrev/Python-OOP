from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student= Student("Ivan")
        self.student_with_courses = Student("Niki", {"math":["a + b = c"]})

    def test_correct_init(self):
        self.assertEqual("Ivan",self.student.name)
        self.assertEqual("Niki", self.student_with_courses.name)
        self.assertEqual({},self.student.courses)
        self.assertEqual({"math":["a + b = c"]}, self.student_with_courses.courses)

    def test_enroll_in_the_same_course_appends_new_notes(self):
        result = self.student_with_courses.enroll("math", ["1+3=4"])
        self.assertEqual("Course already added. Notes have been updated.",result)
        self.assertEqual(["a + b = c","1+3=4"], self.student_with_courses.courses["math"])

    def test_enroll_new_course_without_third_param_adds_notes_to_the_course(self):
        result = self.student.enroll("math",["1+5=6"])
        self.assertEqual("Course and course notes have been added.",result)
        self.assertEqual({"math":["1+5=6"]},self.student.courses)

    def test_enroll_new_course_with_third_param_Y_adds_notes_to_the_course(self):
        result = self.student.enroll("math",["1+5=6"],"Y")
        self.assertEqual("Course and course notes have been added.",result)
        self.assertEqual({"math":["1+5=6"]},self.student.courses)

    def test_enroll_new_course_with_third_param_No_doesnt_add_notes_to_the_course(self):
        result = self.student.enroll("math",["1+5=6"],"No")
        self.assertEqual("Course has been added.",result)
        self.assertEqual([],self.student.courses["math"])

    def test_add_notes_to_existing_course_append_teh_new_notes(self):
        result = self.student_with_courses.add_notes("math","2+8=10")
        self.assertEqual("Notes have been updated",result)
        self.assertEqual(["a + b = c","2+8=10"],self.student_with_courses.courses["math"])

    def test_add_notes_when_course_not_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("python","a+b!=c")
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_course_when_course_not_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("python")
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))

    def test_leave_course_when_course_found_removes_it(self):
        result = self.student_with_courses.leave_course("math")
        self.assertEqual("Course has been removed",result)
        self.assertEqual({},self.student_with_courses.courses)

if __name__ == "__main__":
    main()
