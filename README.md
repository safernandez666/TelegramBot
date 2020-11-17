# Telegram IoC Bot

Add your IoC to your Antivirus Console & Firewall by a message.

### Create your bot with BotFather & generate your Token

[How To](https://core.telegram.org/bots)
<p align="center">
<img src="screenshots/BotTelegram.png" width="400" >
</p>

### Steps

#### Download the Proyect

```bash
git clone git@github.com:safernandez666/TelegramBot.git
```

#### Build the Image

```bash
docker build -t bot .
```

#### Run the Container

```bash
docker run -e TOKEN="YOUR_TOKEN" bot  
```

Dialogue between Bot and the Operator, where you are informed of directions to parse and impact the consoles.
<p align="center">
<img src="screenshots/TelegramDialogo.png" width="400" >
</p>
<p align="center">
<img src="screenshots/Log.png" width="800" >
</p>

#### Working

Depending on the integration you want to do, CrowdStrike, Trend Micro, Palo Alto, etc. you can develop the method in engine.py once the parsing is done.

Sending IoC to the Bot

<p align="center">
<img src="screenshots/Carga.PNG" width="400" >
</p>

Impact on Apex One Trend Micro

<p align="center">
<img src="screenshots/Trend.JPG" width="800" >
</p>
