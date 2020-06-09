
#Zeki Sağlam - 370702063

import os
import requests
import sys
from multiprocessing ieemport Pool
from multiprocessing import Process
import glob
import shutil
import urllib.request
import hashlib

print("The PID of the main process: ", os.getpid()) 
pid = os.fork()  # 

if (pid > 0):  # 
    os.wait()  # 

if (pid == 0):  # .
    print("The PID of the child process: ", os.getpid()) 




    array = [
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

    file_name = ["1.url", "2.url", "3.url", "4.url","5.url"] 


    def download_file(url, file_name):

        r = requests.get(url, stream=True)  
        if r.status_code == 200:  
            r.raw.decode_content = True  

            with open(file_name, 'wb') as f:  
                shutil.copyfileobj(r.raw,
                                   f)  

            print("File Downloaded and checked", file_name)  
        else:
            print("File can not Downloaded Error !")  
            p = multiprocessing.Pool(processes=6)
            file_hashes_list = p.map(hashFile, files)

           
            for file_hash in file_hashes_list:
                pushDictAndCheckDuplicates(file_hash)


    files = ["1.url", "2.url", "3.url", "4.url", "5.url"]
    checksum = [hashlib.md5(open("1.url", 'rb').read()).hexdigest(),
                hashlib.md5(open("2.url", 'rb').read()).hexdigest(),
                hashlib.md5(open("3.url", 'rb').read()).hexdigest(),
                hashlib.md5(open("4.url", 'rb').read()).hexdigest(),
                hashlib.md5(open("5.url", 'rb').read()).hexdigest()]

    for x in range(len(array)):  
        download_file(array[x], file_name[
            x]) 




    os._exit(0) 





