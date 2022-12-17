# with open('ChatAnaghaAnne.txt', encoding="utf8") as f:
    # for line in  
    # lines = f.readline()
    # print(line)
    # print("hi")

file1 = open('ChatAnaghaAnne.txt', encoding='utf8')
count = 0
for line in file1:
    message = line.split(',')[0]
    time = date[1]    