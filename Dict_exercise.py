pois={"Parliment":
}


user_text=input("")
words=user_text.split()
output=""
for word in words:
    if words in pois:
        output+=pois[word]
    else:
        output +=word

print(output)


output=""
for word in words:
    output+=(pois.get(word, word) + "")