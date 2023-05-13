import enum

class Role(enum.IntEnum):
    teacher = 1
    student = 2

class ContentType(enum.IntEnum):
    lesson = 1
    quiz = 2
    assignment = 3