
import requests
from telebot import telebot,TeleBot
from telebot.types import *
from telebot.util import user_link


markup = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
markup.add(group,channel)


bot = telebot.TeleBot("<Your Bot API>",parse_mode="HTML")

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://result.eaes.et',
    'priority': 'u=1, i',
    'referer': 'https://result.eaes.et/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',}

@bot.message_handler(commands=["start"])
def greet(msg):
    user = f"{user_link(msg.from_user)}"
    bot.reply_to(msg,f"""Hello {user} send your admission number and first name separated by comma \nexample: 6281167,Mahitem """,reply_markup=markup)

@bot.message_handler(func=lambda m:True)
def sendResult(msg):
    info = msg.text.split(",")

    id = info[0]
    name = info[1]
    """print(id)
    print(info[1])"""

    json_data = {
    'admissionNo': f'{id}',
    'firstName': f'{name}',
    'turnstileToken': '0.-w3n8Caa-fdbIqBYLv0OoHX0owfCkEcz3ZxyTEtgFVJ10KF4AEVgWcSTTbzkfqHsQQeHuBfb-s3Bssook7dg3ZMIKxNps1pp5egWxQRLvci_8O8vV3E-J6CK0-lGO_Leu3n5If3Sje9CsYlJvrsBrWGvYiRBpgrWRn-XCcJy-WNBgIuqBon0qh-z6GNRqC6oqKyy725NbybUIhUss8FQtSoR--WoJWkJigaWcLQaOI4LySJQI_BjC86-39b1TZnU-w8iieUQORZBkSDpgKymE3xiJN_kb8_FSKViTTLA1YLp3o0YkdWiDuR6g34z1spLM-Zc5nqIJm3MmAfkIdTwKHWCYkPhZHMMRcIKL4zs1KqWjzvBJ8vTaLHPXh4j2BA_E9E126sgYVSioeoA57w36ET7-3s-gzcuBYkguTbCdwYubAI_llCdG8eCQ7KfCRfdhgPxhzEKGxFvRs5oNpxvz258ukK6qONFiYMpML1iEKEzoPebabcczkLsrl9PHtD2XEfqp97jpgRsWii2lRdqDUwPou3IhUvTpFYlDeLZOk9DKagXEERvw7S9xfAajyPPU1BM6Tg0B6uNl8OmSPMXZUJ6veHUOYJw8xWTo991orGxVj1ZHkC69KfuLRnTDfjLsRY_-n9TyZXeuzqSiPca-ol88-icgOUh92VBfDMnYAPfl_s1DzWIJKEm-owGRaOQ5D1LIVQfONtXwInH40ThlyZ1VkRQI4DlKJnfWzYHNQrf2IryXXCqd0G-RxapPWAOIyyNc89NqMsNyAxwU84rSNFusge7k9n_bdaS9SENlcRdWvjBL1MJINlwwH4fOk0mLKa1nVmuOXCU2ea4Bl_jNpqqEp-gWriHiNkPFudcJ3v4sjLjuhIG3_LltE8BZWP48Mw6z9o9Q4tgGL5YDYKWznWmniRUzvmLsoYWt-eVj10.mvUipRAiZ6dRQD04BcwHAg.39c383045474e338065d544c86dad5ba242a04b7b4e9766ef36426b98e397442',}

    response = requests.post('https://api.eaes.et/api/v1/results/web', headers=headers, json=json_data)
    data = response.json()
    # print(response.json())

    fullName = data["studentInfo"]["FullName"]
    admissionID = data["studentInfo"]["Admission_No"]
    sex = data["studentInfo"]["Sex"]
    stream = data["studentInfo"]["Stream"]
    printData = data["studentInfo"]["print"]
    photoUrl = data["studentInfo"]["Photo"]



    resultData = data.get("results")
    
    maths = resultData[0]["Subject"]
    mathResult = resultData[0]["Result"]
    eng = resultData[1]["Subject"]
    engResult = resultData[1]["Result"]
    apt = resultData[2]["Subject"]
    aptResult = resultData[2]["Result"]
    phy = resultData[3]["Subject"]
    phyResult = resultData[3]["Result"]
    chem = resultData[4]["Subject"]
    chemResult = resultData[4]["Result"]
    bio = resultData[5]["Subject"]
    bioResult = resultData[5]["Result"]

    total = resultData[6]["Subject"]
    result = resultData[6]["Result"]
    fullData = f"""Full Name: {fullName}\nAdmissionID: {admissionID}\nGender: {sex} Stream:{stream}\n\n{maths}:{mathResult}\n{eng}:{engResult}\n{apt}:{aptResult}\n{phy}:{phyResult}\n{chem}:{chemResult}\n{bio}:{bioResult}\n{total}:{result} """

    

    mk = InlineKeyboardMarkup()
    downloadData = InlineKeyboardButton("Download Result",url=printData)
    mk.add(downloadData)
    bot.send_photo(chat_id=msg.chat.id,photo=photoUrl,caption=fullData,reply_markup=mk)
    # bot.send_document(msg.chat.id,printData)

bot.infinity_polling()



