import random
str_d = '123456789'
str_l = 'qwertyuiopasdfghjklzxcvbnm'
str_u = str_l.upper()
str_s = '!@#$%^&*-_+='
# create summary string
str_sum = str_d+str_l+str_u+str_s

#input sitename
site = input("sitename : ")
#add txt extension to output file
site_n = site + (".txt")

#input login
lgn = input("login : ")

#input password lenght
len = int(input("password length : "))

# convert string to list
ls = list(str_sum)
# shuffle elenents
random.shuffle(ls)
# extract n elements
psw = ''.join([random.choice(ls) for x in range(len)])
print(site)
print(psw)

site_t = ("site : ") + site
lgn_t = ("login : ") + lgn
pswrd = ("pass : ") + psw

#record to file
passfile = open(site_n,"w")
passfile.write(site_t)
passfile.write('\n')
passfile.write(lgn_t)
passfile.write('\n')
passfile.write(pswrd)
passfile.close()
