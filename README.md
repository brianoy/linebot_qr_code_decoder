# linebot decode QR code with heroku

A simple side project. If you create a linebot channel which is not the type of "login", then it is not possible for us to scan the qr code via "Liff". With PIL and pyzbar, We can scan the qr code and bar code ones user send the picture in the channel. In this demonstration, We deploy the app in the heroku, so we have to add the apt option in the buildpacks of heroku dashboard. Create a file named "apt" in the root directory, and add two lines of words in the file 

```libzbar0```

```libzbar-dev```
  
The picture user sent would save at under ./static temporarily. Heroku might clear the cache every dyno restart.(not sure)

## Requirements
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
**https<area>://github.com/heroku/heroku-buildpack-apt**
![image](https://user-images.githubusercontent.com/24865458/172822053-4568fe28-eab6-442f-8e46-212d4fdedaa7.png)

## Result
**Heroku had changed their terms of use, free Heroku Dynos are no longer available. This line-bot might not respond any more.**
**try it out** https://line.me/R/ti/p/%40127axkbn
  
![image](https://user-images.githubusercontent.com/24865458/172823672-d0bff46c-4e46-45d1-839d-14631aecc7f8.png)

