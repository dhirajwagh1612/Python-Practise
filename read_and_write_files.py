f=open("poem.txt","r")
lines=f.readline()
print(lines)
f.close()


for item in lines:
    item=item.lower()
#print(line[0])

length=len(lines)
for i in range(lengh):
    lines[i]= lines[i].lower()
#print(lines[0])

length=len(lines)
for i in range(lengh):
    lines[i]= lines[i].replace('\n',' ')
#print(lines)

char_to_replace=['\n',',','-','(',')']
for i in range(length):
    for s in char_to_replace:
        lines[i]=lines[i].replace(s, ' ')
#print(lines)

text=""
for line in lines:
    text += line+""
#print(text)

# another way to do this.
text="",join(lines)
#print(text)
words=text.split()
print(len(words), words)


word_freq ={}


for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] = 1
print(word_freq)

