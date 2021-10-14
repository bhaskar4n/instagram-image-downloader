import requests
import shutil

r = requests.get('https://instagram.fmaa2-2.fna.fbcdn.net/v/t51.2885-15/e35/s320x320/13561960_305737823093135_848970822_n.jpg', stream=True)
if r.status_code == 200:
    with open("imge.jpg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        outfile.write(r.content)







#urllib.request.urlretrieve('https://instagram.fmaa2-2.fna.fbcdn.net/v/t51.2885-15/e35/s320x320/13561960_305737823093135_848970822_n.jpg','imagge.jpg')




#url = 'https://instagram.fmaa2-2.fna.fbcdn.net/v/t51.2885-15/e35/s320x320/13561960_305737823093135_848970822_n.jpg'
#r = requests.get(url)
#with open('5.jpg', 'wb') as outfile:
 #   outfile.write(r.content)
