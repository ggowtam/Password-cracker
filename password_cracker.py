import crypt
import sys


def testPass(cryptPass, dictfile):
    file = open(dictfile, 'r')
    for w in file:
        if crypt.crypt(w.strip(), cryptPass[:3]) == cryptPass:
            print("[+] Found Password: " + w + "\n")
            return  # return after password found
    print("[-] Password Not Found.\n")


def main(passwdfile, dictfile):  # opens the password file and call the test function for each password
    with open(passwdfile, 'r') as passw:
        words = passw.readlines()
        for line in words:
            dicti = line.split(":")
            print("Username:", dicti[0])
            cryptPass = dicti[1].strip()
            print("Hashed Password:", cryptPass)
            testPass(cryptPass, dictfile)


if __name__ == "__main__":
    passwdfile = sys.argv[1]
    dictfile = sys.argv[2]
    main(passwdfile, dictfile)
