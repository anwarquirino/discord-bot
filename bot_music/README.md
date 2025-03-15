Discord Music Bot

Este é um bot de música para o Discord, criado usando a biblioteca discord.py e integrado ao Lavalink para fornecer funcionalidades de reprodução de música.
🚀 Tecnologias Utilizadas

    discord.py: Biblioteca para criar bots no Discord.
    Wavelink: Biblioteca Python para se conectar a um servidor Lavalink e reproduzir músicas.
    Lavalink: Servidor de música que permite reproduzir músicas de plataformas como YouTube.
    dotenv: Biblioteca para gerenciar variáveis de ambiente.

🔧 Funcionalidades

Este bot possui comandos para controle de reprodução de música em canais de voz no Discord. As funcionalidades incluem:

    !play [música]: Toca uma música no canal de voz em que o usuário está.
    !pause: Pausa a música que está tocando.
    !stop: Para a música que está tocando.
    !disconnect: Desconecta o bot do canal de voz.
    !ping: Comando simples para testar a latência do bot.

💻 Requisitos

    Python 3.8+ instalado.
    Lavalink em execução localmente (ou em servidor remoto).
    JDK 8+ instalado para rodar o servidor Lavalink.
    Variáveis de ambiente configuradas corretamente para o bot (TOKEN do bot do Discord).

🔑 Configuração
1. Configurar o Lavalink Localmente
Passos para configurar o Lavalink no seu computador:

    Baixar o Lavalink:
    Baixe o arquivo .jar do Lavalink a partir do repositório oficial aqui.

    Instalar o JDK:
    Certifique-se de que você tem o JDK 8 ou superior instalado no seu sistema. Você pode verificar isso com:

java -version

Se você não tiver o JDK instalado, siga as instruções para instalação no site oficial do JDK.

Rodar o Lavalink:

    Crie uma pasta para o Lavalink e coloque o arquivo .jar nela.

    Abra o terminal na pasta onde o .jar está localizado.

    Execute o seguinte comando para rodar o Lavalink:

    java -jar Lavalink.jar

Isso fará o Lavalink rodar localmente na porta padrão 2333. Caso queira alterar a porta ou outros parâmetros, edite o arquivo application.yml (documentação do Lavalink está disponível aqui).

Configuração do Lavalink:

    Abra o arquivo application.yml (se não houver, crie um na mesma pasta do .jar) e adicione a senha de autenticação, como no exemplo:

        server:
          # A porta que o Lavalink irá escutar
          port: 2333
        lavalink:
          password: "youshallnotpass"  # Senha para autenticar a conexão com o Lavalink

    Se você estiver utilizando um servidor público, como lavalink.oops.wtf, a senha e os detalhes do servidor serão fornecidos pelo serviço.

2. Instalar Dependências

Com o Lavalink rodando localmente, o próximo passo é instalar as dependências do bot.

pip install -r requirements.txt

Certifique-se de que você tem as dependências corretas instaladas:

    discord.py
    wavelink
    python-dotenv

3. Configurar o arquivo .env

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

TOKEN=seu_token_aqui

Substitua seu_token_aqui pelo token do seu bot do Discord, que você pode obter no Portal de Desenvolvedores do Discord.
4. Iniciar o Bot

Após configurar o arquivo .env e as dependências, inicie o bot executando o comando:

python bot.py

Isso fará com que o bot se conecte ao Discord e ao servidor Lavalink, e o bot estará pronto para reproduzir músicas no canal de voz do Discord.
🛠️ Comandos

Aqui estão os comandos que o bot oferece:

    !ping: Testa a latência do bot.
    !play [música]: Toca uma música no canal de voz onde o usuário está.
    !pause: Pausa a música.
    !stop: Para a música.
    !disconnect: Desconecta o bot do canal de voz.

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.