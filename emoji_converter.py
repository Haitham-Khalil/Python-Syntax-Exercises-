emojis_mapping={
    ";)":"😉",
    ":)":"😊",
    ":(":"😢",
    ":|":"😑"
}

message=input('>')
words=message.split(" ")

output=""
for word in words:
    output += emojis_mapping.get(word,word)+" "
print(output) 