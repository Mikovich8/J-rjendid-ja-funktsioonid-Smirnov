def input_applicants(n):
    applicants = []
    scores = []
    for i in range(n):
        print("Введите данные о соискателе", i+1)
        applicant = input("ФИО: ")
        score = float(input("Баллы: "))
        applicants.append(applicant)
        scores.append(score)
    return applicants, scores

def print_admitted(applicants):
    print("Список соискателей, поступивших в университет:")
    for applicant in applicants:
        print(applicant)

def print_sorted(applicants, scores):
    print("Список соискателей и их баллов в алфавитном порядке:")
    sorted_applicants = sorted(zip(applicants, scores))
    for applicant, score in sorted_applicants:
        print(applicant, score)

def print_worst(applicants, scores, num_worst):
    worst_scores = sorted(scores)[:num_worst]
    worst_applicants = [applicants[i] for i in range(len(applicants)) if scores[i] in worst_scores]
    print(f"Список {num_worst} соискателей с худшими результатами:")
    for applicant in worst_applicants:
        print(applicant)

def print_average(scores):
    avg_score = sum(scores) / len(scores)
    print(f"Средний балл соискателей: {avg_score}")

def delete_applicant(applicants, scores):
    print("Введите ФИО удаляемого соискателя:")
    name = input()
    if name in applicants:
        index = applicants.index(name)
        applicants.pop(index)
        scores.pop(index)
        print(f"Соискатель {name} успешно удален")
    else:
        print("Соискатель не найден")

def sisseastumine():
    n = int(input("Введите количество соискателей: "))
    applicants, scores = input_applicants(n)
    while True:
        print("\nВыберите действие:")
        print("1. Список соискателей, поступивших в университет")
        print("2. Список соискателей и их баллов в алфавитном порядке")
        print("3. Найти n соискателей с худшими результатами")
        print("4. Найти средний балл соискателей")
        print("5. Удалить из списка соискателя")
        print("0. Выход")
        choice = int(input("Ваш выбор: "))
        if choice == 0:
            break
        elif choice == 1:
            print_admitted(applicants)
        elif choice == 2:
            print_sorted(applicants, scores)
        elif choice == 3:
            num_worst = int(input("Введите количество соискателей с худшими результатами: "))
            print_worst(applicants, scores, num_worst)
        elif choice == 4:
            print_average(scores)
        elif choice == 5:
            delete_applicant(applicants, scores)
