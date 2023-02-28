from Omamodul import *   

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
