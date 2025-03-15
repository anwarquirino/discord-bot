adicionado a função de saida automatica por inatividade de membros ou à não utilização do bot e alterações no comando para desconectar o bot do canal de voz:

disconnect --> leave

## Tecnologias Utilizadas

- **Python 3.8+**
- **discord.py** – Biblioteca para interagir com a API do Discord.
- **yt-dlp** – Ferramenta para extrair áudio dos vídeos do YouTube.
- **FFmpeg** – Processamento e reprodução de áudio.
- **python-dotenv** – Gerenciamento de variáveis de ambiente.

---

## Funcionalidades

- **!play `<consulta>`**: Pesquisa e toca uma música do YouTube no canal de voz onde o usuário estiver.
- **!pause**: Pausa a reprodução da música.
- **!resume**: Retoma a reprodução da música pausada.
- **!stop**: Para a reprodução da música.
- **!leave**: Desconecta o bot imediatamente do canal de voz.
- **Auto-desconexão**: Se o bot ficar 5 minutos sem tocar música, ele se desconecta automaticamente e envia uma mensagem informando a desconexão.

---

## Pré-requisitos

- **Python 3.8 ou superior** instalado.
- **FFmpeg** instalado e configurado no PATH.  
  - **Ubuntu/Debian**: `sudo apt install ffmpeg`
  - **Windows/Mac**: [Download FFmpeg](https://ffmpeg.org/download.html)
- Um **bot do Discord** criado com token (obtenha-o no [Discord Developer Portal](https://discord.com/developers/applications)).
- Arquivo `.env` configurado com a variável `TOKEN`.
