import re
queries = [

    r'\s*subj\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*body\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*from\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*to\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*bcc\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*cc\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*output\s*[:](?:(?!body|to|from|bcc|cc|output|subj).)*',
    r'\s*date\s*[\>\=](?:(?!body|to|from|bcc|cc|output|subj).)*',

]

query = input()

to_proccess = []
wildcards = []

query = re.sub("\s\s+" , " ", query)

for regex in queries:
    match = re.findall(regex, query)
    if match:
        try:
            test =  re.split("(:|>=|<=|>|<)", match[0])
            keyword = test[0]
            values = test[2]
            #keyword = match[0].split(':')[0]
            #values = match[0].split(':')[1]
            value = values.split()[0]
            to_proccess.append([keyword,value])
            wildcard = values.split()
            print(values)

            for i in range(1,len(wildcard)):
                wildcards.append(wildcard[i])
            print(wildcard)

        except:
            proccess =  re.split("(:|>=|<=|>|<|=)", match[0])
            #proccess = match[0].split('>')
            keyword = proccess[0]
            value = proccess[2]
            to_proccess.append([keyword, value])

print(to_proccess)
print(wildcards)