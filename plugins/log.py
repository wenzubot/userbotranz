# Credits: mrconfused
# Recode by @mrismanaziz
# t.me/SharingUserbot

import asyncio

from telethon import events
from telethon.tl.custom import Message

from pyAyiin import ayiin, cmdHelp
from pyAyiin.decorator import ayiinCmd
from pyAyiin.utils import eod, eor
from pyAyiin.lib.tools import media_type
from pyAyiin.database.log import approveLog, disapproveLog, isApprovedLog
from pyAyiin.database.variable import getVar, setVar

from . import cmd
from .carbon import vcmention


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@ayiin.on(events.ChatAction)
async def logaddjoin(yins):
    user = await yins.get_user()
    chat = await yins.get_chat()
    if not (user and user.is_self):
        return
    if hasattr(chat, "username") and chat.username:
        chat = f"[{chat.title}](https://t.me/{chat.username}/{yins.action_message.id})"
    else:
        chat = f"[{chat.title}](https://t.me/c/{chat.id}/{yins.action_message.id})"
    if yins.user_added:
        tmp = yins.added_by
        text = f"📩 **#TAMBAH_LOG\n •** {vcmention(tmp)} **Menambahkan** {vcmention(user)}\n **• Ke Group** {chat}"
    elif yins.user_joined:
        text = f"📨 **#LOG_GABUNG\n •** [{user.first_name}](tg://user?id={user.id}) **Bergabung\n • Ke Group** {chat}"
    else:
        return
    await yins.client.send_message(ayiin.BOTLOG_CHATID, text)


@ayiin.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
@ayiin.on(events.MessageEdited(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(yins: Message):
    if ayiin.BOTLOG_CHATID == -100:
        return
    if not getVar("PMLOG"):
        return
    sender = await yins.get_sender()
    await asyncio.sleep(0.5)
    if not sender.bot:
        chat = await yins.get_chat()
        if not isApprovedLog(chat.id) and chat.id != 777000:
            if LOG_CHATS_.RECENT_USER != chat.id:
                LOG_CHATS_.RECENT_USER = chat.id
                if LOG_CHATS_.NEWPM:
                    await LOG_CHATS_.NEWPM.edit(
                        LOG_CHATS_.NEWPM.text.replace(
                            "**💌 #PESAN_BARU**",
                            f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                        )
                    )
                    LOG_CHATS_.COUNT = 0
                LOG_CHATS_.NEWPM = await yins.client.send_message(
                    ayiin.BOTLOG_CHATID,
                    f"**💌 #MENERUSKAN #PESAN_BARU**\n** • Dari : **{ayiin.mentionuser(sender.first_name , sender.id)}\n** • User ID:** `{chat.id}`",
                )
            try:
                if yins.message:
                    await yins.client.forward_messages(
                        ayiin.BOTLOG_CHATID, yins.message, silent=True
                    )
                LOG_CHATS_.COUNT += 1
            except Exception as e:
                ayiin.log.warn(str(e))


@ayiin.on(events.NewMessage(incoming=True, func=lambda e: e.mentioned))
@ayiin.on(events.MessageEdited(incoming=True, func=lambda e: e.mentioned))
async def log_tagged_messages(event: Message):
    if ayiin.BOTLOG_CHATID == -100:
        return
    xnxx = await event.get_chat()

    if not getVar("GRUPLOG"):
        return
    if (
        (isApprovedLog(xnxx.id))
        or (ayiin.BOTLOG_CHATID == -100)
        or (await event.get_sender() and (await event.get_sender()).bot)
    ):
        return
    full = None
    try:
        full = await event.client.get_entity(event.message.from_id)
        nameyins = full.first_name
        idyins = full.id
    except Exception as e:
        ayiin.log.info(str(e))
    messaget = media_type(event)
    resalt = f"<b>📨 #TAGS #MESSAGE</b>\n<b> • Dari : </b>{ayiin.htmlmentionuser(nameyins, idyins)}"
    if full is not None:
        resalt += f"\n<b> • Grup : </b><code>{xnxx.title}</code>"
    if messaget is not None:
        resalt += f"\n<b> • Jenis Pesan : </b><code>{messaget}</code>"
    else:
        resalt += f"\n<b> • 👀 </b><a href = 'https://t.me/c/{xnxx.id}/{event.message.id}'>Lihat Pesan</a>"
    resalt += f"\n<b> • Message : </b>{event.message.message}"
    await asyncio.sleep(0.5)
    if not event.is_private:
        await event.client.send_message(
            ayiin.BOTLOG_CHATID,
            resalt,
            parse_mode="html",
            link_preview=False,
        )


@ayiinCmd(pattern="savelog(?: |$)(.*)")
async def log(log_text):
    if ayiin.BOTLOG_CHATID:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(ayiin.BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"**#LOG / Chat ID:** {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(ayiin.BOTLOG_CHATID, textx)
        else:
            await eod(log_text, "**Apa yang harus saya simpan?**")
            return
        await eod(log_text, "**Berhasil disimpan di Grup Log**")
    else:
        await eod(
            log_text,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )


@ayiinCmd(pattern="log$")
async def set_no_log_p_m(event):
    if ayiin.BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if isApprovedLog(chat.id):
            approveLog(chat.id)
            await eod(
                event, "**LOG Chat dari Grup ini Berhasil Diaktifkan**", 15
            )


@ayiinCmd(pattern="nolog$")
async def set_no_log_p_m(event):
    if ayiin.BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if not isApprovedLog(chat.id):
            disapproveLog(chat.id)
            await eod(
                event, "**LOG Chat dari Grup ini Berhasil Dimatikan**", 15
            )


@ayiinCmd(pattern="pmlog (on|off)$")
async def set_pmlog(event):
    if ayiin.BOTLOG_CHATID == -100:
        return await eod(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if not getVar("PMLOG"):
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await eor(event, "**PM LOG Sudah Diaktifkan**")
        else:
            setVar("PMLOG", h_type)
            await eor(event, "**PM LOG Berhasil Dimatikan**")
    elif h_type:
        setVar("PMLOG", h_type)
        await eor(event, "**PM LOG Berhasil Diaktifkan**")
    else:
        await eor(event, "**PM LOG Sudah Dimatikan**")


@ayiinCmd(pattern="gruplog (on|off)$")
async def set_gruplog(event):
    if ayiin.BOTLOG_CHATID == -100:
        return await eod(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if not getVar("GRUPLOG"):
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await eor(event, "**Group Log Sudah Diaktifkan**")
        else:
            setVar("GRUPLOG", h_type)
            await eor(event, "**Group Log Berhasil Dimatikan**")
    elif h_type:
        setVar("GRUPLOG", h_type)
        await eor(event, "**Group Log Berhasil Diaktifkan**")
    else:
        await eor(event, "**Group Log Sudah Dimatikan**")


cmdHelp.update(
    {
        "log": f"**Plugin : **`log`\
        \n\n  »  **Perintah :** `{cmd}savelog`\
        \n  »  **Kegunaan : **__Untuk Menyimpan pesan yang ditandai ke grup pribadi.__\
        \n\n  »  **Perintah :** `{cmd}log`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}nolog`\
        \n  »  **Kegunaan : **__Untuk menonaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}pmlog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan pencatatan pesan pribadi__\
        \n\n  »  **Perintah :** `{cmd}gruplog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup pmlogger.__"
    }
)
