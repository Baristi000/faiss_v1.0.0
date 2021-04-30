from encoder import UniversalEncoder
import numpy as np

#fake data
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
    'How are you doing?'#, 'artical', 'student', 'bank', 'accounts'
]
data1 = ['artical', 'student', 'bank', 'accounts']
# example about create connection function
encoder = UniversalEncoder("tstsv.ddns.net", 8501)
#encoder = UniversalEncoder("localhost", 8501)

#example about rebuild index function
#encoder.build_index(data,False)

#example about remove a closest semantic index
#   Note: you need to search first to make sure the data to delete is correct
#   otherwise, the closest semantic index is deleted and cannot be restored
encoder.remove_index("What we do in the shadows?")

#example about search function
r = encoder.search("distance between two planets",2)
[print(i) for i in r]