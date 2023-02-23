import re
import requests
import mysql.connector # 导入库
import urllib.request
from lxml import etree
config = {'host': '',  # 默认127.0.0.1
          'user': '',  # 用户名
          'password': '',  # 密码
          'port': ,  # 端口，默认为3306
          'database': '',  # 数据库名称
          'charset': 'utf8mb4'  # 字符编码
          }
# 链接数据库
def sql_data():
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    sql = f"SELECT * FROM `Notice`"  # SQL语句
    cursor.execute(sql)  # 执行SQL语句
    data = cursor.fetchall()  # 通过fetchall方法获得数据
    return data


# 链接数据库
def sql(user_id):
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    sql = f"SELECT * FROM `Notice` where user_id={user_id}"  # SQL语句
    cursor.execute(sql)  # 执行SQL语句
    data = cursor.fetchall()  # 通过fetchall方法获得数据
    return data
# update data
def sql_upadte(headline,link,date,content,user_id):
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    sql = f"update Notice set headline='{headline}',content='{content}',date='{date}',link='{link}' where user_id={user_id}"
    cursor.execute(sql)  # 执行SQL语句
    cnn.commit() #提交数据库
    print("更新成功")
    cnn.close()
    return True
# insert data
def sql_insert(headline,link,date):
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    sql = f"insert Notice (headline,link,date) values ('{headline}','{link}','{date}')"
    cursor.execute(sql)  # 执行SQL语句
    cnn.commit() #提交数据库
    print("添加成功！")
    cnn.close()
    return True

# find data
def sql_find(user_id):
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    # 按姓名查找并且返回
    sql = f"SELECT * FROM `Notice` where user_id={user_id}"  # SQL语句
    cursor.execute(sql)  # 执行SQL语句
    data = cursor.fetchall()  # 通过fetchall方法获得数据
    if data:
        code = True
        headline = data[0][1]
        link = data[0][2]
        date = data[0][3]
        content = data[0][4]  # 1  sever 2 kutui 3 pushplus 4 hipush
        user = data[0][5]
        use_id = data[0][6]
        user_token = data[0][7]
        # print(f"账户：{user_id}存在！")
    else:
        # print(f"账户：{user_id}不存在！")
        code = False
        headline = ""
        link = ""
        date = ""
        content = ""
        user = ""
        use_id = ""
        user_token = ""
    return code,headline,link,date,content,user,use_id,user_token

def sql_delete(user_id):
    cnn = mysql.connector.connect(**config)  # 建立MySQL连接
    cursor = cnn.cursor()  # 获得游标
    sql = f"delete from Notice where user_id = {user_id} "
    cursor.execute(sql)  # 执行SQL语句
    cnn.commit()  # 提交数据库
    print("删除成功！")
    return True


# 获取网页数据:
def acquire_data():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
    url = "http://jwc.ztbu.edu.cn/27972/"
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    notice_data = re.findall('<a href="(.*?)" target="_blank" title="(.*?)">(.*?)</a><span class="datatime">(.*?)</span>',response.text)
    notice_data = notice_data[0]
    link = notice_data[0]
    headline = notice_data[1]
    date = notice_data[3]
    print(link,headline,date)
    return headline,link,date

# 获取附件信息
def acquire_link_data(link):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
    # 定制请求头
    request = urllib.request.Request(url=link, headers=header)
    # 发送请求访问服务器，返回响应对象
    response = urllib.request.urlopen(request)
    # 解码响应对象，得到页面源码
    content = response.read().decode('utf-8')
    # 解析页面内容link部分内容,fujian
    link_data_fujian = re.findall('<a href="(.*?)" target="_blank">附件(.*?)</a>', content)
    # 数据转换为元组
    fujian_data = tuple(link_data_fujian)
    # 解析服务器响应的文件
    parse_html = etree.HTML(content)
    # 编写xpath路径，获取想要的数据,xpath的返回值是列表类型
    link_content_data = parse_html.xpath('//div[@class="layout_txtcontent_content"]//text()')
    text = ""
    for i in link_content_data:
        text += i
    link_data_content = text
    return link_data_content

    #
# 信息推送
def push_send(title, content, template,push_token):
    content = content
    template = template  # txt/htm/json/markdown
    server_url = f'http://www.pushplus.plus/send?token={push_token}&title={title}&content={content}&template={template}'
    requests.post(server_url)
    return True






# 主函数
def update_detection(user_id):
    # 获取用户存在状态
    code = sql_find(user_id) #,headline,link,date,content,user,use_id,user_token
    if code:
        # 获取数据库数据
        data = sql(user_id)
        # 获取网页数据
        h, l, d = acquire_data()
        for i in data:
            headline = i[1]
            link = i[2]
            date = i[3]
            user_token = i[7]  # 1  sever 2 kutui 3 pushplus 4 hipush
            # 比对数据
            notice_text =""
            if (h == headline and l == link and d == date):
                notice_text = f"当前无新通知！\n"
                print("无最新雄消息")
            else:
                print("教务网更新了")
                # 获取网页最新信息：附件和内容
                link_data_content = acquire_link_data(l)
                notice_text = f"标题：{h}\n通知时间：{d}\n通知内容：{link_data_content}\n" #附件信息：{k}"
                print(notice_text)
                push_send(h, link_data_content, "html",user_token)
                # 更新数据库数据
                sql_upadte(h, l, d, link_data_content, user_id)
        return True

if __name__ == '__main__':
    # 获取数据库数据
    data = sql_data()
    for i in data:
        update_detection(i[6])

    #
