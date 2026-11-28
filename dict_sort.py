scores={
    "Bob": 23,
    "James": 55,
    "Ash": 77,
    "Bobby": 88,
    "Ada": 100,
    "Leon": 95
}
sorted_scores=dict(sorted(scores.items(),key= lambda item: item[1]))
for key,value in sorted_scores.items():
    print(key,":",value)
