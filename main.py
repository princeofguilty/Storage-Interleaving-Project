from Storage import Storage
from Packetize import packetize
from packets import packet
from Network import network
from file import file
from map import map
import os

os.system("cls")

print("\n\t----Ordinary Storage System----\n")

o_storage = Storage()
o_network = network()

o_network.set_storages([o_storage], map())

file1 = file()
file1.record("00000111111101111001010110100001100001100001111010010001010110110100101110111011000110101011111101001001101011001011101000011000011011110010000111111000111000011011111000010110011110111101010101100001x", "file1")

o_network.send_file(file1)
o_network.send_file(file("data ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "fileX"))
o_network.send_file(file("data 2", "file2"))
o_network.send_file(file("IMPORTANT MESSAGE: MEET ME AT 9 OCLOCK", "file3"))
o_network.send_file(file("data 4", "file4"))
o_network.send_file(file("SERVER PASSWORD HAS BEEN CHANGED INTO: AdminAdmin2004", "file5"))
o_network.send_file(file("data 6", "file6"))

o_storage.show_content()

print("\n\t----Ordinary Storage System File Retrieval----\n")
o_network.retrieve_file("fileX")
print("\n\t----Done----\n")


print("\n\t----Interleaving Storages System----\n")

S1 = Storage()
S2 = Storage()
S3 = Storage()

list_of_storages = [S1, S2, S3]

N1 = network()
N1.set_storages(list_of_storages, map())

file1 = file()
file1.record("00000111111101111001010110100001100001100001111010010001010110110100101110111011000110101011111101001001101011001011101000011000011011110010000111111000111000011011111000010110011110111101010101100001x", "file1")

N1.send_file(file1)
N1.send_file(file("data ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "fileX"))
N1.send_file(file("data 2", "file2"))
N1.send_file(file("IMPORTANT MESSAGE: MEET ME AT 9 OCLOCK", "file3"))
N1.send_file(file("data 4", "file4"))
N1.send_file(file("SERVER PASSWORD HAS BEEN CHANGED INTO: AdminAdmin2004", "file5"))
N1.send_file(file("data 6", "file6"))


print("\n\n\t---showing storages content---\n")
print("\n\n\t---Storage 1---\n"); S1.show_content()
print("\n\n\t---Storage 2---\n"); S2.show_content()
print("\n\n\t---Storage 3---\n"); S3.show_content()


print("\n\n\t---retrieving files---\n")
N1.retrieve_file("fileX")
N1.retrieve_file("file3")
N1.retrieve_file("file1")
