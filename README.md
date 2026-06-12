# 🤖 Discord Bot

Bot para Discord em **Python**, com comandos básicos e um módulo de **música** que evoluiu ao longo de várias versões. A reprodução usa `yt-dlp` para buscar áudio e `spotipy` para integração com playlists do Spotify.

> 🚧 Projeto em desenvolvimento / estudo.

## ✨ Funcionalidades

- Comandos básicos (`!ping`)
- Reprodução de música a partir do YouTube (`yt-dlp`)
- Integração com a API do Spotify (`spotipy`)
- Configuração via variáveis de ambiente (`.env`)

## 🗂️ Estrutura

```
discord-bot/
├── bot.py              # Bot base (comandos simples, ex.: !ping)
├── bot_music/          # Módulo de música — versões iterativas
├── bot_music_2.0/
├── bot_music_2.1/
└── bot_music_2.2/      # Versão mais recente (yt-dlp + spotipy)
```

> As pastas `bot_music_*` representam a evolução do módulo de música. Para usar a versão mais completa, rode a partir de `bot_music_2.2/`.

## 🛠️ Tecnologias

- Python 3.12+
- [discord.py](https://discordpy.readthedocs.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — extração de áudio
- [spotipy](https://spotipy.readthedocs.io/) — API do Spotify
- python-dotenv — variáveis de ambiente

## ▶️ Como executar

```bash
git clone https://github.com/anwarquirino/discord-bot.git
cd discord-bot

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com suas credenciais:

```env
TOKEN=seu_token_do_discord
SPOTIPY_CLIENT_ID=seu_client_id
SPOTIPY_CLIENT_SECRET=seu_client_secret
```

Execute o bot base:

```bash
python bot.py
```

## 📜 Licença

MIT — sinta-se livre para usar e modificar.
