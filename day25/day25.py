from sys import path

with open(path[0] + '/input.txt') as f:
    door_pub, card_pub = [int(x) for x in f]

def find_loop_size(pub_key):
    subject, loop_size = 7, 1
    while subject != pub_key:
        subject = subject * 7 % 20201227
        loop_size += 1
    return loop_size

door_loop = find_loop_size(door_pub)
enc_key = 1
for i in range(door_loop):
    enc_key = enc_key * card_pub % 20201227
print(enc_key)