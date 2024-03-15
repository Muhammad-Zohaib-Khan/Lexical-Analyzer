import re
import pandas as pd
from matplotlib import pyplot as plt

class Lexical_Analysis(object):
    def __init__(self,code):
        self.input_code=code
        self.count={}
        self.tokens=[]
        self.class_part=[]
        self.language_specifications = {
            "operators": r'\+\+|--|!=|<=|>=|==|[-+*/%=<>🤝👐💢]',
            "special_keyword": r'✍|🖨|🤔|😅|➰|➿|✅|❌|💔|🧡',
            "special_characters": r'[\(\)\[\]\{\};,:]',
            "integer": r'\b[1-9][0-9]*\b',
            "string": r'"(?:\\.|[^"\\])*"',
            "ID": r'[🔤🔢]\s*[a-zA-Z_]+[a-zA-Z0-9_]*'
        }
        self.attributes_value={
        "✍": "INPUT",
        "🖨": "PRINT",
        "🤔": "IF",
        "😅":"ELSE",
        "➰": "FOR",
        "➿": "While",
        "✅": "TRUE",
        "❌": "FALSE",
        "💔": "BREAK",
        "🧡": "CONTINUE",
        "🤝":"AND",
        "👐":"OR",
        "💢":"NOT",
        ">": "LE",
        "<": "GE",
        "=": "EQ",
        "+": "ADD",
        "-": "SUB",
        "*": "MUL",
        "/": "DIV",
        "%":"Mod",
        "++":"Inc",
        "--":"Dec",
        "!=":"NE",
        "==":"CO",
        "[": "SB",
        "]": "SB",
        "{": "CB",
        "}": "CB",
        "(": "RB",
        ")": "RB",
        ":": "Colon",
        ";": "Semi Colon",
        ",": "Comma",
        "?":"QM",
    }
    #GENERATE TOKENS AND THEIR COUNT
    def tokens_count(self):
        for cls,pattern in self.language_specifications.items():
            pattern=re.findall(pattern,self.input_code)
            self.count.update({cls:len(pattern)})
            self.tokens.extend(pattern)
    #IDENTIFY CLASS PART    
    def class_of_tokens(self):
        for token in self.tokens:
            for cls,pattern in self.language_specifications.items():
                if re.match(pattern,token):
                    if token in self.attributes_value:
                        self.class_part.append((pattern,token,cls,self.attributes_value[token]))
                    elif re.match(self.language_specifications["integer"],token):
                        self.class_part.append((pattern,token,"Datatype",cls))
                    elif re.match(self.language_specifications["string"],token):
                        self.class_part.append((pattern,token,"Datatype",cls))
                    elif re.match(self.language_specifications["ID"],token):
                        self.class_part.append((pattern,token,cls,"ID"))

    def show_result(self):
        print("Lexical Analysis".center(120))
        result=pd.DataFrame(self.class_part,columns=["Regax","Token","Class Part","Value"])
        print(result.to_string(index=False))
        Name=[]
        Count=[]
        print("Count is:")
        for name,count in self.count.items():
            print(f"{name}:{count}\n")
            Name.append(name)
            Count.append(count)
        
        fig = plt.figure(figsize = (10, 5)) 

        plt.bar(Name,Count,color="g",width=0.4)

        plt.xlabel("Class Part") 
        plt.ylabel("Count") 
        plt.title("Compiler Construction") 
                
        plt.show()
        
            

code='''
🔢 num = ✍("Enter a number: "))
🤔(num % 2) == 0:--
   🖨("num is Even")
😅:
   🖨("num is Odd")'''
        
Lexeme=Lexical_Analysis(code)
Lexeme.tokens_count()
Lexeme.class_of_tokens()
Lexeme.show_result()
