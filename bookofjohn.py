infile = open('book of John text.txt', 'r')
readfile = infile.read()

#word_dict = {}
#the empty list did not put the output in the order of the if statements below so I put the words as keys and the if statements would populate the values in the dictionary.
word_dict = {'Father':[],'God':[],'Christ':[],'Spirit':[],'spirit':[],'life':[],'man':[]}
john = readfile.split(' ')

Father =0
God = 0
Christ = 0
Spirit = 0
spirit = 0
life = 0
man = 0

for words in john:
    if words == 'Father':
        Father += 1
        word_dict['Father']=Father
    if words == 'God':
        God += 1
        word_dict['God']=God
    if words == 'Christ':
        Christ += 1
        word_dict['Christ']=Christ
    if words == 'Spirit':
        Spirit += 1
        word_dict['Spirit']=Spirit
    if words == 'spirit':
        spirit += 1
        word_dict['spirit']=spirit
    if words == 'life':
        life += 1
        word_dict['life']= life      
    if words == 'man':
        man += 1
        word_dict['man']= man

for x in word_dict:
    print(x,": ",word_dict[x],sep='')

