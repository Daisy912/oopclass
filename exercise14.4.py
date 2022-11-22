# student: Daisy StudentID: 202110701580008

f = open(r"C:\Users\admin\Desktop\my_words.txt", "w")
f.write('''The thing the Time Traveller held in his hand was a glittering metallic
framework, 
scarcely larger than a small clock, 
and very delicately made.''')
f.close()

f = open(r"C:\Users\admin\Desktop\my_words.txt", "r")
a = f.read()
f.close()
print(a)
