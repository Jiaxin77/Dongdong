from django.shortcuts import render

# Create your views here.
import json
import random

from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib import colors

from needs.models import Needs
from order.models import Order
from order.serializer import OrderSerializer
import time
import reportlab
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Table, TableStyle, Spacer

from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm, inch

pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体

# Create your views here.

# 金额分配比例
# 给app的
from user.models import FarmersMember, Farmers
from user.serializer import FarmersMemberSerializer, FarmersSerializer

price_to_app = 0.2
price_total = 1.0972

# 订单id生成
def create_order_id(needid, userid):
    """

    :return:
    """
    # ###print(time.localtime())
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec

    year_str = str(year).zfill(4)
    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2)
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    second_str = str(second).zfill(2)

    random_str = str(random.randint(0, 99)).zfill(2)
    time_str = year_str + month_str + day_str + hour_str + minute_str + second_str
    orderid = time_str + random_str + str(needid) + str(userid)
    return orderid


def save_orders():  # 开工时产生订单
    """

    :return: 成功/失败
    """
    # 新建订单字段，记录当前时间


def cacel_orders():  # 取消订单
    """
    订单号？
    :return:成功/失败
    """

    # 订单状态设为已取消（并不删除）


def cancel_farmer_order(request):  # 企业取消某包工头订单
    """
    POST
    :param request: 需求ID、包工头id（或直接给订单ID？）
    :return: 成功/失败

    """
    # 调用取消订单函数


def get_orders(request):  # 获取需求对应订单!!!!!!【！！！】
    """
    GET
    :param request: 需求id
    :return: 订单列表（订单id，订单编号、交易时间、工头名字、人员姓名、、身份证号、联系方式，订单总额）+所有订单总额
    """

    # 根据需求id查订单序列化列表
    needid = request.GET.get('id') #需求id
    need = Needs.objects.get(id=needid)
    orders = Order.objects.filter(needId=need).order_by('-beginTime')
    orders_ser = OrderSerializer(orders, many=True)
    allMoney = 0
    allMoneyToFarmers = 0
    allMoneyToApp = 0
    allMoneyNum = 0
    allMoneyToFarmersNum = 0
    allMoneyToAppNum = 0
    orderList = []
    for order in orders:
        group = order.farmers.get(order=order)
        members = FarmersMember.objects.filter(group=group)
        members_ser = FarmersMemberSerializer(members,many=True)
        thisOrder={'id':order.id,'pid':order.p_id,'lastModified':str(order.lastModified),'money':round(order.money,2),'moneyToFarmers':round(order.moneyToFarmers,2),'moneyToApp':round(order.moneyToApp,2),'status':order.status,'group_leader':group.leader.name,'members':members_ser.data}
        allMoney=allMoney+round(order.money,2)
        allMoneyToFarmers=allMoneyToFarmers+round(order.moneyToFarmers,2)
        allMoneyToApp=allMoneyToApp+round(order.moneyToApp,2)
        orderList.append(thisOrder)
    allMoneyNum = allMoney * price_total
    allMoneyToAppNum = allMoney *(price_total - 1)
    allMoneyToFarmersNum = allMoney * 1
    mydict = {'result': SUCCESS,'msg':'成功获取','data':orderList,'allMoney':round(allMoneyNum,2),'allMoneyToFarmers':round(allMoneyToFarmersNum,2),'allMoneyToApp':round(allMoneyToAppNum,2)}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


def pay_for_orders(request):  # 支付订单
    """
    置订单状态为交易完成
    POST
    :param request:订单id列表
    :return:
    """
    req = json.loads(request.body)
    needid = req['needid']
    need = Needs.objects.get(id=needid)
    #idList = req['idList']  # 流水号
    orderList = Order.objects.filter(needId=need).order_by('-beginTime')
    #AllOrders = Order.objects.all()
    for order in orderList:
        #order = Order.objects.get(id=id)
        order.status = "已完成"
        order.save()
        #如果需求的订单全部支付，则状态为已完成
        need = order.needId
        myOrderList = Order.objects.filter(needId=need).order_by('-beginTime')
        flag = True
        for myOrder in myOrderList:
            if myOrder.status != "已完成":
                flag = False
        if flag:
            need.needsType = "交易成功"
            need.save()

    #对某个需求来说！
    mydict = {'result': SUCCESS, 'msg': '交易完成！'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


# def get_all_money(request):  # 获取总金额
#     """
#
#     :param request: 企业id
#     :return: 总金额、总给app金额、给包工头金额
#     """
#
#     # 获取已完成订单金额的和
#     # 按比例计算返回前端
#     mydict = {'msg': ''}
#     return HttpResponse(json.dumps(mydict), content_type="application/json")


def get_order_info(request):  # 根据某订单id获取某订单信息 -- 管理员用
    """
    GET
    :param request: 订单id
    :return: 某订单序列化信息
    """
    id = request.GET.get("pid") #订单pid
    order = Order.objects.get(p_id=id)
    order_ser = OrderSerializer(order)
    group = order.farmers.get(order=order)
    group_ser = FarmersSerializer(group)
    members = FarmersMember.objects.filter(group=group)
    members_ser = FarmersMemberSerializer(members,many=True)
    mydict = {'result': SUCCESS, 'msg': '获取成功！','order_data':order_ser.data,'group_data':group_ser.data,'member_data':members_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

#  订单下载


def get_all_orders(request):  # 获取所有订单列表——管理员用
    """
    get
    :param request:
    :return: 订单列表，总收益？
    """
    orders = Order.objects.all().order_by('-beginTime')
    order_ser = OrderSerializer(orders, many=True)
    mydict = {'result': SUCCESS, 'msg': '成功获取！', 'data': order_ser.data}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

def get_need_orders(request): #获取按需求的订单信息列表
    """
    GET
    :param request:
    :return:
    """
    needs = Needs.objects.all()
    needsList = []
    orderList = []
    order_count = 1
    for need in needs:
        orders = Order.objects.filter(needId=need).order_by('-beginTime')
        ordernum = 0
        orderMoney = 0
        orderMoneytoApp = 0
        orderMoneytoFarmers = 0

        orderFlag = "交易成功"
        for order in orders:
            ordernum = ordernum+1
            orderMoney = orderMoney+round(order.money,2)
            orderMoneytoApp = orderMoneytoApp+round(order.moneyToApp,2)
            orderMoneytoFarmers = orderMoneytoFarmers+round(order.moneyToFarmers,2)
            groups = order.farmers.all()
            for person in groups:
                thisGroup = person

            thisOrder = {'numid':order_count,'enterName':need.enterId.enterName,'needName':need.enterId.nowProject,'needsFarmerType':need.needsFarmerType,'orderStatus':order.status,'orderid':order.id,'orderMoney':round(order.money,2),'orderMoneyToFarmer':round(order.moneyToFarmers,2),'foreman':thisGroup.leader.name,'bank':thisGroup.leader.Bank,'banknum':thisGroup.leader.BankNumber,'idcard':thisGroup.leader.IDCard}
            orderList.append(thisOrder)
            order_count = order_count+1
            if order.status == "交易中":
                orderFlag = "待支付"
        orderMoneyNum = orderMoney * price_total
        orderMoneyToAppNum = orderMoney * (price_total - 1)
        orderMoneyToFarmersNum = orderMoney * 1
        thisNeed = {'id':need.id,'enterName':need.enterId.enterName,'needDes':need.needsDes,'needsFarmerType':need.needsFarmerType,'needsType':need.needsType,'orderNum':ordernum,'orderMoney':round(orderMoneyNum,2),'orderMoneyToApp':round(orderMoneyToAppNum,2),'orderMoneyToFarmers':round(orderMoneyToFarmersNum,2),'needsPayStatus':orderFlag}
        if need.needsType == "匹配完成待支付" or need.needsType == "交易成功":
            needsList.append(thisNeed)

    mydict = {'result': SUCCESS, 'msg': '成功获取！', 'data': needsList,'orderData':orderList}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


#合同确认（农民工端）
def postFarmerContractConfirm(request):
    req = json.loads(request.body)
    needid = req['needid']
    groupid = req['groupid']
    group = Farmers.objects.get(id=groupid)
    group.contractType = 1
    group.save()
    mydict = {'result': SUCCESS, 'msg': '确认成功'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")

#合同确认（企业端）
def postEnterContractConfirm(request):
    req = json.loads(request.body)
    needid = req['needid']
    need = Needs.objects.get(id=needid)
    need.contractType = 1
    need.save()
    mydict = {'result': SUCCESS, 'msg': '确认成功'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")


#咚咚和公司的销售合同 【需求id获取，返回文件路径】
def getComAndDongContract(request):
    id = request.GET.get("needid")  # 需求id
    need = Needs.objects.get(id=id)
    pdf_path="./media/contract/enterAndDong/"+"Con"+id+".pdf"
    successFlag = False
    if(need.needsType == "匹配完成待支付" or need.needsType == "交易成功"):
        #好像不能在这儿生成合同？要在匹配完成待支付时生成合同？不然合同时间不对？
        company = need.enterId.enterName
        location = need.needsLocation
        groups=""
        for group in need.matchResult.all():
            groups = groups+group.type + str(group.classNumber) + "(" + group.leader.name + "工长)    "
        payTime = str(need.needsEndTime)
        contractTime = str(need.contractTime)
        workType=need.needsFarmerType

        successFlag = getContract(pdf_path,company,location,groups,payTime,contractTime,workType)
        status = need.contractType #0为未确认，1为已确认
    if(successFlag == True):
        mypath = pdf_path[1:]
        mydict = {'result': SUCCESS, 'msg': '获取成功！','path':mypath,'status':status}
    else:
        mydict = {'result': ERROR, 'msg': '获取失败！'}

    return HttpResponse(json.dumps(mydict), content_type="application/json")


#咚咚和农民工 【需求id和农民工id获取。返回文件路径】
def getFarmerAndDongContract(request):
    needid = request.GET.get("needid")
    need = Needs.objects.get(id=needid)
    groupid = request.GET.get("groupid")
    group = Farmers.objects.get(id=groupid)
    pdf_path = "./media/contract/famAndDong/"+"Con"+needid+"_"+groupid+".pdf"
    successFlag = False
    if (need.needsType == "匹配完成待支付" or need.needsType == "交易成功"):
        company = need.enterId.enterName
        location = need.needsLocation
       # groupName = group.type+str(group.classNumber)+"("+group.leader.name+"工长)"
        payTime = str(need.needsEndTime)
        contractTime = str(need.contractTime)
        workType = group.type
       # getFarmerContract(PDF_path, company, location, group, payTime, contractTime, workType)
        successFlag = getFarmerContract(pdf_path,company,location,group,payTime,contractTime,workType)
        status = group.contractType  # 0为未确认，1为已确认
    if (successFlag == True):
        mypath = pdf_path[1:]
        mydict = {'result': SUCCESS, 'msg': '获取成功！', 'path': mypath,'status':status}
    else:
        mydict = {'result': ERROR, 'msg': '获取失败！'}
    return HttpResponse(json.dumps(mydict), content_type="application/json")





def getContract(PDF_path,company,location,group,payTime,contractTime,workType): #生成合同
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="./media/contract/enterAndDong/somefilename.pdf"'

    pdf_path = PDF_path
    Style = getSampleStyleSheet()
    reportlab.lib.styles.ParagraphStyle.defaults['wordWrap'] = 'CJK'
    title_style = Style['Normal']
    title_style.fontSize=14
    title_style.fontName='SimSun'
    title_style.wordWrap = 'CJK'
    title_style.leading = 20
    title_style.alignment = 1

    text_style = Style['Normal']
    text_style.fontSize=10
    text_style. fontName = 'SimSun'
    text_style.alignment = 1


    p = canvas.Canvas(pdf_path)
    p.setFont('SimSun', 12)
    content=[]
    #p.drawString(100,700,"咚咚点兵已匹配完成待支付需求简式合同")
    titleContent= '<para align=center fontSize=21 autoLeading="off">咚咚点兵对'+company+\
                  '<br/>的线上简式销售合同/订单</para>'
    title = Paragraph(titleContent,title_style)
    #content.append(title)
    title.wrapOn(p, 8 * inch, 8 * inch)
    title.drawOn(p,5,10 * inch)
    #第一个数字 横向，第二个数字纵向
    company=company
    applyCompany="咚咚点兵"
    location=location
    groups=group
    buycontent="哈哈哈哈"
    money="1234"
    paytime=payTime
    availtime=contractTime


    textContent="<para align=left leftIndent=100 leading=18>注册账户/采购单位：    "+company+\
         "<br/>供应单位：    "+applyCompany+ \
         "<br/>交易地点：    "+location+\
         "<br/>已匹配班组：   "+groups+\
         "<br/>项目名称：    "+"P2020031201安阳新都小区建设二期工程"+\
         "<br/>交易标的：     "+workType+"工时费（劳动价值包）"+ \
         "<br/>工时数量：     " + "100工时  注：1工时=8小时" + \
         "<br/>工时费价款：   "+"24500 元"+\
         "<br/>交易金额（价、税合计）：    "+"本合同/订单交易总金额为：24500✖️（1+6%增值税率）=25970元，采购单位"+company+"将足额支付至郑州咚咚点兵信息技术有限公司银行账户且承担全额支付责任(以银行转款凭证作为履责依据）"+\
         "<br/>质量控制：    "+"由本施工企业现场专业管理人员监督负责"+ \
         "<br/>结算方式：    " + "订单不可撤销，依据约定一次性或分批履行付款义务，逾期产生每天万分之五违约金" + \
         "<br/>质量控制：    " + " 1、本合同/订单具备合同法赋予商业合同的普遍效力；" \
                            "<br/>2、本合同所述及的“标准工时费”是指八个小时的劳动时间产生的价值成果；"\
                            "<br/>3、本合同交易标的为特殊商品“工时费（价值包）”，其产生过程均在采购单位所控制现场范围内且接受采购单位专业技术、管理人员的即时监督，因此本合同约定的工时费价款和数量均符合有效、无瑕疵的“商品特性”，采购单位不具备与此相关的异议主张和经济补偿权；"\
                            "<br/>4、本合同系采购单位和供应单位通过互联网线上沟通而协定产生且所有内容均出自双方真实意思表示，因此双方认可供应单位线上电子签章有效，以线上数据库存储的合同为原件和解释基础。"+\
         "<br/>合同生成时间：  "+availtime+"</para>"

    text = Paragraph(textContent,text_style)
    text.wrapOn(p, 7 * inch, 5 * inch)
    text.drawOn(p, 3, 3 * inch)


   # textContent.drawOn(p)

    partyA = "郑州咚咚点兵信息技术有限公司"
    partyB = company
    textPA = "<para align=left leftIndent=100>甲方：郑州咚咚点兵信息技术有限公司</para>"
    textPB = "<para align=left leftindent=320>乙方："+partyB+"</para>"
    PPA = Paragraph(textPA,text_style)
    PPB = Paragraph(textPB,text_style)
    PPA.wrapOn(p,7 * inch,5 * inch)
    PPA.drawOn(p, 3,2 * inch)
    PPB.wrapOn(p, 7 * inch, 5 * inch)
    PPB.drawOn(p, 7, 2 * inch)
    # #公章
    # img=Image("./static/pic/timg.png")
    # img_url = "./static/pic/timg.png"
    # #img=Image("https://www.dddianbing.com/pic/timg.png")
    # #img_url = "https://www.dddianbing.com/pic/timg.png"
    # # img.drawHeight=50
    # # img.drawWidth=50
    #
    #
    # p.drawImage(img_url,110,2*inch,100,100,'auto')
    p.showPage()
    p.save()

    return True
    #
    # mydict = {'result': SUCCESS, 'msg': '获取成功！'}
    # return HttpResponse(json.dumps(mydict), content_type="application/json")



def getFarmerContract(PDF_path,company,location,group,payTime,contractTime,workType): #生成合同
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="./media/contract/enterAndDong/somefilename.pdf"'
    #print(group.memberNumber)
    pdf_path = PDF_path
    Style = getSampleStyleSheet()
    reportlab.lib.styles.ParagraphStyle.defaults['wordWrap'] = 'CJK'
    title_style = Style['Normal']
    title_style.fontSize=14
    title_style.fontName='SimSun'
    title_style.wordWrap = 'CJK'
    title_style.leading = 20
    title_style.alignment = 1

    text_style = Style['Normal']
    text_style.fontSize=7
    text_style. fontName = 'SimSun'
    text_style.alignment = 1

    mypage=[]

    # p = canvas.Canvas(pdf_path)
    # p.setFont('SimSun', 12)

    content=[]
    #p.drawString(100,700,"咚咚点兵已匹配完成待支付需求简式合同")
    titleContent= '<para align=center fontSize=21 autoLeading="off">咚咚点兵对'+group.leader.name+\
                  '<br/>班组的线上简式销售合同/订单</para>'
    title = Paragraph(titleContent,title_style)
    #content.append(title)
    # title.wrapOn(p, 8 * inch, 8 * inch)
    # title.drawOn(p,5,10 * inch)
    #第一个数字 横向，第二个数字纵向
    company=company
    applyCompany="郑州咚咚点兵信息技术有限公司"
    location=location
    groups=group
    buycontent="哈哈哈哈"
    money="1234"
    paytime=payTime
    availtime=contractTime
    peopleNum = group.memberNumber
   # print(type(peopleNum))

    mypage.append(title)

    mypage.append(Spacer(5*inch, 0.5*inch))  # 添加空白，长度240，宽10

    textContent1="<para align=left leftIndent=0 leading=12>注册账户/供应班组：    "+group.leader.name+"班组"\
         "<br/>采购单位：    "+applyCompany+ \
         "<br/>合同基础：    " + "本合同签订日前，采购单位已与咚咚平台合规注册用户"+company+"签订工时费销售合同（不含税价款24500元），因此供应班组与本合同采购单位一致确认：1.）"+company+"为本合同交易标的之终端用户，2.）采购单位属于贸易商性质并承担相关经济和法律责任，3.）供应班组承担生产商/制造商相关经济和法律责任；" + \
         "<br/>交易地点：    "+location+\
         "<br/>项目名称：    "+"P2020031201安阳新都小区建设二期工程"+ \
         "<br/>工种类别：   " + workType + \
         "<br/>交易标的：     "+workType+"工时费（劳动价值包）"+ \
         "<br/>工时数量：     " + "100工时  注：1工时=8小时" + \
         "<br/>班组成员信息：     " + "共"+str(peopleNum)+"人"+ \
                 "</para>"

    textContent2="<para align=left leftIndent=0 leading=12><br/>工时费价款：   "+"24500 元"+\
         "<br/>交易金额（价、税合计）：    "+"本合同/订单交易总金额为：24500✖️（1+6%增值税率）=25970元，采购单位"+company+"将足额支付至郑州咚咚点兵信息技术有限公司银行账户且承担全额支付责任(以银行转款凭证作为履责依据）"+\
         "<br/>质量控制：    "+"由本施工企业现场专业管理人员监督负责"+ \
         "<br/>结算方式：    " + "订单不可撤销，依据约定一次性或分批履行付款义务，逾期产生每天万分之五违约金" + \
         "<br/>质量控制：    " + " 1、本合同/订单具备合同法赋予商业合同的普遍效力；" \
                            "<br/>2、本合同所述及的“标准工时费”是指八个小时的劳动时间产生的价值成果；"\
                            "<br/>3、本合同交易标的为特殊商品“工时费（价值包）”，其产生过程均在采购单位所控制现场范围内且接受采购单位专业技术、管理人员的即时监督，因此本合同约定的工时费价款和数量均符合有效、无瑕疵的“商品特性”，采购单位不具备与此相关的异议主张和经济补偿权；"\
                            "<br/>4、本合同系采购单位和供应单位通过互联网线上沟通而协定产生且所有内容均出自双方真实意思表示，因此双方认可供应单位线上电子签章有效，以线上数据库存储的合同为原件和解释基础。"+\
         "<br/>合同生成时间：  "+availtime+"</para>"

    table_data=[
        ["班组长: "+group.leader.name,"","",""],
        ["身份证号: "+group.leader.IDCard,"联系方式: "+group.leader.phonenumber,"银行: "+group.leader.Bank,"银行卡号: "+group.leader.BankNumber],
        ["编号","姓名","身份证号","联系方式"]
    ]

    num=1
    members = FarmersMember.objects.filter(group=group)
    for member in members:
        info = [str(num),member.name,member.IDCard,member.phoneNumber]
        table_data.append(info)
        num=num+1

    component_table = Table(table_data, [90, 80, 130, 130])
    component_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
        ('FONTSIZE', (0, 0), (-1, -1), 6),  # 字体大小
        #('SPAN', (0, 0), (3, 1)),  # 合并前两行
       # ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),  # 设置第一行背景颜色
      #  ('SPAN', (-1, 0), (-2, 0)),  # 合并第一行后两列
        # ('ALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 对齐
       # ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 对齐
      #  ('LINEBEFORE', (0, 0), (0, -1), 0.1, colors.grey),  # 设置表格左边线颜色为灰色，线宽为0.1
        #('TEXTCOLOR', (0, 1), (-2, -1), colors.royalblue),  # 设置表格内文字颜色
        ('GRID', (0, 2), (-1, -1), 0.5, colors.grey), # 设置表格框线为灰色，线宽为0.5
        ('BOX', (0, 0), (-1, -1), 0.7, colors.black)
    ]))

    text1 = Paragraph(textContent1,text_style)
    # text1.wrapOn(p, 7 * inch, 5 * inch)
    # text1.drawOn(p, 1, 7.5 * inch)

    mypage.append(text1)

    #
    # component_table.wrapOn(p,1,1)
    # component_table.drawOn(p,1.4*inch,4.5*inch)

    mypage.append(component_table)



    #p.append(component_table)




#    component_table.height


    text2 = Paragraph(textContent2,text_style)
    # text2.wrapOn(p, 7 * inch, 5 * inch)
    # text2.drawOn(p, 3, 2*inch)
    #7.5*inch-component_table.height-2.5*inch
    # 2*inch

    mypage.append(text2)

    mypage.append(Spacer(5 * inch, 0.5 * inch))  # 添加空白，长度240，宽10

   # textContent.drawOn(p)

    partyA = "郑州咚咚点兵信息技术有限公司"
    partyB = company
    textPA = "<para align=left leftIndent=0>甲方：郑州咚咚点兵信息技术有限公司     乙方："+partyB+"</para>"
   # textPB = "<para align=left leftindent=320>乙方："+partyB+"</para>"
    PPA = Paragraph(textPA,text_style)
  #  PPB = Paragraph(textPB,text_style)
    # PPA.wrapOn(p,7 * inch,5 * inch)
    # PPA.drawOn(p, 3,1 * inch)
    # PPB.wrapOn(p, 7 * inch, 5 * inch)
    # PPB.drawOn(p, 7, 1 * inch)
    mypage.append(PPA)
  #  mypage.append(PPB)
    #公章
    # img=Image("./static/pic/timg.png")
    # img_url = "./static/pic/timg.png"
    # #img=Image("https://www.dddianbing.com/pic/timg.png")
    # #img_url = "https://www.dddianbing.com/pic/timg.png"
    # # img.drawHeight=50
    # # img.drawWidth=50
    #
    #
    # p.drawImage(img_url,110,2*inch,100,100,'auto')
    #
    # p.showPage()
    # p.save()

    doc = SimpleDocTemplate(pdf_path)
    doc.build(mypage)

    return True
    #
    # mydict = {'result': SUCCESS, 'msg': '获取成功！'}
    # return HttpResponse(json.dumps(mydict), content_type="application/json")

