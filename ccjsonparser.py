import sys
def hexa(hexn):
    l=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F']
    for i in hexn:
        if not i in l:
         #   print('Invalid hex character',i)
            return False
    return True
def string(token):
    token=token.strip()
    l=['\"','\\','b','f','n','r','t','/']
    if len(token) <2:
        #rint("Invalid String",token)
        return False
    x=0
    if token[x]!="\"" or token[len(token)-1]!="\"":
        #print("Missing \" in string",token)
        return False
    x=x+1
    #print(token)
    if ('\t' in token) or ("\n" in token):
        #print("Tab or Line break should be represented as control characters in string",token)
        return False
    while token[x]!="\"":
        if token[x]=="\\":
            x=x+1
            if x+1>=len(token):
          #      print("Invalid character \\ in string",token)
                return False
            if token[x] in l:
                x=x
            elif token[x]=="u":
                x=x+1
                if x+4>=len(token) and not hexa(token[x:x+4]):
                    return False
            else:
         #       print("Invalid escape character in String",token)
                return False
        x=x+1
    #print(x)
    if x+1<len(token):
        #print("Invalid String",token)
        return False
    return True


def num(token):
    token=token.strip()
    digit=['0','1','2','3','4','5','6','7','8','9']
    x=0
    l=len(token)
    if token[x]=='-':
        x=x+1
        if not x<l:
         #   print("Invalid number",token)
            return False
    if token[x]=='0':
        x=x+1
    elif token[x] in digit[1:]:
        while x<l and token[x] in digit:
            x=x+1
    else:
        #print("Invalid number",token)
        return False
    if x<l and token[x]=='.':
        x=x+1
        if not x<l:
        #    print("Invalid number",token)
            return False
        while x<l and token[x] in digit:
            x=x+1
    if x<l and (token[x]=='e' or token[x]=='E'):
        x=x+1
        if not x<l:
         #   print("Invalid number",token)
            return False
        if token[x]=='+' or token[x]=='-':
            x=x+1
        if not x<l:
          #  print("Invalid number",token)
            return False
        while x<l and token[x] in digit:
            x=x+1
    if x<l:
        print("Invalid number",token)
        return False 
    return True
def arr(token):
    token = remove_empty_lines(token)
    token=token.strip()
    if len(token)<2:
        print("Invalid array",token)
        return False
    if token[0]!='[' or token[-1]!=']':
       # print("Invalid array",token)
        return False
    token=token[1:]
    token=token[:len(token)-1]
    token = token.strip()
    x=0
    while x<len(token):
        val=""
        while x<len(token) and token[x]!=',':
            val=val+token[x]
            if token[x]=="\"":
                x=x+1
                while x<len(token) and token[x]!="\"":
                    val=val+token[x]
                    if token[x]=='\\':
                        x=x+1
                        if x<len(token):
                            val=val+token[x]
                        else:
                       #     print("Invalid array",token)
                            return False
                    x=x+1
                val=val+token[x]
            st=[]
            if token[x]=='{' or token[x]=='[':
                st.append(token[x])
                x=x+1
                while len(st)>0 and x<len(token):
                    val=val+token[x]
                    if token[x]=='}':
                        if st[-1]=='{':
                            st.pop()
                        else:
                      #      print("Invalid array",token)
                            return False
                    if token[x]==']':
                        if st[-1]=='[':
                            st.pop()
                        else:
                     #       print("Invalid array",token)
                            return False
                    if token[x]=='{' or token[x]=='[':
                        st.append(token[x])
                    x=x+1
                if len(st)>0:
                    #print("Invalid array",token)
                    return False
                x=x-1
            x=x+1
        if x<len(token) and x+1>=len(token):
            
            return False
        x=x+1
        if not vals(val):
            return False
    return True

def vals(token):
    token=token.strip()
    #print(token)
    if len(token)==0:
        print("Invalid value",token)
        return False
    if token[0]=="\"":
        if not string(token):    
            return False
    elif token == "true":
        return True
    elif token == "false":
        return True
    elif token == "null":
        return True
    elif token[0]=='-' or token[0] in ['0','1','2','3','4','5','6','7','8','9']:
        #print("n")
        if not num(token):
            return False
    elif token[0]=='{':
        if not obj(token):
            return False
    elif token[0]=='[':
        if not arr(token):
            return False
    else:
        return False
    return True
def record(line):
    if len(line)==0:
        return False
    x=0
    line=line.strip()
    #print(line)
    key=""
    while x<len(line) and line[x]!=':':
        key=key+line[x]
        if line[x]=="\"":
            x=x+1
            while x<len(line) and line[x]!="\"":
                key=key+line[x]
                if line[x]=='\\':
                        x=x+1
                        if x<len(line):
                            key=key+line[x]
                        else:
                            return False
                x=x+1
            key=key+line[x]
        x=x+1
    print(key)
    if len(key)==0:
        return False
    if not string(key):
        return False
    #print(line[x+1:])
    if not vals(line[x+1:]):
        return False
    return True
def records(lines):
    if len(lines)==0:
        return True
    lines=remove_empty_lines(lines)
    x=0
    lines=lines.strip()
    #print(lines)
    while x<len(lines):
        line=""

        while x<len(lines) and lines[x] != ',':
            line=line+lines[x]
            if lines[x]=="\"":
                x=x+1
                while x<len(lines) and lines[x]!="\"":
                    line=line+lines[x]
                    if lines[x]=='\\':
                        x=x+1
                        if x<len(lines):
                            line=line+lines[x]
                        else:
                            return False
                    x=x+1
                line=line+lines[x]
                
            st=[]
            if x<len(lines) and (lines[x]=='{' or lines[x]=='['):
                st.append(lines[x])
                x=x+1
                while len(st)>0 and x<len(lines):
                    line=line+lines[x]
                    if lines[x]=='}':
                        if st[-1]=='{':
                            st.pop()
                        else:
                            return False
                    if lines[x]==']':
                        if st[-1]=='[':
                            st.pop()
                        else:
                            return False
                    if lines[x]=='{' or lines[x]=='[':
                        st.append(lines[x])
                    x=x+1
                if len(st)>0:
                    return False
                x=x-1
            x=x+1
        if x<len(lines) and lines[x] == ',' and x+1>=len(lines):
            return False
        x=x+1
        if not record(line):
            return False
    return True
def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_empty_lines)
def obj(tkn):
    tkn=remove_empty_lines(tkn)
    #print(tkn)
    tkn=tkn.strip()
    if len(tkn)<2 :
        return False
    if tkn[0] != "{" or tkn[len(tkn)-1] !="}":
        return False
    tkn=tkn[1:]
    tkn=tkn[:len(tkn)-1]
    #print(tkn)
    if not records(tkn):
        return False 
    return True

def parser(tkn):
    tkn=remove_empty_lines(tkn)
    tkn=tkn.strip()
    if len(tkn)<2:
        return False
    if tkn[0]=='{':
        if not obj(tkn):
            return False
    else:
        if not arr(tkn):
            return False
    return True

filename=sys.argv[1]
#print(filename)
text=""
try:
    with open(filename,'r') as file:
        text=file.read()
 #       print(text)
except (IOError):
    print("Error in opening file")

#print(tokens)
if(parser(text)):
    print("program exitted with 0")
else:
    print("Invalid json file")
    print("program exitted with status 1")