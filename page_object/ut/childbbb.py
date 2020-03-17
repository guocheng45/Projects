from page_object.ut.fatheraaa import Aaa
class Bbb(Aaa):


    def fun3(self):
        c='fun3'
        if self.driver is None:
            print("self._driver:===== %s", self.driver)
        return c

    @classmethod
    def fun4(cls):
        print("==============%s", cls.driver)
        # if cls.driver is not None:
        #     return cls.driver
        # else:
        #     return False
        cls.fun2()