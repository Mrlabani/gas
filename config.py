import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22419004")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7492087293:AAE6MNgRc9Q-hudikdYPhsvv7a4R1YDjBEY") # ⚠️ Required
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YTDOWNLOAD5_ROBOT") # ⚠️ Required
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
 
    # other configs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/3999ba9e4ce962ff15a78.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6742022802').split()] # ⚠️ Required
    FORCE_SUB_TEXT = os.environ.get('FORCE_SUB_TEXT', "**Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ ᴏᴜʀ Bᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ sᴏ ʏᴏᴜ ᴅᴏɴ'ᴛ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ...\n\nIғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ғɪʟᴇ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '❆ Jᴏɪɴ Oᴜʀ Bᴀᴄᴋ-Uᴘ Cʜᴀɴɴᴇʟ ❆' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '↻ Tʀʏ Aɢᴀɪɴ' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ...\n\nTʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs...**")
    FORCE_SUB = os.environ.get('FORCE_SUB', 'NOOBPrivate') # ⚠️ Required
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL","-1002246016095")  # Updated AUTH_CHANNEL value
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002186778731")) # ⚠️ Required

    
    # Mega User Account ⚠️ Only Set When you have Pro or Enterprise Mega Account
    MEGA_EMAIL = os.environ.get("labani99@outlook.com")
    MEGA_PASSWORD = os.environ.get("@Labani25")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8081"))

class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hello {} 👋,
━━━━━━━━━━━━━━━━━━━━━
This Bot Can Search PornHub
Videos & Download Them For You

Can Also Download Files through
Link of Mega & YouTube
━━━━━━━━━━━━━━━━━━━━━
⚠️The Bot Contains 18+ Content
So Kindly Access it with Your own
Risk. Children Please Stay Away."
We don't intend to spread Pørno-
-graphy here. It's just a bot for a"
purpose as many of them wanted."
━━━━━━━━━━━━━━━━━━━━━
Click The Buttons Below To Search
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/l_abani>ᑎOOᗷ</a>
╰───────────────⍟ """

    HELP_TXT = """
Tʜɪs Bᴏᴛ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Fᴏʟʟᴏᴡɪɴɢ Fɪʟᴇ ᴛʜʀᴏᴜɢʜ ʟɪɴᴋs:

⊚ YouTube
⊚ Mega
⊚ PornHub

❗ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/NOOBPrivate>𝐒𝐔𝐏𝐏𝐎𝐑𝐓</a>
"""


    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
