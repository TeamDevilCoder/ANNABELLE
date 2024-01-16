<h1 align="center">ANNABELLE ROBOT</h1>
<p align="center">
  <img src="https://graph.org/file/07cf9164916f74da2ba1d.jpg">
</p>
<p align="center">
<a href="https://github.com/TeamDevilCoder/ANNABELLE/stargazers"><img src="https://img.shields.io/github/stars/TeamDevilCoder/ANNABELLE?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/TeamDevilCoder/ANNABELLE/network/members"> <img src="https://img.shields.io/github/forks/TeamDevilCoder/ANNABELLE?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/TeamDevilCoder/ANNABELLE/blob/main/LICENSE"> <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-skyblue?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://pypi.org/project/Telethon/"> <img src="https://img.shields.io/pypi/v/telethon?color=white&label=telethon&logo=python&logoColor=blue&style=for-the-badge" /></a>
<a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=white&label=pyrogram&logo=python&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/TeamDevilCoder/ANNABELLE"> <img src="https://img.shields.io/github/repo-size/TeamDevilCoder/ANNABELLE?color=skyblue&logo=github&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/TeamDevilCoder/ANNABELLE/commits/TeamDevilCoder"> <img src="https://img.shields.io/github/last-commit/TeamDevilCoder/ANNABELLE?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
</p>

━━━━━━━━━━━━━━━━━━━━━━
<h2 align="center"> 
    ʀᴇǫᴜɪʀᴇᴍᴇɴᴛs 
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3115/"> ᴘʏᴛʜᴏɴ 3.11.5 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘɪ ᴋᴇʏ </a> |
    <a href="https://t.me/botfather"> ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏᴋᴇɴ </a> | 
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> ᴍᴏɴɢᴏᴅʙ ᴜʀɪ </a>
</p>
━━━━━━━━━━━━━━━━━━━━

<h2>  ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ​ 🚀</h2> 
ᴛʜᴇ ᴇᴀsɪᴇsᴛ ᴡᴀʏ ᴛᴏ ᴅᴇᴘʟᴏʏ.
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/TeamDevilCoder/ANNABELLE"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>
 ━━━━━━━━━━━━━━━━━━━━━━
  ━━━━━━━━━━━━━━━━━━━━
<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴠᴘs/ʟᴏᴄᴀʟ 」─
</h3>


<h3>
- <b> ᴠᴘs/ʟᴏᴄᴀʟ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ </b>
</h3>

- Get your [Necessary Variables](https://github.com/TeamDevilCoder/ANNABELLE/blob/main/DCManeger/config.py)
- Upgrade and Update by :
`sudo apt-get update && sudo apt-get upgrade -y`
- Install required packages by :
`sudo apt-get install python3-pip -y`
- Install pip by :
`sudo pip3 install -U pip`
- Clone the repository by :
`git clone https://github.com/TeamDevilCoder/ANNABELLE && cd DCManeger`
- Install/Upgrade setuptools by :
`pip3 install --upgrade pip setuptools`
- Install requirements by :
`pip3 install -U -r requirements.txt`
- Fill your variables in config by :
`vi DCManeger/config.py`

Press `I` on the keyboard for editing config

Press `Ctrl+C` when you're done with editing config and `:wq` to save the config
- Install tmux to keep running your bot when you close the terminal by :
`sudo apt install tmux && tmux`
- Finally run the bot by :
`python3 -m DCManeger`
- For getting out from tmux session

Press `Ctrl+b` and then `d`

<p align="center">
  <img src="https://graph.org/file/07cf9164916f74da2ba1d.jpg">
</p>


━━━━━━━━━━━━━━━━━━━━


<h2 align="center"> 
    ᴡʀɪᴛᴇ ɴᴇᴡ ᴍᴏᴅᴜʟᴇs 
</h2>

```py
#ᴀᴅᴅ ʟɪᴄᴇɴsᴇ ᴛᴇxᴛ ʜᴇʀᴇ ɢᴇᴛ ɪᴛ ғʀᴏᴍ ʙᴇʟᴏᴡ.

from DCManeger import pbot as dc # This is bot's client
from pyrogram import filters # pyrogram filters



#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "Module Name"
__help__ = "Module help message"


@dc.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("ɪ'ᴍ.ᴀʟɪᴠᴇ ʙᴀʙʏ❣️!!")

# ᴍᴀɴʏ ᴜsᴇғᴜʟ ғᴜɴᴄᴛɪᴏɴs ᴀʀᴇ ɪɴ, DCManeger/utils/,DCManeger, and DCManeger/modules/
```

<h3 align="center"> 
 ᴀɴᴅ ᴘᴜᴛ ᴛʜɪs ғɪʟᴇ ɪɴ DCManeger/modules/, ʀᴇsᴛᴀʀᴛ ᴀɴᴅ ᴛᴇsᴛ ʏᴏᴜʀ ʙᴏᴛ.
</h3>

━━━━━━━━━━━━━━━━━━━━
<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://telegram.me/DC_BOT_Support"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>
<p align="center">
<a href="https://t.me/dcbotz"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=telegram"></a>
</p>

━━━━━━━━━━━━━━━━━━━━
### ㅤㅤㅤㅤᴄʀᴇᴅɪᴛs 
 [ AMBOT ](https://t.me/New_AMBOT)

━━━━━━━━━━━━━━━━━━━━
