"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data(): #coleta os dado no terminal, trata erros de digitação e retorna dicionário nome:nota
    students = {} #dic vazio para começar

    while True: 
        name = input("Enter the student name: ").strip()
        if name.lower() == "done": #encerra a coleta de dados se o usuário digitar done (ignora maiúsculas)
            break
        if not name: #valida entrada vazia
            print("Please type a name")
            continue
        if name in students: #impede duplicatas
            print("Student already exists")
            continue
        while True: #loop interno que garante que as notas sejam válidas pro aluno atual
            try:
                marks = float(input(f"Enter marks for {name}: ")) 
                if marks < 0: #valida a inserção de notas negativas
                    print("Marks can't be negative. Try again.")
                    continue
                break #fim do loop quando a nota válida é inserida
            except ValueError: #valida possibilidade do usuário inserir texto na nota
                print("Please enter a valid number for marks")
        students[name] = marks #salvando a nota no aluno específico

    return students

def display_report(students): #calcula média, maior/menor nota e exibe o relatório
    if not students: #encerra a fç sem erro se o dic estiver vazio
        print("\nNo student data")
        return
    
    marks = list(students.values()) #extrai valores do dic para os cálculos
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    #list comprehensions que identificam os alunos com maior e menor nota
    topper = [name for name, score in students.items() if score == max_score]
    bottom = [name for name, score in students.items() if score == min_score]
    
    #relatório formatado:
    print("\n Students marks report: \n")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"Average marks for students: {average: .2f}") #média com 2 casas decimais
    print(f"Highest marks: {max_score} by {', '.join(topper)}") #join une a lista de nomes por , em caso de empate
    print(f"Lowest marks: {min_score} by {', '.join(bottom)}")
    print("-" * 30)
    print("Detailed Marks: ") #Listagem de cada aluno individualmente com suas notas
    for name, score in students.items():
        print(f" - {name}: {score}")

if __name__ == "__main__": #start do programa
    students = collect_student_data()
    display_report(students)