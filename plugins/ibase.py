#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import *
from Script import txt

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        txt.START_TXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help", callback_data="help"), InlineKeyboardButton("About", callback_data="about")]
        ])
    )


@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(
            txt.HELP_TXT, 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Back', callback_data='back'),
                        InlineKeyboardButton('About', callback_data='about')
                    ]
                ]
            )
        )

    
    elif query.data == "about":
        await query.message.edit_text(
            txt.ABOUT_TXT, 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Help', callback_data='help')
                    ],
                    [
                        InlineKeyboardButton('Source Code', url="https://github.com/Dypixx/Instaloader"),
                        InlineKeyboardButton('Back', callback_data='back')
                    ]
                ]
            )
        )

    
    elif query.data == "back":
        await query.message.edit_text(
            txt.START_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help", callback_data="help"),
                        InlineKeyboardButton("About", callback_data="about")
                    ]
                ]
            )
        )
    
    elif query.data == "close":
        await query.answer("Tʜᴀɴᴋs ғᴏʀ ᴄʟᴏsɪɴɢ ❤️", show_alert=True)
        await query.message.delete()