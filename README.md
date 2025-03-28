# Jogo de Torres de Hanói

Este é um projeto desenvolvido em Java que implementa o jogo das **Torres de Hanói**, um desafio matemático clássico que envolve a movimentação de discos entre pinos seguindo regras específicas.

## 📌 Sobre o Jogo
O objetivo do jogo é mover todos os discos de um pino de origem para um pino de destino, utilizando um pino auxiliar, respeitando as seguintes regras:
- Apenas um disco pode ser movido por vez.
- Um disco maior nunca pode ser colocado sobre um disco menor.
- Todos os discos devem estar empilhados no pino de destino na mesma ordem inicial.

## 🚀 Tecnologias Utilizadas
- **Java**: Linguagem de programação principal do projeto.
- **Swing/AWT**: Para a interface gráfica do jogo (se aplicável).
- **Eclipse/IntelliJ**: Ambiente de desenvolvimento recomendado.

## 📂 Estrutura do Projeto
```
Jogo_Hanoi/
├── src/
│   ├── Main.java       # Classe principal do jogo
│   ├── Torre.java      # Classe que representa uma torre (pino)
│   ├── Disco.java      # Classe que representa um disco
│   ├── JogoHanoi.java  # Lógica do jogo e movimentação dos discos
│   ├── UI.java         # Interface gráfica (se houver)
├── README.md           # Documentação do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── LICENSE             # Licença do projeto (se houver)
```

## 📦 Como Executar
1. **Clone o repositório**:
   ```sh
   git clone https://github.com/felipefortu33/Jogo_Hanoi.git
   ```
2. **Acesse a pasta do projeto**:
   ```sh
   cd Jogo_Hanoi
   ```
3. **Compile e execute**:
   ```sh
   javac src/Main.java
   java -cp src Main
   ```

## 🛠 Melhorias Futuras
- Adicionar animações para a movimentação dos discos.
- Criar diferentes níveis de dificuldade.
- Implementar um contador de jogadas.

## 📄 Licença
Este projeto está sob a licença **MIT**. Sinta-se à vontade para utilizar e modificar conforme necessário.

---
Desenvolvido por **Felipe Augusto Ferreira Fortunato** 🎮
