str="Hello, Sunshine! how was your day? was it good?"
str=str.lower()
freq={}
for word in str.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

for item in freq:
    print(item,freq[item])