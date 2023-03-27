'''Instrução
Para criar um personagem só basta istanciar um objeto. Ex: personagem1 = Personagem()
Após isso o algoritmo chama o método cria_personagem que está privado, só consegue acessar dentro da classe. Nisso o método chamado define os atributos do personagem(nome, descrição, imagem, programa, animador), e depois é chamado o outro método privado mostra_personagem para mostrar o personagem. Por fim é perguntado ao usuário se ele quer criar outro personagem ou não.
'''

class Personagem:
    def __init__(self) -> None:
        self.__nome = ''
        self.__descricao = ''
        self.__imagem = ''
        self.__programa = ''
        self.__animador = ''
        self.__cria_personagem()
    
    def __cria_personagem(self) -> None:
        # --------------------------------------------------- NOME ------------------------------------------------
        self.__nome = str(input('Digite o nome do personagem: ')).title().strip() # Recebendo o nome do personagem
        while not self.__nome.isalpha(): # Validando o nome do personagem
            print('Digite um nome válido para o personagem: ')
            self.__nome = str(input('Nome do personagem: ')).title().strip()
        
        # ------------------------------------------------ DESCRIÇÃO -----------------------------------------------
        self.__descricao = str(input('Escreva a descrição do personagem: ')).title().strip() # Recebendo a descrição do personagem
        if len(self.__descricao) <= 25: # Validando se a descrição é muito curta ou não
            print('Descrição muito curta, descreva com mais clareza. ')
            self.__descricao = str(input('Descrição do personagem: ')).title().strip()
        
        # -------------------------------------------------- IMAGEM ------------------------------------------------
        self.__imagem = str(input('Link da imagem do personagem: ')) # Recebendo a imagem do personagem
        while (not 'http' in self.__imagem) or (not '/' in self.__imagem): # Validando a imagem do personagem
            print('Link inválido. Tente novamente...')
            self.__imagem = str(input('Link da imagem do personagem: '))
        
        # -------------------------------------------------- PROGRAMA -----------------------------------------------
        self.__programa = str(input('Digite o nome do software que criou o personagem: ')).title().strip() # Recebendo o programa 
        while not self.__programa.isalpha(): # Validando o programa
            print('Software não reconhecido. Digite um software válido.')
            self.__programa = str(input('Digite o nome do software que criou o personagem: ')).title().strip()
        
        # -------------------------------------------------- ANIMADOR -----------------------------------------------
        self.__animador = str(input(f'Digite o animador do {self.__nome}: ')).title().strip() # Recebendo o animador do personagem
        while not self.__animador.isalpha(): # Validando o animador
            print('Nome inválido.')
            self.__animador = str(input(f'Digite o animador do {self.__nome}: ')).title().strip()
        

        self.__mostra_personagem() # Mostrando dados do personagem.

        # ----------------------------------------------- NOVO PERSONAGEM --------------------------------------------
        outro_personagem = int(input('Deseja criar outro personagem? [0] - NÃO / [1] - SIM '))
        while True:
            if outro_personagem == 1:
                self.__cria_personagem()
            else:
                break

    def __mostra_personagem(self):
        print()
        print('-' * 50)
        print('Aqui está o personagem que você criou.')
        print(f'Nome: {self.__nome}')
        print(f'Descrição: {self.__descricao}')
        print(f'Imagem: {self.__imagem}')
        print(f'Programa: {self.__programa}')
        print(f'Animador: {self.__animador}')
        

personagem1 = Personagem()