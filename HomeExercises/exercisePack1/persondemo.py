

class Person:

    # 类变量既可以通过实例化调用也可以直接以类名调用
    @classmethod
    def asd(cls):
        pass

    # property 更方便创建只读属性  可以通过实例化对象直接调用不带括号 例：pp.get_sex
    # 在3里面用途不大了，带不带（）都能调出
    @property
    def get_sex(self):
        pass

    def get_sex2(self):
        return self.sex

    def __init__(self):
        self.sex = ''

    def sex(self):
        pass

    def weight(self):
        pass

    def age(self):
        pass

    def set_sex(self, sex):
        self.sex = sex


if __name__ == '__main__':
    toni_instance = Person()
    toni_instance.set_sex('tony')
    print(toni_instance.sex)
