import random

# Lista de fatos e citações de Nikola Tesla
tesla_facts_quotes = [
    # Fatos
    "Nikola Tesla nasceu durante uma tempestade com raios à meia-noite, em 10 de julho de 1856, na atual Croácia.",
    "Tesla é mais conhecido por suas contribuições ao projeto do sistema moderno de fornecimento de eletricidade em corrente alternada (CA).",
    "Ele demonstrou publicamente a comunicação sem fio (rádio) em 1893, antes de Guglielmo Marconi.",
    "Tesla tinha memória fotográfica e conseguia visualizar invenções complexas em sua mente com detalhes incríveis antes de construí-las.",
    "Ele desenvolveu a Bobina de Tesla por volta de 1891, um transformador ressonante capaz de produzir altas voltagens em alta frequência.",
    "Tesla registrou mais de 300 patentes em todo o mundo para suas invenções.",
    "Ele foi um pioneiro em diversas áreas, incluindo rádio, radar, controle remoto, raios-X e energia hidrelétrica (usina de Niagara Falls).",
    "Apesar de suas contribuições, Tesla morreu relativamente pobre e em relativo esquecimento em 1943, em Nova York.",
    "A unidade de medida da densidade do fluxo magnético no Sistema Internacional de Unidades (SI) foi nomeada \"tesla\" em sua homenagem.",
    "Tesla era conhecido por seus hábitos excêntricos, como alimentar pombos e sua obsessão pelo número três.",
    
    # Citações (Atribuídas)
    "\"Se você quiser encontrar os segredos do universo, pense em termos de energia, frequência e vibração.\" - Nikola Tesla",
    "\"O presente é deles; o futuro, pelo qual eu realmente trabalhei, é meu.\" - Nikola Tesla",
    "\"Não me importo que tenham roubado minha ideia... Importo-me que não tenham nenhuma ideia própria.\" - Nikola Tesla",
    "\"As virtudes e as falhas são inseparáveis, como a força e a matéria. Quando se separam, o homem deixa de existir.\" - Nikola Tesla",
    "\"De todas as coisas, o que mais gosto são os livros.\" - Nikola Tesla",
    "\"Nossas virtudes e nossos fracassos são inseparáveis, como força e matéria. Quando eles se separam, o homem não é mais.\" - Nikola Tesla", # Variação da anterior
    "\"A ciência é apenas perversão de si mesma, a menos que tenha como objetivo final melhorar a humanidade.\" - Nikola Tesla",
    "\"O desenvolvimento progressivo do homem é vitalmente dependente da invenção.\" - Nikola Tesla"
]

def get_random_tesla_fact_quote():
    """Retorna um fato ou citação aleatória de Nikola Tesla."""
    return random.choice(tesla_facts_quotes)

if __name__ == "__main__":
    print("--- Fatos e Citações de Nikola Tesla ---")
    
    while True:
        print("\nPressione Enter para ver um fato ou citação aleatória de Nikola Tesla (ou digite 'sair' para terminar):")
        user_input = input("> ").lower().strip()
        
        if user_input == "sair":
            break
        else:
            fact_quote = get_random_tesla_fact_quote()
            print("\n" + "-"*60)
            print(fact_quote)
            print("-"*60)
            
    print("\nObrigado!")

