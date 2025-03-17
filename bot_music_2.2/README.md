🎵 Bot de Música para Discord

Um bot de música para Discord que suporta Spotify e YouTube, utilizando Discord.py, yt-dlp e Spotipy.
🚀 Tecnologias Utilizadas

    discord.py → Biblioteca para criar bots no Discord.
    yt-dlp → Para baixar e reproduzir áudio do YouTube.
    Spotipy → Para buscar músicas do Spotify.
    FFmpeg → Para processar e reproduzir áudio.
    Python-dotenv → Para gerenciar credenciais de forma segura.

⚡ O que há de novo neste código?
🚀 Nova Versão	❌ Versão Antiga
✅ Suporte ao Spotify 🎵	❌ Apenas YouTube
✅ Auto-desconexão após inatividade 🔄	❌ Bot ficava preso no canal de voz
✅ Uso de dotenv para segurança 🔒	❌ Token no código-fonte (inseguro)
✅ Melhor estrutura de comandos 🔧	❌ Código menos organizado
🔧 Instalação
1️⃣ Pré-requisitos

    Python 3.8+
    FFmpeg instalado
    Um bot registrado no Discord Developer Portal
    Credenciais do Spotify obtidas no Spotify Developer

2️⃣ Instale as dependências

pip install -r requirements.txt

3️⃣ Configurar credenciais

Crie um arquivo .env e adicione suas credenciais:

TOKEN=SEU_TOKEN_DISCORD
SPOTIPY_CLIENT_ID=SEU_CLIENT_ID_SPOTIFY
SPOTIPY_CLIENT_SECRET=SEU_CLIENT_SECRET_SPOTIFY
SPOTIPY_REDIRECT_URI=http://localhost:8080/callback

4️⃣ Executar o bot

python bot.py

📜 Comandos Disponíveis
Comando	Descrição
!play <nome/url>	Toca uma música do YouTube ou Spotify
!pause	Pausa a música
!resume	Retoma a música pausada
!stop	Para a música e limpa a fila
!leave	Desconecta o bot do canal de voz
🛠 Possíveis Erros e Soluções
❌ ModuleNotFoundError: No module named 'spotipy'

✅ Execute:

pip install spotipy

❌ O bot desconecta sozinho quando fica sozinho no canal

✅ O Discord força a saída do bot quando ele está sozinho. Como solução alternativa, um servidor Lavalink pode ajudar.
📌 Licença

Este projeto é open-source e pode ser usado livremente para aprendizado e desenvolvimento.

Se tiver dúvidas ou sugestões, fique à vontade para contribuir! 🚀🔥