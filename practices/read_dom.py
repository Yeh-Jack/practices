from xml.dom import minidom

# 讀取XML檔案
tree = minidom.parse("觀光景點.xml")
# 建立空list，等一下要用來存放景點名稱與地址
data = []
# 遍歷整個樹元素找尋標籤<Info>
earthquake_info = tree.getElementsByTagName("Info")
# 用迴圈開始一個一個檢查資料
for child in earthquake_info:
    # 先確認每個<Info>中是否有子節點<Name>
    # child.getElementsByTagName("Name")[0] 意指找到<Name>節點
    name_node = child.getElementsByTagName("Name")
    # 若<Name>節點中的第一個子節點不為空(也就是不為None)
    if name_node and name_node[0].firstChild:
        # 用.nodeValue擷取該本文的值
        # 在此也就是取出景點名稱
        name = name_node[0].firstChild.nodeValue
    else:
        name = "無景點名稱"
    # 同10-19行功能
    address_node = child.getElementsByTagName("Add")
    if address_node and address_node[0].firstChild:
        address = address_node[0].firstChild.nodeValue
    else:
        address = "無地址"
    # 把找出的景點名稱與地址存放到list中
    data.append([name, address])
