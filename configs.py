import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28243586"))
  API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7456518146:AAEY0de8VB537DSXzXMiWhC3CvpFjqecQ9A")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mr_Sung_Pb_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002057330647"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5340652544"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jyotimaurya891824:j8dK84kIE0HrDJTH@cluster0.uwkm5id.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Mr_Persis_Bot")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002057330647"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "0").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "0").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅ꜰɪʟᴇꜱᴛᴏʀᴇʙᴏᴛ🔅]────⍟
│
├🔸 ᴍʏ ɴᴀᴍᴇ: [ꜱᴜɴɢ ᴊɪɴ ᴡᴏᴏ](https://t.me/{BOT_USERNAME})
│
├🔸 ʟᴀɴɢᴜᴀɢᴇ: [ᴘʏᴛʜᴏɴ 3](https://www.python.org)
│
├🔹 ʟɪʙʀᴀʀʏ: [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)
│
├🔸ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠ: [ꜱʜᴜʙʜᴀᴍ](https://t.me/SHubham_X_official)
│
├🔸ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: [ᴄʜᴀɴɴᴇʟ](https://t.me/Mr_Persis_bot)
│
├🔹ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: [ɢʀᴏᴜᴘ](https://t.me/Mr_Persis_SUpport_group)
╰──────[ ᴜ ᴄᴀɴ ʙᴇ ᴀ ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 ᴅᴇᴠ: [ᴘʙ](https://telegram.me/SHubham_X_official)
 
 ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **ꜰɪʟᴇꜱᴛᴏʀᴇʙᴏᴛ**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
