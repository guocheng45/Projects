from WeixinPro.contact.token import Weixin
import pytest
import requests
import logging

from WeixinPro.contact.utils import Utils


class TestDepartment:
    @classmethod
    def setup_class(cls):
        Weixin.get_token()
        print(Weixin.token)

    @pytest.mark.parametrize("name",[
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    # 创建部门
    def test_create_dep(self,name,token):
        data={
            "name": name + Utils.udid(),
            "parentid": 1,
            "order": 1,
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()

        # 解密
        logging.debug(r)
        assert r["errcode"] == 0


    # 更新部门
    def test_update_dep(self):
        pass

    # 删除部门
    def test_delete_dep(self):
        pass

    # 获取部门列表
    def test_list_dep(self):
        pass

    