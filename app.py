#OpenAI için library
import openai
#DALL-E için library
import urllib.request
#Image process
from PIL import Image

# OpenAI API key'i buraya girin
openai.api_key = "Write Your API here"


def chatGPT(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50, #Maksimum Kelime Sayısı, kutucuğa girilebilen kelime sayısı ile eşitlenecek.
        n=1,
        stop=None,
        temperature=0.5, 
        #ChatGPT'nin ne kadar yaratıcı olacağını seçer.
        #Daha yüksek sıcaklıklar daha yaratıcı ancak daha az tutarlı olacaktır. Maksimum değer 1. Minimum değer 0.
    )
    
    # Tamamlanan metnin değişkene tanımlanması
    answer = response.choices[0].text.strip()
    
    return answer


def dall_e(image):
    
    response = openai.Image.create(
        prompt=image,
        n=1,
        size="1024x1024"
        )
    
    image_url = response['data'][0]['url']
    
    return image_url


#Dall-E Deneme Kısmı
image = input("Please decribe your image: ")
req = urllib.request.urlretrieve(dall_e(image), "answer.png")
img = Image.open("answer.png")
img.show()

#ChatGPT Deneme
#for i in range(0,10): #For içerisine alınırsa 10 seferlik bir karşılıklı konuşma yaratılabilir.
inp = input("Write your question: ")
print(chatGPT(inp))
    
