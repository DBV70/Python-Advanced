def softuni_students(*args, **kwargs):
    course_students = {}
    invalid_students = set()

    for arg in args:
        course_id, username = arg
        if course_id not in kwargs:
            invalid_students.add(username)
        else:
            course_name = kwargs[course_id]
            course_students[username] = course_name

    sorted_students = sorted(course_students.items())
    result = []

    for student, course_name in sorted_students:
        result.append(f"*** A student with the username {student} has successfully finished the course {course_name}!")

    if invalid_students:
        invalid_message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        result.append(invalid_message)

    return '\n'.join(result)

# Test code
print(softuni_students(
    ('id_7', 'Silvester1'), ('id_32', 'Katq21'), ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',    id_7='Spring Advanced',))