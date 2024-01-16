
import random, asyncio

from DCManeger import pbot
from pyrogram import filters


loveShayri = [
    "Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...",
    "Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...",
    "Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...",
    "Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...",
    "Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...",
    "Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...",
    "Udas shamo me wo lout\nKar aana bhul jate hain..❤️\nKar ke khafa mujhko wo\nManana bhul jate hain....💞😌",
    "Chalo phir yeha se ghar kaise jaoge...?\n\n🙂🔪Ye humare akhri mulakat h kuch kehna chahoge?🙃❤️\n😔❤️M to khr khel rhi thi tum to sacha isq karte the na😓🔪\nKaise karte karke dekhau..😷🤧\n🤒❤️Tum to kehte the m bichrungi to mar jaooge marke dekhau😖❤️\n😌✨Ek bhola bhala khelta huya dil tut gyi na....🙂❤️\n👀❤️....Ladka chup kyu pata ..?\n😊❤️ ....ladki to margyi naa",
    "Toote huye dil ne bhi uske liye dua\n maangi,\nmeri har saans ne uske liye khushi\n maangi,\nna jaane kaisi dillagi thi uss bewafa se,\naakhiri khwahish mein bhi uski hi wafa maangi.........✍\n\n~ ♡",
    "Main waqt ban jaaun tu ban jaana koi \nlamha, \nMain tujhnme gujar jaaun tu mujhme gujar \njana............✍ \n\n~ ♡ 💘",
    "Udaas lamhon 😞 ki na koi yaad\nrakhna, \ntoofan mein bhi wajood apna sambhal\nRakhna,\nkisi ki zindagi ki khushi ho tum,\n🥰  bs yehi soch tum apna khayal\nRkhna,\n\n~ ♡ 💘❤️",
]


@pbot.on_message(filters.command("loveshayri"))

async def love_shayri(b,m):
    "dont remove this line \n credit  |n github : AbhiModszYT"
    love = random.choice(loveShayri)      
    await m.reply_text(love)
__mod_name__="​​Sʜᴀʏʀɪ"
__help__="""ꜱᴇɴᴅ ʀᴀɴᴅᴏᴍ ꜱʜᴀʏʀɪ
❍ /loveshayri : ʟᴏᴠᴇ ꜱʜᴀʏʀɪ"""
