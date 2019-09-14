from WeixinPro.contact.token import Weixin
import pytest
import requests
import logging

from WeixinPro.contact.utils import Utils


class TestDepartment:

    @classmethod
    def setup_class(cls):
        cls.token = Weixin.get_token()
        print(cls.token)

    # @pytest.mark.parametrize("name",[
    #     "广州研发中心",
    #     "東京アニメーション研究所",
    #     "도쿄 애니메이션 연구소",
    #     "معهد طوكيو للرسوم المتحركة",
    #     "東京動漫研究所"
    # ])

    # 创建部门

    def test_create_dep(cls):
        data={
            "name": "zhazha",
            "parentid": 1,
            "order": 1,
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": cls.token},
                          json=data
                          ).json()
        print('===========',r)
        logging.debug(r)
        assert r["errcode"] == 0


    # 更新部门

    def test_update_dep(cls,name='zhazha'):
        data={
            "id": 2,
            "name": 1,
            "parentid": 1,
        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                        params={"access_token":cls.token},
                        json=data
                        ).json()

        logging.debug(r)
        assert r["errcode"]==0

    # 删除部门

    def test_delete_dep(cls,id=65):

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                          params={"access_token": cls.token,"id":id}
                         ).json()

        logging.debug(r)
        assert r["errcode"] == 0

    # 获取部门列表
    def test_list_dep(cls):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": cls.token}
                         ).json()

        logging.debug(r)
        assert r["errcode"] == 0

    