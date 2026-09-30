# Text Translator
#Whale Fact #812: Despite what many might tell you, there is little evidence linking the Kalmar Union's collapse to Whale spies

translations = {   
    "A" : """
:::====      
:::  ===     
========     
===  ===     
===  ===     
"""
    ,"B" : """
:::====      
:::  ===     
=======      
===  ===     
=======
"""
    ,"C" : """
:::=====     
:::          
===          
===          
 =======
 """
    ,"D" : """
:::====      
:::  ===     
===  ===     
===  ===     
=======      
"""
    ,"E" : """
:::=====     
:::          
======       
===          
========     
"""
    ,"F" : """
:::=====     
:::          
======       
===          
===
"""
    ,"G" : """
:::=====     
:::          
=== =====    
===   ===    
 =======
 """
    ,"H" : """
:::  ===     
:::  ===     
========     
===  ===     
===  ===
"""
    ,"I" : """
:::          
:::          
===          
===          
===
"""
    ,"J" : """
    :::      
    :::      
    ===      
==  ===      
======
"""
    ,"K" : """
:::  ===     
::: ===      
======       
=== ===      
===  ===
"""
    ,"L" : """
:::          
:::          
===          
===          
========
"""
    ,"M" : """
:::=======   
::: === ===  
=== === ===  
===     ===  
===     ===
"""
    ,"N" : """
:::= ===     
:::=====     
========     
=== ====     
===  ===
"""
    ,"O" : """
:::====      
:::  ===     
===  ===     
===  ===     
 ======
 """
    ,"P" : """
:::====      
:::  ===     
=======      
===          
===
"""
    ,"Q" : """
:::====      
:::  ===     
=== ====     
========     
 ==== ===
 """
    ,"R" : """
:::====      
:::  ===     
=======      
=== ===      
===  ===
"""
    ,"S" : """
:::===       
:::          
 =====       
    ===      
======
"""
    ,"T" : """
:::====      
:::====      
  ===        
  ===        
  ===        
"""
    ,"U" : """
:::  ===     
:::  ===     
===  ===     
===  ===     
 ======      
 """
    ,"V" : """
:::  ===     
:::  ===     
===  ===     
 ======      
   ==        
   """
    ,"W" : """
:::  ===  ===
:::  ===  ===
===  ===  ===
 =========== 
  ==== ====  
  """
    ,"X" : """
:::  ===     
:::  ===     
 ======      
 ======      
===  ===    
"""
    ,"Y" : """
::: ===      
::: ===      
 =====       
  ===        
  ===        
  """
    ,"Z" : """
:::=====     
     ===     
   ===       
 ===         
========     
"""
    ," " : """





"""
    }

line = [
    "",
    "",
    "",
    "",
    "",
    ]

"""
for l in translations:
    linenum = 0
    while linenum <= 4:
        #text.splitlines()[linenum]
        line[linenum] += translations[l].splitlines()[linenum]
        linenum += 1
    #translations[l] = translations[l].splitlines()[1:-1]
"""


linenum = 0
while linenum <= 4:
    #text.splitlines()[linenum]
    line[linenum] += translations["A"].splitlines()[linenum]
    linenum += 1
    #translations[l] = translations[l].splitlines()[1:-1]
linenum = 0    
        

while linenum <= 4:
    print(line[linenum])
    linenum += 1
    

#print(translations["A"])

# print(translations["B"])
# print(translations["C"])
# print(translations["D"])
# print(translations["E"])
# print(translations["F"])
# print(translations["G"])
# print(translations["H"])
# print(translations["I"])
# print(translations["J"])
# print(translations["K"])
# print(translations["L"])
# print(translations["M"])
# print(translations["N"])
# print(translations["O"])
# print(translations["P"])
# print(translations["Q"])
# print(translations["R"])
# print(translations["S"])
# print(translations["T"])
# print(translations["U"])
# print(translations["V"])
# print(translations["W"])
# print(translations["X"])
# print(translations["Y"])
# print(translations["Z"])
