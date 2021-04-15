from encoder import UniversalEncoder

data = [
    'What color is chameleon?',
    'When is the festival of colors?',
    'When is the next music festival?',
    'How far is the moon?',
    'How far is the sun?',
    'What happens when the sun goes down?',
    'What we do in the shadows?',
    'What is the meaning of all this?',
    'What is the meaning of Russel\'s paradox?',
    'How are you doing?'
]

data1 = ['accounts', 'artical', 'student', 'bank']

data2 = ["table"]

encoder = UniversalEncoder("tstsv.ddns.net", 8501)

#encoder.build_index(data2,True)

r = encoder.search(data,"sun",2)
[print(i) for i in r]
