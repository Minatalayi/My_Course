from getpass import getpass
import instaloader


username=input("username: ")
password=getpass("password: ")

L=instaloader.Instaloader()
L.login(username)
profile=instaloader.Profile.from_username(L.context, "mina_talayi")

f=open("followers.txt","r")
old_followers=[]
for line in f:
    old_followers.append(line.strip())
    f.close()

new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower.username)

for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)

f=open("followers.txt","w")
for new_follower in new_followers:
    f.write(new_follower + "\n")
f.close()



