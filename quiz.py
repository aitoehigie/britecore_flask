from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb4JljDPwpSoB_dFiFvp8dtVLwOaMuJgGZeeZUUpDTnoo-wCVW2NuDapDU6L4D3p_3Px7zL_Ck_RDXIUVyi2dzzRsKY9Weavg-8iqjSXLvX05zhi3oZWdo8NZ7WiiXn42xrOGRql5OBONLcHS8_H7FIT30hmyOQJB0UoT97BmoJb1v0gg='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
