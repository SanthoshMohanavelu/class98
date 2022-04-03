def countWord():
    count = 0
    fileName = input('Enter the file name..')
    file = open(fileName, 'r')  
    for line in file:
        word = line.split()
        count = count + len(word)
    print('number of words', count)
countWord()