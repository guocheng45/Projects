import yaml

class TestYaml(object):
    def test_yaml(self):
        dict = yaml.load(open("..\data\hys.yaml",'r'))
        print(dict)
        for step in dict["login_app"]:
            print(step['locator'])
        return self
    def test_str_combine(self):
        name="仁和可立克"
        str1="//*[contains(@text,'仁和可立克')]/../..//*[contains(@resource-id,'rb_check')]"
        str2="//*[contains(@text,'"+"仁和可立克"+"')]/../..//*[contains(@resource-id,'rb_check')]"
        str3 = "//*[contains(@text,'%s')]" %name+"/../..//*[contains(@resource-id,'rb_check')]"
        print("str1:",str1)
        print("str2:",str2)
        print("str3:", str3)
        assert str2==str3

    def test_print(self):
        print('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')