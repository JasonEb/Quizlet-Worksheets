#script can be ran at 
#http://www.codeskulptor.org/#user28_fcJVP814x2_5.py
#this will take a copy and pasted exported Quizlet word-definitions list

import simplegui, random

blankbank = []
mastertext = ''
wordlist = []
pos = ['noun','adj','verb','adv', 'conj']
words = []
definitions = []
sep = ' x-x '

##helper functions
#word length analysis
def lengthanalysis():
    global words
    
    biggest = 0
    
    print
    
    for i in words:
        if len(i) > biggest:
            biggest = len(i)
    
    print biggest 

def jumbler(word):
    newword = word
    
    mid = list(word[1:-1])
    
    if len(word) < 4:
        print word
    else:
        while (newword == word):
            random.shuffle(mid)
            newword = word[0]
            for c in mid:
                newword += c
            newword += word[-1]           
            
            if (newword == word):
                newword = word
            

    print newword

def jumblerator():
    global words
    
    print 

    #create a random sequence
    seq = list(range(0,len(words)))
    random.shuffle(seq)
    
    for x in seq:
        jumbler(words[x])
        
    print
    
def hangman(word):
    #print chr(random.randrange(97, 97 + 26 + 1))
    string = word
    string2 = ''
    s = []
    blanks = ''
    
    #blank under scores
    for i in range(0, len(string)):
        s.append('_ ')
        
    #print len(list(s))
    #print s
    
    rng = random.randrange(0,len(string)) #pick a random index for hint
    #print rng
    
    s[rng] = str(list(string)[rng].upper())+' '
    
    string2 = list(string) #create new string for display
    
    string2.pop(rng)
    
    #print string2
            
    for i in s:
        blanks += i
    
    print blanks
                                 
    
    
    #replace one of the blanks with a letter for a hint
    
    
    bank = list(string2)
    
    #add random letters to the mix, up to 12
    #if word > 12, then up to 18
    print
    
    if (len(string) < 13):
        for x in range(0,12-len(string2)):
                l = chr(random.randrange(97, 97 + 26))
                bank.append(l)
        
        
        b = ''
        n = 1
        
        random.shuffle(bank)
            
        for i in bank:   
            #print str(n)+'. '+i
            if (n % 6) == 0:
                
                b += i.upper() + '\n'
            else:
                b += i.upper() + ' '
            n += 1 
            
        print b
    else:
        for x in range(0,18-len(string2)):
                l = chr(random.randrange(97, 97 + 26))
                bank.append(l)
        
        
        b = ''
        n = 1
        
        random.shuffle(bank)
            
        for i in bank:   
            #print str(n)+'. '+i
            if (n % 6) == 0:
                
                b += i.upper() + '\n'
            else:
                b += i.upper() + ' '
            n += 1
        
            
        print b    

def hangmangenerator():
    global words, definitions
    
    #create a random sequence
    seq = list(range(0,len(words)))
    random.shuffle(seq)
    
    for x in seq:
        print 
        print definitions[x]
        hangman(words[x])
    
def wordlistinput(text):
    global wordlist, mastertext, words, definitions
    
    mastertext = text
    
    list1 = text.split('\n')
    
    #split up with seperator
    for i in list1:   
        words.append(i[0:i.find(sep)].strip())
        definitions.append(i[i.find(sep)+len(sep):len(i)].strip())
    
    for i in range(0,len(words)):
        print
        print words[i] + ": " + definitions[i]
         
    print    
    
def printWordlist():
    global words
    
    print words
    for i in words:
        print i
    print     
    
def blankmaker():
    s = ''
    global words, definitions, blankbank
    
    list1 = definitions 
    #create a random sequence
    seq = list(range(0,len(words)))
    random.shuffle(seq)    
    
    for i in seq:
        print words[i]+ " - "+ blankinserter(definitions[i])
        
    print
    print "Blank Bank: "
    
    blankbank.sort()
    
    for i in blankbank:
        print i
        
    print
    
def blankinserter(textline):
    global blankbank
    biggest = ''
    blank = ''
    s = ''
    
    textstring = textline.split()
   
    #search for biggest word in string
    for i in textstring:
        if len(i) >= len(biggest):
            biggest = i
            
    #generate blank underscore
    for i in range(0,len(biggest)):
        blank += '_'
    
    #replace biggest word with blank
    #while adding a word to the blankbanks
    
    blankbank.append(biggest)
    
    textstring[textstring.index(biggest)] = blank
    
    for i in textstring:
        s += i + " "
        
    return s
    
#draw handlers
    
# create frame
f = simplegui.create_frame("Wordsheet Generators",300,300)
#f.set_canvas_background('White')

# register event handlers and create control elements
inp = f.add_input("Enter Quizlet Text", wordlistinput, 100)
f.add_button("Print Word List", printWordlist, 100)
f.add_button("BLANKS Generator", blankmaker, 100)
f.add_button("Print Jumbled List", jumblerator, 100)
#f.add_button("Print Word List", printWlist, 100)
f.add_button("Word Length Analysis", lengthanalysis, 100)
f.add_button("Hangman Generator", hangmangenerator, 100)

# get frame rolling
f.start()
