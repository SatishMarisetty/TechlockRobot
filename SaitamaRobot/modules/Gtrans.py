from SaitamaRobot import pbot as app
from SaitamaRobot import arq
from SaitamaRobot.utils.errors import capture_err
from pyrogram import filters


@app.on_message(filters.command("tr") & ~filters.edited)
@capture_err
async def tr(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/tr [LANGUAGE_CODE]")
    lang = message.text.split(None, 1)[1]
    if not message.reply_to_message or not lang:
        return await message.reply_text(
            "Reply to a message with /tr [language code]"
            + "\nGet supported language list from here -"
            + " https://py-googletrans.readthedocs.io/en"
            + "/latest/#googletrans-languages"
        )
    reply = message.reply_to_message
    text = reply.text or reply.caption
    if not text:
        return await message.reply_text(
            "Reply to a text to translate it"
        )
    result = await arq.translate(text, lang)
    if not result.ok:
        return await message.reply_text(result.result)
    output = result.result.translatedText
    msg = f""" **Successfully translated to {lang}**
` {output} `"""
        await app.send_message(
                message.chat.id,
                text=msg
            )
