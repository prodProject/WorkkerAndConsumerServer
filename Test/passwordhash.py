import bcrypt
print("shub@123")
#hased_pass = bcrypt.hashpw("shub@123", bcrypt.gensalt())
#print(hased_pass)
dcrypt = bcrypt.checkpw("shub@123", "$2a$12$.LErnnFTlG5HBK649RoUM.1Kgaa8VrmiUmSk.uHavscYBvDKKve7h")
print(dcrypt)
