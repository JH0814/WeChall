plain = "2E 56 56 4B 20 51 56 49 13 20 60 56 5C 20 5A 56 53 5D 4C 4B 20 56 55 4C 20 54 56 59 4C 20 4A 4F 48 53 53 4C 55 4E 4C 20 50 55 20 60 56 5C 59 20 51 56 5C 59 55 4C 60 15 20 3B 4F 50 5A 20 56 55 4C 20 5E 48 5A 20 4D 48 50 59 53 60 20 4C 48 5A 60 20 5B 56 20 4A 59 48 4A 52 15 20 3E 48 5A 55 0E 5B 20 50 5B 26 20 18 19 1F 20 52 4C 60 5A 20 50 5A 20 48 20 58 5C 50 5B 4C 20 5A 54 48 53 53 20 52 4C 60 5A 57 48 4A 4C 13 20 5A 56 20 50 5B 20 5A 4F 56 5C 53 4B 55 0E 5B 20 4F 48 5D 4C 20 5B 48 52 4C 55 20 60 56 5C 20 5B 56 56 20 53 56 55 4E 20 5B 56 20 4B 4C 4A 59 60 57 5B 20 5B 4F 50 5A 20 54 4C 5A 5A 48 4E 4C 15 20 3E 4C 53 53 20 4B 56 55 4C 13 20 60 56 5C 59 20 5A 56 53 5C 5B 50 56 55 20 50 5A 20 50 59 59 4D 4F 48 56 59 49 48 56 55 15"

ascii_arr = list(plain.split())
S = ""
for i in range(len(ascii_arr)):
    S += chr(int(ascii_arr[i], 16))

for j in range(128):
    message = ""
    for i in range(len(S)):
        message += chr((ord(S[i]) + j) % 128)
    print("Key : " + str(j) + " Message : " + message)