
def jonatish(ism: str, texnalogiya: str, tg_username: str, aloqa: str, hudud: str, narx: str, kasb: str, vaqt: str, maqsad: str, yosh: int=None, ustoz: str=None):
    jonatish = ''
    if yosh is not None:
        jonatish = f"<b>Ish joyi kerak:</b>\n\n" \
            f"🏅 Ishchi: <b>{ism}</b>\n" \
            f"🕑 Yoshi: <b>{yosh}</b>\n" \
            f"📚 Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"🇺🇿 Telegram: @{tg_username}\n" \
            f"📞 Aloqa: {aloqa}\n" \
            f"🌐 Hudud: {hudud}\n" \
            f"💰 Narxi: {narx}\n" \
            f"👨🏻‍💻 Kasbi: {kasb}\n" \
            f"🕰 Murojaat qilish vaqti: {vaqt}\n" \
            f"🔎 Maqsad: {maqsad} \n\n" \
            f"#hodim" \


    else:
        jonatish = f"<b>Sherik kerak:</b>\n\n" \
            f"🏅 Sherik: <b>{ism}</b>\n" \
            f"📚 Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"🇺🇿 Telegram: @{tg_username}\n" \
            f"📞 Aloqa: {aloqa}\n" \
            f"🌐 Hudud: {hudud}\n" \
            f"💰 Narxi: {narx}\n" \
            f"👨🏻‍💻 Kasbi: {kasb}\n" \
            f"🕰 Murojaat qilish vaqti: {vaqt}\n" \
            f"🔎 Maqsad: {maqsad} \n\n" \
            f"#sherik" \




    texnalogiyalar = texnalogiya.split(',')
    for t in list(texnalogiyalar):
        jonatish += f' #{t.strip().lower()}'

    jonatish += f"\n\nyozuvchi: @Asadbek_Muxtorov"

    return jonatish
