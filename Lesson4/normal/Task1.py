# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


# посчитал, что данная форула неверна re.findall(r"[a-z]+", line), так как в случае,
# если в строке не будет символов верхнего регистра, то она все равно возвращает символы нижнего регистра
# поэтоу верная формула выглядит так re.findall(r"[a-z]+(?=[A-Z])|(?<=[A-Z])[a-z]+", line)
# если уберем ис строки символы верхнего регистра, то формула ничего возвращать не будет!

re_list = re.findall(r"[a-z]+(?=[A-Z])|(?<=[A-Z])[a-z]+", line)
print(re_list)

re_list = re.findall(r"[a-z]+(?=[A-Z])|(?<=[A-Z])[a-z]+", "aaaAbbbBccc")
print(re_list)

re_list = re.findall(r"[a-z]+(?=[A-Z])|(?<=[A-Z])[a-z]+", "aaabbbccc")
print(re_list)


simpl_list = []
temp = ""

for a in range(len(line)):
       if line[a].islower():
              temp += line[a]
       if line[a].isupper():
              if temp:
                     simpl_list.append(temp)
                     temp = ""

if line[-1].islower():
       for a in range(len(line), -1):
              if line[a].islower():
                     temp += line[a]
              else:
                     break

simpl_list.append(temp)

print(simpl_list)

