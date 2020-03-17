from page_object.ut.childbbb import Bbb


class TestExtends():

    def test_class_ectends1(self):
        # clb = Bbb()
        # print("=============print1======",clb.fun1())
        # print("=============print2======",clb.fun2())
        # print("=============print3======",clb.fun3())
        # print("=============print4======",clb.fun4())
        Bbb.fun4()

    def test_class_extends2(self):
        Bbb().fun3()        # 此位置必须实例化才能实现self.driver赋值，每次都要初始化，所以对PO想只启动一次APP是行不通的