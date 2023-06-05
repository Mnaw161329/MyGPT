import openai
from googletrans import Translator

openai.api_key = "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"

Qs = []

print(" Welcome to MyGPT!!!" + "\n")

def gptMy(Q):
    T = Translator()
    
    QTs = T.translate(Q, dest="en").text
    
    Qs.append({"role": "user", "content": QTs})
    ans = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=Qs
    )
    ansC = ans.choices[0].message.content
    Qs.append({"role": "assistant", "content": ansC})

    ansCT = T.translate(ansC, src="en", dest="my").text 
    return ansCT

while True:
    question = input(" Question >>> ")
    if (question == "exit"):
        print("\n" + " MyGPT >>> ကောင်းသောနေ့လေးဖြစ်ပါစေ။")
        break
    else:
        print("\n" + " MyGPT >>> " + gptMy(question) + "\n")

# Qs  = Questions
# Q   = Question
# T   = Translate
# C   = Cleaned
# ans = Answer
