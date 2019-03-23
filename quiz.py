from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="

# Oh no! The code is going over the edge! What are you going to do?
message = b"gAAAAABclSebC3fJnYmg5Qcn1Z7yFkWpwiPnucrc4AFstA-NiyJ-3-MAbfqW8lxmkm7yhgnIhKdT28sZPP-vVfN0jctqm26UmeVrVdyz-TEK4__-O2_VOT-j5wMXdcGNnVXDu9afph-MwYuucFq3rBp1bRvcG9dj8Sc-CGDJJ6OVwIyxJQiXBWS7rf12a7qXYHHze5c2Tp__"


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
