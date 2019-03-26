from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcmZNjB1CqmvCWcO8ByvVTKas3rKh5Py67Al5tOma1TtHeQBQJi55SmpN86uNXNFX7_clMNLWCB5HzqkcOkkz3V7KzxeFo7q4ZNIGsa4tb82l0sVTcS2zCW7-Rk7kcnkLl_Jsw2F98JMpnnLa4ZrlZqPoteBSgjBr7vmk4Z5GXIpAqPU5TBk2K51m2RE47HogruLsO'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
