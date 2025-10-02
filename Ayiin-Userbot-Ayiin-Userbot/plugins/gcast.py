# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.errors import FloodWaitError

from pyAyiin import ayiin, cmdHelp
from pyAyiin.config import GCAST_BLACKLIST
from pyAyiin.decorator import ayiinCmd
from pyAyiin.utils import eod, eor
from pyAyiin.database.blGcast import (
    addGcastGroup,
    addGcastPrivate,
    delGcastGroup,
    delGcastPrivate,
    getGcastGroup,
    getGcastPrivate,
)

from . import cmd


@ayiinCmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    BLACKLIST_GCAST = getGcastGroup()
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
    else:
        return await eod(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await eor(event, "`Sedang Mengirim Mohon Bersabar... Kalo Limit Jangan Salahin Saya...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** {done} **Grup Tod.**\n**Sorry Tod Gagal Mengirim Pesan Ke** {er} **Grup.**"
    )


@ayiinCmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    BLACKLIST_GCAST = getGcastPrivate()
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
    else:
        return await eod(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await eor(event, "`Sedang Mengirim Mohon Bersabar... Kalo Limit Jangan Salahin Saya...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in ayiin._devs and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** {done} **Chat Tod.**\n**Sorry Tod Gagal Mengirim Pesan Ke** {er} **Chat.**"
    )


@ayiinCmd(pattern="blchat$")
async def sudo(event):
    me = await event.client.get_me()
    BLACKLIST_GCAST = getGcastGroup()
    BLACKLIST_GCAST_PRIVATE = getGcastPrivate()
    textGroup = '\n'
    for bl in BLACKLIST_GCAST:
        textGroup += f"   » {bl}\n"

    textPrivate = '\n'
    for bl in BLACKLIST_GCAST_PRIVATE:
        textPrivate += f"   » {bl}\n"

    await eor(
        event, 
        f"""
**🔮 Blacklist GCAST:** `Enabled`

📚 **Blacklist Group:**
{textGroup}

📚 **Blacklist Private:**
{textPrivate}


Ketik `{cmd}addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast."""
    )


@ayiinCmd(pattern="addblacklist (.*)")
async def add(event):
    command = event.pattern_match.group(1)
    if not command:
        return await eod(event, f"**Berikan saya kata kunci g/p. Contoh :** `{cmd}addblacklist g` atau `{cmd}addblacklist p`")

    xxnx = await eor(event, '**Memproses...**')
    if command == "g":
        gcastGroup = getGcastGroup()
        if event.chat_id in gcastGroup:
            await eod(
                event,
                "**Grup ini sudah ada dalam daftar blacklist gcast.**"
            )
            return
        else:
            addGcastGroup(event.chat_id)
            await xxnx.edit(
                f"**Berhasil Menambahkan** `{event.chat_id}` **ke daftar blacklist gcast grup.**"
            )

    elif command == "p":
        gcastPrivate = getGcastPrivate()
        if event.chat_id in gcastPrivate:
            await eod(
                event,
                "**ID Pengguna ini sudah ada dalam daftar blacklist gcast.**"
            )
            return
        else:
            addGcastPrivate(event.chat_id)
            await xxnx.edit(
                f"**Berhasil Menambahkan** `{event.chat_id}` **ke daftar blacklist gcast pribadi.**"
            )

    else:
        await eod(event, f"**Berikan saya kata kunci g/p. Contoh :** `{cmd}addblacklist g` atau `{cmd}addblacklist p`")


@ayiinCmd(pattern="delblacklist(?:\\s|$)([\\s\\S]*)")
async def _(event):
    command = event.pattern_match.group(1)
    if not command:
        return await eod(event, f"**Berikan saya kata kunci g/p. Contoh :** `{cmd}addblacklist g` atau `{cmd}addblacklist p`")
    
    xxx = await eor(event, '**Memproses...**')
    
    if command == "g":
        gcastGroup = getGcastGroup()
        if event.chat_id in gcastGroup:
            delGcastGroup(event.chat_id)
            await xxx.edit(f"**Berhasil Menghapus** `{event.chat_id}` **dari daftar blacklist gcast grup.**"
            )
        else:
            await eod(
                xxx,
                "**Grup ini tidak ada dalam daftar blacklist gcast.**",
                time=45
            )

    elif command == "p":
        gcastPrivate = getGcastPrivate()
        if event.chat_id in gcastPrivate:
            delGcastPrivate(event.chat_id)
            await xxx.edit(f"**Berhasil Menghapus** `{event.chat_id}` **dari daftar blacklist gcast pribadi.**"
            )
        else:
            await eod(
                xxx,
                "**ID Pengguna ini tidak ada dalam daftar blacklist gcast.**",
                time=45
            )

    else:
        await eod(event, f"**Berikan saya kata kunci g/p. Contoh :** `{cmd}addblacklist g` atau `{cmd}addblacklist p`")


cmdHelp.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  »  **Perintah :** `{cmd}gcast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  »  **Perintah :** `{cmd}blchat`\
        \n  »  **Kegunaan : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}addblacklist`\
        \n  »  **Kegunaan : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}delblacklist`\
        \n  »  **Kegunaan : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  •  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


cmdHelp.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  »  **Perintah :** `{cmd}gucast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
