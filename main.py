import discord
import random
import requests
import json
from replit import db
from keep_alive import keep_alive
cryptolist = [key for key in db.keys()]


TOKEN='ODk3MDc1NTc5OTMxNzM4MTIz.YWQYvQ.d2r7oghpicEOx-SDP7mBppKt9I4' #discord TOken


client =discord.Client()  #create a client for discord

words=['hey','hi','hey bot']
answer=["Hello , How are you  ?",'kem 6o']

def get_quote():   #api connection
  response=requests.get("https://zenquotes.io/api/quotes/random")
  json_data=json.loads(response.text)
  quote= json_data[0]['q'] +"-" + json_data[0]['a']
  
  return(quote);


def getCryptoPrices(crypto):#crypto api add
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
  r = requests.get(url=URL)
  data = r.json() #convert the data in json
  print("Hello")
  for i in range(len(data)):# check the id(currency name) and get price of the currency
    if data[i]['id'] == crypto:
      return data[i]['current_price'];
  return None;



def getList():
  URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
  r = requests.get(url=URL)
  data = r.json()

  ans = []
  print("Hello")
  for i in range(len(data)):
    ans.push(data[i]['id'])
    # if data[i]['id'] == crypto:
      # return data[i]['current_price'];
  return ans;  


@client.event #when bot is ready
async def on_ready():
    print('bot is on fire as {0.user}'.format(client))


@client.event #when message is on chat
async def on_message(message):
    
    if message.author == client.user:
        return

    elif message.content.startswith('Hey'):
      await message.channel.send('Hello!')    

    elif message.content.startswith('motivation'):
      quote=get_quote()
      await message.channel.send(quote)

    elif message.content in [word for word in words]:
      await message.channel.send(random.choice(answer))
    
    elif message.content.startswith('list'):#get the list of currency which are stored db database
     cryptolist = [key for key in db.keys()]
     print(cryptolist)
     await message.channel.send(cryptolist)
    
    elif message.content in [coin for coin in db.keys() ]: #return the price of currency in format to discord
      await message.channel.send(f'```The current price of {message.content} is: {getCryptoPrices(message.content.lower())} USD```')
      print(message.content)
    else:
      await message.channel.send("what are you saying?")  
    
keep_alive()#hosting to website
    
client.run(TOKEN)  #run the TOKEN