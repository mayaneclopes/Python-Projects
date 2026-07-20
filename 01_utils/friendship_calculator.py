"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    #ajuste para que nomes iguais deem 100% autom 
    if name1 == name2:
        return 100
    score = 0

    #letrais iguais por intersec de conjuntos
    shared_letters = set(name1) & set(name2)
    score += len(shared_letters) * 5 #letras em comum pontuam + 5
    #vogais presentes nos 2 nomes
    vowels = set('aeiou')
    score += len(vowels & shared_letters) * 10 #+10 pontos por vogal igual

    #compara as letras em cada posição até acabar o nome menor
    min_len = min(len(name1), len(name2))
    for i in range(min_len):
        if name1[i] == name2[i]:
            score += 15 #add bonus por letras no mesmo index
    return min(score, 100) #pontuação sempre entre 0 e 100

def get_feedback(score):
    #Retorna mensagem automática + conselho com base na pontuação
    if score >= 80:
        message = "You're like rice and beans, made for each other!"
        advice = "Advice: Plan a vacation together!"
    elif score >= 50:
        message = "You're like coxinha and guaraná!"
        advice = "Advice: Grab a coffee and hang out this weekend!"
    elif score >= 25:
        message = "Well... opposites attract, maybe?"
        advice = "Advice: Find a shared hobby to bridge the gap!"
    else:
        message = "Total mystery duo!"
        advice = "Advice: Communication is key!"
        
    return message, advice

def framed_result(name1, name2, score, message, advice):
    #Formatação e exibição do resultado centralizado em uma moldura
    #CABEÇALHO:
    title = f"{name1.upper()} & {name2.upper()}" 
    score_text = f"Your compatibility score is: {score}%!"
    #ESTRUTURA EM LINHAS:
    lines = [
        title,
        "",
        score_text,
        message,
        advice
    ]
    #CÁLCULO DA LARGURA TOTAL DA CAIXA (baseado na parte mais longa do texto + 4 espaços extras para margem interna)
    width = max(len(line) for line in lines) + 4
    #BORDA SUPERIOR:
    print("\n" + "=" * width)
    #Loop por cada linha centralizada com o contorno das bordas:
    for line in lines:
        print(f"║ {line.center(width - 4)} ║")
    #BORDA INFERIOR
    print("=" * width)

def run_friendship_calculator():
    #Gerenciamento da entrada do usuário, validação e exibição no terminal.
    #CABEÇALHO:
    print("💗FRIENDSHIP COMPATIBILITY CALCULATOR💗\n")
    #Coleta dos dados:
    name1 = input("Enter the first name: ").strip()
    name2 = input("Enter the second name: ").strip()
    #Validação contra entradas nulas
    if not name1 or not name2:
        print("Please enter valid names.")
        return
    #Processamento dos inputs e calculo do score
    score = friendship_score(name1, name2)
    message, advice = get_feedback(score)
    #Exibição:
    framed_result(name1, name2, score, message, advice)
#execução final:
run_friendship_calculator()