# Python

## 1. 基本概念和语法

1. Python语言特点：解释型语言，面向对象
2. 编码规范：https://www.runoob.com/w3cnote/google-python-styleguide.html
3. 基本语言元素：语句，缩进，注释，变量，名字，对象，保留字，数据类型

## 2. 基本数据类型

1. 数字类型：

   - **整型(Int)** - 通常被称为是整型或整数，是正或负整数，不带小数点。
   - **长整型(long integers)** - 无限大小的整数，整数最后是一个大写或小写的L。
   - **浮点型(floating point real values)** - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 10 = 250）
   - **复数(complex numbers)** - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

2. 字符串类型

   1. 索引：str[2]

   2. 切片：

      ```python
      str[2:5] # 选择从下标为2的元素开始到下标为4的元素
      str[2:] # 选择从下标为2的元素开始到最后一个元素
      str[2::2] # 选择从下标为2的元素开始并且每隔一个元素
      str[::2] # 选择从第一个开始并且相隔为1的元素
      str[::-1] # 字符串逆序
      str[-3: -1] # 选择倒数第3个元素到倒数第一个元素之前的元素
      ```

   3. 拼接：‘a’ + ‘b’

   4. 格式化输出字符串

   ```python
   a, b = 5, 10
   print('%d * %d = %d' % (a, b, a * b))
   print('{0} * {1} = {3}'.format(a, b. a * b))
   #语法糖
   print(f'{a} * {b} = {a * b}')
   ```

3. 类型操作

   1. 类型转换https://www.cnblogs.com/shockerli/p/python3-data-type-convert.html

   ```python
   #只支持float,str,bytes -> int
   # 1. float -> int，去掉小数点后面的数值，仅保留整数部分
   int(12.1)
   # 2. str -> int，只支持转换字符串（-/+）(int_number)
   int('1234')
   int('-12')
   # 3. byte -> int, 
   ```

   b. 数值运算符

   +, -, *, /, %（取模）, ** , //（整除）

## 3. 容器（复合）数据类型

1. 列表的定义和操作

   ```python
   # 列表定义
   # 直接定义
   list1 = [1，3，5，7，100]
   # 定义重复元素的列表
   list2 = ['hello'] * 5
   
   # 计算列表长度
   len(list1)
   # 添加元素
   list1.append(200) # 直接在末尾添加元素
   list1.insert(1, 100) # 在指定下标添加元素
   list1 += [1000, 2000] # 在末尾连接一组元素
   # 删除元素
   list1.remove(3) # 删除列表中的指定元素
   list1.clear() # 清空列表元素
   
   # 列表切片操作
   list3 = list1[1:4]
   ...与字符串切片操作一致
   
   # 列表排序
   list4 = sorted(list1) # list本身不改变
   list1.sort() # list本身改变
   
   # 生成式语法创建列表
   f = [x + y for x in 'ABCDE' for y in '1234567']
   # 生成式语法创建列表的说明
   f = []
   for x in 'ABCDE':
       for y in '1234567':
           f.append(x + y)
   ```

2. 元祖的定义和操作

   1. 元祖定义

   ```python
   t = ('tuple', 1, True)
   ```

   b. 元祖的操作

3. 字典的定义和操作

   1. 字典的定义

      ```python
      # 键值对
      scores = {'a': 1, 'b': 2}
      ```

   2. 字典的操作

      ```python
      # 通过键获取字典中对应的值
      scores['a']
      scores.get('a')
      # 更新字典中的元素
      scores['a'] = 3 # 修改原有的元素
      scores['c'] = 4 # 添加新元素
      scores.update(d=5, e=6)
      # 删除字典中的元素
      scores.popitem() # 删除字典最后一对键值对
      scores.pop('a') # 指定键值删除元素
      ```

4. 集合的定义和操作

## 4. 控制结构及语句

1. 程序的基本控制结构

   1. 顺序结构

   2. 分支结构

      ```python
      if
      if...else
      if...elif...else
      if...elif...elif...else
      ```

   3. 循环结构

      ```python
      for...in
      while 
      ```

2. 命名空间及作用域

   命名空间：避免项目中的命名冲突，一个命名空间中不能重名，不同命名空间可以重名

   命名空间的类别：

   - 内置名称：Python语言内置的变量
   - 全局名称：在模块内定义的变量、函数、类、常量以及其他模块引入的变量
   - 局部名称：函数和类中定义的变量

   作用域

   - 局部作用域：函数或方法的内部，外部无法访问到

   - 嵌套作用域：两个嵌套函数fun1和fun2，变量c属于fun1的局部作用域又属于fun2的嵌套作用域

     ```python
     def fun1():
     	c = 1
     	def fun2():
     		pass
     ```

   - 全局作用域：__mian__中的变量

   - 内置（内建）作用域：系统内建的变量和关键字

3. 异常处理

   1. Python中的异常是一个对象，表示一个错误

   2. try-except语句块

      ```python
      try:
      .........
      except(Exception1[, Exception2[,...ExceptionN]]):
      .........产生异常执行
      else:
      	没有产生异常执行
      ```

## 5. 代码复用

1. 函数定义与使用
2. 函数的定义与使用
3. 包的定义与使用
4. Python库

## 6. 文件操作

1. 文件的打开和关闭：

   ```python
   # 使用Open()内置函数打开文件
   f = open('文件名,txt', mode='r', encoding='utf-8')
   # file对象方法close()关闭文件
   f.close()
   ```

   open的参数：

   - file: 必需，文件路径（相对或者绝对路径）。
   - mode: 可选，文件打开模式
   - buffering: 设置缓冲
   - encoding: 一般使用utf8
   - errors: 报错级别
   - newline: 区分换行符
   - closefd: 传入的file参数类型
   - opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

2. 文件的输入与输出：

   ```python
   # write方法可以将任何字符串写入一个打开的文件
   f.write(string)
   # read方法可以读取二进制数据或字符串，并且可以指定输出字符的数量
   f.read()
   ```

3. 文件定位：

   1. tell()方法告诉文件定位的当前位置，也就是下一次读写的会发生在这么多字节后
   2. seek(offset, [from])方法改变文件定位，offset表示要移动的字节数，from = 0表示从文件头进行偏移，from=1表示从文件当前定位处开始偏移，from=2表示从文件尾部开始偏移

4. 常见结构化文本文件：CSV、JSON

## 7. 对象与类

1. 对象与类的基本概念

   > 什么是面向对象程序设计：把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。

   类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

   对象：类的实例化。包括两个数据对象和方法

2. 类的定义和实例化：

   ```python
   class Employee:
   	# 可以用Employee.empCount获取或者对象.empCount获取，内部也可以用self.empCount获取
   	empCount = 0
   
   	# __init__构造函数
   	def __init__(self, name, salary):
   		self.name = name
   		self.salary = salary
   		Employee.empCount += 1
   	
   	def displayCount(self):
   		print "Total Employee %d" % Employee.empCount
   	
   	def displayEmployee(self):
   		print "Name : ", self.name,  ", Salary: ", self.salary
   
   emp = Employee('gy', 1000)
   ```

   - empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
   - 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
   - **self 代表类的实例**，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

3. 继承

   1. 继承的作用：代码的重用

   2. 继承语法

      ```python
      class SubClassName (ParentClass1[, ParentClass2, ...]):
          ...
      ```

4. 方法覆盖（也称为重写）

   > 父类中的方法不符合功能需求，子类中可以重写父类中的方法

## 8. 系统函数

1. 文件操作函数：https://www.runoob.com/python/file-methods.html

2. 目录操作函数：https://www.runoob.com/python/os-file-methods.html

3. 日期与时间函数

   1. time

   ```python
   time.time() # 获取时间戳
   
   time.localtime() # 获取时间元祖 
   # 输出形式
   # time.struct_time(tm_year=2022, 
   # tm_mon=3, tm_mday=31, tm_hour=15, tm_min=12, tm_sec=59, tm_wday=3, tm_yday=90,
   # tm_isdst=0)
   
   # %Y四位数年份、%m月份、%d日、%H时、%M秒、%S秒
   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   ```

   b. 获取月日历

   ```python
   import calendar
   
   cal = calendar.month(2022, 3)
   print(cal)
   #
   #March 2022
   #Mo Tu We Th Fr Sa Su
   #    1  2  3  4  5  6
   # 7  8  9 10 11 12 13
   #14 15 16 17 18 19 20
   #21 22 23 24 25 26 27
   #28 29 30 31
   ```