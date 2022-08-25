from aiogram.dispatcher.filters.state import State, StatesGroup

class Holatlar(StatesGroup):
    #sherik_kerak_holati
    sherik_ism_holati = State()
    sherik_texnalogiya_holati = State()
    sherik_aloqa_holati = State()
    sherik_hudud_holati = State()
    sherik_narx_holati = State()
    sherik_kasb_holati = State()
    sherik_vaqt_holati = State()
    sherik_maqsad_holati = State()
    sherik_tasdiqlash_holati = State()

    #ish_joyi_kerak_holati
    ish_texnalogiya_holati = State()
    ish_ism_holati = State()
    ish_yosh_holati = State()
    ish_aloqa_holati = State()
    ish_hudud_holati = State()
    ish_narx_holati = State()
    ish_kasb_holati = State()
    ish_vaqt_holati = State()
    ish_maqsad_holati = State()
    ish_tasdiqlash_holati = State()

    #ustoz_kerak_holati
    ustoz_texnalogiya_holati = State()
    ustoz_ism_holati = State()
    ustoz_yosh_holati = State()
    ustoz_aloqa_holati = State()
    ustoz_hudud_holati = State()
    ustoz_narx_holati = State()
    ustoz_kasb_holati = State()
    ustoz_vaqt_holati = State()
    ustoz_maqsad_holati = State()
    ustoz_tasdiqlash_holati = State()


    hodim_kerak_holati = State()
    ustoz_kerak_holati = State()
    shogirt_kerak_holati = State()