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

`docker pull elgalu/selenium`

`docker build . --tag [name]`

This will build the docker file and you will then have a local image, now run:

`docker run -it --name [whatever] [name] bash`

You will then have to run the `init.py` script.

Finally run the following and then exit the docker container:

`crond -l 2 -f` To run crond with log level 2

Hit`Ctrl-Z` To stop crond

`bg` To run previously stopped command in background

Hit `Ctrl-p` then `Ctrl-q` To exit interactive mode for docker

You will know if the process is working if you get an email + text with a list of your previous grades.
This initial email and text message will be sent everytime you run the container (no persistant storage).
Afterwards it will send you grades when they update.
