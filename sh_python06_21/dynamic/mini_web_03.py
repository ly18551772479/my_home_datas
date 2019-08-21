# # 处理我们的逻辑,返回一个数据
#
# def application(file_name):
#     if file_name == "/index.py":
#         return "index.py is show"
#     elif file_name == "/center.py":
#         return "center.py is show"
#     else:
#         return "not page is find!"
#

import re

from pymysql import  *


address_params = dict()  # 路由表


def route(data):
    def set_fun(func):
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        address_params[data] = call_fun
        return call_fun

    return set_fun


@route("/index.py")
def index():
    with open("./templates/index.html") as f:
        content = f.read()


    row_str = """
<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
    """

    # 1. 去数据库拿到数据
        # 1.1 连接数据 库
        # 1.2 执行操作
        # 1.3 相关处理
        # 1.4 关闭
    # 2. 循环替换我们查询出来的数制
    # 3. 替换展示
    # 正则
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 执行 sql
    cs1.execute("select * from info;")

    # 拿到数据
    tables_str = cs1.fetchall()

    # 关闭
    cs1.close()
    conn.close()


    # 拼接数据
    all_row_str = ""

    for temp in tables_str:
        all_row_str += row_str%(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])

    content_new  = re.sub(r"\{%content%\}", all_row_str ,content)

    return content_new

@route("/center.py")
def center():
    with open("./templates/center.html")  as f:
        content = f.read()

    search_sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i , focus as f where i.id = f.info_id;"""


    row_str = """
    <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/000059.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000059">
            </td>
        </tr>
    """
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    cs1.execute(search_sql)

    tables_str = cs1.fetchall()

    cs1.close()
    conn.close()

    show_all_row_strs = ""


    for temp in tables_str:
        show_all_row_strs += row_str%(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6])


    # 正则
    content_new  = re.sub(r"\{%content%\}",show_all_row_strs, content)

    return content_new

@route("/login.py")
def login():
    return "login is show"


@route("/xxx.py")
def xxx():
    return "xxx"




def application(dict_url, head_params):
    head_params("200 OK", [("Content-Type", "text/html;charset=utf-8"), ("hm", "sh_python6")])

    file_name = dict_url['file_name']

    # address_params = {"/index.py": index, "/center.py": center, "/login.py": login}
    print(address_params)
    try:

        method = address_params[file_name]
        return method()  # 返回数据
    except Exception as e:
        print(e)
        return "not page is find!"

        # if file_name == "/index.py":
        #     return index()
        #
        # elif file_name == "/center.py":
        #     return center()
        #
        # else:
        #     return "not page is find!"
