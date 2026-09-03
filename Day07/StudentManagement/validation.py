def validate_roll_no(roll_no):

    return roll_no.isdigit()


def validate_name(name):

    return name.strip() != ""


def validate_marks(marks):

    return 0 <= marks <= 100