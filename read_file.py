#content for small files, open(), close()
file = open("c:\\Python\\pythonstuff\\joke.txt","r")

content = file.read()
print(content)
file.close()

#big files
with open('c:\\Python\\pythonstuff\\joke.txt','r') as file:
    content = file.read()
    print(content)

#big files read line by line
with open('c:\\Python\\pythonstuff\\joke.txt','r') as file:
    for line in file:
        print(line)


#open(),close() with for 
file = open("c:\\Python\\pythonstuff\\joke.txt","r")
for line in file:
    print(line)
file.close()


#reading 10 bytes to the end of the loop
file = open("c:\\Python\\pythonstuff\\joke.txt","r")
fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()
