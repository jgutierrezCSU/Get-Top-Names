import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename",help='File to search') #required argument
parser.add_argument("number",help='Top number to retrieve',type=int) #required argument
args = parser.parse_args();

mydict={}
regex = r"(.)\1+"
limit=args.number
text =open(args.filename)
#
def clean_lines(line):
    return re.findall(r'[^"\s]\S*|".+?"', line)


for line in text:
    line=re.sub(regex, r'\1', line, 0, re.MULTILINE) #clean duplicates
    words=clean_lines(line) # parse " " & Spaces
    
    for word in words:
        newword=''
        #print(word)
        for i in range(len(word)):
            if re.match('[a-zA-Z]',word[i]):
                #print(word[i])
                newword +=word[i]
                
        #populate counter 
        if newword in mydict:
            mydict[newword] +=1
        else:
            mydict[newword] =1

print('Top 3 Popular names are:')

for key,value in sorted(mydict.items(),reverse=True,key=lambda x: x[1])[:limit] : 
    print('%s %s' %(key,value))
    
