以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

##定位模块
#import sys 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

Python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
因此，如果要给全局变量在一个函数里赋值，必须使用global语句。

dir()函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

##创建类
#使用class语句来创建一个新类，class之后为类的名称并以冒号结尾，如下实例:
#可以添加，删除，修改类的属性
#getattr(obj, name[, default]) : 访问对象的属性。
#hasattr(obj,name) : 检查是否存在一个属性。
#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#delattr(obj, name) : 删除属性。

##Python内置类属性
#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#__doc__ :类的文档字符串
#__name__: 类名
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
#class_name = object.__class__.__name__
#__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs
#__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods

<a href="http://www.cnblogs.com/dreamer-fish/p/3821762.html">http://www.cnblogs.com/dreamer-fish/p/3821762.html</a>

执行环境
 
9.1.     可调用对象（Python有4种可调用对象：函数、方法、类和一些类的实例）

9.1.1.   函数

a．  内建函数（BIF）：用C/C++写的，编译后放入Python解释器，作为第一（内建）名称空间的一部分加载进系统。这些函数中__bulitin__模块中，作为__builtins__模块导入到解释器中。

表格 26 内建函数属性

属性	描述
bif.__doc__	文档字符串（或None）
bif.__name__	字符串类型的文档名字
bif.__self__	设置为None（保留给内建方法）
bif.__module__	存放bif定义的模块名字（或None）
b．  用户定义的函数（UDF）：定义在模块最高级，作为全局名称空间都一部分装载到系统中。

表格 27 用户自定义函数属性

属性	描述
udf.__doc__	文档字符串（也可用udf.func_doc）
udf.__name__	字符串类型的函数名字（也可用udf.func_name）
udf.func_code	字节编译的代码对象
udf.func_defaults	默认的参数元组
udf.func_globals	全局名称空间字典；和从函数内部调用globals(x)一样
udf.func_dict	函数属性的名称空间
udf.func_doc	见上
udf.func_name	见上
udf.func_closure	包含自由变量的引用的单元对象元组
c．  lambda表达式（名为“<lambda>”的函数）

9.1.2.   方法

a．  内建方法（BIM）

如下是内建方法的属性：

表格 28 内建方法的属性

属性	描述
bim.__doc__	文档字符串
bim.__name__	字符串类型的函数名字
bim.__self__	绑定的对象
 

b．  用户定义的方法（UDM）：包含在类定义中，只有标准函数都包装，仅有定义它们都类可以使用。

表格 29 用户自定义方法的属性

属性	描述
udm.__doc__	文档字符串（与dum.im_func.__doc__相同
udm.__name__	字符串类型的方法名字（与udm.im_func.__name__相同
udm.__module__	定于udm的模块的名字（或none）
udm.im_class	方法相关联的类（如果是非绑定，则为要求udm的类
udm.im_func	方法的对象
udm.im_self	如果绑定的话为相关联的实例，如果非绑定则为none
 

9.1.3.   类：“调用”类的结果便是创建了实例

9.1.4.   类的实例：Python给类提供了名为__call__的特殊方法，允许程序员创建可调用对象（实例），默认情况没有实现该方法，即大多数实例都是不可调用的。

 

9.2.     代码对象（每个可调用物的核心都是代码对象，可以作为函数或者方法调用的一部分来执行，也可用exec语句或内建函数eval()来执行。整体上，一个Python模块的代码对象是构成该模块全部代码。

 

9.3.     可执行对象声明和内建函数
