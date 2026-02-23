from lxml import etree


#xpath解析
#（1）本地文件         etree.parse
#（2）服务器响应的数据response.read().decode("UTF-8")        etree.HTML()
#xpath解析本地文件
tree=etree.parse("xpath的基本使用.html")
#通过tree.xpath("xpath路径")

#查照ul下面的li
#li_list=tree.xpath("//body/ul/li")

#判断列表长度
#print(li_list)
#print(len(li_list))
#查找所以有id属性的标签
#li1_list=tree.xpath("//ul/li[@id]/text()")    #text()获取标签中的内容

#找到id为l1的标签
li1_list=tree.xpath("//ul/li[@ id='l1']/text")

print(li1_list)
print(len(li1_list))






























