d={'name':'tanmay','age':22,'quali':'btech'}
print(d)
print(max(d))
#print(sum(d))
d1={1:'tanmay',2:22,3:'btech'}
d2={1:'tanmay','2':22,3:'btech'}
print(sum(d1))
#print(sum(d2)) ek bhi string form me aaya toh sum nahi
d.clear()# yeh likhenge toh empty set aayega
#print(d.clear()) print ke andar likhenge toh output none
print(d)
#del d
print(d)
x={'name':'tanmay','age':22,'quali':'btech'}
print(x.get('name'))
print(x.keys())
print(x.values())
print(x.items())
print(x.pop('age'))
print(x)
x.popitem()
print(x)
#string ko dict me convert typecasting
s='python'
a=dict.fromkeys(s)
print(a)
s1=[10,20,30,'python']
b=dict.fromkeys(s1)
print(b)

y=['name','email','contact','add']
a1=dict.fromkeys(y)
print(a1)
#a1['keys]=updated_value
a1['name']='tanmay'
a1['email']='1234@gmail.com'
a1['contact']=123456789
a1['add']='bhopal ,mp'
print(a1)
# update function
e={'x':10,'y':20}
f={'z':30}
e.update(f)
print(e)
#set default()
d5={'x':10,'y':20}
print(d5.setdefault('x',10))
print(d5)
print(d5.setdefault('z',30))
print(d5)







