a= {
    'list' : ['python','php','laravel','Django']
}

b = {}

for i in range(0,len(a['list'])) :
  b[a['list'][i]] = a['list'][i][0]
print(b)    
