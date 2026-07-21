"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os
import re

def is_valid_phone(phone:str) -> bool: #remove espaços, hífens e parênteses e chega se sobraram só números
    clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
    #r'..' = raw string (garante que as barras invertidas sejam interpretadas dentro do re), [...] define o conjunto de caracteres lido pela expressão,
    #\s representa espaços em branco, - representa o hífen mesmo, \(\) representa abertura e fechamento de parênteses
    return clean_phone.isdigit() and len(clean_phone) >= 8

def is_valid_email(email: str) -> bool: #valida o formato do email para usuario@dominio.ext
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    #de acordo com a doc de re -> ^ = começo da str, [\w\.-] = 1 ou mais caracts são letra, nums, sublinhados, pontos ou hífens
    #@ é um @ mesmo, [\w\.-]+ domínio, permite letras, nums, pontos e hifens, \. exige um ponto, 
    #\w+ corresponde a uma ou mais letras p/ extensão (.com, .br), $ = fim da str
    return bool(re.match(pattern, email))

FILENAME = "contacts.csv"

#cria arquivo + cabeçalho caso não exista 
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f) #arquivo tipo csv
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    while True: #Valida se nome foi inserido corretamente
       name = input("Name: ").strip().title()
       if name:
           break
       print("Name cannot be empty, try again")

    with open(FILENAME, "r", encoding="utf-8") as f: #lê o arq csv e verifica se o nome está cadastrado desconsiderando maiúsculas
       reader = csv.DictReader(f)
       for row in reader:
           if row["Name"].lower() == name.lower():
               print("Contact name already exists and cannot be added again")
               return #se o contato já existir, a fç é interrompida

#loops que usas as fçs auxiliares do topo p/ validar os dados:
    while True: 
        phone = input("Phone: ").strip()
        if is_valid_phone(phone):
            break
        print("Invalid phone number.")
    while True: 
        email = input("Email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email.")
    #salva os dados já validados (a => append)
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("\nContact successfully added.")

def view_contacts(): #abertura e leitura de todas as linhas do csv
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        #valid que se só há 1 linha (cabeçalho) então não existem contatos cadastrados
        if len(rows) <= 1:
            print("No contacts found")
            return
        
        print("\n Your contacts: \n")

        #print de cada linha, ignorando o cabeçalho que fica fixo
        for row in rows[1:]:
            if len(row) == 3: #a linha tem de ter ao menos 3 colunas pra printar
                print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact(): #solicita um input para busca
    term = input("Enter the contact name you want to search: ").strip().lower()
    found = False #controle

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader: #verifica se o termo digitado está em "Name" e, se sim, muda o valor booleano do controle
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True
    if not found: #se não, segue a vida
        print("No matching contact found")

def main(): #main loop que mantém a interface interativa rodando até o usuário decidir sair na opção 4
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option from 1 to 4: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thank you for using our software")
            break #encerra o loop e o programa
        else:
            print("Invalid choice")

#garante a excução da fç main apenas se executada diretamente pelo usuário
if __name__ == "__main__":
    main()