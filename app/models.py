from patterns.prototypes import PrototypeMixin


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Course(PrototypeMixin):
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        super().__init__()


class WebConference(Course):
    pass


class RecordCourse(Course):
    pass


class CourseFactory:
    types = {
        'webconf': WebConference,
        'offline': RecordCourse,
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class LearnSite:
    def __init__(self):
        self.courses = []
        self.categories = []
        self.students = []

    def create_category(self, name, category=None):
        return Category(name, category)

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')


class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Student(User):
    def __init__(self, name, lastname, age, email):
        self.age = age
        self.email = email
        self.courses = []
        super().__init__(name, lastname)
