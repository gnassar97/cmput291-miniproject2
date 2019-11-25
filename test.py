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
    print(match)
    if match:
        try:
            #keyword =  re.split("(:|>=|<=|>|<)", match[0])
            #values = re.split("(:|>=|<=|>|<)", match[1])
            keyword = match[0].split(':|>=|<=|>|<')[0]
            values = match[0].split(':|>=|<=|>|<')[1]
            value = values.split()[0]
            to_proccess.append([keyword,value])
            wildcard = values.split()

            for i in range(1,len(wildcard)):
                wildcards.append(wildcard[i])

        except:
            proccess = match[0].split(':')
            keyword = proccess[0]
            value = proccess[1]
            to_proccess.append([keyword, value])

print(to_proccess)
print(wildcards)