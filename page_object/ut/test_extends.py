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
        Bbb().fun3()        # ��λ�ñ���ʵ��������ʵ��self.driver��ֵ��ÿ�ζ�Ҫ��ʼ�������Զ�PO��ֻ����һ��APP���в�ͨ��