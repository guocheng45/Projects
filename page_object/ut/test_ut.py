import yaml

class TestYaml(object):
    def test_yaml(self):
        dict = yaml.load(open("..\data\hys.yaml",'r'))
        print(dict)
        for step in dict["login_app"]:
            print(step['locator'])
        return self