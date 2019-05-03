MyConcordiaGrades
=================

This project assumes you have docker and basic understanding on how to work with docker.

#### IMPORTANT NOTE: 

We are not responsible if someone takes your computer and looks at this file. Right now nothing is compiled or hashed 
so your password is stored in plain text.

Also, using the email-to-SMS service that many cell phone carriers provide can result in extra costs on your phone bill; use at your own discretion.

For the "Gmail username/password to send texts/emails from" we recommend that you create a dummy email.
For that account, you must have "Allow less secured apps" enabled.

You can do so here: [link](https://www.google.com/settings/security/lesssecureapps)

Setting up
====================

Run the following docker commands:

`docker build . --tag [name]`

This will build the docker file and you will then have a local image, now run:

`docker run -d -e (Environment Variables) --name [whatever] [name] bash`

Currently configurable environment variables:

```
'USERNAME' = You MyConcordia username
'PASSWORD' = Your MyConcordia password
'EMAIL' = Your dummy email
'EMAIL_PASSWORD' = Your dummy emails password
'TEXT_ME' = 0 or 1
'EMAIL_ME' = 0 or 1
'PHONE_NUMBER' = Your phone number
'PROVIDER' = Your phone provider, check smsGateways.txt
'RECEIVE_EMAIL' = Your email you want to receive an email at
```

Example of run command:

`docker run -d -e USERNAME="USER" -e PASSWORD="PASS." -e EMAIL="dummy@gmail.com" -e EMAIL_PASSWORD="dummypass" -e TEXT_ME=1 -e EMAIL_ME=1 -e PHONE_NUMBER="5141234567" -e PROVIDER="Koodo Mobile" -e RECEIVE_EMAIL="myactualemail@gmail.com" --name grades grades`

You will know if the process is working if you get an email + text with a list of your previous grades.
This initial email and text message will be sent everytime you run the container from scratch (no persistant storage).
Afterwards it will send you grades when they update.
