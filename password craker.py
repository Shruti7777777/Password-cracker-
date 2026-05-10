import hashlib
from urllib.request import urlopen
import urllib.request
def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordist, error:",e)
        exit()
    return wordlistfile
        

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! Got your password it is:", guess_password,
                  "\n please change this, it was easy to guess it :)")
            exit()

############## append the below code #################

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = '123456'
actual_password_hash = hash(actual_password)

wordlist = readwordlist(url).decode('UTF-8')
guesspsswordlist = wordlist.split('\n')

#Running the Brute Force attack
bruteforce(guesspsswordlist, actual_password_hash)
#It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it wasnot in mywordlist, this is 'good news! you win :)")


