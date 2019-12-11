'''
python中初始化实例属性
虽然我们可以自由地给一个实例绑定各种属性，但是，现实世界中，一种类型的实例应该拥有相同名字的属性。例如，Person类应该在创建的时候就拥有 name、gender 和 birth 属性，怎么办？
在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
'''

class Person(object):
    def __init__(self,name,gender,birth):
        self.name = name
        self.gender = gender
        self.birth = birth

xiaoming = Person('小明','Male','19900420')

print(xiaoming.name)
print('#'*20)

'''
python中访问限制
我们可以给一个实例绑定很多属性，如果有些属性不希望被外部访问到怎么办？
Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，
该属性就无法被外部访问。看例子：


可见，只有以双下划线开头的"__job"不能直接被外部访问。
但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，
以"__xxx__"定义的属性在Python的类中被称为特殊属性，
有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，
他们不应该被外部访问。
'''

class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print(p.name)
print(p._title)
# print(p.__job)
print('#'*20)


'''
python中创建类属性
类是模板，而实例则是根据类创建的对象。
绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，
如果在类上绑定一个属性，则所有实例都可以访问类的属性，
并且，所有实例访问的类属性都是同一个！
也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

'''