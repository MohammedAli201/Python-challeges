""" files used to read and write data to files; this example will be log system record every user login in file system """
import time
name_user_login = input("what is your name : ")
second = time.time()
time_loggedIn = time.ctime(second)

with open("logins.txt", "a") as file:
    file.write(f"Usier {name_user_login}  at {time_loggedIn} \n")