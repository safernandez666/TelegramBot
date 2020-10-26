# Telegram IoC Bot

Add your IoC to your Antivirus Console & Firewall by a message.

### Create your bot with BotFather & generate your Token

[How To](https://core.telegram.org/bots)
<p align="center">
<img src="screenshots/BotTelegram.png" width="400" >
</p>
### Steps

#### Build the Image

```bash
docker build -t bot .
```

#### Run the Container

```bash
docker run -e TOKEN="YOUR_TOKEN" bot  
```

Dialogue between Bot and the Operator, where you are informed of directions to parse and impact the consoles.

<img src="screenshots/TelegramDialogo.png" width="400" >

<img src="screenshots/Log.png" width="800" >
