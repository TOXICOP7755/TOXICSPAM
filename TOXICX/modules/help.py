from config import TX1, TX2, TX3, TX4,TX5, TX6, TX7, TX8, TX9, TX10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"★ 𝙏𝙊𝙓𝙄𝘾 𝙓 𝙎𝙋𝘼𝙈 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @MERA_JIJA_HAI_TU**"


@TX1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@TX10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://graph.org/file/9ba2e1c637ca3d2809769.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ᴇxᴛʀᴀ •", data="extra"),
           ],
           [    
            Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/KNOW_UR_JIJA"),
            Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/TOXIC_X_SUPPORT")
           ],
           ],
           )


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**
𝗨𝘀𝗲𝗿𝗕𝗼𝘁: ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd
𝗘𝗰𝗵𝗼: ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>
𝗟𝗲𝗮𝘃𝗲: ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group
**© @MERA_JIJA_HAI_TU**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**
𝗥𝗮𝗶𝗱: ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>
𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>
𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>
𝐌𝐑𝐚𝐢𝐝: ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>
𝐒𝐑𝐚𝐢𝐝: ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>
𝐂𝐑𝐚𝐢𝐝: ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ!!
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>
**© @MERA_JIJA_HAI_TU**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**
𝗦𝗽𝗮𝗺: ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>
𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.
  1) {hl}pspam <count>
𝗛𝗮𝗻𝗴: ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.
  1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)
** © @MERA_JIJA_HAI_TU**
"""                     
           
           
@TX1.on(events.CallbackQuery(pattern=r"help_back"))
@TX2.on(events.CallbackQuery(pattern=r"help_back"))
@TX3.on(events.CallbackQuery(pattern=r"help_back"))
@TX4.on(events.CallbackQuery(pattern=r"help_back"))
@TX5.on(events.CallbackQuery(pattern=r"help_back"))
@TX6.on(events.CallbackQuery(pattern=r"help_back"))
@TX7.on(events.CallbackQuery(pattern=r"help_back"))
@TX8.on(events.CallbackQuery(pattern=r"help_back"))
@TX9.on(events.CallbackQuery(pattern=r"help_back"))
@TX10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ᴇxᴛʀᴀ •", data="extra"),
           ],
           [
            Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/KNOW_UR_JIJA"),
            Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/TOXIC_X_SUPPORT")
           ],
           ],
        )           
   else:
        await event.answer("Make Your Own Tosu Bots !! @MERA_JIJA_HAI_TU", cache_time=0, alert=True)


@TX1.on(events.CallbackQuery(pattern=r"spam"))
@TX2.on(events.CallbackQuery(pattern=r"spam"))
@TX3.on(events.CallbackQuery(pattern=r"spam"))
@TX4.on(events.CallbackQuery(pattern=r"spam"))
@TX5.on(events.CallbackQuery(pattern=r"spam"))
@TX6.on(events.CallbackQuery(pattern=r"spam"))
@TX7.on(events.CallbackQuery(pattern=r"spam"))
@TX8.on(events.CallbackQuery(pattern=r"spam"))
@TX9.on(events.CallbackQuery(pattern=r"spam"))
@TX10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            ) 
   else:
        await event.answer("Make Your Own TOXIC Bots !! @MERA_JIJA_HAI_TU", cache_time=0, alert=True)


@TX1.on(events.CallbackQuery(pattern=r"raid"))
@TX2.on(events.CallbackQuery(pattern=r"raid"))
@TX3.on(events.CallbackQuery(pattern=r"raid"))
@TX4.on(events.CallbackQuery(pattern=r"raid"))
@TX5.on(events.CallbackQuery(pattern=r"raid"))
@TX6.on(events.CallbackQuery(pattern=r"raid"))
@TX7.on(events.CallbackQuery(pattern=r"raid"))
@TX8.on(events.CallbackQuery(pattern=r"raid"))
@TX9.on(events.CallbackQuery(pattern=r"raid"))
@TX10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )  
     else:
        await event.answer("Make Your Own TOXIC bots !! @MERA_JIJA_HAI_TU", cache_time=0, alert=True)


@TX1.on(events.CallbackQuery(pattern=r"extra"))
@TX2.on(events.CallbackQuery(pattern=r"extra"))
@TX3.on(events.CallbackQuery(pattern=r"extra"))
@TX4.on(events.CallbackQuery(pattern=r"extra"))
@TX5.on(events.CallbackQuery(pattern=r"extra"))
@TX6.on(events.CallbackQuery(pattern=r"extra"))
@TX7.on(events.CallbackQuery(pattern=r"extra"))
@TX8.on(events.CallbackQuery(pattern=r"extra"))
@TX9.on(events.CallbackQuery(pattern=r"extra"))
@TX10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
   else:
        await event.answer("Make Your Own TOXIC Bots !! @MERA_JIJA_HAI_TU", cache_time=0, alert=True)
