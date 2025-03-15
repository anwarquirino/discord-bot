# Discord Music Bot (YouTube Only)

Este é uma atualização do bot de música para Discord desenvolvido em Python. Ele utiliza a biblioteca o [yt-dlp](https://github.com/yt-dlp/yt-dlp) (como substituto atualizado do youtube_dl) e o FFmpeg para buscar e reproduzir músicas do YouTube diretamente no canal de voz.

---

## Tecnologias Utilizadas

- **Python 3.8+**  
- **discord.py** – Biblioteca para interação com a API do Discord  
- **yt-dlp** – Ferramenta para extrair áudio dos vídeos do YouTube  
- **FFmpeg** – Para processamento e reprodução de áudio  
- **python-dotenv** – Gerenciamento de variáveis de ambiente (para armazenar o token do bot)

---

## Funcionalidades

- **!play `<query>`**: Procura e toca uma música do YouTube baseada na pesquisa do usuário.
- **!pause**: Pausa a reprodução da música atual.
- **!resume**: Retoma a reprodução da música pausada.
- **!stop**: Para a reprodução da música.
- **!disconnect**: Desconecta o bot do canal de voz.

---

## Pré-requisitos

- **Python 3.8 ou superior**  
- **FFmpeg** instalado no sistema  
  - **Ubuntu/Debian**: `sudo apt install ffmpeg`  
  - **Windows/Mac**: [Baixe e configure o FFmpeg](https://ffmpeg.org/download.html)
- Um bot do Discord criado (obtenha o token no [Discord Developer Portal](https://discord.com/developers/applications))
- Um arquivo `.env` configurado com a variável `TOKEN`

---

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/SEU_USUARIO/discord-music-bot.git
   cd discord-music-bot

    Crie e ative um ambiente virtual:

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Instale as dependências:

pip install -r requirements.txt

Caso não tenha um arquivo requirements.txt, você pode instalar manualmente:

pip install discord.py python-dotenv yt-dlp

Crie um arquivo .env na raiz do projeto e adicione:

    TOKEN=seu_token_aqui

    Substitua seu_token_aqui pelo token do seu bot.

Uso

    Inicie o bot:

    python bot.py

    No Discord:
        Entre em um canal de voz.
        Utilize os comandos do bot, por exemplo:
            !play nome da música
            !pause
            !resume
            !stop
            !disconnect

Estrutura do Projeto

    bot.py: Arquivo principal com a lógica do bot.
    .env: Arquivo de configuração (não versionado) para armazenar o token.
    requirements.txt: Lista de dependências do projeto (se aplicável).

Contribuição

Pull requests são bem-vindos!
Para mudanças maiores, abra uma issue para discutir suas ideias.
Licença

Este projeto está licenciado sob a MIT License.
Notas

    Este bot é um projeto em desenvolvimento. Feedbacks e sugestões são muito bem-vindos!
    Caso encontre problemas com o yt-dlp, certifique-se de estar usando a versão mais recente.