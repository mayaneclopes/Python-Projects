"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os 
TASK_FILE = "tasks.txt" #constante c/ nome do arquivo a ser gerado

def load_taks():
   #Lê o arqiuvo e reconstroi a lista de tarefas, retorna uma lista em dicionário e tica como feito (bool)
   tasks = []
   if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f: #with open = garante que o arquive feche automatc após leitura
            #encoding UTF-8 salva no padrão de caracteres usado na web, compatível com acentos e símbolos
            for line in f: 
                text, status = line.strip().rsplit("||", 1) 
                #rsplit separa a string a partir da direita (r) apenas na >primeira< aparição de ||
                tasks.append({"text": text, "done": status == "done"}) #adiciona a task no dic, se o status for done -> bool = true
   return tasks

def save_tasks(tasks): #Sobrescreve a lista atual com a atualizada
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done" #converte o bool de volta pra string (done/not done)
            f.write(f"{task['text']}||{status}\n") #escreve no arquivo

def display_tasks(tasks):
    #Exibe as tarefas no terminal com índice numerado e seleção 
    if not tasks:
       print(f"No tasks found")
    else:
        for i, task in enumerate(tasks, 1): #percorre a lista e gera um índice a partir do 1
            checkbox = "✔" if task["done"] else " " #mostra o tique a partir do valor booleano
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager(): #loop no menu e gerenciamento das ações do usuário
    tasks = load_taks() #carrega as tarefas armazenadas quando o programa inicia

    while True: #exibição das opções do menu
        print("\n------Task List Manager--------")
        print("1. Add taks")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option from 1 to 5: ").strip() #pega as respotas do usuário pro menu

        match choice: #gerenciamento das escolhas do menu, levando aos caminhos corretos de acordo com as escolhas do user
            case "1": #add tarefa
                text = input("Enter your task: ").strip()
                if text: #valida se a string está vazia ounão
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks) #salva
                else:
                    print("Task cannot be empty")

            case "2": #visualização das tarefas salvas
                display_tasks(tasks)
            case "3": #ticar tarefa como feita
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks): #validação que garante que o número existe na lista
                        tasks[num-1]["done"] = True #conversão do número inserido para o usuário para index iniciado em 0
                        save_tasks(tasks)
                        print("Task markers as done")
                    else:
                        print("Invalid task number")
                except ValueError: #trata a possibilidade do usuário inserir algo que não seja um número
                    print("Please enter a number")
            case "4": #deleta a tarefa x
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"Task {removed['text']} removed")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5": #fecha o programa
                print("Exiting task manager")
                break
            case _:
                print("Please choose a valid option")

task_manager() #start 