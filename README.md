# 🤖 Discord Music Bot

Bot de música para Discord em **Python**. Toca áudio do **YouTube** (via `yt-dlp`) e aceita links do **Spotify** (track, álbum ou playlist), resolvendo cada faixa no YouTube. Inclui auto-desconexão por inatividade.

> 🚧 Projeto em desenvolvimento / estudo.

## ✨ Comandos

| Comando | Descrição |
|---------|-----------|
| `!ping` | Testa a latência do bot |
| `!play <busca ou link>` | Toca do YouTube; aceita link de track/álbum/playlist do Spotify |
| `!pause` | Pausa a reprodução |
| `!resume` | Retoma a reprodução |
| `!stop` | Para a música |
| `!leave` | Desconecta o bot do canal de voz |

Auto-desconecta após **5 minutos** de inatividade.

## 🛠️ Tecnologias

- Python 3.12+
- [discord.py](https://discordpy.readthedocs.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — extração de áudio do YouTube
- [spotipy](https://spotipy.readthedocs.io/) — API do Spotify
- python-dotenv — variáveis de ambiente
- **FFmpeg** — necessário no sistema para reproduzir áudio

## ▶️ Como executar

**Pré-requisito:** ter o [FFmpeg](https://ffmpeg.org/download.html) instalado e disponível no `PATH`.

```bash
git clone https://github.com/anwarquirino/discord-bot.git
cd discord-bot

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz (use o `.env.example` como base):

```env
TOKEN=seu_token_do_discord
SPOTIFY_CLIENT_ID=seu_client_id
SPOTIFY_CLIENT_SECRET=seu_client_secret
```

Execute:

```bash
python bot.py
```

## 🗂️ Estrutura

```
discord-bot/
├── bot.py              # Bot completo (música YouTube/Spotify + !ping)
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

## 📜 Histórico de versões

O módulo de música evoluiu por várias iterações (Lavalink → yt-dlp → auto-disconnect → Spotify).
As versões antigas estão preservadas na branch [`archive/music-versions`](https://github.com/anwarquirino/discord-bot/tree/archive/music-versions).

## 📜 Licença

MIT — sinta-se livre para usar e modificar.
