import os

def main():
    i=0
    path= "c:/Users/larat/Documents/Tomi Files/test"
    for filename in os.listdir(path):
        my_dest="img"+str(i)+".jpg"
        my_source = path+filename
        my_dest = path+my_dest
        os.rename(my_source,my_dest)
        i+=1
