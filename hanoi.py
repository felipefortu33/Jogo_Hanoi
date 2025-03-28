from colorama import Fore, Style, init

# Inicializa o suporte a cores no terminal
init(autoreset=True)

def print_torres(towers):
    # Função para imprimir o estado atual das torres com cores
    print(Fore.YELLOW + "\n=== Estado Atual das Torres ===" + Style.RESET_ALL)
    for torre, discos in towers.items():
        # Exibe a torre e seus discos com formatação colorida
        print(f"Torre {Fore.BLUE}{torre}{Style.RESET_ALL}: {discos}")
    print(Fore.YELLOW + "===============================\n" + Style.RESET_ALL)

def jogar_hanoi(discos, torres):
    # Inicializa as torres como dicionário com listas vazias
    towers = {torre: [] for torre in torres}
    # Coloca todos os discos na primeira torre
    towers[torres[0]] = list(range(discos, 0, -1))
    destino_final = torres[-1]  # Define a torre de destino final
    
    while True:
        # Exibe o estado atual das torres
        print_torres(towers)
        
        # Verifica se a torre final contém todos os discos na ordem correta
        if towers[destino_final] == list(range(discos, 0, -1)):
            print(Fore.GREEN + "\n🎉 Parabéns! Você resolveu a Torre de Hanói! 🎉" + Style.RESET_ALL)
            break
        
        # Solicita o movimento ao jogador
        move = input(Fore.CYAN + "Digite o movimento (Exemplo: A C para mover da Torre A para C): " + Style.RESET_ALL).strip().split()
        
        # Valida o movimento inserido pelo jogador
        if len(move) == 2 and move[0] in towers and move[1] in towers:
            if towers[move[0]] and (not towers[move[1]] or towers[move[1]][-1] > towers[move[0]][-1]):
                # Move o disco da torre de origem para a torre de destino
                disk = towers[move[0]].pop()
                towers[move[1]].append(disk)
            else:
                # Mensagem de erro caso o movimento viole as regras
                print(Fore.RED + "❌ Movimento inválido. Certifique-se de seguir as regras!" + Style.RESET_ALL)
        else:
            # Mensagem de erro caso a entrada seja inválida
            print(Fore.RED + "❌ Entrada inválida. Tente novamente." + Style.RESET_ALL)

def main():
    # Mensagem inicial de boas-vindas
    print(Fore.MAGENTA + "Bem-vindo à Torre de Hanói!" + Style.RESET_ALL)
    
    while True:
        try:
            # Solicita o número de discos
            discos = int(input(Fore.CYAN + "Digite o número de discos (1 ou mais): " + Style.RESET_ALL))
            if discos > 0:
                break
            else:
                print(Fore.RED + "Por favor, insira um número maior que 0." + Style.RESET_ALL)
        except ValueError:
            # Mensagem de erro caso a entrada seja inválida
            print(Fore.RED + "Entrada inválida. Tente novamente com um número inteiro." + Style.RESET_ALL)

    while True:
        try:
            # Solicita o número de torres
            torres = int(input(Fore.CYAN + "Digite o número de torres (mínimo 3): " + Style.RESET_ALL))
            if torres >= 3:
                break
            else:
                print(Fore.RED + "Você precisa de pelo menos 3 torres para jogar." + Style.RESET_ALL)
        except ValueError:
            # Mensagem de erro caso a entrada seja inválida
            print(Fore.RED + "Entrada inválida. Tente novamente com um número inteiro." + Style.RESET_ALL)

    # Gera as letras das torres com base na quantidade inserida
    letras_torres = [chr(65 + i) for i in range(torres)]
    # Chama a função para iniciar o jogo
    jogar_hanoi(discos, letras_torres)

if __name__ == "__main__":
    # Início da execução do programa
    main()