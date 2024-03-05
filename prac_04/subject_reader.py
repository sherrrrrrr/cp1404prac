FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)

    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)

    input_file.close()
    return data


def display_subject_details(data):
    for entry in data:
        subject_code, lecturer, student_count = entry
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


if __name__ == '__main__':
    main()