from mysql import connector
from decimal import Decimal


class DBOperation(object):

    def __init__(self, connections):
        # 连接数据库
        self.cnn = connector.connect(**connections)
        # 获取数据库游标
        self.cursor = self.cnn.cursor(cursor_class=connector.cursor.MySQLCursorDict)

    # 查询一条语句,返回字典
    # 例子：{'supplier_id': 139, 'supplier_name': '供应商勿动', 'link_phone': '13312345678'}
    def search_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    # 查询多条数据
    def search_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    # 更新数据
    def update(self, sql):
        self.cursor.execute(sql)
        self.cnn.commit()

    # 关闭数据库连接
    def close_db(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.cnn.close()

    def search_all_result_to_dict(self):
        """
        处理查询到多条数据的结果,
        返回结果类型：字典
        { fieldname1: [value1， value2， value3, value4]
        feildname2: [value11, value22, value33, value44]
        }
        """
        sql2 = "select resource_id from tb_sup_resource where resource_id in (select resource_id from tb_sup_role_resource where role_id = 66) and resource_type=1 and parent_id is not NULL"
        result = self.search_all(sql2)
        r = {}
        keys = list(result[0])
        for k in keys:
            value = []
            for m in result:
                value.append(m[k])
            r[k] = value
        return r


if __name__ == "__main__":
    from common.fileReader import IniUtil
    import json
    ini = IniUtil()
    cof = ini.get_value_of_option("db_pre", "supp_connection")
    connection = json.loads(cof)
    db = DBOperation(connection)
    sql = "select supplier_ID, supplier_name, link_phone from tb_sup_b2b t where t.supplier_name='供应商勿动'"
    x = db.search_one(sql)
    # print(x)

    sql2 = "select resource_id, resource_name from tb_sup_resource where resource_id in (select resource_id from tb_sup_role_resource where role_id = 3) and resource_type=1 and parent_id is not NULL"
    y = db.search_all(sql2)
    # print(y)

    zz = db.search_all_result_to_dict()
    # print(zz)

    sql3 = "select target_amount,start_date,end_date from tb_sup_task_target where sup_user_id = (select sup_user_id from tb_sup_user where login_name='wumeng')"
    aaaa = db.search_one(sql3)
    print(aaaa)
    a1 = aaaa['target_amount']
    a2 = aaaa['start_date']
    a3 = aaaa['end_date']
    print(a1)
    print(isinstance(a1, (Decimal, float)))
    print([str(a1), int(a1)][int(a1)==a1])







