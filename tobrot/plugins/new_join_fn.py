#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>🙋🏻‍♂️ Hello dear!\n\n This Is A Leech Bot .This Chat Is Not Supposed To Use Me</b>\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Github', url='https://github.com/AmirulAndalib')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    if UPLOAD_AS_DOC:
        utxt = "Document"
    else:
        utxt = "Streamable"
    await message.reply_text(
        """<b>𝐇𝐞𝐥𝐥𝐨 𝐚𝐧𝐝 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐋𝐞𝐜𝐜𝐡𝐢𝐧𝐠 𝐇𝐮𝐛 ✌️\n 𝐞𝐧𝐣𝐨𝐲 𝐥𝐞𝐞𝐜𝐡𝐢𝐧𝐠 𝐚𝐧𝐝 𝐦𝐢𝐫𝐫𝐨𝐫𝐢𝐧𝐠</i>""",
        disable_web_page_preview=True,
    )
