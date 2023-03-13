from groupmates import groupmates

def filter_marks(average_rating):
    print(u'Имя'.ljust(15), u'Фамилия'.ljust(20), u'Средний балл')
    for student in groupmates:
        if sum(student['marks']) / len(student['marks']) > average_rating:
            print(student['name'].ljust(15), student['surname'].ljust(20), int(sum(student['marks']) / len(student['marks'])))

average_rating = int(input("Введите средний балл: "))
if __name__ == '__main__':
    filter_marks(average_rating)

