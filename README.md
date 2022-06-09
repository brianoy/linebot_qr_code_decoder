# using linebot to decode the qr/bar code via heroku inside the chatroom
  一個簡單的小作品，因為當初創立linebot時，不是選擇login的頻道類型，所以不能用Liff來掃描qr code，不過藉由heroku可以由line bot機器人實現由heroku app來解碼qr/bar code的訊息，因為上傳到heroku，所以需要在buildpack中加入apt，以及根目錄內aptfile內加入libzbar0、libzbar-dev

## requirements
1. A heroku app **(https<area>://dashboard.heroku.com/apps)**

2. A line bot channel in line developer console 

3. Enable the webhook function in your line bot channel console **(https<area>://manager.line.biz/account/[your_linebot_id]/setting)**
  
4. Link the webhook in the line bot channel console to **https<area>://[your_app_name].herokuapp.com/callback**


## Add the env config manually
Copy the CHANNEL_SECRET and CHANNEL_ACCESS_TOKEN into the env config 
![image](https://user-images.githubusercontent.com/24865458/172822152-c5c3c5ee-c135-4857-a692-052e23556956.png)

## Add the build pack
**heroku/python**
and
**https://github.com/heroku/heroku-buildpack-apt**
![image](https://user-images.githubusercontent.com/24865458/172822053-4568fe28-eab6-442f-8e46-212d4fdedaa7.png)

## Result
**try it out** https://line.me/R/ti/p/%40127axkbn
  
![image](https://user-images.githubusercontent.com/24865458/172823672-d0bff46c-4e46-45d1-839d-14631aecc7f8.png)

