
def jonatish(status: str,ism: str, texnalogiya: str, tg_username: str, aloqa: str, hudud: str, narx: str, kasb: str, vaqt: str, maqsad: str, yosh: int=None, ustoz: str=None):
    jonatish = ''
    if status == "Ish joyi":
        jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"π Ishchi: <b>{ism}</b>\n" \
            f"π Yoshi: <b>{yosh}</b>\n" \
            f"π Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"πΊπΏ Telegram: @{tg_username}\n" \
            f"π Aloqa: {aloqa}\n" \
            f"π Hudud: {hudud}\n" \
            f"π° Narxi: {narx}\n" \
            f"π¨π»βπ» Kasbi: {kasb}\n" \
            f"π° Murojaat qilish vaqti: {vaqt}\n" \
            f"π Maqsad: {maqsad} \n\n" \
            f"#hodim #{hudud.strip()}" \

    elif status == "Ustoz":
        jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"π Ishchi: <b>{ism}</b>\n" \
            f"π Yoshi: <b>{yosh}</b>\n" \
            f"π Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"πΊπΏ Telegram: @{tg_username}\n" \
            f"π Aloqa: {aloqa}\n" \
            f"π Hudud: {hudud}\n" \
            f"π° Narxi: {narx}\n" \
            f"π¨π»βπ» Kasbi: {kasb}\n" \
            f"π° Murojaat qilish vaqti: {vaqt}\n" \
            f"π Maqsad: {maqsad} \n\n" \
            f"#shogirt #{hudud.strip()}" \

    elif status == "Shogirt":
        jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"π Ishchi: <b>{ism}</b>\n" \
            f"π Yoshi: <b>{yosh}</b>\n" \
            f"π Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"πΊπΏ Telegram: @{tg_username}\n" \
            f"π Aloqa: {aloqa}\n" \
            f"π Hudud: {hudud}\n" \
            f"π° Narxi: {narx}\n" \
            f"π¨π»βπ» Kasbi: {kasb}\n" \
            f"π° Murojaat qilish vaqti: {vaqt}\n" \
            f"π Maqsad: {maqsad} \n\n" \
            f"#shogirt #{hudud.strip()}" \


    else:
        jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"π Sherik: <b>{ism}</b>\n" \
            f"π Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"πΊπΏ Telegram: @{tg_username}\n" \
            f"π Aloqa: {aloqa}\n" \
            f"π Hudud: {hudud}\n" \
            f"π° Narxi: {narx}\n" \
            f"π¨π»βπ» Kasbi: {kasb}\n" \
            f"π° Murojaat qilish vaqti: {vaqt}\n" \
            f"π Maqsad: {maqsad} \n\n" \
            f"#sherik #{hudud.strip()}" \




    texnalogiyalar = texnalogiya.split(',')
    for t in list(texnalogiyalar):
        jonatish += f' #{t.strip().lower()}'

    jonatish += f"\n\nyozuvchi: @Asadbek_Muxtorov"

    return jonatish
