import json
from multiprocessing.pool import ThreadPool

import requests

import http.cookiejar
import time
from multiprocessing.pool import Pool

import threadpool as threadpool

cookies = {}  # 构建一个空字典用来存放cookies

headers = {

    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://lib2.ecjtu.edu.cn/ClientWeb/m/ic2/Default.aspx',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'lib2.ecjtu.edu.cn',
}


def initRoom():
    a = []
    b = []
    c = []
    a.append('一层A区')
    b.append('100531890')
    c.append('100531916')
    a.append('一层B区')
    b.append('100531890')
    c.append('100531919')
    a.append('一层C区')
    b.append('100531890')
    c.append('100531921')
    a.append('一层D区')
    b.append('100531890')
    c.append('100531923')
    a.append('电子阅览区')
    b.append('104556463')
    c.append('104558576')
    a.append('文学厅（301）')
    b.append('103762297')
    c.append('103762303')
    a.append('史地厅（302）')
    b.append('103762297')
    c.append('103762305')
    a.append('交通厅（309）')
    b.append('103762297')
    c.append('103762307')
    a.append('经济厅（401）')
    b.append('103762299')
    c.append('103762309')
    a.append('经济厅（402）')
    b.append('103762299')
    c.append('103762311')
    a.append('经济厅（409）')
    b.append('103762299')
    c.append('103762313')
    a.append('政法厅（501）')
    b.append('103762301')
    c.append('103762315')
    a.append('社科厅（502）')
    b.append('103762301')
    c.append('103762317')
    a.append('哲学厅（509）')
    b.append('103762301')
    c.append('103762319')
    a.append('南馆302自习室')
    b.append('103763032')
    c.append('103763036')
    a.append('南馆307自习室')
    b.append('103763032')
    c.append('103763038')
    a.append('南馆402自习室')
    b.append('103763034')
    c.append('103763040')
    a.append('南馆404自习室')
    b.append('103763034')
    c.append('103763042')
    a.append('南馆410自习室')
    b.append('103763034')
    c.append('103763044')
    ans = []
    ans.append(a)
    ans.append(b)
    ans.append(c)
    return ans

def initSeat():
    a=[]
    b=[]
    c=[]
    a.append('1F-A001')
    b.append('100531924')
    c.append('北馆一层自习室')

    a.append('1F-A002')
    b.append('100531925')
    c.append('北馆一层自习室')

    a.append('1F-A003')
    b.append('100531926')
    c.append('北馆一层自习室')

    a.append('1F-A004')
    b.append('100531927')
    c.append('北馆一层自习室')

    a.append('1F-A005')
    b.append('100531928')
    c.append('北馆一层自习室')

    a.append('1F-A006')
    b.append('100531929')
    c.append('北馆一层自习室')

    a.append('1F-A007')
    b.append('100531930')
    c.append('北馆一层自习室')

    a.append('1F-A008')
    b.append('100531931')
    c.append('北馆一层自习室')

    a.append('1F-A009')
    b.append('100531932')
    c.append('北馆一层自习室')

    a.append('1F-A010')
    b.append('100531933')
    c.append('北馆一层自习室')

    a.append('1F-A011')
    b.append('100531934')
    c.append('北馆一层自习室')

    a.append('1F-A012')
    b.append('100531935')
    c.append('北馆一层自习室')

    a.append('1F-A013')
    b.append('100531936')
    c.append('北馆一层自习室')

    a.append('1F-A014')
    b.append('100531937')
    c.append('北馆一层自习室')

    a.append('1F-A015')
    b.append('100531938')
    c.append('北馆一层自习室')

    a.append('1F-A016')
    b.append('100531939')
    c.append('北馆一层自习室')

    a.append('1F-A017')
    b.append('100531940')
    c.append('北馆一层自习室')

    a.append('1F-A018')
    b.append('100531941')
    c.append('北馆一层自习室')

    a.append('1F-A019')
    b.append('100531942')
    c.append('北馆一层自习室')

    a.append('1F-A020')
    b.append('100531943')
    c.append('北馆一层自习室')

    a.append('1F-A021')
    b.append('100531944')
    c.append('北馆一层自习室')

    a.append('1F-A022')
    b.append('100531945')
    c.append('北馆一层自习室')

    a.append('1F-A023')
    b.append('100531946')
    c.append('北馆一层自习室')

    a.append('1F-A024')
    b.append('100531947')
    c.append('北馆一层自习室')

    a.append('1F-A025')
    b.append('100531948')
    c.append('北馆一层自习室')

    a.append('1F-A026')
    b.append('100531949')
    c.append('北馆一层自习室')

    a.append('1F-A027')
    b.append('100531950')
    c.append('北馆一层自习室')

    a.append('1F-A028')
    b.append('100531951')
    c.append('北馆一层自习室')

    a.append('1F-A029')
    b.append('100531952')
    c.append('北馆一层自习室')

    a.append('1F-A030')
    b.append('100531953')
    c.append('北馆一层自习室')

    a.append('1F-A031')
    b.append('100531954')
    c.append('北馆一层自习室')

    a.append('1F-A032')
    b.append('100531955')
    c.append('北馆一层自习室')

    a.append('1F-A033')
    b.append('100531956')
    c.append('北馆一层自习室')

    a.append('1F-A034')
    b.append('100531957')
    c.append('北馆一层自习室')

    a.append('1F-A035')
    b.append('100531958')
    c.append('北馆一层自习室')

    a.append('1F-A036')
    b.append('100531959')
    c.append('北馆一层自习室')

    a.append('1F-A037')
    b.append('100531960')
    c.append('北馆一层自习室')

    a.append('1F-A038')
    b.append('100531961')
    c.append('北馆一层自习室')

    a.append('1F-A039')
    b.append('100531962')
    c.append('北馆一层自习室')

    a.append('1F-A040')
    b.append('100531963')
    c.append('北馆一层自习室')

    a.append('1F-A041')
    b.append('100531964')
    c.append('北馆一层自习室')

    a.append('1F-A042')
    b.append('100531965')
    c.append('北馆一层自习室')

    a.append('1F-A043')
    b.append('100531966')
    c.append('北馆一层自习室')

    a.append('1F-A044')
    b.append('100531967')
    c.append('北馆一层自习室')

    a.append('1F-A045')
    b.append('100531968')
    c.append('北馆一层自习室')

    a.append('1F-A046')
    b.append('100531969')
    c.append('北馆一层自习室')

    a.append('1F-A047')
    b.append('100531970')
    c.append('北馆一层自习室')

    a.append('1F-A048')
    b.append('100531971')
    c.append('北馆一层自习室')

    a.append('1F-A049')
    b.append('100531972')
    c.append('北馆一层自习室')

    a.append('1F-A050')
    b.append('100531973')
    c.append('北馆一层自习室')

    a.append('1F-A051')
    b.append('100531974')
    c.append('北馆一层自习室')

    a.append('1F-A052')
    b.append('100531975')
    c.append('北馆一层自习室')

    a.append('1F-A053')
    b.append('100531976')
    c.append('北馆一层自习室')

    a.append('1F-A054')
    b.append('100531977')
    c.append('北馆一层自习室')

    a.append('1F-A055')
    b.append('100531978')
    c.append('北馆一层自习室')

    a.append('1F-A056')
    b.append('100531979')
    c.append('北馆一层自习室')

    a.append('1F-A057')
    b.append('100531980')
    c.append('北馆一层自习室')

    a.append('1F-A058')
    b.append('100531981')
    c.append('北馆一层自习室')

    a.append('1F-A059')
    b.append('100531982')
    c.append('北馆一层自习室')

    a.append('1F-A060')
    b.append('100531983')
    c.append('北馆一层自习室')

    a.append('1F-A061')
    b.append('100531984')
    c.append('北馆一层自习室')

    a.append('1F-A062')
    b.append('100531985')
    c.append('北馆一层自习室')

    a.append('1F-A063')
    b.append('100531986')
    c.append('北馆一层自习室')

    a.append('1F-A064')
    b.append('100531987')
    c.append('北馆一层自习室')

    a.append('1F-A065')
    b.append('100531988')
    c.append('北馆一层自习室')

    a.append('1F-A066')
    b.append('100531989')
    c.append('北馆一层自习室')

    a.append('1F-A067')
    b.append('100531990')
    c.append('北馆一层自习室')

    a.append('1F-A068')
    b.append('100531991')
    c.append('北馆一层自习室')

    a.append('1F-A069')
    b.append('100531992')
    c.append('北馆一层自习室')

    a.append('1F-A070')
    b.append('100531993')
    c.append('北馆一层自习室')

    a.append('1F-A071')
    b.append('100531994')
    c.append('北馆一层自习室')

    a.append('1F-A072')
    b.append('100531995')
    c.append('北馆一层自习室')

    a.append('1F-A073')
    b.append('100531996')
    c.append('北馆一层自习室')

    a.append('1F-A074')
    b.append('100531997')
    c.append('北馆一层自习室')

    a.append('1F-A075')
    b.append('100531998')
    c.append('北馆一层自习室')

    a.append('1F-A076')
    b.append('100531999')
    c.append('北馆一层自习室')

    a.append('1F-A077')
    b.append('100532000')
    c.append('北馆一层自习室')

    a.append('1F-A078')
    b.append('100532001')
    c.append('北馆一层自习室')

    a.append('1F-A079')
    b.append('100532002')
    c.append('北馆一层自习室')

    a.append('1F-A080')
    b.append('100532003')
    c.append('北馆一层自习室')

    a.append('1F-A081')
    b.append('100532004')
    c.append('北馆一层自习室')

    a.append('1F-A082')
    b.append('100532005')
    c.append('北馆一层自习室')

    a.append('1F-A083')
    b.append('100532006')
    c.append('北馆一层自习室')

    a.append('1F-A084')
    b.append('100532007')
    c.append('北馆一层自习室')

    a.append('1F-A085')
    b.append('100532008')
    c.append('北馆一层自习室')

    a.append('1F-A086')
    b.append('100532009')
    c.append('北馆一层自习室')

    a.append('1F-A087')
    b.append('100532010')
    c.append('北馆一层自习室')

    a.append('1F-A088')
    b.append('100532011')
    c.append('北馆一层自习室')

    a.append('1F-A089')
    b.append('100532012')
    c.append('北馆一层自习室')

    a.append('1F-A090')
    b.append('100532013')
    c.append('北馆一层自习室')

    a.append('1F-A091')
    b.append('100532014')
    c.append('北馆一层自习室')

    a.append('1F-A092')
    b.append('100532015')
    c.append('北馆一层自习室')

    a.append('1F-A093')
    b.append('100532016')
    c.append('北馆一层自习室')

    a.append('1F-A094')
    b.append('100532017')
    c.append('北馆一层自习室')

    a.append('1F-A095')
    b.append('100532018')
    c.append('北馆一层自习室')

    a.append('1F-A096')
    b.append('100532019')
    c.append('北馆一层自习室')

    a.append('1F-A097')
    b.append('100532020')
    c.append('北馆一层自习室')

    a.append('1F-A098')
    b.append('100532021')
    c.append('北馆一层自习室')

    a.append('1F-A099')
    b.append('100532022')
    c.append('北馆一层自习室')

    a.append('1F-A100')
    b.append('100532023')
    c.append('北馆一层自习室')

    a.append('1F-A101')
    b.append('100532024')
    c.append('北馆一层自习室')

    a.append('1F-A102')
    b.append('100532025')
    c.append('北馆一层自习室')

    a.append('1F-A103')
    b.append('100532026')
    c.append('北馆一层自习室')

    a.append('1F-A104')
    b.append('100532027')
    c.append('北馆一层自习室')

    a.append('1F-A105')
    b.append('100532028')
    c.append('北馆一层自习室')

    a.append('1F-A106')
    b.append('100532029')
    c.append('北馆一层自习室')

    a.append('1F-A107')
    b.append('100532030')
    c.append('北馆一层自习室')

    a.append('1F-A108')
    b.append('100532031')
    c.append('北馆一层自习室')

    a.append('1F-A109')
    b.append('100532032')
    c.append('北馆一层自习室')

    a.append('1F-A110')
    b.append('100532033')
    c.append('北馆一层自习室')

    a.append('1F-A111')
    b.append('100532034')
    c.append('北馆一层自习室')

    a.append('1F-A112')
    b.append('100532035')
    c.append('北馆一层自习室')

    a.append('1F-A113')
    b.append('100532036')
    c.append('北馆一层自习室')

    a.append('1F-A114')
    b.append('100532037')
    c.append('北馆一层自习室')

    a.append('1F-A115')
    b.append('100532038')
    c.append('北馆一层自习室')

    a.append('1F-A116')
    b.append('100532039')
    c.append('北馆一层自习室')

    a.append('1F-A117')
    b.append('100532040')
    c.append('北馆一层自习室')

    a.append('1F-A118')
    b.append('100532041')
    c.append('北馆一层自习室')

    a.append('1F-A119')
    b.append('100532042')
    c.append('北馆一层自习室')

    a.append('1F-A120')
    b.append('100532043')
    c.append('北馆一层自习室')

    a.append('1F-A121')
    b.append('100532044')
    c.append('北馆一层自习室')

    a.append('1F-A122')
    b.append('100532045')
    c.append('北馆一层自习室')

    a.append('1F-A123')
    b.append('100532046')
    c.append('北馆一层自习室')

    a.append('1F-A124')
    b.append('100532047')
    c.append('北馆一层自习室')

    a.append('1F-A125')
    b.append('100532048')
    c.append('北馆一层自习室')

    a.append('1F-A126')
    b.append('100532049')
    c.append('北馆一层自习室')

    a.append('1F-A127')
    b.append('100532050')
    c.append('北馆一层自习室')

    a.append('1F-A128')
    b.append('100532051')
    c.append('北馆一层自习室')

    a.append('1F-A129')
    b.append('100532052')
    c.append('北馆一层自习室')

    a.append('1F-A130')
    b.append('100532053')
    c.append('北馆一层自习室')

    a.append('1F-A131')
    b.append('100532054')
    c.append('北馆一层自习室')

    a.append('1F-A132')
    b.append('100532055')
    c.append('北馆一层自习室')

    a.append('1F-A133')
    b.append('100532056')
    c.append('北馆一层自习室')

    a.append('1F-A134')
    b.append('100532057')
    c.append('北馆一层自习室')

    a.append('1F-A135')
    b.append('100532058')
    c.append('北馆一层自习室')

    a.append('1F-A136')
    b.append('100532059')
    c.append('北馆一层自习室')

    a.append('1F-A137')
    b.append('100532060')
    c.append('北馆一层自习室')

    a.append('1F-A138')
    b.append('100532061')
    c.append('北馆一层自习室')

    a.append('1F-A139')
    b.append('100532062')
    c.append('北馆一层自习室')

    a.append('1F-A140')
    b.append('100532063')
    c.append('北馆一层自习室')

    a.append('1F-A141')
    b.append('100532064')
    c.append('北馆一层自习室')

    a.append('1F-A142')
    b.append('100532065')
    c.append('北馆一层自习室')

    a.append('1F-A143')
    b.append('100532066')
    c.append('北馆一层自习室')

    a.append('1F-A144')
    b.append('100532067')
    c.append('北馆一层自习室')

    a.append('1F-A145')
    b.append('100532068')
    c.append('北馆一层自习室')

    a.append('1F-A146')
    b.append('100532069')
    c.append('北馆一层自习室')

    a.append('1F-A147')
    b.append('100532070')
    c.append('北馆一层自习室')

    a.append('1F-A148')
    b.append('100532071')
    c.append('北馆一层自习室')

    a.append('1F-A149')
    b.append('100532072')
    c.append('北馆一层自习室')

    a.append('1F-A150')
    b.append('100532073')
    c.append('北馆一层自习室')

    a.append('1F-A151')
    b.append('100532074')
    c.append('北馆一层自习室')

    a.append('1F-A152')
    b.append('100532075')
    c.append('北馆一层自习室')

    a.append('1F-A153')
    b.append('100532076')
    c.append('北馆一层自习室')

    a.append('1F-A154')
    b.append('100532077')
    c.append('北馆一层自习室')

    a.append('1F-A155')
    b.append('100532078')
    c.append('北馆一层自习室')

    a.append('1F-A156')
    b.append('100532079')
    c.append('北馆一层自习室')

    a.append('1F-A157')
    b.append('100532080')
    c.append('北馆一层自习室')

    a.append('1F-A158')
    b.append('100532081')
    c.append('北馆一层自习室')

    a.append('1F-B001')
    b.append('100532082')
    c.append('北馆一层自习室')

    a.append('1F-B002')
    b.append('100532083')
    c.append('北馆一层自习室')

    a.append('1F-B003')
    b.append('100532084')
    c.append('北馆一层自习室')

    a.append('1F-B004')
    b.append('100532085')
    c.append('北馆一层自习室')

    a.append('1F-B005')
    b.append('100532086')
    c.append('北馆一层自习室')

    a.append('1F-B006')
    b.append('100532087')
    c.append('北馆一层自习室')

    a.append('1F-B007')
    b.append('100532088')
    c.append('北馆一层自习室')

    a.append('1F-B008')
    b.append('100532089')
    c.append('北馆一层自习室')

    a.append('1F-B009')
    b.append('100532090')
    c.append('北馆一层自习室')

    a.append('1F-B010')
    b.append('100532091')
    c.append('北馆一层自习室')

    a.append('1F-B011')
    b.append('100532092')
    c.append('北馆一层自习室')

    a.append('1F-B012')
    b.append('100532093')
    c.append('北馆一层自习室')

    a.append('1F-B013')
    b.append('100532094')
    c.append('北馆一层自习室')

    a.append('1F-B014')
    b.append('100532095')
    c.append('北馆一层自习室')

    a.append('1F-B015')
    b.append('100532096')
    c.append('北馆一层自习室')

    a.append('1F-B016')
    b.append('100532097')
    c.append('北馆一层自习室')

    a.append('1F-B017')
    b.append('100532098')
    c.append('北馆一层自习室')

    a.append('1F-B018')
    b.append('100532099')
    c.append('北馆一层自习室')

    a.append('1F-B019')
    b.append('100532100')
    c.append('北馆一层自习室')

    a.append('1F-B020')
    b.append('100532101')
    c.append('北馆一层自习室')

    a.append('1F-B021')
    b.append('100532102')
    c.append('北馆一层自习室')

    a.append('1F-B022')
    b.append('100532103')
    c.append('北馆一层自习室')

    a.append('1F-B023')
    b.append('100532104')
    c.append('北馆一层自习室')

    a.append('1F-B024')
    b.append('100532105')
    c.append('北馆一层自习室')

    a.append('1F-B025')
    b.append('100532106')
    c.append('北馆一层自习室')

    a.append('1F-B026')
    b.append('100532107')
    c.append('北馆一层自习室')

    a.append('1F-B027')
    b.append('100532108')
    c.append('北馆一层自习室')

    a.append('1F-B028')
    b.append('100532109')
    c.append('北馆一层自习室')

    a.append('1F-B029')
    b.append('100532110')
    c.append('北馆一层自习室')

    a.append('1F-B030')
    b.append('100532111')
    c.append('北馆一层自习室')

    a.append('1F-B031')
    b.append('100532112')
    c.append('北馆一层自习室')

    a.append('1F-B032')
    b.append('100532113')
    c.append('北馆一层自习室')

    a.append('1F-B033')
    b.append('100532114')
    c.append('北馆一层自习室')

    a.append('1F-B034')
    b.append('100532115')
    c.append('北馆一层自习室')

    a.append('1F-B035')
    b.append('100532116')
    c.append('北馆一层自习室')

    a.append('1F-B036')
    b.append('100532117')
    c.append('北馆一层自习室')

    a.append('1F-B037')
    b.append('100532118')
    c.append('北馆一层自习室')

    a.append('1F-B038')
    b.append('100532119')
    c.append('北馆一层自习室')

    a.append('1F-B039')
    b.append('100532120')
    c.append('北馆一层自习室')

    a.append('1F-B040')
    b.append('100532121')
    c.append('北馆一层自习室')

    a.append('1F-B041')
    b.append('100532122')
    c.append('北馆一层自习室')

    a.append('1F-B042')
    b.append('100532123')
    c.append('北馆一层自习室')

    a.append('1F-B043')
    b.append('100532124')
    c.append('北馆一层自习室')

    a.append('1F-B044')
    b.append('100532125')
    c.append('北馆一层自习室')

    a.append('1F-B045')
    b.append('100532126')
    c.append('北馆一层自习室')

    a.append('1F-B046')
    b.append('100532127')
    c.append('北馆一层自习室')

    a.append('1F-B047')
    b.append('100532128')
    c.append('北馆一层自习室')

    a.append('1F-B048')
    b.append('100532129')
    c.append('北馆一层自习室')

    a.append('1F-B049')
    b.append('100532130')
    c.append('北馆一层自习室')

    a.append('1F-B050')
    b.append('100532131')
    c.append('北馆一层自习室')

    a.append('1F-B051')
    b.append('100532132')
    c.append('北馆一层自习室')

    a.append('1F-B052')
    b.append('100532133')
    c.append('北馆一层自习室')

    a.append('1F-B053')
    b.append('100532134')
    c.append('北馆一层自习室')

    a.append('1F-B054')
    b.append('100532135')
    c.append('北馆一层自习室')

    a.append('1F-B055')
    b.append('100532136')
    c.append('北馆一层自习室')

    a.append('1F-B056')
    b.append('100532137')
    c.append('北馆一层自习室')

    a.append('1F-B057')
    b.append('100532138')
    c.append('北馆一层自习室')

    a.append('1F-B058')
    b.append('100532139')
    c.append('北馆一层自习室')

    a.append('1F-B059')
    b.append('100532140')
    c.append('北馆一层自习室')

    a.append('1F-B060')
    b.append('100532141')
    c.append('北馆一层自习室')

    a.append('1F-B061')
    b.append('100532142')
    c.append('北馆一层自习室')

    a.append('1F-B062')
    b.append('100532143')
    c.append('北馆一层自习室')

    a.append('1F-B063')
    b.append('100532144')
    c.append('北馆一层自习室')

    a.append('1F-B064')
    b.append('100532145')
    c.append('北馆一层自习室')

    a.append('1F-B065')
    b.append('100532146')
    c.append('北馆一层自习室')

    a.append('1F-B066')
    b.append('100532147')
    c.append('北馆一层自习室')

    a.append('1F-B067')
    b.append('100532148')
    c.append('北馆一层自习室')

    a.append('1F-B068')
    b.append('100532149')
    c.append('北馆一层自习室')

    a.append('1F-B069')
    b.append('100532150')
    c.append('北馆一层自习室')

    a.append('1F-B070')
    b.append('100532151')
    c.append('北馆一层自习室')

    a.append('1F-B071')
    b.append('100532152')
    c.append('北馆一层自习室')

    a.append('1F-B072')
    b.append('100532153')
    c.append('北馆一层自习室')

    a.append('1F-B073')
    b.append('100532154')
    c.append('北馆一层自习室')

    a.append('1F-B074')
    b.append('100532155')
    c.append('北馆一层自习室')

    a.append('1F-B075')
    b.append('100532156')
    c.append('北馆一层自习室')

    a.append('1F-B076')
    b.append('100532157')
    c.append('北馆一层自习室')

    a.append('1F-B077')
    b.append('100532158')
    c.append('北馆一层自习室')

    a.append('1F-B078')
    b.append('100532159')
    c.append('北馆一层自习室')

    a.append('1F-B079')
    b.append('100532160')
    c.append('北馆一层自习室')

    a.append('1F-B080')
    b.append('100532161')
    c.append('北馆一层自习室')

    a.append('1F-B081')
    b.append('100532162')
    c.append('北馆一层自习室')

    a.append('1F-B082')
    b.append('100532163')
    c.append('北馆一层自习室')

    a.append('1F-B083')
    b.append('100532164')
    c.append('北馆一层自习室')

    a.append('1F-B084')
    b.append('100532165')
    c.append('北馆一层自习室')

    a.append('1F-B085')
    b.append('100532166')
    c.append('北馆一层自习室')

    a.append('1F-B086')
    b.append('100532167')
    c.append('北馆一层自习室')

    a.append('1F-B087')
    b.append('100532168')
    c.append('北馆一层自习室')

    a.append('1F-B088')
    b.append('100532169')
    c.append('北馆一层自习室')

    a.append('1F-B089')
    b.append('100532170')
    c.append('北馆一层自习室')

    a.append('1F-B090')
    b.append('100532171')
    c.append('北馆一层自习室')

    a.append('1F-B091')
    b.append('100532172')
    c.append('北馆一层自习室')

    a.append('1F-B092')
    b.append('100532173')
    c.append('北馆一层自习室')

    a.append('1F-B093')
    b.append('100532174')
    c.append('北馆一层自习室')

    a.append('1F-B094')
    b.append('100532175')
    c.append('北馆一层自习室')

    a.append('1F-B095')
    b.append('100532176')
    c.append('北馆一层自习室')

    a.append('1F-B096')
    b.append('100532177')
    c.append('北馆一层自习室')

    a.append('1F-B097')
    b.append('100532178')
    c.append('北馆一层自习室')

    a.append('1F-B098')
    b.append('100532179')
    c.append('北馆一层自习室')

    a.append('1F-B099')
    b.append('100532180')
    c.append('北馆一层自习室')

    a.append('1F-B100')
    b.append('100532181')
    c.append('北馆一层自习室')

    a.append('1F-B101')
    b.append('100532182')
    c.append('北馆一层自习室')

    a.append('1F-B102')
    b.append('100532183')
    c.append('北馆一层自习室')

    a.append('1F-B103')
    b.append('100532184')
    c.append('北馆一层自习室')

    a.append('1F-B104')
    b.append('100532185')
    c.append('北馆一层自习室')

    a.append('1F-B105')
    b.append('100532186')
    c.append('北馆一层自习室')

    a.append('1F-B106')
    b.append('100532187')
    c.append('北馆一层自习室')

    a.append('1F-B107')
    b.append('100532188')
    c.append('北馆一层自习室')

    a.append('1F-B108')
    b.append('100532189')
    c.append('北馆一层自习室')

    a.append('1F-B109')
    b.append('100532190')
    c.append('北馆一层自习室')

    a.append('1F-B110')
    b.append('100532191')
    c.append('北馆一层自习室')

    a.append('1F-B111')
    b.append('100532192')
    c.append('北馆一层自习室')

    a.append('1F-B112')
    b.append('100532193')
    c.append('北馆一层自习室')

    a.append('1F-B113')
    b.append('100532194')
    c.append('北馆一层自习室')

    a.append('1F-B114')
    b.append('100532195')
    c.append('北馆一层自习室')

    a.append('1F-B115')
    b.append('100532196')
    c.append('北馆一层自习室')

    a.append('1F-B116')
    b.append('100532197')
    c.append('北馆一层自习室')

    a.append('1F-B117')
    b.append('100532198')
    c.append('北馆一层自习室')

    a.append('1F-B118')
    b.append('100532199')
    c.append('北馆一层自习室')

    a.append('1F-B119')
    b.append('100532200')
    c.append('北馆一层自习室')

    a.append('1F-B120')
    b.append('100532201')
    c.append('北馆一层自习室')

    a.append('1F-B121')
    b.append('100532202')
    c.append('北馆一层自习室')

    a.append('1F-B122')
    b.append('100532203')
    c.append('北馆一层自习室')

    a.append('1F-B123')
    b.append('100532204')
    c.append('北馆一层自习室')

    a.append('1F-B124')
    b.append('100532205')
    c.append('北馆一层自习室')

    a.append('1F-B125')
    b.append('100532206')
    c.append('北馆一层自习室')

    a.append('1F-B126')
    b.append('100532207')
    c.append('北馆一层自习室')

    a.append('1F-B127')
    b.append('100532208')
    c.append('北馆一层自习室')

    a.append('1F-B128')
    b.append('100532209')
    c.append('北馆一层自习室')

    a.append('1F-B129')
    b.append('100532210')
    c.append('北馆一层自习室')

    a.append('1F-B130')
    b.append('100532211')
    c.append('北馆一层自习室')

    a.append('1F-B131')
    b.append('100532212')
    c.append('北馆一层自习室')

    a.append('1F-B132')
    b.append('100532213')
    c.append('北馆一层自习室')

    a.append('1F-B133')
    b.append('100532214')
    c.append('北馆一层自习室')

    a.append('1F-B134')
    b.append('100532215')
    c.append('北馆一层自习室')

    a.append('1F-B135')
    b.append('100532216')
    c.append('北馆一层自习室')

    a.append('1F-B136')
    b.append('100532217')
    c.append('北馆一层自习室')

    a.append('1F-B137')
    b.append('100532218')
    c.append('北馆一层自习室')

    a.append('1F-B138')
    b.append('100532219')
    c.append('北馆一层自习室')

    a.append('1F-B139')
    b.append('100532220')
    c.append('北馆一层自习室')

    a.append('1F-B140')
    b.append('100532221')
    c.append('北馆一层自习室')

    a.append('1F-B141')
    b.append('100532222')
    c.append('北馆一层自习室')

    a.append('1F-B142')
    b.append('100532223')
    c.append('北馆一层自习室')

    a.append('1F-C001')
    b.append('100532224')
    c.append('北馆一层自习室')

    a.append('1F-C002')
    b.append('100532225')
    c.append('北馆一层自习室')

    a.append('1F-C003')
    b.append('100532226')
    c.append('北馆一层自习室')

    a.append('1F-C004')
    b.append('100532227')
    c.append('北馆一层自习室')

    a.append('1F-C005')
    b.append('100532228')
    c.append('北馆一层自习室')

    a.append('1F-C006')
    b.append('100532229')
    c.append('北馆一层自习室')

    a.append('1F-C007')
    b.append('100532230')
    c.append('北馆一层自习室')

    a.append('1F-C008')
    b.append('100532231')
    c.append('北馆一层自习室')

    a.append('1F-C009')
    b.append('100532232')
    c.append('北馆一层自习室')

    a.append('1F-C010')
    b.append('100532233')
    c.append('北馆一层自习室')

    a.append('1F-C011')
    b.append('100532234')
    c.append('北馆一层自习室')

    a.append('1F-C012')
    b.append('100532235')
    c.append('北馆一层自习室')

    a.append('1F-C013')
    b.append('100532236')
    c.append('北馆一层自习室')

    a.append('1F-C014')
    b.append('100532237')
    c.append('北馆一层自习室')

    a.append('1F-C015')
    b.append('100532238')
    c.append('北馆一层自习室')

    a.append('1F-C016')
    b.append('100532239')
    c.append('北馆一层自习室')

    a.append('1F-C017')
    b.append('100532240')
    c.append('北馆一层自习室')

    a.append('1F-C018')
    b.append('100532241')
    c.append('北馆一层自习室')

    a.append('1F-C019')
    b.append('100532242')
    c.append('北馆一层自习室')

    a.append('1F-C020')
    b.append('100532243')
    c.append('北馆一层自习室')

    a.append('1F-C021')
    b.append('100532244')
    c.append('北馆一层自习室')

    a.append('1F-C022')
    b.append('100532245')
    c.append('北馆一层自习室')

    a.append('1F-C023')
    b.append('100532246')
    c.append('北馆一层自习室')

    a.append('1F-C024')
    b.append('100532247')
    c.append('北馆一层自习室')

    a.append('1F-C025')
    b.append('100532248')
    c.append('北馆一层自习室')

    a.append('1F-C026')
    b.append('100532249')
    c.append('北馆一层自习室')

    a.append('1F-C027')
    b.append('100532250')
    c.append('北馆一层自习室')

    a.append('1F-C028')
    b.append('100532251')
    c.append('北馆一层自习室')

    a.append('1F-C029')
    b.append('100532252')
    c.append('北馆一层自习室')

    a.append('1F-C030')
    b.append('100532253')
    c.append('北馆一层自习室')

    a.append('1F-C031')
    b.append('100532254')
    c.append('北馆一层自习室')

    a.append('1F-C032')
    b.append('100532255')
    c.append('北馆一层自习室')

    a.append('1F-C033')
    b.append('100532256')
    c.append('北馆一层自习室')

    a.append('1F-C034')
    b.append('100532257')
    c.append('北馆一层自习室')

    a.append('1F-C035')
    b.append('100532258')
    c.append('北馆一层自习室')

    a.append('1F-C036')
    b.append('100532259')
    c.append('北馆一层自习室')

    a.append('1F-C037')
    b.append('100532260')
    c.append('北馆一层自习室')

    a.append('1F-C038')
    b.append('100532261')
    c.append('北馆一层自习室')

    a.append('1F-C039')
    b.append('100532262')
    c.append('北馆一层自习室')

    a.append('1F-C040')
    b.append('100532263')
    c.append('北馆一层自习室')

    a.append('1F-C041')
    b.append('100532264')
    c.append('北馆一层自习室')

    a.append('1F-C042')
    b.append('100532265')
    c.append('北馆一层自习室')

    a.append('1F-C043')
    b.append('100532266')
    c.append('北馆一层自习室')

    a.append('1F-C044')
    b.append('100532267')
    c.append('北馆一层自习室')

    a.append('1F-C045')
    b.append('100532268')
    c.append('北馆一层自习室')

    a.append('1F-C046')
    b.append('100532269')
    c.append('北馆一层自习室')

    a.append('1F-C047')
    b.append('100532270')
    c.append('北馆一层自习室')

    a.append('1F-C048')
    b.append('100532271')
    c.append('北馆一层自习室')

    a.append('1F-C049')
    b.append('100532272')
    c.append('北馆一层自习室')

    a.append('1F-C050')
    b.append('100532273')
    c.append('北馆一层自习室')

    a.append('1F-C051')
    b.append('100532274')
    c.append('北馆一层自习室')

    a.append('1F-C052')
    b.append('100532275')
    c.append('北馆一层自习室')

    a.append('1F-C053')
    b.append('100532276')
    c.append('北馆一层自习室')

    a.append('1F-C054')
    b.append('100532277')
    c.append('北馆一层自习室')

    a.append('1F-C055')
    b.append('100532278')
    c.append('北馆一层自习室')

    a.append('1F-C056')
    b.append('100532279')
    c.append('北馆一层自习室')

    a.append('1F-C057')
    b.append('100532280')
    c.append('北馆一层自习室')

    a.append('1F-C058')
    b.append('100532281')
    c.append('北馆一层自习室')

    a.append('1F-C059')
    b.append('100532282')
    c.append('北馆一层自习室')

    a.append('1F-C060')
    b.append('100532283')
    c.append('北馆一层自习室')

    a.append('1F-C061')
    b.append('100532284')
    c.append('北馆一层自习室')

    a.append('1F-C062')
    b.append('100532285')
    c.append('北馆一层自习室')

    a.append('1F-C063')
    b.append('100532286')
    c.append('北馆一层自习室')

    a.append('1F-C064')
    b.append('100532287')
    c.append('北馆一层自习室')

    a.append('1F-C065')
    b.append('100532288')
    c.append('北馆一层自习室')

    a.append('1F-C066')
    b.append('100532289')
    c.append('北馆一层自习室')

    a.append('1F-C067')
    b.append('100532290')
    c.append('北馆一层自习室')

    a.append('1F-C068')
    b.append('100532291')
    c.append('北馆一层自习室')

    a.append('1F-C069')
    b.append('100532292')
    c.append('北馆一层自习室')

    a.append('1F-C070')
    b.append('100532293')
    c.append('北馆一层自习室')

    a.append('1F-C071')
    b.append('100532294')
    c.append('北馆一层自习室')

    a.append('1F-C072')
    b.append('100532295')
    c.append('北馆一层自习室')

    a.append('1F-C073')
    b.append('100532296')
    c.append('北馆一层自习室')

    a.append('1F-C074')
    b.append('100532297')
    c.append('北馆一层自习室')

    a.append('1F-C075')
    b.append('100532298')
    c.append('北馆一层自习室')

    a.append('1F-C076')
    b.append('100532299')
    c.append('北馆一层自习室')

    a.append('1F-C077')
    b.append('100532300')
    c.append('北馆一层自习室')

    a.append('1F-C078')
    b.append('100532301')
    c.append('北馆一层自习室')

    a.append('1F-C079')
    b.append('100532302')
    c.append('北馆一层自习室')

    a.append('1F-C080')
    b.append('100532303')
    c.append('北馆一层自习室')

    a.append('1F-C081')
    b.append('100532304')
    c.append('北馆一层自习室')

    a.append('1F-C082')
    b.append('100532305')
    c.append('北馆一层自习室')

    a.append('1F-C083')
    b.append('100532306')
    c.append('北馆一层自习室')

    a.append('1F-C084')
    b.append('100532307')
    c.append('北馆一层自习室')

    a.append('1F-C085')
    b.append('100532308')
    c.append('北馆一层自习室')

    a.append('1F-C086')
    b.append('100532309')
    c.append('北馆一层自习室')

    a.append('1F-C087')
    b.append('100532310')
    c.append('北馆一层自习室')

    a.append('1F-C088')
    b.append('100532311')
    c.append('北馆一层自习室')

    a.append('1F-C089')
    b.append('100532312')
    c.append('北馆一层自习室')

    a.append('1F-C090')
    b.append('100532313')
    c.append('北馆一层自习室')

    a.append('1F-C091')
    b.append('100532314')
    c.append('北馆一层自习室')

    a.append('1F-C092')
    b.append('100532315')
    c.append('北馆一层自习室')

    a.append('1F-C093')
    b.append('100532316')
    c.append('北馆一层自习室')

    a.append('1F-C094')
    b.append('100532317')
    c.append('北馆一层自习室')

    a.append('1F-C095')
    b.append('100532318')
    c.append('北馆一层自习室')

    a.append('1F-C096')
    b.append('100532319')
    c.append('北馆一层自习室')

    a.append('1F-C097')
    b.append('100532320')
    c.append('北馆一层自习室')

    a.append('1F-C098')
    b.append('100532321')
    c.append('北馆一层自习室')

    a.append('1F-C099')
    b.append('100532322')
    c.append('北馆一层自习室')

    a.append('1F-C100')
    b.append('100532323')
    c.append('北馆一层自习室')

    a.append('1F-C101')
    b.append('100532324')
    c.append('北馆一层自习室')

    a.append('1F-C102')
    b.append('100532325')
    c.append('北馆一层自习室')

    a.append('1F-C103')
    b.append('100532326')
    c.append('北馆一层自习室')

    a.append('1F-C104')
    b.append('100532327')
    c.append('北馆一层自习室')

    a.append('1F-C105')
    b.append('100532328')
    c.append('北馆一层自习室')

    a.append('1F-C106')
    b.append('100532329')
    c.append('北馆一层自习室')

    a.append('1F-C107')
    b.append('100532330')
    c.append('北馆一层自习室')

    a.append('1F-C108')
    b.append('100532331')
    c.append('北馆一层自习室')

    a.append('1F-C109')
    b.append('100532332')
    c.append('北馆一层自习室')

    a.append('1F-C110')
    b.append('100532333')
    c.append('北馆一层自习室')

    a.append('1F-C111')
    b.append('100532334')
    c.append('北馆一层自习室')

    a.append('1F-C112')
    b.append('100532335')
    c.append('北馆一层自习室')

    a.append('1F-C113')
    b.append('100532336')
    c.append('北馆一层自习室')

    a.append('1F-C114')
    b.append('100532337')
    c.append('北馆一层自习室')

    a.append('1F-C115')
    b.append('100532338')
    c.append('北馆一层自习室')

    a.append('1F-C116')
    b.append('100532339')
    c.append('北馆一层自习室')

    a.append('1F-C117')
    b.append('100532340')
    c.append('北馆一层自习室')

    a.append('1F-C118')
    b.append('100532341')
    c.append('北馆一层自习室')

    a.append('1F-C119')
    b.append('100532342')
    c.append('北馆一层自习室')

    a.append('1F-C120')
    b.append('100532343')
    c.append('北馆一层自习室')

    a.append('1F-C121')
    b.append('100532344')
    c.append('北馆一层自习室')

    a.append('1F-C122')
    b.append('100532345')
    c.append('北馆一层自习室')

    a.append('1F-C123')
    b.append('100532346')
    c.append('北馆一层自习室')

    a.append('1F-C124')
    b.append('100532347')
    c.append('北馆一层自习室')

    a.append('1F-C125')
    b.append('100532348')
    c.append('北馆一层自习室')

    a.append('1F-C126')
    b.append('100532349')
    c.append('北馆一层自习室')

    a.append('1F-C127')
    b.append('100532350')
    c.append('北馆一层自习室')

    a.append('1F-C128')
    b.append('100532351')
    c.append('北馆一层自习室')

    a.append('1F-C129')
    b.append('100532352')
    c.append('北馆一层自习室')

    a.append('1F-C130')
    b.append('100532353')
    c.append('北馆一层自习室')

    a.append('1F-C131')
    b.append('100532354')
    c.append('北馆一层自习室')

    a.append('1F-C132')
    b.append('100532355')
    c.append('北馆一层自习室')

    a.append('1F-C133')
    b.append('100532356')
    c.append('北馆一层自习室')

    a.append('1F-C134')
    b.append('100532357')
    c.append('北馆一层自习室')

    a.append('1F-C135')
    b.append('100532358')
    c.append('北馆一层自习室')

    a.append('1F-C136')
    b.append('100532359')
    c.append('北馆一层自习室')

    a.append('1F-C137')
    b.append('100532360')
    c.append('北馆一层自习室')

    a.append('1F-C138')
    b.append('100532361')
    c.append('北馆一层自习室')

    a.append('1F-C139')
    b.append('100532362')
    c.append('北馆一层自习室')

    a.append('1F-C140')
    b.append('100532363')
    c.append('北馆一层自习室')

    a.append('1F-C141')
    b.append('100532364')
    c.append('北馆一层自习室')

    a.append('1F-C142')
    b.append('100532365')
    c.append('北馆一层自习室')

    a.append('1F-C143')
    b.append('100532366')
    c.append('北馆一层自习室')

    a.append('1F-C144')
    b.append('100532367')
    c.append('北馆一层自习室')

    a.append('1F-C145')
    b.append('100532368')
    c.append('北馆一层自习室')

    a.append('1F-C146')
    b.append('100532369')
    c.append('北馆一层自习室')

    a.append('1F-C147')
    b.append('100532370')
    c.append('北馆一层自习室')

    a.append('1F-C148')
    b.append('100532371')
    c.append('北馆一层自习室')

    a.append('1F-C149')
    b.append('100532372')
    c.append('北馆一层自习室')

    a.append('1F-C150')
    b.append('100532373')
    c.append('北馆一层自习室')

    a.append('1F-C151')
    b.append('100532374')
    c.append('北馆一层自习室')

    a.append('1F-C152')
    b.append('100532375')
    c.append('北馆一层自习室')

    a.append('1F-C153')
    b.append('100532376')
    c.append('北馆一层自习室')

    a.append('1F-C154')
    b.append('100532377')
    c.append('北馆一层自习室')

    a.append('1F-C155')
    b.append('100532378')
    c.append('北馆一层自习室')

    a.append('1F-C156')
    b.append('100532379')
    c.append('北馆一层自习室')

    a.append('1F-C157')
    b.append('100532380')
    c.append('北馆一层自习室')

    a.append('1F-C158')
    b.append('100532381')
    c.append('北馆一层自习室')

    a.append('1F-C159')
    b.append('100532382')
    c.append('北馆一层自习室')

    a.append('1F-C160')
    b.append('100532383')
    c.append('北馆一层自习室')

    a.append('1F-D001')
    b.append('100532384')
    c.append('北馆一层自习室')

    a.append('1F-D002')
    b.append('100532385')
    c.append('北馆一层自习室')

    a.append('1F-D003')
    b.append('100532386')
    c.append('北馆一层自习室')

    a.append('1F-D004')
    b.append('100532387')
    c.append('北馆一层自习室')

    a.append('1F-D005')
    b.append('100532388')
    c.append('北馆一层自习室')

    a.append('1F-D006')
    b.append('100532389')
    c.append('北馆一层自习室')

    a.append('1F-D007')
    b.append('100532390')
    c.append('北馆一层自习室')

    a.append('1F-D008')
    b.append('100532391')
    c.append('北馆一层自习室')

    a.append('1F-D009')
    b.append('100532392')
    c.append('北馆一层自习室')

    a.append('1F-D010')
    b.append('100532393')
    c.append('北馆一层自习室')

    a.append('1F-D011')
    b.append('100532394')
    c.append('北馆一层自习室')

    a.append('1F-D012')
    b.append('100532395')
    c.append('北馆一层自习室')

    a.append('1F-D013')
    b.append('100532396')
    c.append('北馆一层自习室')

    a.append('1F-D014')
    b.append('100532397')
    c.append('北馆一层自习室')

    a.append('1F-D015')
    b.append('100532398')
    c.append('北馆一层自习室')

    a.append('1F-D016')
    b.append('100532399')
    c.append('北馆一层自习室')

    a.append('1F-D017')
    b.append('100532400')
    c.append('北馆一层自习室')

    a.append('1F-D018')
    b.append('100532401')
    c.append('北馆一层自习室')

    a.append('1F-D019')
    b.append('100532402')
    c.append('北馆一层自习室')

    a.append('1F-D020')
    b.append('100532403')
    c.append('北馆一层自习室')

    a.append('1F-D021')
    b.append('100532404')
    c.append('北馆一层自习室')

    a.append('1F-D022')
    b.append('100532405')
    c.append('北馆一层自习室')

    a.append('1F-D023')
    b.append('100532406')
    c.append('北馆一层自习室')

    a.append('1F-D024')
    b.append('100532407')
    c.append('北馆一层自习室')

    a.append('1F-D025')
    b.append('100532408')
    c.append('北馆一层自习室')

    a.append('1F-D026')
    b.append('100532409')
    c.append('北馆一层自习室')

    a.append('1F-D027')
    b.append('100532410')
    c.append('北馆一层自习室')

    a.append('1F-D028')
    b.append('100532411')
    c.append('北馆一层自习室')

    a.append('1F-D029')
    b.append('100532412')
    c.append('北馆一层自习室')

    a.append('1F-D030')
    b.append('100532413')
    c.append('北馆一层自习室')

    a.append('1F-D031')
    b.append('100532414')
    c.append('北馆一层自习室')

    a.append('1F-D032')
    b.append('100532415')
    c.append('北馆一层自习室')

    a.append('1F-D033')
    b.append('100532416')
    c.append('北馆一层自习室')

    a.append('1F-D034')
    b.append('100532417')
    c.append('北馆一层自习室')

    a.append('1F-D035')
    b.append('100532418')
    c.append('北馆一层自习室')

    a.append('1F-D036')
    b.append('100532419')
    c.append('北馆一层自习室')

    a.append('1F-D037')
    b.append('100532420')
    c.append('北馆一层自习室')

    a.append('1F-D038')
    b.append('100532421')
    c.append('北馆一层自习室')

    a.append('1F-D039')
    b.append('100532422')
    c.append('北馆一层自习室')

    a.append('1F-D040')
    b.append('100532423')
    c.append('北馆一层自习室')

    a.append('1F-D041')
    b.append('100532424')
    c.append('北馆一层自习室')

    a.append('1F-D042')
    b.append('100532425')
    c.append('北馆一层自习室')

    a.append('1F-D043')
    b.append('100532426')
    c.append('北馆一层自习室')

    a.append('1F-D044')
    b.append('100532427')
    c.append('北馆一层自习室')

    a.append('1F-D045')
    b.append('100532428')
    c.append('北馆一层自习室')

    a.append('1F-D046')
    b.append('100532429')
    c.append('北馆一层自习室')

    a.append('1F-D047')
    b.append('100532430')
    c.append('北馆一层自习室')

    a.append('1F-D048')
    b.append('100532431')
    c.append('北馆一层自习室')

    a.append('1F-D049')
    b.append('100532432')
    c.append('北馆一层自习室')

    a.append('1F-D050')
    b.append('100532433')
    c.append('北馆一层自习室')

    a.append('1F-D051')
    b.append('100532434')
    c.append('北馆一层自习室')

    a.append('1F-D052')
    b.append('100532435')
    c.append('北馆一层自习室')

    a.append('1F-D053')
    b.append('100532436')
    c.append('北馆一层自习室')

    a.append('1F-D054')
    b.append('100532437')
    c.append('北馆一层自习室')

    a.append('1F-D055')
    b.append('100532438')
    c.append('北馆一层自习室')

    a.append('1F-D056')
    b.append('100532439')
    c.append('北馆一层自习室')

    a.append('1F-D057')
    b.append('100532440')
    c.append('北馆一层自习室')

    a.append('1F-D058')
    b.append('100532441')
    c.append('北馆一层自习室')

    a.append('1F-D059')
    b.append('100532442')
    c.append('北馆一层自习室')

    a.append('1F-D060')
    b.append('100532443')
    c.append('北馆一层自习室')

    a.append('1F-D061')
    b.append('100532444')
    c.append('北馆一层自习室')

    a.append('1F-D062')
    b.append('100532445')
    c.append('北馆一层自习室')

    a.append('1F-D063')
    b.append('100532446')
    c.append('北馆一层自习室')

    a.append('1F-D064')
    b.append('100532447')
    c.append('北馆一层自习室')

    a.append('1F-D065')
    b.append('100532448')
    c.append('北馆一层自习室')

    a.append('1F-D066')
    b.append('100532449')
    c.append('北馆一层自习室')

    a.append('1F-D067')
    b.append('100532450')
    c.append('北馆一层自习室')

    a.append('1F-D068')
    b.append('100532451')
    c.append('北馆一层自习室')

    a.append('1F-D069')
    b.append('100532452')
    c.append('北馆一层自习室')

    a.append('1F-D070')
    b.append('100532453')
    c.append('北馆一层自习室')

    a.append('1F-D071')
    b.append('100532454')
    c.append('北馆一层自习室')

    a.append('1F-D072')
    b.append('100532455')
    c.append('北馆一层自习室')

    a.append('1F-D073')
    b.append('100532456')
    c.append('北馆一层自习室')

    a.append('1F-D074')
    b.append('100532457')
    c.append('北馆一层自习室')

    a.append('1F-D075')
    b.append('100532458')
    c.append('北馆一层自习室')

    a.append('1F-D076')
    b.append('100532459')
    c.append('北馆一层自习室')

    a.append('1F-D077')
    b.append('100532460')
    c.append('北馆一层自习室')

    a.append('1F-D078')
    b.append('100532461')
    c.append('北馆一层自习室')

    a.append('1F-D079')
    b.append('100532462')
    c.append('北馆一层自习室')

    a.append('1F-D080')
    b.append('100532463')
    c.append('北馆一层自习室')

    a.append('1F-D081')
    b.append('100532464')
    c.append('北馆一层自习室')

    a.append('1F-D082')
    b.append('100532465')
    c.append('北馆一层自习室')

    a.append('1F-D083')
    b.append('100532466')
    c.append('北馆一层自习室')

    a.append('1F-D084')
    b.append('100532467')
    c.append('北馆一层自习室')

    a.append('1F-D085')
    b.append('100532468')
    c.append('北馆一层自习室')

    a.append('1F-D086')
    b.append('100532469')
    c.append('北馆一层自习室')

    a.append('1F-D087')
    b.append('100532470')
    c.append('北馆一层自习室')

    a.append('1F-D088')
    b.append('100532471')
    c.append('北馆一层自习室')

    a.append('1F-D089')
    b.append('100532472')
    c.append('北馆一层自习室')

    a.append('1F-D090')
    b.append('100532473')
    c.append('北馆一层自习室')

    a.append('1F-D091')
    b.append('100532474')
    c.append('北馆一层自习室')

    a.append('1F-D092')
    b.append('100532475')
    c.append('北馆一层自习室')

    a.append('1F-D093')
    b.append('100532476')
    c.append('北馆一层自习室')

    a.append('1F-D094')
    b.append('100532477')
    c.append('北馆一层自习室')

    a.append('1F-D095')
    b.append('100532478')
    c.append('北馆一层自习室')

    a.append('1F-D096')
    b.append('100532479')
    c.append('北馆一层自习室')

    a.append('1F-D097')
    b.append('100532480')
    c.append('北馆一层自习室')

    a.append('1F-D098')
    b.append('100532481')
    c.append('北馆一层自习室')

    a.append('1F-D099')
    b.append('100532482')
    c.append('北馆一层自习室')

    a.append('1F-D100')
    b.append('100532483')
    c.append('北馆一层自习室')

    a.append('1F-D101')
    b.append('100532484')
    c.append('北馆一层自习室')

    a.append('1F-D102')
    b.append('100532485')
    c.append('北馆一层自习室')

    a.append('1F-D103')
    b.append('100532486')
    c.append('北馆一层自习室')

    a.append('1F-D104')
    b.append('100532487')
    c.append('北馆一层自习室')

    a.append('1F-D105')
    b.append('100532488')
    c.append('北馆一层自习室')

    a.append('1F-D106')
    b.append('100532489')
    c.append('北馆一层自习室')

    a.append('1F-D107')
    b.append('100532490')
    c.append('北馆一层自习室')

    a.append('1F-D108')
    b.append('100532491')
    c.append('北馆一层自习室')

    a.append('1F-D109')
    b.append('100532492')
    c.append('北馆一层自习室')

    a.append('1F-D110')
    b.append('100532493')
    c.append('北馆一层自习室')

    a.append('1F-D111')
    b.append('100532494')
    c.append('北馆一层自习室')

    a.append('1F-D112')
    b.append('100532495')
    c.append('北馆一层自习室')

    a.append('1F-D113')
    b.append('100532496')
    c.append('北馆一层自习室')

    a.append('1F-D114')
    b.append('100532497')
    c.append('北馆一层自习室')

    a.append('1F-D115')
    b.append('100532498')
    c.append('北馆一层自习室')

    a.append('1F-D116')
    b.append('100532499')
    c.append('北馆一层自习室')

    a.append('1F-D117')
    b.append('100532500')
    c.append('北馆一层自习室')

    a.append('1F-D118')
    b.append('100532501')
    c.append('北馆一层自习室')

    a.append('1F-D119')
    b.append('100532502')
    c.append('北馆一层自习室')

    a.append('1F-D120')
    b.append('100532503')
    c.append('北馆一层自习室')

    a.append('1F-D121')
    b.append('100532504')
    c.append('北馆一层自习室')

    a.append('1F-D122')
    b.append('100532505')
    c.append('北馆一层自习室')

    a.append('1F-D123')
    b.append('100532506')
    c.append('北馆一层自习室')

    a.append('1F-D124')
    b.append('100532507')
    c.append('北馆一层自习室')

    a.append('1F-D125')
    b.append('100532508')
    c.append('北馆一层自习室')

    a.append('1F-D126')
    b.append('100532509')
    c.append('北馆一层自习室')

    a.append('1F-D127')
    b.append('100532510')
    c.append('北馆一层自习室')

    a.append('1F-D128')
    b.append('100532511')
    c.append('北馆一层自习室')

    a.append('1F-D129')
    b.append('100532512')
    c.append('北馆一层自习室')

    a.append('1F-D130')
    b.append('100532513')
    c.append('北馆一层自习室')

    a.append('1F-D131')
    b.append('100532514')
    c.append('北馆一层自习室')

    a.append('1F-D132')
    b.append('100532515')
    c.append('北馆一层自习室')

    a.append('1F-D133')
    b.append('100532516')
    c.append('北馆一层自习室')

    a.append('1F-D134')
    b.append('100532517')
    c.append('北馆一层自习室')

    a.append('1F-D135')
    b.append('100532518')
    c.append('北馆一层自习室')

    a.append('1F-D136')
    b.append('100532519')
    c.append('北馆一层自习室')

    a.append('1F-D137')
    b.append('100532520')
    c.append('北馆一层自习室')

    a.append('1F-D138')
    b.append('100532521')
    c.append('北馆一层自习室')

    a.append('1F-D139')
    b.append('100532522')
    c.append('北馆一层自习室')

    a.append('1F-D140')
    b.append('100532523')
    c.append('北馆一层自习室')

    a.append('1F-D141')
    b.append('100532524')
    c.append('北馆一层自习室')

    a.append('1F-D142')
    b.append('100532525')
    c.append('北馆一层自习室')

    a.append('1F-D143')
    b.append('100532526')
    c.append('北馆一层自习室')

    a.append('1F-D144')
    b.append('100532527')
    c.append('北馆一层自习室')

    a.append('1F-D145')
    b.append('100532528')
    c.append('北馆一层自习室')

    a.append('1F-D146')
    b.append('100532529')
    c.append('北馆一层自习室')

    a.append('1F-D147')
    b.append('100532530')
    c.append('北馆一层自习室')

    a.append('1F-D148')
    b.append('100532531')
    c.append('北馆一层自习室')

    a.append('1F-D149')
    b.append('100532532')
    c.append('北馆一层自习室')

    a.append('1F-D150')
    b.append('100532533')
    c.append('北馆一层自习室')

    a.append('1F-D151')
    b.append('100532534')
    c.append('北馆一层自习室')

    a.append('1F-D152')
    b.append('100532535')
    c.append('北馆一层自习室')

    a.append('1F-D153')
    b.append('100532536')
    c.append('北馆一层自习室')

    a.append('1F-D154')
    b.append('100532537')
    c.append('北馆一层自习室')

    a.append('1F-D155')
    b.append('100532538')
    c.append('北馆一层自习室')

    a.append('1F-D156')
    b.append('100532539')
    c.append('北馆一层自习室')

    a.append('2FN-A001')
    b.append('104558776')
    c.append('北馆二层阅览区')

    a.append('2FN-A002')
    b.append('104558777')
    c.append('北馆二层阅览区')

    a.append('2FN-A003')
    b.append('104558778')
    c.append('北馆二层阅览区')

    a.append('2FN-A004')
    b.append('104558779')
    c.append('北馆二层阅览区')

    a.append('2FN-A005')
    b.append('104558780')
    c.append('北馆二层阅览区')

    a.append('2FN-A006')
    b.append('104558781')
    c.append('北馆二层阅览区')

    a.append('2FN-A007')
    b.append('104558782')
    c.append('北馆二层阅览区')

    a.append('2FN-A008')
    b.append('104558783')
    c.append('北馆二层阅览区')

    a.append('2FN-A009')
    b.append('104558784')
    c.append('北馆二层阅览区')

    a.append('2FN-A010')
    b.append('104558785')
    c.append('北馆二层阅览区')

    a.append('2FN-A011')
    b.append('104558786')
    c.append('北馆二层阅览区')

    a.append('2FN-A012')
    b.append('104558787')
    c.append('北馆二层阅览区')

    a.append('2FN-A013')
    b.append('104558788')
    c.append('北馆二层阅览区')

    a.append('2FN-A014')
    b.append('104558789')
    c.append('北馆二层阅览区')

    a.append('2FN-A015')
    b.append('104558790')
    c.append('北馆二层阅览区')

    a.append('2FN-A016')
    b.append('104558791')
    c.append('北馆二层阅览区')

    a.append('2FN-A017')
    b.append('104558792')
    c.append('北馆二层阅览区')

    a.append('2FN-A018')
    b.append('104558793')
    c.append('北馆二层阅览区')

    a.append('2FN-A019')
    b.append('104558794')
    c.append('北馆二层阅览区')

    a.append('2FN-A020')
    b.append('104558795')
    c.append('北馆二层阅览区')

    a.append('2FN-A021')
    b.append('104558796')
    c.append('北馆二层阅览区')

    a.append('2FN-A022')
    b.append('104558797')
    c.append('北馆二层阅览区')

    a.append('2FN-A023')
    b.append('104558798')
    c.append('北馆二层阅览区')

    a.append('2FN-A024')
    b.append('104558799')
    c.append('北馆二层阅览区')

    a.append('2FN-A025')
    b.append('104558800')
    c.append('北馆二层阅览区')

    a.append('2FN-A026')
    b.append('104558801')
    c.append('北馆二层阅览区')

    a.append('2FN-A027')
    b.append('104558802')
    c.append('北馆二层阅览区')

    a.append('2FN-A028')
    b.append('104558803')
    c.append('北馆二层阅览区')

    a.append('2FN-A029')
    b.append('104558804')
    c.append('北馆二层阅览区')

    a.append('2FN-A030')
    b.append('104558805')
    c.append('北馆二层阅览区')

    a.append('2FN-A031')
    b.append('104558806')
    c.append('北馆二层阅览区')

    a.append('2FN-A032')
    b.append('104558807')
    c.append('北馆二层阅览区')

    a.append('2FN-A033')
    b.append('104558808')
    c.append('北馆二层阅览区')

    a.append('2FN-A034')
    b.append('104558809')
    c.append('北馆二层阅览区')

    a.append('2FN-A035')
    b.append('104558810')
    c.append('北馆二层阅览区')

    a.append('2FN-A036')
    b.append('104558811')
    c.append('北馆二层阅览区')

    a.append('2FN-A037')
    b.append('104558812')
    c.append('北馆二层阅览区')

    a.append('2FN-A038')
    b.append('104558813')
    c.append('北馆二层阅览区')

    a.append('2FN-A039')
    b.append('104558814')
    c.append('北馆二层阅览区')

    a.append('2FN-A040')
    b.append('104558815')
    c.append('北馆二层阅览区')

    a.append('2FN-A041')
    b.append('104558816')
    c.append('北馆二层阅览区')

    a.append('2FN-A042')
    b.append('104558817')
    c.append('北馆二层阅览区')

    a.append('2FN-A043')
    b.append('104558818')
    c.append('北馆二层阅览区')

    a.append('2FN-A044')
    b.append('104558819')
    c.append('北馆二层阅览区')

    a.append('2FN-A045')
    b.append('104558820')
    c.append('北馆二层阅览区')

    a.append('2FN-A046')
    b.append('104558821')
    c.append('北馆二层阅览区')

    a.append('2FN-A047')
    b.append('104558822')
    c.append('北馆二层阅览区')

    a.append('2FN-A048')
    b.append('104558823')
    c.append('北馆二层阅览区')

    a.append('3FN-B001')
    b.append('103762429')
    c.append('北馆三层自习区')

    a.append('3FN-B002')
    b.append('103762430')
    c.append('北馆三层自习区')

    a.append('3FN-B003')
    b.append('103762431')
    c.append('北馆三层自习区')

    a.append('3FN-B004')
    b.append('103762432')
    c.append('北馆三层自习区')

    a.append('3FN-B005')
    b.append('103762433')
    c.append('北馆三层自习区')

    a.append('3FN-B006')
    b.append('103762434')
    c.append('北馆三层自习区')

    a.append('3FN-B007')
    b.append('103762435')
    c.append('北馆三层自习区')

    a.append('3FN-B008')
    b.append('103762436')
    c.append('北馆三层自习区')

    a.append('3FN-B009')
    b.append('103762437')
    c.append('北馆三层自习区')

    a.append('3FN-B010')
    b.append('103762438')
    c.append('北馆三层自习区')

    a.append('3FN-B011')
    b.append('103762439')
    c.append('北馆三层自习区')

    a.append('3FN-B012')
    b.append('103762440')
    c.append('北馆三层自习区')

    a.append('3FN-B013')
    b.append('103762441')
    c.append('北馆三层自习区')

    a.append('3FN-B014')
    b.append('103762442')
    c.append('北馆三层自习区')

    a.append('3FN-B015')
    b.append('103762443')
    c.append('北馆三层自习区')

    a.append('3FN-B016')
    b.append('103762444')
    c.append('北馆三层自习区')

    a.append('3FN-B017')
    b.append('103762445')
    c.append('北馆三层自习区')

    a.append('3FN-B018')
    b.append('103762446')
    c.append('北馆三层自习区')

    a.append('3FN-B019')
    b.append('103762447')
    c.append('北馆三层自习区')

    a.append('3FN-B020')
    b.append('103762448')
    c.append('北馆三层自习区')

    a.append('3FN-B021')
    b.append('103762449')
    c.append('北馆三层自习区')

    a.append('3FN-B022')
    b.append('103762450')
    c.append('北馆三层自习区')

    a.append('3FN-B023')
    b.append('103762451')
    c.append('北馆三层自习区')

    a.append('3FN-B024')
    b.append('103762452')
    c.append('北馆三层自习区')

    a.append('3FN-B025')
    b.append('103762453')
    c.append('北馆三层自习区')

    a.append('3FN-B026')
    b.append('103762454')
    c.append('北馆三层自习区')

    a.append('3FN-B027')
    b.append('103762455')
    c.append('北馆三层自习区')

    a.append('3FN-B028')
    b.append('103762456')
    c.append('北馆三层自习区')

    a.append('3FN-B029')
    b.append('103762457')
    c.append('北馆三层自习区')

    a.append('3FN-B030')
    b.append('103762458')
    c.append('北馆三层自习区')

    a.append('3FN-B031')
    b.append('103762459')
    c.append('北馆三层自习区')

    a.append('3FN-B032')
    b.append('103762460')
    c.append('北馆三层自习区')

    a.append('3FN-B033')
    b.append('103762461')
    c.append('北馆三层自习区')

    a.append('3FN-B034')
    b.append('103762462')
    c.append('北馆三层自习区')

    a.append('3FN-B035')
    b.append('103762463')
    c.append('北馆三层自习区')

    a.append('3FN-B036')
    b.append('103762464')
    c.append('北馆三层自习区')

    a.append('3FN-B037')
    b.append('103762465')
    c.append('北馆三层自习区')

    a.append('3FN-B038')
    b.append('103762466')
    c.append('北馆三层自习区')

    a.append('3FN-B039')
    b.append('103762467')
    c.append('北馆三层自习区')

    a.append('3FN-B040')
    b.append('103762468')
    c.append('北馆三层自习区')

    a.append('3FN-B041')
    b.append('103762469')
    c.append('北馆三层自习区')

    a.append('3FN-B042')
    b.append('103762470')
    c.append('北馆三层自习区')

    a.append('3FN-B043')
    b.append('103762471')
    c.append('北馆三层自习区')

    a.append('3FN-B044')
    b.append('103762472')
    c.append('北馆三层自习区')

    a.append('3FN-B045')
    b.append('103762473')
    c.append('北馆三层自习区')

    a.append('3FN-B046')
    b.append('103762474')
    c.append('北馆三层自习区')

    a.append('3FN-B047')
    b.append('103762475')
    c.append('北馆三层自习区')

    a.append('3FN-B048')
    b.append('103762476')
    c.append('北馆三层自习区')

    a.append('3FN-B049')
    b.append('103762477')
    c.append('北馆三层自习区')

    a.append('3FN-B050')
    b.append('103762478')
    c.append('北馆三层自习区')

    a.append('3FN-B051')
    b.append('103762479')
    c.append('北馆三层自习区')

    a.append('3FN-B052')
    b.append('103762480')
    c.append('北馆三层自习区')

    a.append('3FN-B053')
    b.append('103762481')
    c.append('北馆三层自习区')

    a.append('3FN-B054')
    b.append('103762482')
    c.append('北馆三层自习区')

    a.append('3FN-B055')
    b.append('103762483')
    c.append('北馆三层自习区')

    a.append('3FN-B056')
    b.append('103762484')
    c.append('北馆三层自习区')

    a.append('3FN-B057')
    b.append('103762485')
    c.append('北馆三层自习区')

    a.append('3FN-B058')
    b.append('103762486')
    c.append('北馆三层自习区')

    a.append('3FN-B059')
    b.append('103762487')
    c.append('北馆三层自习区')

    a.append('3FN-B060')
    b.append('103762488')
    c.append('北馆三层自习区')

    a.append('3FN-B061')
    b.append('103762489')
    c.append('北馆三层自习区')

    a.append('3FN-B062')
    b.append('103762490')
    c.append('北馆三层自习区')

    a.append('3FN-B063')
    b.append('103762491')
    c.append('北馆三层自习区')

    a.append('3FN-B064')
    b.append('103762492')
    c.append('北馆三层自习区')

    a.append('3FN-B065')
    b.append('103762493')
    c.append('北馆三层自习区')

    a.append('3FN-B066')
    b.append('103762494')
    c.append('北馆三层自习区')

    a.append('3FN-B067')
    b.append('103762495')
    c.append('北馆三层自习区')

    a.append('3FN-B068')
    b.append('103762496')
    c.append('北馆三层自习区')

    a.append('3FN-B069')
    b.append('103762497')
    c.append('北馆三层自习区')

    a.append('3FN-B070')
    b.append('103762498')
    c.append('北馆三层自习区')

    a.append('3FN-B071')
    b.append('103762499')
    c.append('北馆三层自习区')

    a.append('3FN-B072')
    b.append('103762500')
    c.append('北馆三层自习区')

    a.append('3FN-B073')
    b.append('103762501')
    c.append('北馆三层自习区')

    a.append('3FN-B074')
    b.append('103762502')
    c.append('北馆三层自习区')

    a.append('3FN-B075')
    b.append('103762503')
    c.append('北馆三层自习区')

    a.append('3FN-B076')
    b.append('103762504')
    c.append('北馆三层自习区')

    a.append('3FN-B077')
    b.append('103762505')
    c.append('北馆三层自习区')

    a.append('3FN-B078')
    b.append('103762506')
    c.append('北馆三层自习区')

    a.append('3FN-B079')
    b.append('103762507')
    c.append('北馆三层自习区')

    a.append('3FN-B080')
    b.append('103762508')
    c.append('北馆三层自习区')

    a.append('3FN-B081')
    b.append('103762509')
    c.append('北馆三层自习区')

    a.append('3FN-B082')
    b.append('103762510')
    c.append('北馆三层自习区')

    a.append('3FN-B083')
    b.append('103762511')
    c.append('北馆三层自习区')

    a.append('3FN-B084')
    b.append('103762512')
    c.append('北馆三层自习区')

    a.append('3FN-B085')
    b.append('103762513')
    c.append('北馆三层自习区')

    a.append('3FN-B086')
    b.append('103762514')
    c.append('北馆三层自习区')

    a.append('3FN-B087')
    b.append('103762515')
    c.append('北馆三层自习区')

    a.append('3FN-B088')
    b.append('103762516')
    c.append('北馆三层自习区')

    a.append('3FN-B089')
    b.append('103762517')
    c.append('北馆三层自习区')

    a.append('3FN-B090')
    b.append('103762518')
    c.append('北馆三层自习区')

    a.append('3FN-B091')
    b.append('103762519')
    c.append('北馆三层自习区')

    a.append('3FN-B092')
    b.append('103762520')
    c.append('北馆三层自习区')

    a.append('3FN-C001')
    b.append('103762521')
    c.append('北馆三层自习区')

    a.append('3FN-C002')
    b.append('103762522')
    c.append('北馆三层自习区')

    a.append('3FN-C003')
    b.append('103762523')
    c.append('北馆三层自习区')

    a.append('3FN-C004')
    b.append('103762524')
    c.append('北馆三层自习区')

    a.append('3FN-C005')
    b.append('103762525')
    c.append('北馆三层自习区')

    a.append('3FN-C006')
    b.append('103762526')
    c.append('北馆三层自习区')

    a.append('3FN-C007')
    b.append('103762527')
    c.append('北馆三层自习区')

    a.append('3FN-C008')
    b.append('103762528')
    c.append('北馆三层自习区')

    a.append('3FN-C009')
    b.append('103762529')
    c.append('北馆三层自习区')

    a.append('3FN-C010')
    b.append('103762530')
    c.append('北馆三层自习区')

    a.append('3FN-C011')
    b.append('103762531')
    c.append('北馆三层自习区')

    a.append('3FN-C012')
    b.append('103762532')
    c.append('北馆三层自习区')

    a.append('3FN-C013')
    b.append('103762533')
    c.append('北馆三层自习区')

    a.append('3FN-C014')
    b.append('103762534')
    c.append('北馆三层自习区')

    a.append('3FN-C015')
    b.append('103762535')
    c.append('北馆三层自习区')

    a.append('3FN-C016')
    b.append('103762536')
    c.append('北馆三层自习区')

    a.append('3FN-C017')
    b.append('103762537')
    c.append('北馆三层自习区')

    a.append('3FN-C018')
    b.append('103762538')
    c.append('北馆三层自习区')

    a.append('3FN-C019')
    b.append('103762539')
    c.append('北馆三层自习区')

    a.append('3FN-C020')
    b.append('103762540')
    c.append('北馆三层自习区')

    a.append('3FN-C021')
    b.append('103762541')
    c.append('北馆三层自习区')

    a.append('3FN-C022')
    b.append('103762542')
    c.append('北馆三层自习区')

    a.append('3FN-C023')
    b.append('103762543')
    c.append('北馆三层自习区')

    a.append('3FN-C024')
    b.append('103762544')
    c.append('北馆三层自习区')

    a.append('3FN-A001')
    b.append('103762321')
    c.append('北馆三层自习区')

    a.append('3FN-A002')
    b.append('103762322')
    c.append('北馆三层自习区')

    a.append('3FN-A003')
    b.append('103762323')
    c.append('北馆三层自习区')

    a.append('3FN-A004')
    b.append('103762324')
    c.append('北馆三层自习区')

    a.append('3FN-A005')
    b.append('103762325')
    c.append('北馆三层自习区')

    a.append('3FN-A006')
    b.append('103762326')
    c.append('北馆三层自习区')

    a.append('3FN-A007')
    b.append('103762327')
    c.append('北馆三层自习区')

    a.append('3FN-A008')
    b.append('103762328')
    c.append('北馆三层自习区')

    a.append('3FN-A009')
    b.append('103762329')
    c.append('北馆三层自习区')

    a.append('3FN-A010')
    b.append('103762330')
    c.append('北馆三层自习区')

    a.append('3FN-A011')
    b.append('103762331')
    c.append('北馆三层自习区')

    a.append('3FN-A012')
    b.append('103762332')
    c.append('北馆三层自习区')

    a.append('3FN-A013')
    b.append('103762333')
    c.append('北馆三层自习区')

    a.append('3FN-A014')
    b.append('103762334')
    c.append('北馆三层自习区')

    a.append('3FN-A015')
    b.append('103762335')
    c.append('北馆三层自习区')

    a.append('3FN-A016')
    b.append('103762336')
    c.append('北馆三层自习区')

    a.append('3FN-A017')
    b.append('103762337')
    c.append('北馆三层自习区')

    a.append('3FN-A018')
    b.append('103762338')
    c.append('北馆三层自习区')

    a.append('3FN-A019')
    b.append('103762339')
    c.append('北馆三层自习区')

    a.append('3FN-A020')
    b.append('103762340')
    c.append('北馆三层自习区')

    a.append('3FN-A021')
    b.append('103762341')
    c.append('北馆三层自习区')

    a.append('3FN-A022')
    b.append('103762342')
    c.append('北馆三层自习区')

    a.append('3FN-A023')
    b.append('103762343')
    c.append('北馆三层自习区')

    a.append('3FN-A024')
    b.append('103762344')
    c.append('北馆三层自习区')

    a.append('3FN-A025')
    b.append('103762345')
    c.append('北馆三层自习区')

    a.append('3FN-A026')
    b.append('103762346')
    c.append('北馆三层自习区')

    a.append('3FN-A027')
    b.append('103762347')
    c.append('北馆三层自习区')

    a.append('3FN-A028')
    b.append('103762348')
    c.append('北馆三层自习区')

    a.append('3FN-A029')
    b.append('103762349')
    c.append('北馆三层自习区')

    a.append('3FN-A030')
    b.append('103762350')
    c.append('北馆三层自习区')

    a.append('3FN-A031')
    b.append('103762351')
    c.append('北馆三层自习区')

    a.append('3FN-A032')
    b.append('103762352')
    c.append('北馆三层自习区')

    a.append('3FN-A033')
    b.append('103762353')
    c.append('北馆三层自习区')

    a.append('3FN-A034')
    b.append('103762354')
    c.append('北馆三层自习区')

    a.append('3FN-A035')
    b.append('103762355')
    c.append('北馆三层自习区')

    a.append('3FN-A036')
    b.append('103762356')
    c.append('北馆三层自习区')

    a.append('3FN-A037')
    b.append('103762357')
    c.append('北馆三层自习区')

    a.append('3FN-A038')
    b.append('103762358')
    c.append('北馆三层自习区')

    a.append('3FN-A039')
    b.append('103762359')
    c.append('北馆三层自习区')

    a.append('3FN-A040')
    b.append('103762360')
    c.append('北馆三层自习区')

    a.append('3FN-A041')
    b.append('103762361')
    c.append('北馆三层自习区')

    a.append('3FN-A042')
    b.append('103762362')
    c.append('北馆三层自习区')

    a.append('3FN-A043')
    b.append('103762363')
    c.append('北馆三层自习区')

    a.append('3FN-A044')
    b.append('103762364')
    c.append('北馆三层自习区')

    a.append('3FN-A045')
    b.append('103762365')
    c.append('北馆三层自习区')

    a.append('3FN-A046')
    b.append('103762366')
    c.append('北馆三层自习区')

    a.append('3FN-A047')
    b.append('103762367')
    c.append('北馆三层自习区')

    a.append('3FN-A048')
    b.append('103762368')
    c.append('北馆三层自习区')

    a.append('3FN-A049')
    b.append('103762369')
    c.append('北馆三层自习区')

    a.append('3FN-A050')
    b.append('103762370')
    c.append('北馆三层自习区')

    a.append('3FN-A051')
    b.append('103762371')
    c.append('北馆三层自习区')

    a.append('3FN-A052')
    b.append('103762372')
    c.append('北馆三层自习区')

    a.append('3FN-A053')
    b.append('103762373')
    c.append('北馆三层自习区')

    a.append('3FN-A054')
    b.append('103762374')
    c.append('北馆三层自习区')

    a.append('3FN-A055')
    b.append('103762375')
    c.append('北馆三层自习区')

    a.append('3FN-A056')
    b.append('103762376')
    c.append('北馆三层自习区')

    a.append('3FN-A057')
    b.append('103762377')
    c.append('北馆三层自习区')

    a.append('3FN-A058')
    b.append('103762378')
    c.append('北馆三层自习区')

    a.append('3FN-A059')
    b.append('103762379')
    c.append('北馆三层自习区')

    a.append('3FN-A060')
    b.append('103762380')
    c.append('北馆三层自习区')

    a.append('3FN-A061')
    b.append('103762381')
    c.append('北馆三层自习区')

    a.append('3FN-A062')
    b.append('103762382')
    c.append('北馆三层自习区')

    a.append('3FN-A063')
    b.append('103762383')
    c.append('北馆三层自习区')

    a.append('3FN-A064')
    b.append('103762384')
    c.append('北馆三层自习区')

    a.append('3FN-A065')
    b.append('103762385')
    c.append('北馆三层自习区')

    a.append('3FN-A066')
    b.append('103762386')
    c.append('北馆三层自习区')

    a.append('3FN-A067')
    b.append('103762387')
    c.append('北馆三层自习区')

    a.append('3FN-A068')
    b.append('103762388')
    c.append('北馆三层自习区')

    a.append('3FN-A069')
    b.append('103762389')
    c.append('北馆三层自习区')

    a.append('3FN-A070')
    b.append('103762390')
    c.append('北馆三层自习区')

    a.append('3FN-A071')
    b.append('103762391')
    c.append('北馆三层自习区')

    a.append('3FN-A072')
    b.append('103762392')
    c.append('北馆三层自习区')

    a.append('3FN-A073')
    b.append('103762393')
    c.append('北馆三层自习区')

    a.append('3FN-A074')
    b.append('103762394')
    c.append('北馆三层自习区')

    a.append('3FN-A075')
    b.append('103762395')
    c.append('北馆三层自习区')

    a.append('3FN-A076')
    b.append('103762396')
    c.append('北馆三层自习区')

    a.append('3FN-A077')
    b.append('103762397')
    c.append('北馆三层自习区')

    a.append('3FN-A078')
    b.append('103762398')
    c.append('北馆三层自习区')

    a.append('3FN-A079')
    b.append('103762399')
    c.append('北馆三层自习区')

    a.append('3FN-A080')
    b.append('103762400')
    c.append('北馆三层自习区')

    a.append('3FN-A081')
    b.append('103762401')
    c.append('北馆三层自习区')

    a.append('3FN-A082')
    b.append('103762402')
    c.append('北馆三层自习区')

    a.append('3FN-A083')
    b.append('103762403')
    c.append('北馆三层自习区')

    a.append('3FN-A084')
    b.append('103762404')
    c.append('北馆三层自习区')

    a.append('3FN-A085')
    b.append('103762405')
    c.append('北馆三层自习区')

    a.append('3FN-A086')
    b.append('103762406')
    c.append('北馆三层自习区')

    a.append('3FN-A087')
    b.append('103762407')
    c.append('北馆三层自习区')

    a.append('3FN-A088')
    b.append('103762408')
    c.append('北馆三层自习区')

    a.append('3FN-A089')
    b.append('103762409')
    c.append('北馆三层自习区')

    a.append('3FN-A090')
    b.append('103762410')
    c.append('北馆三层自习区')

    a.append('3FN-A091')
    b.append('103762411')
    c.append('北馆三层自习区')

    a.append('3FN-A092')
    b.append('103762412')
    c.append('北馆三层自习区')

    a.append('3FN-A093')
    b.append('103762413')
    c.append('北馆三层自习区')

    a.append('3FN-A094')
    b.append('103762414')
    c.append('北馆三层自习区')

    a.append('3FN-A095')
    b.append('103762415')
    c.append('北馆三层自习区')

    a.append('3FN-A096')
    b.append('103762416')
    c.append('北馆三层自习区')

    a.append('3FN-A097')
    b.append('103762417')
    c.append('北馆三层自习区')

    a.append('3FN-A098')
    b.append('103762418')
    c.append('北馆三层自习区')

    a.append('3FN-A099')
    b.append('103762419')
    c.append('北馆三层自习区')

    a.append('3FN-A100')
    b.append('103762420')
    c.append('北馆三层自习区')

    a.append('3FN-A101')
    b.append('103762421')
    c.append('北馆三层自习区')

    a.append('3FN-A102')
    b.append('103762422')
    c.append('北馆三层自习区')

    a.append('3FN-A103')
    b.append('103762423')
    c.append('北馆三层自习区')

    a.append('3FN-A104')
    b.append('103762424')
    c.append('北馆三层自习区')

    a.append('4FN-B001')
    b.append('103762653')
    c.append('北馆四层自习区')

    a.append('4FN-B002')
    b.append('103762654')
    c.append('北馆四层自习区')

    a.append('4FN-B003')
    b.append('103762655')
    c.append('北馆四层自习区')

    a.append('4FN-B004')
    b.append('103762656')
    c.append('北馆四层自习区')

    a.append('4FN-B005')
    b.append('103762657')
    c.append('北馆四层自习区')

    a.append('4FN-B006')
    b.append('103762658')
    c.append('北馆四层自习区')

    a.append('4FN-B007')
    b.append('103762659')
    c.append('北馆四层自习区')

    a.append('4FN-B008')
    b.append('103762660')
    c.append('北馆四层自习区')

    a.append('4FN-B009')
    b.append('103762661')
    c.append('北馆四层自习区')

    a.append('4FN-B010')
    b.append('103762662')
    c.append('北馆四层自习区')

    a.append('4FN-B011')
    b.append('103762663')
    c.append('北馆四层自习区')

    a.append('4FN-B012')
    b.append('103762664')
    c.append('北馆四层自习区')

    a.append('4FN-B013')
    b.append('103762665')
    c.append('北馆四层自习区')

    a.append('4FN-B014')
    b.append('103762666')
    c.append('北馆四层自习区')

    a.append('4FN-B015')
    b.append('103762667')
    c.append('北馆四层自习区')

    a.append('4FN-B016')
    b.append('103762668')
    c.append('北馆四层自习区')

    a.append('4FN-B017')
    b.append('103762669')
    c.append('北馆四层自习区')

    a.append('4FN-B018')
    b.append('103762670')
    c.append('北馆四层自习区')

    a.append('4FN-B019')
    b.append('103762671')
    c.append('北馆四层自习区')

    a.append('4FN-B020')
    b.append('103762672')
    c.append('北馆四层自习区')

    a.append('4FN-B021')
    b.append('103762673')
    c.append('北馆四层自习区')

    a.append('4FN-B022')
    b.append('103762674')
    c.append('北馆四层自习区')

    a.append('4FN-B023')
    b.append('103762675')
    c.append('北馆四层自习区')

    a.append('4FN-B024')
    b.append('103762676')
    c.append('北馆四层自习区')

    a.append('4FN-B025')
    b.append('103762677')
    c.append('北馆四层自习区')

    a.append('4FN-B026')
    b.append('103762678')
    c.append('北馆四层自习区')

    a.append('4FN-B027')
    b.append('103762679')
    c.append('北馆四层自习区')

    a.append('4FN-B028')
    b.append('103762680')
    c.append('北馆四层自习区')

    a.append('4FN-B029')
    b.append('103762681')
    c.append('北馆四层自习区')

    a.append('4FN-B030')
    b.append('103762682')
    c.append('北馆四层自习区')

    a.append('4FN-B031')
    b.append('103762683')
    c.append('北馆四层自习区')

    a.append('4FN-B032')
    b.append('103762684')
    c.append('北馆四层自习区')

    a.append('4FN-B033')
    b.append('103762685')
    c.append('北馆四层自习区')

    a.append('4FN-B034')
    b.append('103762686')
    c.append('北馆四层自习区')

    a.append('4FN-B035')
    b.append('103762687')
    c.append('北馆四层自习区')

    a.append('4FN-B036')
    b.append('103762688')
    c.append('北馆四层自习区')

    a.append('4FN-B037')
    b.append('103762689')
    c.append('北馆四层自习区')

    a.append('4FN-B038')
    b.append('103762690')
    c.append('北馆四层自习区')

    a.append('4FN-B039')
    b.append('103762691')
    c.append('北馆四层自习区')

    a.append('4FN-B040')
    b.append('103762692')
    c.append('北馆四层自习区')

    a.append('4FN-B041')
    b.append('103762693')
    c.append('北馆四层自习区')

    a.append('4FN-B042')
    b.append('103762694')
    c.append('北馆四层自习区')

    a.append('4FN-B043')
    b.append('103762695')
    c.append('北馆四层自习区')

    a.append('4FN-B044')
    b.append('103762696')
    c.append('北馆四层自习区')

    a.append('4FN-B045')
    b.append('103762697')
    c.append('北馆四层自习区')

    a.append('4FN-B046')
    b.append('103762698')
    c.append('北馆四层自习区')

    a.append('4FN-B047')
    b.append('103762699')
    c.append('北馆四层自习区')

    a.append('4FN-B048')
    b.append('103762700')
    c.append('北馆四层自习区')

    a.append('4FN-B049')
    b.append('103762701')
    c.append('北馆四层自习区')

    a.append('4FN-B050')
    b.append('103762702')
    c.append('北馆四层自习区')

    a.append('4FN-B051')
    b.append('103762703')
    c.append('北馆四层自习区')

    a.append('4FN-B052')
    b.append('103762704')
    c.append('北馆四层自习区')

    a.append('4FN-B053')
    b.append('103762705')
    c.append('北馆四层自习区')

    a.append('4FN-B054')
    b.append('103762706')
    c.append('北馆四层自习区')

    a.append('4FN-B055')
    b.append('103762707')
    c.append('北馆四层自习区')

    a.append('4FN-B056')
    b.append('103762708')
    c.append('北馆四层自习区')

    a.append('4FN-B057')
    b.append('103762709')
    c.append('北馆四层自习区')

    a.append('4FN-B058')
    b.append('103762710')
    c.append('北馆四层自习区')

    a.append('4FN-B059')
    b.append('103762711')
    c.append('北馆四层自习区')

    a.append('4FN-B060')
    b.append('103762712')
    c.append('北馆四层自习区')

    a.append('4FN-B061')
    b.append('103762713')
    c.append('北馆四层自习区')

    a.append('4FN-B062')
    b.append('103762714')
    c.append('北馆四层自习区')

    a.append('4FN-B063')
    b.append('103762715')
    c.append('北馆四层自习区')

    a.append('4FN-B064')
    b.append('103762716')
    c.append('北馆四层自习区')

    a.append('4FN-B065')
    b.append('103762717')
    c.append('北馆四层自习区')

    a.append('4FN-B066')
    b.append('103762718')
    c.append('北馆四层自习区')

    a.append('4FN-B067')
    b.append('103762719')
    c.append('北馆四层自习区')

    a.append('4FN-B068')
    b.append('103762720')
    c.append('北馆四层自习区')

    a.append('4FN-B069')
    b.append('103762721')
    c.append('北馆四层自习区')

    a.append('4FN-B070')
    b.append('103762722')
    c.append('北馆四层自习区')

    a.append('4FN-B071')
    b.append('103762723')
    c.append('北馆四层自习区')

    a.append('4FN-B072')
    b.append('103762724')
    c.append('北馆四层自习区')

    a.append('4FN-B073')
    b.append('103762725')
    c.append('北馆四层自习区')

    a.append('4FN-B074')
    b.append('103762726')
    c.append('北馆四层自习区')

    a.append('4FN-B075')
    b.append('103762727')
    c.append('北馆四层自习区')

    a.append('4FN-B076')
    b.append('103762728')
    c.append('北馆四层自习区')

    a.append('4FN-B077')
    b.append('103762729')
    c.append('北馆四层自习区')

    a.append('4FN-B078')
    b.append('103762730')
    c.append('北馆四层自习区')

    a.append('4FN-B079')
    b.append('103762731')
    c.append('北馆四层自习区')

    a.append('4FN-B080')
    b.append('103762732')
    c.append('北馆四层自习区')

    a.append('4FN-B081')
    b.append('103762733')
    c.append('北馆四层自习区')

    a.append('4FN-B082')
    b.append('103762734')
    c.append('北馆四层自习区')

    a.append('4FN-B083')
    b.append('103762735')
    c.append('北馆四层自习区')

    a.append('4FN-B084')
    b.append('103762736')
    c.append('北馆四层自习区')

    a.append('4FN-B085')
    b.append('103762737')
    c.append('北馆四层自习区')

    a.append('4FN-B086')
    b.append('103762738')
    c.append('北馆四层自习区')

    a.append('4FN-B087')
    b.append('103762739')
    c.append('北馆四层自习区')

    a.append('4FN-B088')
    b.append('103762740')
    c.append('北馆四层自习区')

    a.append('4FN-B089')
    b.append('103762741')
    c.append('北馆四层自习区')

    a.append('4FN-B090')
    b.append('103762742')
    c.append('北馆四层自习区')

    a.append('4FN-B091')
    b.append('103762743')
    c.append('北馆四层自习区')

    a.append('4FN-B092')
    b.append('103762744')
    c.append('北馆四层自习区')

    a.append('4FN-C001')
    b.append('103762745')
    c.append('北馆四层自习区')

    a.append('4FN-C002')
    b.append('103762746')
    c.append('北馆四层自习区')

    a.append('4FN-C003')
    b.append('103762747')
    c.append('北馆四层自习区')

    a.append('4FN-C004')
    b.append('103762748')
    c.append('北馆四层自习区')

    a.append('4FN-C005')
    b.append('103762749')
    c.append('北馆四层自习区')

    a.append('4FN-C006')
    b.append('103762750')
    c.append('北馆四层自习区')

    a.append('4FN-C007')
    b.append('103762751')
    c.append('北馆四层自习区')

    a.append('4FN-C008')
    b.append('103762752')
    c.append('北馆四层自习区')

    a.append('4FN-C009')
    b.append('103762753')
    c.append('北馆四层自习区')

    a.append('4FN-C010')
    b.append('103762754')
    c.append('北馆四层自习区')

    a.append('4FN-C011')
    b.append('103762755')
    c.append('北馆四层自习区')

    a.append('4FN-C012')
    b.append('103762756')
    c.append('北馆四层自习区')

    a.append('4FN-C013')
    b.append('103762757')
    c.append('北馆四层自习区')

    a.append('4FN-C014')
    b.append('103762758')
    c.append('北馆四层自习区')

    a.append('4FN-C015')
    b.append('103762759')
    c.append('北馆四层自习区')

    a.append('4FN-C016')
    b.append('103762760')
    c.append('北馆四层自习区')

    a.append('4FN-C017')
    b.append('103762761')
    c.append('北馆四层自习区')

    a.append('4FN-C018')
    b.append('103762762')
    c.append('北馆四层自习区')

    a.append('4FN-C019')
    b.append('103762763')
    c.append('北馆四层自习区')

    a.append('4FN-C020')
    b.append('103762764')
    c.append('北馆四层自习区')

    a.append('4FN-C021')
    b.append('103762765')
    c.append('北馆四层自习区')

    a.append('4FN-C022')
    b.append('103762766')
    c.append('北馆四层自习区')

    a.append('4FN-C023')
    b.append('103762767')
    c.append('北馆四层自习区')

    a.append('4FN-C024')
    b.append('103762768')
    c.append('北馆四层自习区')

    a.append('4FN-C025')
    b.append('103762769')
    c.append('北馆四层自习区')

    a.append('4FN-C026')
    b.append('103762770')
    c.append('北馆四层自习区')

    a.append('4FN-C027')
    b.append('103762771')
    c.append('北馆四层自习区')

    a.append('4FN-C028')
    b.append('103762772')
    c.append('北馆四层自习区')

    a.append('4FN-C029')
    b.append('103762773')
    c.append('北馆四层自习区')

    a.append('4FN-C030')
    b.append('103762774')
    c.append('北馆四层自习区')

    a.append('4FN-C031')
    b.append('103762775')
    c.append('北馆四层自习区')

    a.append('4FN-C032')
    b.append('103762776')
    c.append('北馆四层自习区')

    a.append('4FN-C033')
    b.append('103762777')
    c.append('北馆四层自习区')

    a.append('4FN-C034')
    b.append('103762778')
    c.append('北馆四层自习区')

    a.append('4FN-C035')
    b.append('103762779')
    c.append('北馆四层自习区')

    a.append('4FN-C036')
    b.append('103762780')
    c.append('北馆四层自习区')

    a.append('4FN-C037')
    b.append('103762781')
    c.append('北馆四层自习区')

    a.append('4FN-C038')
    b.append('103762782')
    c.append('北馆四层自习区')

    a.append('4FN-C039')
    b.append('103762783')
    c.append('北馆四层自习区')

    a.append('4FN-C040')
    b.append('103762784')
    c.append('北馆四层自习区')

    a.append('4FN-A001')
    b.append('103762545')
    c.append('北馆四层自习区')

    a.append('4FN-A002')
    b.append('103762546')
    c.append('北馆四层自习区')

    a.append('4FN-A003')
    b.append('103762547')
    c.append('北馆四层自习区')

    a.append('4FN-A004')
    b.append('103762548')
    c.append('北馆四层自习区')

    a.append('4FN-A005')
    b.append('103762549')
    c.append('北馆四层自习区')

    a.append('4FN-A006')
    b.append('103762550')
    c.append('北馆四层自习区')

    a.append('4FN-A007')
    b.append('103762551')
    c.append('北馆四层自习区')

    a.append('4FN-A008')
    b.append('103762552')
    c.append('北馆四层自习区')

    a.append('4FN-A009')
    b.append('103762553')
    c.append('北馆四层自习区')

    a.append('4FN-A010')
    b.append('103762554')
    c.append('北馆四层自习区')

    a.append('4FN-A011')
    b.append('103762555')
    c.append('北馆四层自习区')

    a.append('4FN-A012')
    b.append('103762556')
    c.append('北馆四层自习区')

    a.append('4FN-A013')
    b.append('103762557')
    c.append('北馆四层自习区')

    a.append('4FN-A014')
    b.append('103762558')
    c.append('北馆四层自习区')

    a.append('4FN-A015')
    b.append('103762559')
    c.append('北馆四层自习区')

    a.append('4FN-A016')
    b.append('103762560')
    c.append('北馆四层自习区')

    a.append('4FN-A017')
    b.append('103762561')
    c.append('北馆四层自习区')

    a.append('4FN-A018')
    b.append('103762562')
    c.append('北馆四层自习区')

    a.append('4FN-A019')
    b.append('103762563')
    c.append('北馆四层自习区')

    a.append('4FN-A020')
    b.append('103762564')
    c.append('北馆四层自习区')

    a.append('4FN-A021')
    b.append('103762565')
    c.append('北馆四层自习区')

    a.append('4FN-A022')
    b.append('103762566')
    c.append('北馆四层自习区')

    a.append('4FN-A023')
    b.append('103762567')
    c.append('北馆四层自习区')

    a.append('4FN-A024')
    b.append('103762568')
    c.append('北馆四层自习区')

    a.append('4FN-A025')
    b.append('103762569')
    c.append('北馆四层自习区')

    a.append('4FN-A026')
    b.append('103762570')
    c.append('北馆四层自习区')

    a.append('4FN-A027')
    b.append('103762571')
    c.append('北馆四层自习区')

    a.append('4FN-A028')
    b.append('103762572')
    c.append('北馆四层自习区')

    a.append('4FN-A029')
    b.append('103762573')
    c.append('北馆四层自习区')

    a.append('4FN-A030')
    b.append('103762574')
    c.append('北馆四层自习区')

    a.append('4FN-A031')
    b.append('103762575')
    c.append('北馆四层自习区')

    a.append('4FN-A032')
    b.append('103762576')
    c.append('北馆四层自习区')

    a.append('4FN-A033')
    b.append('103762577')
    c.append('北馆四层自习区')

    a.append('4FN-A034')
    b.append('103762578')
    c.append('北馆四层自习区')

    a.append('4FN-A035')
    b.append('103762579')
    c.append('北馆四层自习区')

    a.append('4FN-A036')
    b.append('103762580')
    c.append('北馆四层自习区')

    a.append('4FN-A037')
    b.append('103762581')
    c.append('北馆四层自习区')

    a.append('4FN-A038')
    b.append('103762582')
    c.append('北馆四层自习区')

    a.append('4FN-A039')
    b.append('103762583')
    c.append('北馆四层自习区')

    a.append('4FN-A040')
    b.append('103762584')
    c.append('北馆四层自习区')

    a.append('4FN-A041')
    b.append('103762585')
    c.append('北馆四层自习区')

    a.append('4FN-A042')
    b.append('103762586')
    c.append('北馆四层自习区')

    a.append('4FN-A043')
    b.append('103762587')
    c.append('北馆四层自习区')

    a.append('4FN-A044')
    b.append('103762588')
    c.append('北馆四层自习区')

    a.append('4FN-A045')
    b.append('103762589')
    c.append('北馆四层自习区')

    a.append('4FN-A046')
    b.append('103762590')
    c.append('北馆四层自习区')

    a.append('4FN-A047')
    b.append('103762591')
    c.append('北馆四层自习区')

    a.append('4FN-A048')
    b.append('103762592')
    c.append('北馆四层自习区')

    a.append('4FN-A049')
    b.append('103762593')
    c.append('北馆四层自习区')

    a.append('4FN-A050')
    b.append('103762594')
    c.append('北馆四层自习区')

    a.append('4FN-A051')
    b.append('103762595')
    c.append('北馆四层自习区')

    a.append('4FN-A052')
    b.append('103762596')
    c.append('北馆四层自习区')

    a.append('4FN-A053')
    b.append('103762597')
    c.append('北馆四层自习区')

    a.append('4FN-A054')
    b.append('103762598')
    c.append('北馆四层自习区')

    a.append('4FN-A055')
    b.append('103762599')
    c.append('北馆四层自习区')

    a.append('4FN-A056')
    b.append('103762600')
    c.append('北馆四层自习区')

    a.append('4FN-A057')
    b.append('103762601')
    c.append('北馆四层自习区')

    a.append('4FN-A058')
    b.append('103762602')
    c.append('北馆四层自习区')

    a.append('4FN-A059')
    b.append('103762603')
    c.append('北馆四层自习区')

    a.append('4FN-A060')
    b.append('103762604')
    c.append('北馆四层自习区')

    a.append('4FN-A061')
    b.append('103762605')
    c.append('北馆四层自习区')

    a.append('4FN-A062')
    b.append('103762606')
    c.append('北馆四层自习区')

    a.append('4FN-A063')
    b.append('103762607')
    c.append('北馆四层自习区')

    a.append('4FN-A064')
    b.append('103762608')
    c.append('北馆四层自习区')

    a.append('4FN-A065')
    b.append('103762609')
    c.append('北馆四层自习区')

    a.append('4FN-A066')
    b.append('103762610')
    c.append('北馆四层自习区')

    a.append('4FN-A067')
    b.append('103762611')
    c.append('北馆四层自习区')

    a.append('4FN-A068')
    b.append('103762612')
    c.append('北馆四层自习区')

    a.append('4FN-A069')
    b.append('103762613')
    c.append('北馆四层自习区')

    a.append('4FN-A070')
    b.append('103762614')
    c.append('北馆四层自习区')

    a.append('4FN-A071')
    b.append('103762615')
    c.append('北馆四层自习区')

    a.append('4FN-A072')
    b.append('103762616')
    c.append('北馆四层自习区')

    a.append('4FN-A073')
    b.append('103762617')
    c.append('北馆四层自习区')

    a.append('4FN-A074')
    b.append('103762618')
    c.append('北馆四层自习区')

    a.append('4FN-A075')
    b.append('103762619')
    c.append('北馆四层自习区')

    a.append('4FN-A076')
    b.append('103762620')
    c.append('北馆四层自习区')

    a.append('4FN-A077')
    b.append('103762621')
    c.append('北馆四层自习区')

    a.append('4FN-A078')
    b.append('103762622')
    c.append('北馆四层自习区')

    a.append('4FN-A079')
    b.append('103762623')
    c.append('北馆四层自习区')

    a.append('4FN-A080')
    b.append('103762624')
    c.append('北馆四层自习区')

    a.append('4FN-A081')
    b.append('103762625')
    c.append('北馆四层自习区')

    a.append('4FN-A082')
    b.append('103762626')
    c.append('北馆四层自习区')

    a.append('4FN-A083')
    b.append('103762627')
    c.append('北馆四层自习区')

    a.append('4FN-A084')
    b.append('103762628')
    c.append('北馆四层自习区')

    a.append('4FN-A085')
    b.append('103762629')
    c.append('北馆四层自习区')

    a.append('4FN-A086')
    b.append('103762630')
    c.append('北馆四层自习区')

    a.append('4FN-A087')
    b.append('103762631')
    c.append('北馆四层自习区')

    a.append('4FN-A088')
    b.append('103762632')
    c.append('北馆四层自习区')

    a.append('4FN-A089')
    b.append('103762633')
    c.append('北馆四层自习区')

    a.append('4FN-A090')
    b.append('103762634')
    c.append('北馆四层自习区')

    a.append('4FN-A091')
    b.append('103762635')
    c.append('北馆四层自习区')

    a.append('4FN-A092')
    b.append('103762636')
    c.append('北馆四层自习区')

    a.append('4FN-A093')
    b.append('103762637')
    c.append('北馆四层自习区')

    a.append('4FN-A094')
    b.append('103762638')
    c.append('北馆四层自习区')

    a.append('4FN-A095')
    b.append('103762639')
    c.append('北馆四层自习区')

    a.append('4FN-A096')
    b.append('103762640')
    c.append('北馆四层自习区')

    a.append('4FN-A097')
    b.append('103762641')
    c.append('北馆四层自习区')

    a.append('4FN-A098')
    b.append('103762642')
    c.append('北馆四层自习区')

    a.append('4FN-A099')
    b.append('103762643')
    c.append('北馆四层自习区')

    a.append('4FN-A100')
    b.append('103762644')
    c.append('北馆四层自习区')

    a.append('4FN-A101')
    b.append('103762645')
    c.append('北馆四层自习区')

    a.append('4FN-A102')
    b.append('103762646')
    c.append('北馆四层自习区')

    a.append('4FN-A103')
    b.append('103762647')
    c.append('北馆四层自习区')

    a.append('4FN-A104')
    b.append('103762648')
    c.append('北馆四层自习区')

    a.append('4FN-A105')
    b.append('103762649')
    c.append('北馆四层自习区')

    a.append('4FN-A106')
    b.append('103762650')
    c.append('北馆四层自习区')

    a.append('4FN-A107')
    b.append('103762651')
    c.append('北馆四层自习区')

    a.append('4FN-A108')
    b.append('103762652')
    c.append('北馆四层自习区')

    a.append('5FN-B001')
    b.append('103762893')
    c.append('北馆五层自习区')

    a.append('5FN-B002')
    b.append('103762894')
    c.append('北馆五层自习区')

    a.append('5FN-B003')
    b.append('103762895')
    c.append('北馆五层自习区')

    a.append('5FN-B004')
    b.append('103762896')
    c.append('北馆五层自习区')

    a.append('5FN-B005')
    b.append('103762897')
    c.append('北馆五层自习区')

    a.append('5FN-B006')
    b.append('103762898')
    c.append('北馆五层自习区')

    a.append('5FN-B007')
    b.append('103762899')
    c.append('北馆五层自习区')

    a.append('5FN-B008')
    b.append('103762900')
    c.append('北馆五层自习区')

    a.append('5FN-B009')
    b.append('103762901')
    c.append('北馆五层自习区')

    a.append('5FN-B010')
    b.append('103762902')
    c.append('北馆五层自习区')

    a.append('5FN-B011')
    b.append('103762903')
    c.append('北馆五层自习区')

    a.append('5FN-B012')
    b.append('103762904')
    c.append('北馆五层自习区')

    a.append('5FN-B013')
    b.append('103762905')
    c.append('北馆五层自习区')

    a.append('5FN-B014')
    b.append('103762906')
    c.append('北馆五层自习区')

    a.append('5FN-B015')
    b.append('103762907')
    c.append('北馆五层自习区')

    a.append('5FN-B016')
    b.append('103762908')
    c.append('北馆五层自习区')

    a.append('5FN-B017')
    b.append('103762909')
    c.append('北馆五层自习区')

    a.append('5FN-B018')
    b.append('103762910')
    c.append('北馆五层自习区')

    a.append('5FN-B019')
    b.append('103762911')
    c.append('北馆五层自习区')

    a.append('5FN-B020')
    b.append('103762912')
    c.append('北馆五层自习区')

    a.append('5FN-B021')
    b.append('103762913')
    c.append('北馆五层自习区')

    a.append('5FN-B022')
    b.append('103762914')
    c.append('北馆五层自习区')

    a.append('5FN-B023')
    b.append('103762915')
    c.append('北馆五层自习区')

    a.append('5FN-B024')
    b.append('103762916')
    c.append('北馆五层自习区')

    a.append('5FN-B025')
    b.append('103762917')
    c.append('北馆五层自习区')

    a.append('5FN-B026')
    b.append('103762918')
    c.append('北馆五层自习区')

    a.append('5FN-B027')
    b.append('103762919')
    c.append('北馆五层自习区')

    a.append('5FN-B028')
    b.append('103762920')
    c.append('北馆五层自习区')

    a.append('5FN-B029')
    b.append('103762921')
    c.append('北馆五层自习区')

    a.append('5FN-B030')
    b.append('103762922')
    c.append('北馆五层自习区')

    a.append('5FN-B031')
    b.append('103762923')
    c.append('北馆五层自习区')

    a.append('5FN-B032')
    b.append('103762924')
    c.append('北馆五层自习区')

    a.append('5FN-B033')
    b.append('103762925')
    c.append('北馆五层自习区')

    a.append('5FN-B034')
    b.append('103762926')
    c.append('北馆五层自习区')

    a.append('5FN-B035')
    b.append('103762927')
    c.append('北馆五层自习区')

    a.append('5FN-B036')
    b.append('103762928')
    c.append('北馆五层自习区')

    a.append('5FN-B037')
    b.append('103762929')
    c.append('北馆五层自习区')

    a.append('5FN-B038')
    b.append('103762930')
    c.append('北馆五层自习区')

    a.append('5FN-B039')
    b.append('103762931')
    c.append('北馆五层自习区')

    a.append('5FN-B040')
    b.append('103762932')
    c.append('北馆五层自习区')

    a.append('5FN-B041')
    b.append('103762933')
    c.append('北馆五层自习区')

    a.append('5FN-B042')
    b.append('103762934')
    c.append('北馆五层自习区')

    a.append('5FN-B043')
    b.append('103762935')
    c.append('北馆五层自习区')

    a.append('5FN-B044')
    b.append('103762936')
    c.append('北馆五层自习区')

    a.append('5FN-B045')
    b.append('103762937')
    c.append('北馆五层自习区')

    a.append('5FN-B046')
    b.append('103762938')
    c.append('北馆五层自习区')

    a.append('5FN-B047')
    b.append('103762939')
    c.append('北馆五层自习区')

    a.append('5FN-B048')
    b.append('103762940')
    c.append('北馆五层自习区')

    a.append('5FN-B049')
    b.append('103762941')
    c.append('北馆五层自习区')

    a.append('5FN-B050')
    b.append('103762942')
    c.append('北馆五层自习区')

    a.append('5FN-B051')
    b.append('103762943')
    c.append('北馆五层自习区')

    a.append('5FN-B052')
    b.append('103762944')
    c.append('北馆五层自习区')

    a.append('5FN-B053')
    b.append('103762945')
    c.append('北馆五层自习区')

    a.append('5FN-B054')
    b.append('103762946')
    c.append('北馆五层自习区')

    a.append('5FN-B055')
    b.append('103762947')
    c.append('北馆五层自习区')

    a.append('5FN-B056')
    b.append('103762948')
    c.append('北馆五层自习区')

    a.append('5FN-B057')
    b.append('103762949')
    c.append('北馆五层自习区')

    a.append('5FN-B058')
    b.append('103762950')
    c.append('北馆五层自习区')

    a.append('5FN-B059')
    b.append('103762951')
    c.append('北馆五层自习区')

    a.append('5FN-B060')
    b.append('103762952')
    c.append('北馆五层自习区')

    a.append('5FN-B061')
    b.append('103762953')
    c.append('北馆五层自习区')

    a.append('5FN-B062')
    b.append('103762954')
    c.append('北馆五层自习区')

    a.append('5FN-B063')
    b.append('103762955')
    c.append('北馆五层自习区')

    a.append('5FN-B064')
    b.append('103762956')
    c.append('北馆五层自习区')

    a.append('5FN-B065')
    b.append('103762957')
    c.append('北馆五层自习区')

    a.append('5FN-B066')
    b.append('103762958')
    c.append('北馆五层自习区')

    a.append('5FN-B067')
    b.append('103762959')
    c.append('北馆五层自习区')

    a.append('5FN-B068')
    b.append('103762960')
    c.append('北馆五层自习区')

    a.append('5FN-B069')
    b.append('103762961')
    c.append('北馆五层自习区')

    a.append('5FN-B070')
    b.append('103762962')
    c.append('北馆五层自习区')

    a.append('5FN-B071')
    b.append('103762963')
    c.append('北馆五层自习区')

    a.append('5FN-B072')
    b.append('103762964')
    c.append('北馆五层自习区')

    a.append('5FN-B073')
    b.append('103762965')
    c.append('北馆五层自习区')

    a.append('5FN-B074')
    b.append('103762966')
    c.append('北馆五层自习区')

    a.append('5FN-B075')
    b.append('103762967')
    c.append('北馆五层自习区')

    a.append('5FN-B076')
    b.append('103762968')
    c.append('北馆五层自习区')

    a.append('5FN-B077')
    b.append('103762969')
    c.append('北馆五层自习区')

    a.append('5FN-B078')
    b.append('103762970')
    c.append('北馆五层自习区')

    a.append('5FN-B079')
    b.append('103762971')
    c.append('北馆五层自习区')

    a.append('5FN-B080')
    b.append('103762972')
    c.append('北馆五层自习区')

    a.append('5FN-B081')
    b.append('103762973')
    c.append('北馆五层自习区')

    a.append('5FN-B082')
    b.append('103762974')
    c.append('北馆五层自习区')

    a.append('5FN-B083')
    b.append('103762975')
    c.append('北馆五层自习区')

    a.append('5FN-B084')
    b.append('103762976')
    c.append('北馆五层自习区')

    a.append('5FN-B085')
    b.append('103762977')
    c.append('北馆五层自习区')

    a.append('5FN-B086')
    b.append('103762978')
    c.append('北馆五层自习区')

    a.append('5FN-B087')
    b.append('103762979')
    c.append('北馆五层自习区')

    a.append('5FN-B088')
    b.append('103762980')
    c.append('北馆五层自习区')

    a.append('5FN-B089')
    b.append('103762981')
    c.append('北馆五层自习区')

    a.append('5FN-B090')
    b.append('103762982')
    c.append('北馆五层自习区')

    a.append('5FN-B091')
    b.append('103762983')
    c.append('北馆五层自习区')

    a.append('5FN-B092')
    b.append('103762984')
    c.append('北馆五层自习区')

    a.append('5FN-C001')
    b.append('103762985')
    c.append('北馆五层自习区')

    a.append('5FN-C002')
    b.append('103762986')
    c.append('北馆五层自习区')

    a.append('5FN-C003')
    b.append('103762987')
    c.append('北馆五层自习区')

    a.append('5FN-C004')
    b.append('103762988')
    c.append('北馆五层自习区')

    a.append('5FN-C005')
    b.append('103762989')
    c.append('北馆五层自习区')

    a.append('5FN-C006')
    b.append('103762990')
    c.append('北馆五层自习区')

    a.append('5FN-C007')
    b.append('103762991')
    c.append('北馆五层自习区')

    a.append('5FN-C008')
    b.append('103762992')
    c.append('北馆五层自习区')

    a.append('5FN-C009')
    b.append('103762993')
    c.append('北馆五层自习区')

    a.append('5FN-C010')
    b.append('103762994')
    c.append('北馆五层自习区')

    a.append('5FN-C011')
    b.append('103762995')
    c.append('北馆五层自习区')

    a.append('5FN-C012')
    b.append('103762996')
    c.append('北馆五层自习区')

    a.append('5FN-C013')
    b.append('103762997')
    c.append('北馆五层自习区')

    a.append('5FN-C014')
    b.append('103762998')
    c.append('北馆五层自习区')

    a.append('5FN-C015')
    b.append('103762999')
    c.append('北馆五层自习区')

    a.append('5FN-C016')
    b.append('103763000')
    c.append('北馆五层自习区')

    a.append('5FN-C017')
    b.append('103763001')
    c.append('北馆五层自习区')

    a.append('5FN-C018')
    b.append('103763002')
    c.append('北馆五层自习区')

    a.append('5FN-C019')
    b.append('103763003')
    c.append('北馆五层自习区')

    a.append('5FN-C020')
    b.append('103763004')
    c.append('北馆五层自习区')

    a.append('5FN-C021')
    b.append('103763005')
    c.append('北馆五层自习区')

    a.append('5FN-C022')
    b.append('103763006')
    c.append('北馆五层自习区')

    a.append('5FN-C023')
    b.append('103763007')
    c.append('北馆五层自习区')

    a.append('5FN-C024')
    b.append('103763008')
    c.append('北馆五层自习区')

    a.append('5FN-C025')
    b.append('103763009')
    c.append('北馆五层自习区')

    a.append('5FN-C026')
    b.append('103763010')
    c.append('北馆五层自习区')

    a.append('5FN-C027')
    b.append('103763011')
    c.append('北馆五层自习区')

    a.append('5FN-C028')
    b.append('103763012')
    c.append('北馆五层自习区')

    a.append('5FN-C029')
    b.append('103763013')
    c.append('北馆五层自习区')

    a.append('5FN-C030')
    b.append('103763014')
    c.append('北馆五层自习区')

    a.append('5FN-C031')
    b.append('103763015')
    c.append('北馆五层自习区')

    a.append('5FN-C032')
    b.append('103763016')
    c.append('北馆五层自习区')

    a.append('5FN-C033')
    b.append('103763017')
    c.append('北馆五层自习区')

    a.append('5FN-C034')
    b.append('103763018')
    c.append('北馆五层自习区')

    a.append('5FN-C035')
    b.append('103763019')
    c.append('北馆五层自习区')

    a.append('5FN-C036')
    b.append('103763020')
    c.append('北馆五层自习区')

    a.append('5FN-C037')
    b.append('103763021')
    c.append('北馆五层自习区')

    a.append('5FN-C038')
    b.append('103763022')
    c.append('北馆五层自习区')

    a.append('5FN-C039')
    b.append('103763023')
    c.append('北馆五层自习区')

    a.append('5FN-C040')
    b.append('103763024')
    c.append('北馆五层自习区')

    a.append('5FN-A001')
    b.append('103762785')
    c.append('北馆五层自习区')

    a.append('5FN-A002')
    b.append('103762786')
    c.append('北馆五层自习区')

    a.append('5FN-A003')
    b.append('103762787')
    c.append('北馆五层自习区')

    a.append('5FN-A004')
    b.append('103762788')
    c.append('北馆五层自习区')

    a.append('5FN-A005')
    b.append('103762789')
    c.append('北馆五层自习区')

    a.append('5FN-A006')
    b.append('103762790')
    c.append('北馆五层自习区')

    a.append('5FN-A007')
    b.append('103762791')
    c.append('北馆五层自习区')

    a.append('5FN-A008')
    b.append('103762792')
    c.append('北馆五层自习区')

    a.append('5FN-A009')
    b.append('103762793')
    c.append('北馆五层自习区')

    a.append('5FN-A010')
    b.append('103762794')
    c.append('北馆五层自习区')

    a.append('5FN-A011')
    b.append('103762795')
    c.append('北馆五层自习区')

    a.append('5FN-A012')
    b.append('103762796')
    c.append('北馆五层自习区')

    a.append('5FN-A013')
    b.append('103762797')
    c.append('北馆五层自习区')

    a.append('5FN-A014')
    b.append('103762798')
    c.append('北馆五层自习区')

    a.append('5FN-A015')
    b.append('103762799')
    c.append('北馆五层自习区')

    a.append('5FN-A016')
    b.append('103762800')
    c.append('北馆五层自习区')

    a.append('5FN-A017')
    b.append('103762801')
    c.append('北馆五层自习区')

    a.append('5FN-A018')
    b.append('103762802')
    c.append('北馆五层自习区')

    a.append('5FN-A019')
    b.append('103762803')
    c.append('北馆五层自习区')

    a.append('5FN-A020')
    b.append('103762804')
    c.append('北馆五层自习区')

    a.append('5FN-A021')
    b.append('103762805')
    c.append('北馆五层自习区')

    a.append('5FN-A022')
    b.append('103762806')
    c.append('北馆五层自习区')

    a.append('5FN-A023')
    b.append('103762807')
    c.append('北馆五层自习区')

    a.append('5FN-A024')
    b.append('103762808')
    c.append('北馆五层自习区')

    a.append('5FN-A025')
    b.append('103762809')
    c.append('北馆五层自习区')

    a.append('5FN-A026')
    b.append('103762810')
    c.append('北馆五层自习区')

    a.append('5FN-A027')
    b.append('103762811')
    c.append('北馆五层自习区')

    a.append('5FN-A028')
    b.append('103762812')
    c.append('北馆五层自习区')

    a.append('5FN-A029')
    b.append('103762813')
    c.append('北馆五层自习区')

    a.append('5FN-A030')
    b.append('103762814')
    c.append('北馆五层自习区')

    a.append('5FN-A031')
    b.append('103762815')
    c.append('北馆五层自习区')

    a.append('5FN-A032')
    b.append('103762816')
    c.append('北馆五层自习区')

    a.append('5FN-A033')
    b.append('103762817')
    c.append('北馆五层自习区')

    a.append('5FN-A034')
    b.append('103762818')
    c.append('北馆五层自习区')

    a.append('5FN-A035')
    b.append('103762819')
    c.append('北馆五层自习区')

    a.append('5FN-A036')
    b.append('103762820')
    c.append('北馆五层自习区')

    a.append('5FN-A037')
    b.append('103762821')
    c.append('北馆五层自习区')

    a.append('5FN-A038')
    b.append('103762822')
    c.append('北馆五层自习区')

    a.append('5FN-A039')
    b.append('103762823')
    c.append('北馆五层自习区')

    a.append('5FN-A040')
    b.append('103762824')
    c.append('北馆五层自习区')

    a.append('5FN-A041')
    b.append('103762825')
    c.append('北馆五层自习区')

    a.append('5FN-A042')
    b.append('103762826')
    c.append('北馆五层自习区')

    a.append('5FN-A043')
    b.append('103762827')
    c.append('北馆五层自习区')

    a.append('5FN-A044')
    b.append('103762828')
    c.append('北馆五层自习区')

    a.append('5FN-A045')
    b.append('103762829')
    c.append('北馆五层自习区')

    a.append('5FN-A046')
    b.append('103762830')
    c.append('北馆五层自习区')

    a.append('5FN-A047')
    b.append('103762831')
    c.append('北馆五层自习区')

    a.append('5FN-A048')
    b.append('103762832')
    c.append('北馆五层自习区')

    a.append('5FN-A049')
    b.append('103762833')
    c.append('北馆五层自习区')

    a.append('5FN-A050')
    b.append('103762834')
    c.append('北馆五层自习区')

    a.append('5FN-A051')
    b.append('103762835')
    c.append('北馆五层自习区')

    a.append('5FN-A052')
    b.append('103762836')
    c.append('北馆五层自习区')

    a.append('5FN-A053')
    b.append('103762837')
    c.append('北馆五层自习区')

    a.append('5FN-A054')
    b.append('103762838')
    c.append('北馆五层自习区')

    a.append('5FN-A055')
    b.append('103762839')
    c.append('北馆五层自习区')

    a.append('5FN-A056')
    b.append('103762840')
    c.append('北馆五层自习区')

    a.append('5FN-A057')
    b.append('103762841')
    c.append('北馆五层自习区')

    a.append('5FN-A058')
    b.append('103762842')
    c.append('北馆五层自习区')

    a.append('5FN-A059')
    b.append('103762843')
    c.append('北馆五层自习区')

    a.append('5FN-A060')
    b.append('103762844')
    c.append('北馆五层自习区')

    a.append('5FN-A061')
    b.append('103762845')
    c.append('北馆五层自习区')

    a.append('5FN-A062')
    b.append('103762846')
    c.append('北馆五层自习区')

    a.append('5FN-A063')
    b.append('103762847')
    c.append('北馆五层自习区')

    a.append('5FN-A064')
    b.append('103762848')
    c.append('北馆五层自习区')

    a.append('5FN-A065')
    b.append('103762849')
    c.append('北馆五层自习区')

    a.append('5FN-A066')
    b.append('103762850')
    c.append('北馆五层自习区')

    a.append('5FN-A067')
    b.append('103762851')
    c.append('北馆五层自习区')

    a.append('5FN-A068')
    b.append('103762852')
    c.append('北馆五层自习区')

    a.append('5FN-A069')
    b.append('103762853')
    c.append('北馆五层自习区')

    a.append('5FN-A070')
    b.append('103762854')
    c.append('北馆五层自习区')

    a.append('5FN-A071')
    b.append('103762855')
    c.append('北馆五层自习区')

    a.append('5FN-A072')
    b.append('103762856')
    c.append('北馆五层自习区')

    a.append('5FN-A073')
    b.append('103762857')
    c.append('北馆五层自习区')

    a.append('5FN-A074')
    b.append('103762858')
    c.append('北馆五层自习区')

    a.append('5FN-A075')
    b.append('103762859')
    c.append('北馆五层自习区')

    a.append('5FN-A076')
    b.append('103762860')
    c.append('北馆五层自习区')

    a.append('5FN-A077')
    b.append('103762861')
    c.append('北馆五层自习区')

    a.append('5FN-A078')
    b.append('103762862')
    c.append('北馆五层自习区')

    a.append('5FN-A079')
    b.append('103762863')
    c.append('北馆五层自习区')

    a.append('5FN-A080')
    b.append('103762864')
    c.append('北馆五层自习区')

    a.append('5FN-A081')
    b.append('103762865')
    c.append('北馆五层自习区')

    a.append('5FN-A082')
    b.append('103762866')
    c.append('北馆五层自习区')

    a.append('5FN-A083')
    b.append('103762867')
    c.append('北馆五层自习区')

    a.append('5FN-A084')
    b.append('103762868')
    c.append('北馆五层自习区')

    a.append('5FN-A085')
    b.append('103762869')
    c.append('北馆五层自习区')

    a.append('5FN-A086')
    b.append('103762870')
    c.append('北馆五层自习区')

    a.append('5FN-A087')
    b.append('103762871')
    c.append('北馆五层自习区')

    a.append('5FN-A088')
    b.append('103762872')
    c.append('北馆五层自习区')

    a.append('5FN-A089')
    b.append('103762873')
    c.append('北馆五层自习区')

    a.append('5FN-A090')
    b.append('103762874')
    c.append('北馆五层自习区')

    a.append('5FN-A091')
    b.append('103762875')
    c.append('北馆五层自习区')

    a.append('5FN-A092')
    b.append('103762876')
    c.append('北馆五层自习区')

    a.append('5FN-A093')
    b.append('103762877')
    c.append('北馆五层自习区')

    a.append('5FN-A094')
    b.append('103762878')
    c.append('北馆五层自习区')

    a.append('5FN-A095')
    b.append('103762879')
    c.append('北馆五层自习区')

    a.append('5FN-A096')
    b.append('103762880')
    c.append('北馆五层自习区')

    a.append('5FN-A097')
    b.append('103762881')
    c.append('北馆五层自习区')

    a.append('5FN-A098')
    b.append('103762882')
    c.append('北馆五层自习区')

    a.append('5FN-A099')
    b.append('103762883')
    c.append('北馆五层自习区')

    a.append('5FN-A100')
    b.append('103762884')
    c.append('北馆五层自习区')

    a.append('5FN-A101')
    b.append('103762885')
    c.append('北馆五层自习区')

    a.append('5FN-A102')
    b.append('103762886')
    c.append('北馆五层自习区')

    a.append('5FN-A103')
    b.append('103762887')
    c.append('北馆五层自习区')

    a.append('5FN-A104')
    b.append('103762888')
    c.append('北馆五层自习区')

    a.append('5FN-A105')
    b.append('103762889')
    c.append('北馆五层自习区')

    a.append('5FN-A106')
    b.append('103762890')
    c.append('北馆五层自习区')

    a.append('5FN-A107')
    b.append('103762891')
    c.append('北馆五层自习区')

    a.append('5FN-A108')
    b.append('103762892')
    c.append('北馆五层自习区')

    a.append('3FS-A001')
    b.append('103763045')
    c.append('南馆三层自习室')

    a.append('3FS-A002')
    b.append('103763046')
    c.append('南馆三层自习室')

    a.append('3FS-A003')
    b.append('103763047')
    c.append('南馆三层自习室')

    a.append('3FS-A004')
    b.append('103763048')
    c.append('南馆三层自习室')

    a.append('3FS-A005')
    b.append('103763049')
    c.append('南馆三层自习室')

    a.append('3FS-A006')
    b.append('103763050')
    c.append('南馆三层自习室')

    a.append('3FS-A007')
    b.append('103763051')
    c.append('南馆三层自习室')

    a.append('3FS-A008')
    b.append('103763052')
    c.append('南馆三层自习室')

    a.append('3FS-A009')
    b.append('103763053')
    c.append('南馆三层自习室')

    a.append('3FS-A010')
    b.append('103763054')
    c.append('南馆三层自习室')

    a.append('3FS-A011')
    b.append('103763055')
    c.append('南馆三层自习室')

    a.append('3FS-A012')
    b.append('103763056')
    c.append('南馆三层自习室')

    a.append('3FS-A013')
    b.append('103763057')
    c.append('南馆三层自习室')

    a.append('3FS-A014')
    b.append('103763058')
    c.append('南馆三层自习室')

    a.append('3FS-A015')
    b.append('103763059')
    c.append('南馆三层自习室')

    a.append('3FS-A016')
    b.append('103763060')
    c.append('南馆三层自习室')

    a.append('3FS-A017')
    b.append('103763061')
    c.append('南馆三层自习室')

    a.append('3FS-A018')
    b.append('103763062')
    c.append('南馆三层自习室')

    a.append('3FS-A019')
    b.append('103763063')
    c.append('南馆三层自习室')

    a.append('3FS-A020')
    b.append('103763064')
    c.append('南馆三层自习室')

    a.append('3FS-A021')
    b.append('103763065')
    c.append('南馆三层自习室')

    a.append('3FS-A022')
    b.append('103763066')
    c.append('南馆三层自习室')

    a.append('3FS-A023')
    b.append('103763067')
    c.append('南馆三层自习室')

    a.append('3FS-A024')
    b.append('103763068')
    c.append('南馆三层自习室')

    a.append('3FS-A025')
    b.append('103763069')
    c.append('南馆三层自习室')

    a.append('3FS-A026')
    b.append('103763070')
    c.append('南馆三层自习室')

    a.append('3FS-A027')
    b.append('103763071')
    c.append('南馆三层自习室')

    a.append('3FS-A028')
    b.append('103763072')
    c.append('南馆三层自习室')

    a.append('3FS-A029')
    b.append('103763073')
    c.append('南馆三层自习室')

    a.append('3FS-A030')
    b.append('103763074')
    c.append('南馆三层自习室')

    a.append('3FS-A031')
    b.append('103763075')
    c.append('南馆三层自习室')

    a.append('3FS-A032')
    b.append('103763076')
    c.append('南馆三层自习室')

    a.append('3FS-A033')
    b.append('103763077')
    c.append('南馆三层自习室')

    a.append('3FS-A034')
    b.append('103763078')
    c.append('南馆三层自习室')

    a.append('3FS-A035')
    b.append('103763079')
    c.append('南馆三层自习室')

    a.append('3FS-A036')
    b.append('103763080')
    c.append('南馆三层自习室')

    a.append('3FS-A037')
    b.append('103763081')
    c.append('南馆三层自习室')

    a.append('3FS-A038')
    b.append('103763082')
    c.append('南馆三层自习室')

    a.append('3FS-A039')
    b.append('103763083')
    c.append('南馆三层自习室')

    a.append('3FS-A040')
    b.append('103763084')
    c.append('南馆三层自习室')

    a.append('3FS-A041')
    b.append('103763085')
    c.append('南馆三层自习室')

    a.append('3FS-A042')
    b.append('103763086')
    c.append('南馆三层自习室')

    a.append('3FS-A043')
    b.append('103763087')
    c.append('南馆三层自习室')

    a.append('3FS-A044')
    b.append('103763088')
    c.append('南馆三层自习室')

    a.append('3FS-A045')
    b.append('103763089')
    c.append('南馆三层自习室')

    a.append('3FS-A046')
    b.append('103763090')
    c.append('南馆三层自习室')

    a.append('3FS-A047')
    b.append('103763091')
    c.append('南馆三层自习室')

    a.append('3FS-A048')
    b.append('103763092')
    c.append('南馆三层自习室')

    a.append('3FS-A049')
    b.append('103763093')
    c.append('南馆三层自习室')

    a.append('3FS-A050')
    b.append('103763094')
    c.append('南馆三层自习室')

    a.append('3FS-A051')
    b.append('103763095')
    c.append('南馆三层自习室')

    a.append('3FS-A052')
    b.append('103763096')
    c.append('南馆三层自习室')

    a.append('3FS-A053')
    b.append('103763097')
    c.append('南馆三层自习室')

    a.append('3FS-A054')
    b.append('103763098')
    c.append('南馆三层自习室')

    a.append('3FS-A055')
    b.append('103763099')
    c.append('南馆三层自习室')

    a.append('3FS-A056')
    b.append('103763100')
    c.append('南馆三层自习室')

    a.append('3FS-A057')
    b.append('103763101')
    c.append('南馆三层自习室')

    a.append('3FS-A058')
    b.append('103763102')
    c.append('南馆三层自习室')

    a.append('3FS-A059')
    b.append('103763103')
    c.append('南馆三层自习室')

    a.append('3FS-A060')
    b.append('103763104')
    c.append('南馆三层自习室')

    a.append('3FS-A061')
    b.append('103763105')
    c.append('南馆三层自习室')

    a.append('3FS-A062')
    b.append('103763106')
    c.append('南馆三层自习室')

    a.append('3FS-A063')
    b.append('103763107')
    c.append('南馆三层自习室')

    a.append('3FS-A064')
    b.append('103763108')
    c.append('南馆三层自习室')

    a.append('3FS-A065')
    b.append('103763109')
    c.append('南馆三层自习室')

    a.append('3FS-A066')
    b.append('103763110')
    c.append('南馆三层自习室')

    a.append('3FS-A067')
    b.append('103763111')
    c.append('南馆三层自习室')

    a.append('3FS-A068')
    b.append('103763112')
    c.append('南馆三层自习室')

    a.append('3FS-A069')
    b.append('103763113')
    c.append('南馆三层自习室')

    a.append('3FS-A070')
    b.append('103763114')
    c.append('南馆三层自习室')

    a.append('3FS-A071')
    b.append('103763115')
    c.append('南馆三层自习室')

    a.append('3FS-A072')
    b.append('103763116')
    c.append('南馆三层自习室')

    a.append('3FS-A073')
    b.append('103763117')
    c.append('南馆三层自习室')

    a.append('3FS-A074')
    b.append('103763118')
    c.append('南馆三层自习室')

    a.append('3FS-A075')
    b.append('103763119')
    c.append('南馆三层自习室')

    a.append('3FS-A076')
    b.append('103763120')
    c.append('南馆三层自习室')

    a.append('3FS-A077')
    b.append('103763121')
    c.append('南馆三层自习室')

    a.append('3FS-A078')
    b.append('103763122')
    c.append('南馆三层自习室')

    a.append('3FS-A079')
    b.append('103763123')
    c.append('南馆三层自习室')

    a.append('3FS-A080')
    b.append('103763124')
    c.append('南馆三层自习室')

    a.append('3FS-A081')
    b.append('103763125')
    c.append('南馆三层自习室')

    a.append('3FS-A082')
    b.append('103763126')
    c.append('南馆三层自习室')

    a.append('3FS-A083')
    b.append('103763127')
    c.append('南馆三层自习室')

    a.append('3FS-A084')
    b.append('103763128')
    c.append('南馆三层自习室')

    a.append('3FS-A085')
    b.append('103763129')
    c.append('南馆三层自习室')

    a.append('3FS-A086')
    b.append('103763130')
    c.append('南馆三层自习室')

    a.append('3FS-A087')
    b.append('103763131')
    c.append('南馆三层自习室')

    a.append('3FS-A088')
    b.append('103763132')
    c.append('南馆三层自习室')

    a.append('3FS-A089')
    b.append('103763133')
    c.append('南馆三层自习室')

    a.append('3FS-A090')
    b.append('103763134')
    c.append('南馆三层自习室')

    a.append('3FS-A091')
    b.append('103763135')
    c.append('南馆三层自习室')

    a.append('3FS-A092')
    b.append('103763136')
    c.append('南馆三层自习室')

    a.append('3FS-A093')
    b.append('103763137')
    c.append('南馆三层自习室')

    a.append('3FS-A094')
    b.append('103763138')
    c.append('南馆三层自习室')

    a.append('3FS-A095')
    b.append('103763139')
    c.append('南馆三层自习室')

    a.append('3FS-A096')
    b.append('103763140')
    c.append('南馆三层自习室')

    a.append('3FS-A097')
    b.append('103763141')
    c.append('南馆三层自习室')

    a.append('3FS-A098')
    b.append('103763142')
    c.append('南馆三层自习室')

    a.append('3FS-A099')
    b.append('103763143')
    c.append('南馆三层自习室')

    a.append('3FS-A100')
    b.append('103763144')
    c.append('南馆三层自习室')

    a.append('3FS-A101')
    b.append('103763145')
    c.append('南馆三层自习室')

    a.append('3FS-A102')
    b.append('103763146')
    c.append('南馆三层自习室')

    a.append('3FS-A103')
    b.append('103763147')
    c.append('南馆三层自习室')

    a.append('3FS-A104')
    b.append('103763148')
    c.append('南馆三层自习室')

    a.append('3FS-A105')
    b.append('103763149')
    c.append('南馆三层自习室')

    a.append('3FS-A106')
    b.append('103763150')
    c.append('南馆三层自习室')

    a.append('3FS-A107')
    b.append('103763151')
    c.append('南馆三层自习室')

    a.append('3FS-A108')
    b.append('103763152')
    c.append('南馆三层自习室')

    a.append('3FS-A109')
    b.append('103763153')
    c.append('南馆三层自习室')

    a.append('3FS-A110')
    b.append('103763154')
    c.append('南馆三层自习室')

    a.append('3FS-A111')
    b.append('103763155')
    c.append('南馆三层自习室')

    a.append('3FS-A112')
    b.append('103763156')
    c.append('南馆三层自习室')

    a.append('3FS-A113')
    b.append('103763157')
    c.append('南馆三层自习室')

    a.append('3FS-A114')
    b.append('103763158')
    c.append('南馆三层自习室')

    a.append('3FS-A115')
    b.append('103763159')
    c.append('南馆三层自习室')

    a.append('3FS-A116')
    b.append('103763160')
    c.append('南馆三层自习室')

    a.append('3FS-A117')
    b.append('103763161')
    c.append('南馆三层自习室')

    a.append('3FS-A118')
    b.append('103763162')
    c.append('南馆三层自习室')

    a.append('3FS-A119')
    b.append('103763163')
    c.append('南馆三层自习室')

    a.append('3FS-A120')
    b.append('103763164')
    c.append('南馆三层自习室')

    a.append('3FS-A121')
    b.append('103763165')
    c.append('南馆三层自习室')

    a.append('3FS-A122')
    b.append('103763166')
    c.append('南馆三层自习室')

    a.append('3FS-A123')
    b.append('103763167')
    c.append('南馆三层自习室')

    a.append('3FS-A124')
    b.append('103763168')
    c.append('南馆三层自习室')

    a.append('3FS-A125')
    b.append('103763169')
    c.append('南馆三层自习室')

    a.append('3FS-A126')
    b.append('103763170')
    c.append('南馆三层自习室')

    a.append('3FS-A127')
    b.append('103763171')
    c.append('南馆三层自习室')

    a.append('3FS-A128')
    b.append('103763172')
    c.append('南馆三层自习室')

    a.append('3FS-A129')
    b.append('103763173')
    c.append('南馆三层自习室')

    a.append('3FS-A130')
    b.append('103763174')
    c.append('南馆三层自习室')

    a.append('3FS-A131')
    b.append('103763175')
    c.append('南馆三层自习室')

    a.append('3FS-A132')
    b.append('103763176')
    c.append('南馆三层自习室')

    a.append('3FS-A133')
    b.append('103763177')
    c.append('南馆三层自习室')

    a.append('3FS-A134')
    b.append('103763178')
    c.append('南馆三层自习室')

    a.append('3FS-A135')
    b.append('103763179')
    c.append('南馆三层自习室')

    a.append('3FS-A136')
    b.append('103763180')
    c.append('南馆三层自习室')

    a.append('3FS-A137')
    b.append('103763181')
    c.append('南馆三层自习室')

    a.append('3FS-A138')
    b.append('103763182')
    c.append('南馆三层自习室')

    a.append('3FS-A139')
    b.append('103763183')
    c.append('南馆三层自习室')

    a.append('3FS-A140')
    b.append('103763184')
    c.append('南馆三层自习室')

    a.append('3FS-A141')
    b.append('103763185')
    c.append('南馆三层自习室')

    a.append('3FS-A142')
    b.append('103763186')
    c.append('南馆三层自习室')

    a.append('3FS-A143')
    b.append('103763187')
    c.append('南馆三层自习室')

    a.append('3FS-A144')
    b.append('103763188')
    c.append('南馆三层自习室')

    a.append('3FS-A145')
    b.append('103763189')
    c.append('南馆三层自习室')

    a.append('3FS-A146')
    b.append('103763190')
    c.append('南馆三层自习室')

    a.append('3FS-A147')
    b.append('103763191')
    c.append('南馆三层自习室')

    a.append('3FS-A148')
    b.append('103763192')
    c.append('南馆三层自习室')

    a.append('3FS-A149')
    b.append('103763193')
    c.append('南馆三层自习室')

    a.append('3FS-A150')
    b.append('103763194')
    c.append('南馆三层自习室')

    a.append('3FS-A151')
    b.append('103763195')
    c.append('南馆三层自习室')

    a.append('3FS-A152')
    b.append('103763196')
    c.append('南馆三层自习室')

    a.append('3FS-A153')
    b.append('103763197')
    c.append('南馆三层自习室')

    a.append('3FS-A154')
    b.append('103763198')
    c.append('南馆三层自习室')

    a.append('3FS-A155')
    b.append('103763199')
    c.append('南馆三层自习室')

    a.append('3FS-A156')
    b.append('103763200')
    c.append('南馆三层自习室')

    a.append('3FS-A157')
    b.append('103763201')
    c.append('南馆三层自习室')

    a.append('3FS-A158')
    b.append('103763202')
    c.append('南馆三层自习室')

    a.append('3FS-A159')
    b.append('103763203')
    c.append('南馆三层自习室')

    a.append('3FS-A160')
    b.append('103763204')
    c.append('南馆三层自习室')

    a.append('3FS-A161')
    b.append('103763205')
    c.append('南馆三层自习室')

    a.append('3FS-A162')
    b.append('103763206')
    c.append('南馆三层自习室')

    a.append('3FS-A163')
    b.append('103763207')
    c.append('南馆三层自习室')

    a.append('3FS-A164')
    b.append('103763208')
    c.append('南馆三层自习室')

    a.append('3FS-A165')
    b.append('103763209')
    c.append('南馆三层自习室')

    a.append('3FS-A166')
    b.append('103763210')
    c.append('南馆三层自习室')

    a.append('3FS-A167')
    b.append('103763211')
    c.append('南馆三层自习室')

    a.append('3FS-A168')
    b.append('103763212')
    c.append('南馆三层自习室')

    a.append('3FS-A169')
    b.append('103763213')
    c.append('南馆三层自习室')

    a.append('3FS-A170')
    b.append('103763214')
    c.append('南馆三层自习室')

    a.append('3FS-A171')
    b.append('103763215')
    c.append('南馆三层自习室')

    a.append('3FS-A172')
    b.append('103763216')
    c.append('南馆三层自习室')

    a.append('3FS-A173')
    b.append('103763217')
    c.append('南馆三层自习室')

    a.append('3FS-A174')
    b.append('103763218')
    c.append('南馆三层自习室')

    a.append('3FS-A175')
    b.append('103763219')
    c.append('南馆三层自习室')

    a.append('3FS-A176')
    b.append('103763220')
    c.append('南馆三层自习室')

    a.append('3FS-A177')
    b.append('103763221')
    c.append('南馆三层自习室')

    a.append('3FS-A178')
    b.append('103763222')
    c.append('南馆三层自习室')

    a.append('3FS-A179')
    b.append('103763223')
    c.append('南馆三层自习室')

    a.append('3FS-A180')
    b.append('103763224')
    c.append('南馆三层自习室')

    a.append('3FS-A181')
    b.append('103763225')
    c.append('南馆三层自习室')

    a.append('3FS-A182')
    b.append('103763226')
    c.append('南馆三层自习室')

    a.append('3FS-A183')
    b.append('103763227')
    c.append('南馆三层自习室')

    a.append('3FS-A184')
    b.append('103763228')
    c.append('南馆三层自习室')

    a.append('3FS-A185')
    b.append('103763229')
    c.append('南馆三层自习室')

    a.append('3FS-A186')
    b.append('103763230')
    c.append('南馆三层自习室')

    a.append('3FS-A187')
    b.append('103763231')
    c.append('南馆三层自习室')

    a.append('3FS-A188')
    b.append('103763232')
    c.append('南馆三层自习室')

    a.append('3FS-A189')
    b.append('103763233')
    c.append('南馆三层自习室')

    a.append('3FS-A190')
    b.append('103763234')
    c.append('南馆三层自习室')

    a.append('3FS-A191')
    b.append('103763235')
    c.append('南馆三层自习室')

    a.append('3FS-A192')
    b.append('103763236')
    c.append('南馆三层自习室')

    a.append('3FS-A193')
    b.append('103763237')
    c.append('南馆三层自习室')

    a.append('3FS-A194')
    b.append('103763238')
    c.append('南馆三层自习室')

    a.append('3FS-A195')
    b.append('103763239')
    c.append('南馆三层自习室')

    a.append('3FS-A196')
    b.append('103763240')
    c.append('南馆三层自习室')

    a.append('3FS-A197')
    b.append('103763241')
    c.append('南馆三层自习室')

    a.append('3FS-A198')
    b.append('103763242')
    c.append('南馆三层自习室')

    a.append('3FS-A199')
    b.append('103763243')
    c.append('南馆三层自习室')

    a.append('3FS-A200')
    b.append('103763244')
    c.append('南馆三层自习室')

    a.append('3FS-A201')
    b.append('103763245')
    c.append('南馆三层自习室')

    a.append('3FS-A202')
    b.append('103763246')
    c.append('南馆三层自习室')

    a.append('3FS-A203')
    b.append('103763247')
    c.append('南馆三层自习室')

    a.append('3FS-A204')
    b.append('103763248')
    c.append('南馆三层自习室')

    a.append('3FS-A205')
    b.append('103763249')
    c.append('南馆三层自习室')

    a.append('3FS-A206')
    b.append('103763250')
    c.append('南馆三层自习室')

    a.append('3FS-A207')
    b.append('103763251')
    c.append('南馆三层自习室')

    a.append('3FS-A208')
    b.append('103763252')
    c.append('南馆三层自习室')

    a.append('3FS-A209')
    b.append('103763253')
    c.append('南馆三层自习室')

    a.append('3FS-A210')
    b.append('103763254')
    c.append('南馆三层自习室')

    a.append('3FS-A211')
    b.append('103763255')
    c.append('南馆三层自习室')

    a.append('3FS-A212')
    b.append('103763256')
    c.append('南馆三层自习室')

    a.append('3FS-A213')
    b.append('103763257')
    c.append('南馆三层自习室')

    a.append('3FS-A214')
    b.append('103763258')
    c.append('南馆三层自习室')

    a.append('3FS-A215')
    b.append('103763259')
    c.append('南馆三层自习室')

    a.append('3FS-A216')
    b.append('103763260')
    c.append('南馆三层自习室')

    a.append('3FS-A217')
    b.append('103763261')
    c.append('南馆三层自习室')

    a.append('3FS-A218')
    b.append('103763262')
    c.append('南馆三层自习室')

    a.append('3FS-A219')
    b.append('103763263')
    c.append('南馆三层自习室')

    a.append('3FS-A220')
    b.append('103763264')
    c.append('南馆三层自习室')

    a.append('3FS-A221')
    b.append('103763265')
    c.append('南馆三层自习室')

    a.append('3FS-A222')
    b.append('103763266')
    c.append('南馆三层自习室')

    a.append('3FS-A223')
    b.append('103763267')
    c.append('南馆三层自习室')

    a.append('3FS-A224')
    b.append('103763268')
    c.append('南馆三层自习室')

    a.append('3FS-B001')
    b.append('103763269')
    c.append('南馆三层自习室')

    a.append('3FS-B002')
    b.append('103763270')
    c.append('南馆三层自习室')

    a.append('3FS-B003')
    b.append('103763271')
    c.append('南馆三层自习室')

    a.append('3FS-B004')
    b.append('103763272')
    c.append('南馆三层自习室')

    a.append('3FS-B005')
    b.append('103763273')
    c.append('南馆三层自习室')

    a.append('3FS-B006')
    b.append('103763274')
    c.append('南馆三层自习室')

    a.append('3FS-B007')
    b.append('103763275')
    c.append('南馆三层自习室')

    a.append('3FS-B008')
    b.append('103763276')
    c.append('南馆三层自习室')

    a.append('3FS-B009')
    b.append('103763277')
    c.append('南馆三层自习室')

    a.append('3FS-B010')
    b.append('103763278')
    c.append('南馆三层自习室')

    a.append('3FS-B011')
    b.append('103763279')
    c.append('南馆三层自习室')

    a.append('3FS-B012')
    b.append('103763280')
    c.append('南馆三层自习室')

    a.append('3FS-B013')
    b.append('103763281')
    c.append('南馆三层自习室')

    a.append('3FS-B014')
    b.append('103763282')
    c.append('南馆三层自习室')

    a.append('3FS-B015')
    b.append('103763283')
    c.append('南馆三层自习室')

    a.append('3FS-B016')
    b.append('103763284')
    c.append('南馆三层自习室')

    a.append('3FS-B017')
    b.append('103763285')
    c.append('南馆三层自习室')

    a.append('3FS-B018')
    b.append('103763286')
    c.append('南馆三层自习室')

    a.append('3FS-B019')
    b.append('103763287')
    c.append('南馆三层自习室')

    a.append('3FS-B020')
    b.append('103763288')
    c.append('南馆三层自习室')

    a.append('3FS-B021')
    b.append('103763289')
    c.append('南馆三层自习室')

    a.append('3FS-B022')
    b.append('103763290')
    c.append('南馆三层自习室')

    a.append('3FS-B023')
    b.append('103763291')
    c.append('南馆三层自习室')

    a.append('3FS-B024')
    b.append('103763292')
    c.append('南馆三层自习室')

    a.append('3FS-B025')
    b.append('103763293')
    c.append('南馆三层自习室')

    a.append('3FS-B026')
    b.append('103763294')
    c.append('南馆三层自习室')

    a.append('3FS-B027')
    b.append('103763295')
    c.append('南馆三层自习室')

    a.append('3FS-B028')
    b.append('103763296')
    c.append('南馆三层自习室')

    a.append('3FS-B029')
    b.append('103763297')
    c.append('南馆三层自习室')

    a.append('3FS-B030')
    b.append('103763298')
    c.append('南馆三层自习室')

    a.append('3FS-B031')
    b.append('103763299')
    c.append('南馆三层自习室')

    a.append('3FS-B032')
    b.append('103763300')
    c.append('南馆三层自习室')

    a.append('3FS-B033')
    b.append('103763301')
    c.append('南馆三层自习室')

    a.append('3FS-B034')
    b.append('103763302')
    c.append('南馆三层自习室')

    a.append('3FS-B035')
    b.append('103763303')
    c.append('南馆三层自习室')

    a.append('3FS-B036')
    b.append('103763304')
    c.append('南馆三层自习室')

    a.append('3FS-B037')
    b.append('103763305')
    c.append('南馆三层自习室')

    a.append('3FS-B038')
    b.append('103763306')
    c.append('南馆三层自习室')

    a.append('3FS-B039')
    b.append('103763307')
    c.append('南馆三层自习室')

    a.append('3FS-B040')
    b.append('103763308')
    c.append('南馆三层自习室')

    a.append('3FS-B041')
    b.append('103763309')
    c.append('南馆三层自习室')

    a.append('3FS-B042')
    b.append('103763310')
    c.append('南馆三层自习室')

    a.append('3FS-B043')
    b.append('103763311')
    c.append('南馆三层自习室')

    a.append('3FS-B044')
    b.append('103763312')
    c.append('南馆三层自习室')

    a.append('3FS-B045')
    b.append('103763313')
    c.append('南馆三层自习室')

    a.append('3FS-B046')
    b.append('103763314')
    c.append('南馆三层自习室')

    a.append('3FS-B047')
    b.append('103763315')
    c.append('南馆三层自习室')

    a.append('3FS-B048')
    b.append('103763316')
    c.append('南馆三层自习室')

    a.append('3FS-B049')
    b.append('103763317')
    c.append('南馆三层自习室')

    a.append('3FS-B050')
    b.append('103763318')
    c.append('南馆三层自习室')

    a.append('3FS-B051')
    b.append('103763319')
    c.append('南馆三层自习室')

    a.append('3FS-B052')
    b.append('103763320')
    c.append('南馆三层自习室')

    a.append('3FS-B053')
    b.append('103763321')
    c.append('南馆三层自习室')

    a.append('3FS-B054')
    b.append('103763322')
    c.append('南馆三层自习室')

    a.append('3FS-B055')
    b.append('103763323')
    c.append('南馆三层自习室')

    a.append('3FS-B056')
    b.append('103763324')
    c.append('南馆三层自习室')

    a.append('3FS-B057')
    b.append('103763325')
    c.append('南馆三层自习室')

    a.append('3FS-B058')
    b.append('103763326')
    c.append('南馆三层自习室')

    a.append('3FS-B059')
    b.append('103763327')
    c.append('南馆三层自习室')

    a.append('3FS-B060')
    b.append('103763328')
    c.append('南馆三层自习室')

    a.append('3FS-B061')
    b.append('103763329')
    c.append('南馆三层自习室')

    a.append('3FS-B062')
    b.append('103763330')
    c.append('南馆三层自习室')

    a.append('3FS-B063')
    b.append('103763331')
    c.append('南馆三层自习室')

    a.append('3FS-B064')
    b.append('103763332')
    c.append('南馆三层自习室')

    a.append('3FS-B065')
    b.append('103763333')
    c.append('南馆三层自习室')

    a.append('3FS-B066')
    b.append('103763334')
    c.append('南馆三层自习室')

    a.append('3FS-B067')
    b.append('103763335')
    c.append('南馆三层自习室')

    a.append('3FS-B068')
    b.append('103763336')
    c.append('南馆三层自习室')

    a.append('3FS-B069')
    b.append('103763337')
    c.append('南馆三层自习室')

    a.append('3FS-B070')
    b.append('103763338')
    c.append('南馆三层自习室')

    a.append('3FS-B071')
    b.append('103763339')
    c.append('南馆三层自习室')

    a.append('3FS-B072')
    b.append('103763340')
    c.append('南馆三层自习室')

    a.append('3FS-B073')
    b.append('103763341')
    c.append('南馆三层自习室')

    a.append('3FS-B074')
    b.append('103763342')
    c.append('南馆三层自习室')

    a.append('3FS-B075')
    b.append('103763343')
    c.append('南馆三层自习室')

    a.append('3FS-B076')
    b.append('103763344')
    c.append('南馆三层自习室')

    a.append('3FS-B077')
    b.append('103763345')
    c.append('南馆三层自习室')

    a.append('3FS-B078')
    b.append('103763346')
    c.append('南馆三层自习室')

    a.append('3FS-B079')
    b.append('103763347')
    c.append('南馆三层自习室')

    a.append('3FS-B080')
    b.append('103763348')
    c.append('南馆三层自习室')

    a.append('3FS-B081')
    b.append('103763349')
    c.append('南馆三层自习室')

    a.append('3FS-B082')
    b.append('103763350')
    c.append('南馆三层自习室')

    a.append('3FS-B083')
    b.append('103763351')
    c.append('南馆三层自习室')

    a.append('3FS-B084')
    b.append('103763352')
    c.append('南馆三层自习室')

    a.append('3FS-B085')
    b.append('103763353')
    c.append('南馆三层自习室')

    a.append('3FS-B086')
    b.append('103763354')
    c.append('南馆三层自习室')

    a.append('3FS-B087')
    b.append('103763355')
    c.append('南馆三层自习室')

    a.append('3FS-B088')
    b.append('103763356')
    c.append('南馆三层自习室')

    a.append('3FS-B089')
    b.append('103763357')
    c.append('南馆三层自习室')

    a.append('3FS-B090')
    b.append('103763358')
    c.append('南馆三层自习室')

    a.append('3FS-B091')
    b.append('103763359')
    c.append('南馆三层自习室')

    a.append('3FS-B092')
    b.append('103763360')
    c.append('南馆三层自习室')

    a.append('3FS-B093')
    b.append('103763361')
    c.append('南馆三层自习室')

    a.append('3FS-B094')
    b.append('103763362')
    c.append('南馆三层自习室')

    a.append('3FS-B095')
    b.append('103763363')
    c.append('南馆三层自习室')

    a.append('3FS-B096')
    b.append('103763364')
    c.append('南馆三层自习室')

    a.append('3FS-B097')
    b.append('103763365')
    c.append('南馆三层自习室')

    a.append('3FS-B098')
    b.append('103763366')
    c.append('南馆三层自习室')

    a.append('3FS-B099')
    b.append('103763367')
    c.append('南馆三层自习室')

    a.append('3FS-B100')
    b.append('103763368')
    c.append('南馆三层自习室')

    a.append('3FS-B101')
    b.append('103763369')
    c.append('南馆三层自习室')

    a.append('3FS-B102')
    b.append('103763370')
    c.append('南馆三层自习室')

    a.append('3FS-B103')
    b.append('103763371')
    c.append('南馆三层自习室')

    a.append('3FS-B104')
    b.append('103763372')
    c.append('南馆三层自习室')

    a.append('3FS-B105')
    b.append('103763373')
    c.append('南馆三层自习室')

    a.append('3FS-B106')
    b.append('103763374')
    c.append('南馆三层自习室')

    a.append('3FS-B107')
    b.append('103763375')
    c.append('南馆三层自习室')

    a.append('3FS-B108')
    b.append('103763376')
    c.append('南馆三层自习室')

    a.append('3FS-B109')
    b.append('103763377')
    c.append('南馆三层自习室')

    a.append('3FS-B110')
    b.append('103763378')
    c.append('南馆三层自习室')

    a.append('3FS-B111')
    b.append('103763379')
    c.append('南馆三层自习室')

    a.append('3FS-B112')
    b.append('103763380')
    c.append('南馆三层自习室')

    a.append('3FS-B113')
    b.append('103763381')
    c.append('南馆三层自习室')

    a.append('3FS-B114')
    b.append('103763382')
    c.append('南馆三层自习室')

    a.append('3FS-B115')
    b.append('103763383')
    c.append('南馆三层自习室')

    a.append('3FS-B116')
    b.append('103763384')
    c.append('南馆三层自习室')

    a.append('3FS-B117')
    b.append('103763385')
    c.append('南馆三层自习室')

    a.append('3FS-B118')
    b.append('103763386')
    c.append('南馆三层自习室')

    a.append('3FS-B119')
    b.append('103763387')
    c.append('南馆三层自习室')

    a.append('3FS-B120')
    b.append('103763388')
    c.append('南馆三层自习室')

    a.append('3FS-B121')
    b.append('103763389')
    c.append('南馆三层自习室')

    a.append('3FS-B122')
    b.append('103763390')
    c.append('南馆三层自习室')

    a.append('3FS-B123')
    b.append('103763391')
    c.append('南馆三层自习室')

    a.append('3FS-B124')
    b.append('103763392')
    c.append('南馆三层自习室')

    a.append('3FS-B125')
    b.append('103763393')
    c.append('南馆三层自习室')

    a.append('3FS-B126')
    b.append('103763394')
    c.append('南馆三层自习室')

    a.append('3FS-B127')
    b.append('103763395')
    c.append('南馆三层自习室')

    a.append('3FS-B128')
    b.append('103763396')
    c.append('南馆三层自习室')

    a.append('3FS-B129')
    b.append('103763397')
    c.append('南馆三层自习室')

    a.append('3FS-B130')
    b.append('103763398')
    c.append('南馆三层自习室')

    a.append('3FS-B131')
    b.append('103763399')
    c.append('南馆三层自习室')

    a.append('3FS-B132')
    b.append('103763400')
    c.append('南馆三层自习室')

    a.append('3FS-B133')
    b.append('103763401')
    c.append('南馆三层自习室')

    a.append('3FS-B134')
    b.append('103763402')
    c.append('南馆三层自习室')

    a.append('3FS-B135')
    b.append('103763403')
    c.append('南馆三层自习室')

    a.append('3FS-B136')
    b.append('103763404')
    c.append('南馆三层自习室')

    a.append('3FS-B137')
    b.append('103763405')
    c.append('南馆三层自习室')

    a.append('3FS-B138')
    b.append('103763406')
    c.append('南馆三层自习室')

    a.append('3FS-B139')
    b.append('103763407')
    c.append('南馆三层自习室')

    a.append('3FS-B140')
    b.append('103763408')
    c.append('南馆三层自习室')

    a.append('3FS-B141')
    b.append('103763409')
    c.append('南馆三层自习室')

    a.append('3FS-B142')
    b.append('103763410')
    c.append('南馆三层自习室')

    a.append('3FS-B143')
    b.append('103763411')
    c.append('南馆三层自习室')

    a.append('3FS-B144')
    b.append('103763412')
    c.append('南馆三层自习室')

    a.append('3FS-B145')
    b.append('103763413')
    c.append('南馆三层自习室')

    a.append('3FS-B146')
    b.append('103763414')
    c.append('南馆三层自习室')

    a.append('3FS-B147')
    b.append('103763415')
    c.append('南馆三层自习室')

    a.append('3FS-B148')
    b.append('103763416')
    c.append('南馆三层自习室')

    a.append('3FS-B149')
    b.append('103763417')
    c.append('南馆三层自习室')

    a.append('3FS-B150')
    b.append('103763418')
    c.append('南馆三层自习室')

    a.append('3FS-B151')
    b.append('103763419')
    c.append('南馆三层自习室')

    a.append('3FS-B152')
    b.append('103763420')
    c.append('南馆三层自习室')

    a.append('3FS-B153')
    b.append('103763421')
    c.append('南馆三层自习室')

    a.append('3FS-B154')
    b.append('103763422')
    c.append('南馆三层自习室')

    a.append('3FS-B155')
    b.append('103763423')
    c.append('南馆三层自习室')

    a.append('3FS-B156')
    b.append('103763424')
    c.append('南馆三层自习室')

    a.append('3FS-B157')
    b.append('103763425')
    c.append('南馆三层自习室')

    a.append('3FS-B158')
    b.append('103763426')
    c.append('南馆三层自习室')

    a.append('3FS-B159')
    b.append('103763427')
    c.append('南馆三层自习室')

    a.append('3FS-B160')
    b.append('103763428')
    c.append('南馆三层自习室')

    a.append('3FS-B161')
    b.append('103763429')
    c.append('南馆三层自习室')

    a.append('3FS-B163')
    b.append('103763431')
    c.append('南馆三层自习室')

    a.append('3FS-B164')
    b.append('103763432')
    c.append('南馆三层自习室')

    a.append('3FS-B165')
    b.append('103763433')
    c.append('南馆三层自习室')

    a.append('3FS-B166')
    b.append('103763434')
    c.append('南馆三层自习室')

    a.append('3FS-B167')
    b.append('103763435')
    c.append('南馆三层自习室')

    a.append('3FS-B168')
    b.append('103763436')
    c.append('南馆三层自习室')

    a.append('3FS-B169')
    b.append('103763437')
    c.append('南馆三层自习室')

    a.append('3FS-B170')
    b.append('103763438')
    c.append('南馆三层自习室')

    a.append('3FS-B171')
    b.append('103763439')
    c.append('南馆三层自习室')

    a.append('3FS-B172')
    b.append('103763440')
    c.append('南馆三层自习室')

    a.append('3FS-B173')
    b.append('103763441')
    c.append('南馆三层自习室')

    a.append('3FS-B174')
    b.append('103763442')
    c.append('南馆三层自习室')

    a.append('3FS-B175')
    b.append('103763443')
    c.append('南馆三层自习室')

    a.append('3FS-B176')
    b.append('103763444')
    c.append('南馆三层自习室')

    a.append('3FS-B177')
    b.append('103763445')
    c.append('南馆三层自习室')

    a.append('3FS-B178')
    b.append('103763446')
    c.append('南馆三层自习室')

    a.append('3FS-B179')
    b.append('103763447')
    c.append('南馆三层自习室')

    a.append('3FS-B180')
    b.append('103763448')
    c.append('南馆三层自习室')

    a.append('3FS-B181')
    b.append('103763449')
    c.append('南馆三层自习室')

    a.append('3FS-B182')
    b.append('103763450')
    c.append('南馆三层自习室')

    a.append('3FS-B183')
    b.append('103763451')
    c.append('南馆三层自习室')

    a.append('3FS-B184')
    b.append('103763452')
    c.append('南馆三层自习室')

    a.append('3FS-B185')
    b.append('103763453')
    c.append('南馆三层自习室')

    a.append('3FS-B186')
    b.append('103763454')
    c.append('南馆三层自习室')

    a.append('3FS-B187')
    b.append('103763455')
    c.append('南馆三层自习室')

    a.append('3FS-B188')
    b.append('103763456')
    c.append('南馆三层自习室')

    a.append('3FS-B189')
    b.append('103763457')
    c.append('南馆三层自习室')

    a.append('3FS-B190')
    b.append('103763458')
    c.append('南馆三层自习室')

    a.append('3FS-B191')
    b.append('103763459')
    c.append('南馆三层自习室')

    a.append('3FS-B192')
    b.append('103763460')
    c.append('南馆三层自习室')

    a.append('3FS-B193')
    b.append('103763461')
    c.append('南馆三层自习室')

    a.append('3FS-B194')
    b.append('103763462')
    c.append('南馆三层自习室')

    a.append('3FS-B195')
    b.append('103763463')
    c.append('南馆三层自习室')

    a.append('3FS-B196')
    b.append('103763464')
    c.append('南馆三层自习室')

    a.append('3FS-B197')
    b.append('103763465')
    c.append('南馆三层自习室')

    a.append('3FS-B198')
    b.append('103763466')
    c.append('南馆三层自习室')

    a.append('3FS-B199')
    b.append('103763467')
    c.append('南馆三层自习室')

    a.append('3FS-B200')
    b.append('103763468')
    c.append('南馆三层自习室')

    a.append('3FS-B201')
    b.append('103763469')
    c.append('南馆三层自习室')

    a.append('3FS-B202')
    b.append('103763470')
    c.append('南馆三层自习室')

    a.append('3FS-B203')
    b.append('103763471')
    c.append('南馆三层自习室')

    a.append('3FS-B204')
    b.append('103763472')
    c.append('南馆三层自习室')

    a.append('3FS-B205')
    b.append('103763473')
    c.append('南馆三层自习室')

    a.append('3FS-B206')
    b.append('103763474')
    c.append('南馆三层自习室')

    a.append('3FS-B207')
    b.append('103763475')
    c.append('南馆三层自习室')

    a.append('3FS-B208')
    b.append('103763476')
    c.append('南馆三层自习室')

    a.append('3FS-B209')
    b.append('103763477')
    c.append('南馆三层自习室')

    a.append('3FS-B210')
    b.append('103763478')
    c.append('南馆三层自习室')

    a.append('3FS-B211')
    b.append('103763479')
    c.append('南馆三层自习室')

    a.append('3FS-B212')
    b.append('103763480')
    c.append('南馆三层自习室')

    a.append('3FS-B213')
    b.append('103763481')
    c.append('南馆三层自习室')

    a.append('3FS-B214')
    b.append('103763482')
    c.append('南馆三层自习室')

    a.append('3FS-B215')
    b.append('103763483')
    c.append('南馆三层自习室')

    a.append('3FS-B216')
    b.append('103763484')
    c.append('南馆三层自习室')

    a.append('3FS-B217')
    b.append('103763485')
    c.append('南馆三层自习室')

    a.append('3FS-B218')
    b.append('103763486')
    c.append('南馆三层自习室')

    a.append('3FS-B219')
    b.append('103763487')
    c.append('南馆三层自习室')

    a.append('3FS-B220')
    b.append('103763488')
    c.append('南馆三层自习室')

    a.append('3FS-B221')
    b.append('103763489')
    c.append('南馆三层自习室')

    a.append('3FS-B222')
    b.append('103763490')
    c.append('南馆三层自习室')

    a.append('3FS-B223')
    b.append('103763491')
    c.append('南馆三层自习室')

    a.append('3FS-B224')
    b.append('103763492')
    c.append('南馆三层自习室')

    a.append('3FS-B225')
    b.append('103763493')
    c.append('南馆三层自习室')

    a.append('3FS-B226')
    b.append('103763494')
    c.append('南馆三层自习室')

    a.append('3FS-B227')
    b.append('103763495')
    c.append('南馆三层自习室')

    a.append('3FS-B228')
    b.append('103763496')
    c.append('南馆三层自习室')

    a.append('3FS-B229')
    b.append('103763497')
    c.append('南馆三层自习室')

    a.append('3FS-B230')
    b.append('103763498')
    c.append('南馆三层自习室')

    a.append('3FS-B231')
    b.append('103763499')
    c.append('南馆三层自习室')

    a.append('3FS-B232')
    b.append('103763500')
    c.append('南馆三层自习室')

    a.append('3FS-B233')
    b.append('103763501')
    c.append('南馆三层自习室')

    a.append('3FS-B234')
    b.append('103763502')
    c.append('南馆三层自习室')

    a.append('3FS-B235')
    b.append('103763503')
    c.append('南馆三层自习室')

    a.append('3FS-B236')
    b.append('103763504')
    c.append('南馆三层自习室')

    a.append('3FS-B237')
    b.append('103763505')
    c.append('南馆三层自习室')

    a.append('3FS-B238')
    b.append('103763506')
    c.append('南馆三层自习室')

    a.append('3FS-B239')
    b.append('103763507')
    c.append('南馆三层自习室')

    a.append('3FS-B240')
    b.append('103763508')
    c.append('南馆三层自习室')

    a.append('3FS-B241')
    b.append('103763509')
    c.append('南馆三层自习室')

    a.append('3FS-B242')
    b.append('103763510')
    c.append('南馆三层自习室')

    a.append('3FS-B243')
    b.append('103763511')
    c.append('南馆三层自习室')

    a.append('3FS-B244')
    b.append('103763512')
    c.append('南馆三层自习室')

    a.append('3FS-B245')
    b.append('103763513')
    c.append('南馆三层自习室')

    a.append('3FS-B246')
    b.append('103763514')
    c.append('南馆三层自习室')

    a.append('3FS-B247')
    b.append('103763515')
    c.append('南馆三层自习室')

    a.append('3FS-B248')
    b.append('103763516')
    c.append('南馆三层自习室')

    a.append('3FS-B249')
    b.append('103763517')
    c.append('南馆三层自习室')

    a.append('3FS-B250')
    b.append('103763518')
    c.append('南馆三层自习室')

    a.append('3FS-B251')
    b.append('103763519')
    c.append('南馆三层自习室')

    a.append('3FS-B252')
    b.append('103763520')
    c.append('南馆三层自习室')

    a.append('3FS-B253')
    b.append('103763521')
    c.append('南馆三层自习室')

    a.append('3FS-B254')
    b.append('103763522')
    c.append('南馆三层自习室')

    a.append('3FS-B255')
    b.append('103763523')
    c.append('南馆三层自习室')

    a.append('3FS-B256')
    b.append('103763524')
    c.append('南馆三层自习室')

    a.append('3FS-B257')
    b.append('103763525')
    c.append('南馆三层自习室')

    a.append('3FS-B258')
    b.append('103763526')
    c.append('南馆三层自习室')

    a.append('3FS-B259')
    b.append('103763527')
    c.append('南馆三层自习室')

    a.append('3FS-B260')
    b.append('103763528')
    c.append('南馆三层自习室')

    a.append('3FS-B261')
    b.append('103763529')
    c.append('南馆三层自习室')

    a.append('3FS-B262')
    b.append('103763530')
    c.append('南馆三层自习室')

    a.append('3FS-B263')
    b.append('103763531')
    c.append('南馆三层自习室')

    a.append('3FS-B264')
    b.append('103763532')
    c.append('南馆三层自习室')

    a.append('3FS-B265')
    b.append('103763533')
    c.append('南馆三层自习室')

    a.append('3FS-B266')
    b.append('103763534')
    c.append('南馆三层自习室')

    a.append('3FS-B267')
    b.append('103763535')
    c.append('南馆三层自习室')

    a.append('3FS-B268')
    b.append('103763536')
    c.append('南馆三层自习室')

    a.append('3FS-B269')
    b.append('103763537')
    c.append('南馆三层自习室')

    a.append('3FS-B270')
    b.append('103763538')
    c.append('南馆三层自习室')

    a.append('3FS-B271')
    b.append('103763539')
    c.append('南馆三层自习室')

    a.append('3FS-B272')
    b.append('103763540')
    c.append('南馆三层自习室')

    a.append('3FS-B273')
    b.append('103763541')
    c.append('南馆三层自习室')

    a.append('3FS-B274')
    b.append('103763542')
    c.append('南馆三层自习室')

    a.append('3FS-B275')
    b.append('103763543')
    c.append('南馆三层自习室')

    a.append('3FS-B276')
    b.append('103763544')
    c.append('南馆三层自习室')

    a.append('3FS-B277')
    b.append('103763545')
    c.append('南馆三层自习室')

    a.append('3FS-B278')
    b.append('103763546')
    c.append('南馆三层自习室')

    a.append('3FS-B279')
    b.append('103763547')
    c.append('南馆三层自习室')

    a.append('3FS-B280')
    b.append('103763548')
    c.append('南馆三层自习室')

    a.append('3FS-B281')
    b.append('103763549')
    c.append('南馆三层自习室')

    a.append('3FS-B282')
    b.append('103763550')
    c.append('南馆三层自习室')

    a.append('3FS-B283')
    b.append('103763551')
    c.append('南馆三层自习室')

    a.append('3FS-B284')
    b.append('103763552')
    c.append('南馆三层自习室')

    a.append('3FS-B285')
    b.append('103763553')
    c.append('南馆三层自习室')

    a.append('3FS-B286')
    b.append('103763554')
    c.append('南馆三层自习室')

    a.append('3FS-B287')
    b.append('103763555')
    c.append('南馆三层自习室')

    a.append('3FS-B288')
    b.append('103763556')
    c.append('南馆三层自习室')

    a.append('3FS-B289')
    b.append('103763557')
    c.append('南馆三层自习室')

    a.append('3FS-B290')
    b.append('103763558')
    c.append('南馆三层自习室')

    a.append('3FS-B291')
    b.append('103763559')
    c.append('南馆三层自习室')

    a.append('3FS-B292')
    b.append('103763560')
    c.append('南馆三层自习室')

    a.append('3FS-B293')
    b.append('103763561')
    c.append('南馆三层自习室')

    a.append('3FS-B294')
    b.append('103763562')
    c.append('南馆三层自习室')

    a.append('3FS-B295')
    b.append('103763563')
    c.append('南馆三层自习室')

    a.append('3FS-B296')
    b.append('103763564')
    c.append('南馆三层自习室')

    a.append('3FS-B298')
    b.append('103763566')
    c.append('南馆三层自习室')

    a.append('3FS-B299')
    b.append('103763567')
    c.append('南馆三层自习室')

    a.append('3FS-B300')
    b.append('103763568')
    c.append('南馆三层自习室')

    a.append('3FS-B301')
    b.append('103763569')
    c.append('南馆三层自习室')

    a.append('3FS-B302')
    b.append('103763570')
    c.append('南馆三层自习室')

    a.append('3FS-B303')
    b.append('103763571')
    c.append('南馆三层自习室')

    a.append('3FS-B304')
    b.append('103763572')
    c.append('南馆三层自习室')

    a.append('3FS-B305')
    b.append('103763573')
    c.append('南馆三层自习室')

    a.append('3FS-B306')
    b.append('103763574')
    c.append('南馆三层自习室')

    a.append('3FS-B307')
    b.append('103763575')
    c.append('南馆三层自习室')

    a.append('3FS-B308')
    b.append('103763576')
    c.append('南馆三层自习室')

    a.append('3FS-B309')
    b.append('103763577')
    c.append('南馆三层自习室')

    a.append('3FS-B310')
    b.append('103763578')
    c.append('南馆三层自习室')

    a.append('3FS-B311')
    b.append('103763579')
    c.append('南馆三层自习室')

    a.append('3FS-B312')
    b.append('103763580')
    c.append('南馆三层自习室')

    a.append('3FS-B313')
    b.append('103763581')
    c.append('南馆三层自习室')

    a.append('3FS-B314')
    b.append('103763582')
    c.append('南馆三层自习室')

    a.append('3FS-B315')
    b.append('103763583')
    c.append('南馆三层自习室')

    a.append('3FS-B316')
    b.append('103763584')
    c.append('南馆三层自习室')

    a.append('3FS-B317')
    b.append('104456010')
    c.append('南馆三层自习室')

    a.append('3FS-B318')
    b.append('104456011')
    c.append('南馆三层自习室')

    a.append('3FS-B319')
    b.append('104456012')
    c.append('南馆三层自习室')

    a.append('3FS-B320')
    b.append('104456013')
    c.append('南馆三层自习室')

    a.append('4FS-A001')
    b.append('103763585')
    c.append('南馆四层自习室')

    a.append('4FS-A002')
    b.append('103763586')
    c.append('南馆四层自习室')

    a.append('4FS-A003')
    b.append('103763587')
    c.append('南馆四层自习室')

    a.append('4FS-A004')
    b.append('103763588')
    c.append('南馆四层自习室')

    a.append('4FS-A005')
    b.append('103763589')
    c.append('南馆四层自习室')

    a.append('4FS-A006')
    b.append('103763590')
    c.append('南馆四层自习室')

    a.append('4FS-A007')
    b.append('103763591')
    c.append('南馆四层自习室')

    a.append('4FS-A008')
    b.append('103763592')
    c.append('南馆四层自习室')

    a.append('4FS-A009')
    b.append('103763593')
    c.append('南馆四层自习室')

    a.append('4FS-A010')
    b.append('103763594')
    c.append('南馆四层自习室')

    a.append('4FS-A011')
    b.append('103763595')
    c.append('南馆四层自习室')

    a.append('4FS-A012')
    b.append('103763596')
    c.append('南馆四层自习室')

    a.append('4FS-A013')
    b.append('103763597')
    c.append('南馆四层自习室')

    a.append('4FS-A014')
    b.append('103763598')
    c.append('南馆四层自习室')

    a.append('4FS-A015')
    b.append('103763599')
    c.append('南馆四层自习室')

    a.append('4FS-A016')
    b.append('103763600')
    c.append('南馆四层自习室')

    a.append('4FS-A017')
    b.append('103763601')
    c.append('南馆四层自习室')

    a.append('4FS-A018')
    b.append('103763602')
    c.append('南馆四层自习室')

    a.append('4FS-A019')
    b.append('103763603')
    c.append('南馆四层自习室')

    a.append('4FS-A020')
    b.append('103763604')
    c.append('南馆四层自习室')

    a.append('4FS-A021')
    b.append('103763605')
    c.append('南馆四层自习室')

    a.append('4FS-A022')
    b.append('103763606')
    c.append('南馆四层自习室')

    a.append('4FS-A023')
    b.append('103763607')
    c.append('南馆四层自习室')

    a.append('4FS-A024')
    b.append('103763608')
    c.append('南馆四层自习室')

    a.append('4FS-A025')
    b.append('103763609')
    c.append('南馆四层自习室')

    a.append('4FS-A026')
    b.append('103763610')
    c.append('南馆四层自习室')

    a.append('4FS-A027')
    b.append('103763611')
    c.append('南馆四层自习室')

    a.append('4FS-A028')
    b.append('103763612')
    c.append('南馆四层自习室')

    a.append('4FS-A029')
    b.append('103763613')
    c.append('南馆四层自习室')

    a.append('4FS-A030')
    b.append('103763614')
    c.append('南馆四层自习室')

    a.append('4FS-A031')
    b.append('103763615')
    c.append('南馆四层自习室')

    a.append('4FS-A032')
    b.append('103763616')
    c.append('南馆四层自习室')

    a.append('4FS-A033')
    b.append('103763617')
    c.append('南馆四层自习室')

    a.append('4FS-A034')
    b.append('103763618')
    c.append('南馆四层自习室')

    a.append('4FS-A035')
    b.append('103763619')
    c.append('南馆四层自习室')

    a.append('4FS-A036')
    b.append('103763620')
    c.append('南馆四层自习室')

    a.append('4FS-A037')
    b.append('103763621')
    c.append('南馆四层自习室')

    a.append('4FS-A038')
    b.append('103763622')
    c.append('南馆四层自习室')

    a.append('4FS-A039')
    b.append('103763623')
    c.append('南馆四层自习室')

    a.append('4FS-A040')
    b.append('103763624')
    c.append('南馆四层自习室')

    a.append('4FS-A041')
    b.append('103763625')
    c.append('南馆四层自习室')

    a.append('4FS-A042')
    b.append('103763626')
    c.append('南馆四层自习室')

    a.append('4FS-A043')
    b.append('103763627')
    c.append('南馆四层自习室')

    a.append('4FS-A044')
    b.append('103763628')
    c.append('南馆四层自习室')

    a.append('4FS-A045')
    b.append('103763629')
    c.append('南馆四层自习室')

    a.append('4FS-A046')
    b.append('103763630')
    c.append('南馆四层自习室')

    a.append('4FS-A047')
    b.append('103763631')
    c.append('南馆四层自习室')

    a.append('4FS-A048')
    b.append('103763632')
    c.append('南馆四层自习室')

    a.append('4FS-A049')
    b.append('103763633')
    c.append('南馆四层自习室')

    a.append('4FS-A050')
    b.append('103763634')
    c.append('南馆四层自习室')

    a.append('4FS-A051')
    b.append('103763635')
    c.append('南馆四层自习室')

    a.append('4FS-A052')
    b.append('103763636')
    c.append('南馆四层自习室')

    a.append('4FS-A053')
    b.append('103763637')
    c.append('南馆四层自习室')

    a.append('4FS-A054')
    b.append('103763638')
    c.append('南馆四层自习室')

    a.append('4FS-A055')
    b.append('103763639')
    c.append('南馆四层自习室')

    a.append('4FS-A056')
    b.append('103763640')
    c.append('南馆四层自习室')

    a.append('4FS-A057')
    b.append('103763641')
    c.append('南馆四层自习室')

    a.append('4FS-A058')
    b.append('103763642')
    c.append('南馆四层自习室')

    a.append('4FS-A059')
    b.append('103763643')
    c.append('南馆四层自习室')

    a.append('4FS-A060')
    b.append('103763644')
    c.append('南馆四层自习室')

    a.append('4FS-A061')
    b.append('103763645')
    c.append('南馆四层自习室')

    a.append('4FS-A062')
    b.append('103763646')
    c.append('南馆四层自习室')

    a.append('4FS-A063')
    b.append('103763647')
    c.append('南馆四层自习室')

    a.append('4FS-A064')
    b.append('103763648')
    c.append('南馆四层自习室')

    a.append('4FS-A065')
    b.append('103763649')
    c.append('南馆四层自习室')

    a.append('4FS-A066')
    b.append('103763650')
    c.append('南馆四层自习室')

    a.append('4FS-A067')
    b.append('103763651')
    c.append('南馆四层自习室')

    a.append('4FS-A068')
    b.append('103763652')
    c.append('南馆四层自习室')

    a.append('4FS-A069')
    b.append('103763653')
    c.append('南馆四层自习室')

    a.append('4FS-A070')
    b.append('103763654')
    c.append('南馆四层自习室')

    a.append('4FS-A071')
    b.append('103763655')
    c.append('南馆四层自习室')

    a.append('4FS-A072')
    b.append('103763656')
    c.append('南馆四层自习室')

    a.append('4FS-A073')
    b.append('103763657')
    c.append('南馆四层自习室')

    a.append('4FS-A074')
    b.append('103763658')
    c.append('南馆四层自习室')

    a.append('4FS-A075')
    b.append('103763659')
    c.append('南馆四层自习室')

    a.append('4FS-A076')
    b.append('103763660')
    c.append('南馆四层自习室')

    a.append('4FS-A077')
    b.append('103763661')
    c.append('南馆四层自习室')

    a.append('4FS-A078')
    b.append('103763662')
    c.append('南馆四层自习室')

    a.append('4FS-A079')
    b.append('103763663')
    c.append('南馆四层自习室')

    a.append('4FS-A080')
    b.append('103763664')
    c.append('南馆四层自习室')

    a.append('4FS-A081')
    b.append('103763665')
    c.append('南馆四层自习室')

    a.append('4FS-A082')
    b.append('103763666')
    c.append('南馆四层自习室')

    a.append('4FS-A083')
    b.append('103763667')
    c.append('南馆四层自习室')

    a.append('4FS-A084')
    b.append('103763668')
    c.append('南馆四层自习室')

    a.append('4FS-A085')
    b.append('103763669')
    c.append('南馆四层自习室')

    a.append('4FS-A086')
    b.append('103763670')
    c.append('南馆四层自习室')

    a.append('4FS-A087')
    b.append('103763671')
    c.append('南馆四层自习室')

    a.append('4FS-A088')
    b.append('103763672')
    c.append('南馆四层自习室')

    a.append('4FS-A089')
    b.append('103763673')
    c.append('南馆四层自习室')

    a.append('4FS-A090')
    b.append('103763674')
    c.append('南馆四层自习室')

    a.append('4FS-A091')
    b.append('103763675')
    c.append('南馆四层自习室')

    a.append('4FS-A092')
    b.append('103763676')
    c.append('南馆四层自习室')

    a.append('4FS-A093')
    b.append('103763677')
    c.append('南馆四层自习室')

    a.append('4FS-A094')
    b.append('103763678')
    c.append('南馆四层自习室')

    a.append('4FS-A095')
    b.append('103763679')
    c.append('南馆四层自习室')

    a.append('4FS-A096')
    b.append('103763680')
    c.append('南馆四层自习室')

    a.append('4FS-A097')
    b.append('103763681')
    c.append('南馆四层自习室')

    a.append('4FS-A098')
    b.append('103763682')
    c.append('南馆四层自习室')

    a.append('4FS-A099')
    b.append('103763683')
    c.append('南馆四层自习室')

    a.append('4FS-A100')
    b.append('103763684')
    c.append('南馆四层自习室')

    a.append('4FS-A101')
    b.append('103763685')
    c.append('南馆四层自习室')

    a.append('4FS-A102')
    b.append('103763686')
    c.append('南馆四层自习室')

    a.append('4FS-A103')
    b.append('103763687')
    c.append('南馆四层自习室')

    a.append('4FS-A104')
    b.append('103763688')
    c.append('南馆四层自习室')

    a.append('4FS-A105')
    b.append('103763689')
    c.append('南馆四层自习室')

    a.append('4FS-A106')
    b.append('103763690')
    c.append('南馆四层自习室')

    a.append('4FS-A107')
    b.append('103763691')
    c.append('南馆四层自习室')

    a.append('4FS-A108')
    b.append('103763692')
    c.append('南馆四层自习室')

    a.append('4FS-A109')
    b.append('103763693')
    c.append('南馆四层自习室')

    a.append('4FS-A110')
    b.append('103763694')
    c.append('南馆四层自习室')

    a.append('4FS-A111')
    b.append('103763695')
    c.append('南馆四层自习室')

    a.append('4FS-A112')
    b.append('103763696')
    c.append('南馆四层自习室')

    a.append('4FS-A113')
    b.append('103763697')
    c.append('南馆四层自习室')

    a.append('4FS-A114')
    b.append('103763698')
    c.append('南馆四层自习室')

    a.append('4FS-A115')
    b.append('103763699')
    c.append('南馆四层自习室')

    a.append('4FS-A116')
    b.append('103763700')
    c.append('南馆四层自习室')

    a.append('4FS-A117')
    b.append('103763701')
    c.append('南馆四层自习室')

    a.append('4FS-A118')
    b.append('103763702')
    c.append('南馆四层自习室')

    a.append('4FS-A119')
    b.append('103763703')
    c.append('南馆四层自习室')

    a.append('4FS-A120')
    b.append('103763704')
    c.append('南馆四层自习室')

    a.append('4FS-A121')
    b.append('103763705')
    c.append('南馆四层自习室')

    a.append('4FS-A122')
    b.append('103763706')
    c.append('南馆四层自习室')

    a.append('4FS-A123')
    b.append('103763707')
    c.append('南馆四层自习室')

    a.append('4FS-A124')
    b.append('103763708')
    c.append('南馆四层自习室')

    a.append('4FS-A125')
    b.append('103763709')
    c.append('南馆四层自习室')

    a.append('4FS-A126')
    b.append('103763710')
    c.append('南馆四层自习室')

    a.append('4FS-A127')
    b.append('103763711')
    c.append('南馆四层自习室')

    a.append('4FS-A128')
    b.append('103763712')
    c.append('南馆四层自习室')

    a.append('4FS-A129')
    b.append('103763713')
    c.append('南馆四层自习室')

    a.append('4FS-A130')
    b.append('103763714')
    c.append('南馆四层自习室')

    a.append('4FS-A131')
    b.append('103763715')
    c.append('南馆四层自习室')

    a.append('4FS-A132')
    b.append('103763716')
    c.append('南馆四层自习室')

    a.append('4FS-A133')
    b.append('103763717')
    c.append('南馆四层自习室')

    a.append('4FS-A134')
    b.append('103763718')
    c.append('南馆四层自习室')

    a.append('4FS-A135')
    b.append('103763719')
    c.append('南馆四层自习室')

    a.append('4FS-A136')
    b.append('103763720')
    c.append('南馆四层自习室')

    a.append('4FS-A137')
    b.append('103763721')
    c.append('南馆四层自习室')

    a.append('4FS-A138')
    b.append('103763722')
    c.append('南馆四层自习室')

    a.append('4FS-A139')
    b.append('103763723')
    c.append('南馆四层自习室')

    a.append('4FS-A140')
    b.append('103763724')
    c.append('南馆四层自习室')

    a.append('4FS-A141')
    b.append('103763725')
    c.append('南馆四层自习室')

    a.append('4FS-A142')
    b.append('103763726')
    c.append('南馆四层自习室')

    a.append('4FS-A143')
    b.append('103763727')
    c.append('南馆四层自习室')

    a.append('4FS-A144')
    b.append('103763728')
    c.append('南馆四层自习室')

    a.append('4FS-A145')
    b.append('103763729')
    c.append('南馆四层自习室')

    a.append('4FS-A146')
    b.append('103763730')
    c.append('南馆四层自习室')

    a.append('4FS-A147')
    b.append('103763731')
    c.append('南馆四层自习室')

    a.append('4FS-A148')
    b.append('103763732')
    c.append('南馆四层自习室')

    a.append('4FS-A149')
    b.append('103763733')
    c.append('南馆四层自习室')

    a.append('4FS-A150')
    b.append('103763734')
    c.append('南馆四层自习室')

    a.append('4FS-A151')
    b.append('103763735')
    c.append('南馆四层自习室')

    a.append('4FS-A152')
    b.append('103763736')
    c.append('南馆四层自习室')

    a.append('4FS-A153')
    b.append('103763737')
    c.append('南馆四层自习室')

    a.append('4FS-A154')
    b.append('103763738')
    c.append('南馆四层自习室')

    a.append('4FS-A155')
    b.append('103763739')
    c.append('南馆四层自习室')

    a.append('4FS-A156')
    b.append('103763740')
    c.append('南馆四层自习室')

    a.append('4FS-A157')
    b.append('103763741')
    c.append('南馆四层自习室')

    a.append('4FS-A158')
    b.append('103763742')
    c.append('南馆四层自习室')

    a.append('4FS-A159')
    b.append('103763743')
    c.append('南馆四层自习室')

    a.append('4FS-A160')
    b.append('103763744')
    c.append('南馆四层自习室')

    a.append('4FS-A161')
    b.append('103763745')
    c.append('南馆四层自习室')

    a.append('4FS-A162')
    b.append('103763746')
    c.append('南馆四层自习室')

    a.append('4FS-A163')
    b.append('103763747')
    c.append('南馆四层自习室')

    a.append('4FS-A164')
    b.append('103763748')
    c.append('南馆四层自习室')

    a.append('4FS-A165')
    b.append('103763749')
    c.append('南馆四层自习室')

    a.append('4FS-A166')
    b.append('103763750')
    c.append('南馆四层自习室')

    a.append('4FS-A167')
    b.append('103763751')
    c.append('南馆四层自习室')

    a.append('4FS-A168')
    b.append('103763752')
    c.append('南馆四层自习室')

    a.append('4FS-A169')
    b.append('103763753')
    c.append('南馆四层自习室')

    a.append('4FS-A170')
    b.append('103763754')
    c.append('南馆四层自习室')

    a.append('4FS-A171')
    b.append('103763755')
    c.append('南馆四层自习室')

    a.append('4FS-A172')
    b.append('103763756')
    c.append('南馆四层自习室')

    a.append('4FS-B001')
    b.append('103763757')
    c.append('南馆四层自习室')

    a.append('4FS-B002')
    b.append('103763758')
    c.append('南馆四层自习室')

    a.append('4FS-B003')
    b.append('103763759')
    c.append('南馆四层自习室')

    a.append('4FS-B004')
    b.append('103763760')
    c.append('南馆四层自习室')

    a.append('4FS-B005')
    b.append('103763761')
    c.append('南馆四层自习室')

    a.append('4FS-B006')
    b.append('103763762')
    c.append('南馆四层自习室')

    a.append('4FS-B007')
    b.append('103763763')
    c.append('南馆四层自习室')

    a.append('4FS-B008')
    b.append('103763764')
    c.append('南馆四层自习室')

    a.append('4FS-B009')
    b.append('103763765')
    c.append('南馆四层自习室')

    a.append('4FS-B010')
    b.append('103763766')
    c.append('南馆四层自习室')

    a.append('4FS-B011')
    b.append('103763767')
    c.append('南馆四层自习室')

    a.append('4FS-B012')
    b.append('103763768')
    c.append('南馆四层自习室')

    a.append('4FS-B013')
    b.append('103763769')
    c.append('南馆四层自习室')

    a.append('4FS-B014')
    b.append('103763770')
    c.append('南馆四层自习室')

    a.append('4FS-B015')
    b.append('103763771')
    c.append('南馆四层自习室')

    a.append('4FS-B016')
    b.append('103763772')
    c.append('南馆四层自习室')

    a.append('4FS-B017')
    b.append('103763773')
    c.append('南馆四层自习室')

    a.append('4FS-B018')
    b.append('103763774')
    c.append('南馆四层自习室')

    a.append('4FS-B019')
    b.append('103763775')
    c.append('南馆四层自习室')

    a.append('4FS-B020')
    b.append('103763776')
    c.append('南馆四层自习室')

    a.append('4FS-B021')
    b.append('103763777')
    c.append('南馆四层自习室')

    a.append('4FS-B022')
    b.append('103763778')
    c.append('南馆四层自习室')

    a.append('4FS-B023')
    b.append('103763779')
    c.append('南馆四层自习室')

    a.append('4FS-B024')
    b.append('103763780')
    c.append('南馆四层自习室')

    a.append('4FS-B025')
    b.append('103763781')
    c.append('南馆四层自习室')

    a.append('4FS-B026')
    b.append('103763782')
    c.append('南馆四层自习室')

    a.append('4FS-B027')
    b.append('103763783')
    c.append('南馆四层自习室')

    a.append('4FS-B028')
    b.append('103763784')
    c.append('南馆四层自习室')

    a.append('4FS-B029')
    b.append('103763785')
    c.append('南馆四层自习室')

    a.append('4FS-B030')
    b.append('103763786')
    c.append('南馆四层自习室')

    a.append('4FS-B031')
    b.append('103763787')
    c.append('南馆四层自习室')

    a.append('4FS-B032')
    b.append('103763788')
    c.append('南馆四层自习室')

    a.append('4FS-B033')
    b.append('103763789')
    c.append('南馆四层自习室')

    a.append('4FS-B034')
    b.append('103763790')
    c.append('南馆四层自习室')

    a.append('4FS-B035')
    b.append('103763791')
    c.append('南馆四层自习室')

    a.append('4FS-B036')
    b.append('103763792')
    c.append('南馆四层自习室')

    a.append('4FS-B037')
    b.append('103763793')
    c.append('南馆四层自习室')

    a.append('4FS-B038')
    b.append('103763794')
    c.append('南馆四层自习室')

    a.append('4FS-B039')
    b.append('103763795')
    c.append('南馆四层自习室')

    a.append('4FS-B040')
    b.append('103763796')
    c.append('南馆四层自习室')

    a.append('4FS-B041')
    b.append('103763797')
    c.append('南馆四层自习室')

    a.append('4FS-B042')
    b.append('103763798')
    c.append('南馆四层自习室')

    a.append('4FS-B043')
    b.append('103763799')
    c.append('南馆四层自习室')

    a.append('4FS-B044')
    b.append('103763800')
    c.append('南馆四层自习室')

    a.append('4FS-B045')
    b.append('103763801')
    c.append('南馆四层自习室')

    a.append('4FS-B046')
    b.append('103763802')
    c.append('南馆四层自习室')

    a.append('4FS-B047')
    b.append('103763803')
    c.append('南馆四层自习室')

    a.append('4FS-B048')
    b.append('103763804')
    c.append('南馆四层自习室')

    a.append('4FS-B049')
    b.append('103763805')
    c.append('南馆四层自习室')

    a.append('4FS-B050')
    b.append('103763806')
    c.append('南馆四层自习室')

    a.append('4FS-B051')
    b.append('103763807')
    c.append('南馆四层自习室')

    a.append('4FS-B052')
    b.append('103763808')
    c.append('南馆四层自习室')

    a.append('4FS-B053')
    b.append('103763809')
    c.append('南馆四层自习室')

    a.append('4FS-B054')
    b.append('103763810')
    c.append('南馆四层自习室')

    a.append('4FS-B055')
    b.append('103763811')
    c.append('南馆四层自习室')

    a.append('4FS-B056')
    b.append('103763812')
    c.append('南馆四层自习室')

    a.append('4FS-B057')
    b.append('103763813')
    c.append('南馆四层自习室')

    a.append('4FS-B058')
    b.append('103763814')
    c.append('南馆四层自习室')

    a.append('4FS-B059')
    b.append('103763815')
    c.append('南馆四层自习室')

    a.append('4FS-B060')
    b.append('103763816')
    c.append('南馆四层自习室')

    a.append('4FS-B061')
    b.append('103763817')
    c.append('南馆四层自习室')

    a.append('4FS-B062')
    b.append('103763818')
    c.append('南馆四层自习室')

    a.append('4FS-B063')
    b.append('103763819')
    c.append('南馆四层自习室')

    a.append('4FS-B064')
    b.append('103763820')
    c.append('南馆四层自习室')

    a.append('4FS-B065')
    b.append('103763821')
    c.append('南馆四层自习室')

    a.append('4FS-B066')
    b.append('103763822')
    c.append('南馆四层自习室')

    a.append('4FS-B067')
    b.append('103763823')
    c.append('南馆四层自习室')

    a.append('4FS-B068')
    b.append('103763824')
    c.append('南馆四层自习室')

    a.append('4FS-B069')
    b.append('103763825')
    c.append('南馆四层自习室')

    a.append('4FS-B070')
    b.append('103763826')
    c.append('南馆四层自习室')

    a.append('4FS-B071')
    b.append('103763827')
    c.append('南馆四层自习室')

    a.append('4FS-B072')
    b.append('103763828')
    c.append('南馆四层自习室')

    a.append('4FS-B073')
    b.append('103763829')
    c.append('南馆四层自习室')

    a.append('4FS-B074')
    b.append('103763830')
    c.append('南馆四层自习室')

    a.append('4FS-B075')
    b.append('103763831')
    c.append('南馆四层自习室')

    a.append('4FS-B076')
    b.append('103763832')
    c.append('南馆四层自习室')

    a.append('4FS-B077')
    b.append('103763833')
    c.append('南馆四层自习室')

    a.append('4FS-B078')
    b.append('103763834')
    c.append('南馆四层自习室')

    a.append('4FS-B079')
    b.append('103763835')
    c.append('南馆四层自习室')

    a.append('4FS-B080')
    b.append('103763836')
    c.append('南馆四层自习室')

    a.append('4FS-B081')
    b.append('103763837')
    c.append('南馆四层自习室')

    a.append('4FS-B082')
    b.append('103763838')
    c.append('南馆四层自习室')

    a.append('4FS-B083')
    b.append('103763839')
    c.append('南馆四层自习室')

    a.append('4FS-B084')
    b.append('103763840')
    c.append('南馆四层自习室')

    a.append('4FS-B085')
    b.append('103763841')
    c.append('南馆四层自习室')

    a.append('4FS-B086')
    b.append('103763842')
    c.append('南馆四层自习室')

    a.append('4FS-B087')
    b.append('103763843')
    c.append('南馆四层自习室')

    a.append('4FS-B088')
    b.append('103763844')
    c.append('南馆四层自习室')

    a.append('4FS-B089')
    b.append('103763845')
    c.append('南馆四层自习室')

    a.append('4FS-B090')
    b.append('103763846')
    c.append('南馆四层自习室')

    a.append('4FS-B091')
    b.append('103763847')
    c.append('南馆四层自习室')

    a.append('4FS-B092')
    b.append('103763848')
    c.append('南馆四层自习室')

    a.append('4FS-B093')
    b.append('103763849')
    c.append('南馆四层自习室')

    a.append('4FS-B094')
    b.append('103763850')
    c.append('南馆四层自习室')

    a.append('4FS-B095')
    b.append('103763851')
    c.append('南馆四层自习室')

    a.append('4FS-B096')
    b.append('103763852')
    c.append('南馆四层自习室')

    a.append('4FS-B097')
    b.append('103763853')
    c.append('南馆四层自习室')

    a.append('4FS-B098')
    b.append('103763854')
    c.append('南馆四层自习室')

    a.append('4FS-B099')
    b.append('103763855')
    c.append('南馆四层自习室')

    a.append('4FS-B100')
    b.append('103763856')
    c.append('南馆四层自习室')

    a.append('4FS-B101')
    b.append('103763857')
    c.append('南馆四层自习室')

    a.append('4FS-B102')
    b.append('103763858')
    c.append('南馆四层自习室')

    a.append('4FS-B103')
    b.append('103763859')
    c.append('南馆四层自习室')

    a.append('4FS-B104')
    b.append('103763860')
    c.append('南馆四层自习室')

    a.append('4FS-B105')
    b.append('103763861')
    c.append('南馆四层自习室')

    a.append('4FS-B106')
    b.append('103763862')
    c.append('南馆四层自习室')

    a.append('4FS-B107')
    b.append('103763863')
    c.append('南馆四层自习室')

    a.append('4FS-B108')
    b.append('103763864')
    c.append('南馆四层自习室')

    a.append('4FS-B111')
    b.append('103763867')
    c.append('南馆四层自习室')

    a.append('4FS-B112')
    b.append('103763868')
    c.append('南馆四层自习室')

    a.append('4FS-B115')
    b.append('103763871')
    c.append('南馆四层自习室')

    a.append('4FS-B116')
    b.append('103763872')
    c.append('南馆四层自习室')

    a.append('4FS-B119')
    b.append('103763875')
    c.append('南馆四层自习室')

    a.append('4FS-B120')
    b.append('103763876')
    c.append('南馆四层自习室')

    a.append('4FS-B121')
    b.append('103763877')
    c.append('南馆四层自习室')

    a.append('4FS-B122')
    b.append('103763878')
    c.append('南馆四层自习室')

    a.append('4FS-B123')
    b.append('103763879')
    c.append('南馆四层自习室')

    a.append('4FS-B124')
    b.append('103763880')
    c.append('南馆四层自习室')

    a.append('4FS-B125')
    b.append('103763881')
    c.append('南馆四层自习室')

    a.append('4FS-B126')
    b.append('103763882')
    c.append('南馆四层自习室')

    a.append('4FS-B127')
    b.append('103763883')
    c.append('南馆四层自习室')

    a.append('4FS-B128')
    b.append('103763884')
    c.append('南馆四层自习室')

    a.append('4FS-B129')
    b.append('103763885')
    c.append('南馆四层自习室')

    a.append('4FS-B130')
    b.append('103763886')
    c.append('南馆四层自习室')

    a.append('4FS-B131')
    b.append('103763887')
    c.append('南馆四层自习室')

    a.append('4FS-B132')
    b.append('103763888')
    c.append('南馆四层自习室')

    a.append('4FS-B133')
    b.append('103763889')
    c.append('南馆四层自习室')

    a.append('4FS-B134')
    b.append('103763890')
    c.append('南馆四层自习室')

    a.append('4FS-B135')
    b.append('103763891')
    c.append('南馆四层自习室')

    a.append('4FS-B136')
    b.append('103763892')
    c.append('南馆四层自习室')

    a.append('4FS-B137')
    b.append('103763893')
    c.append('南馆四层自习室')

    a.append('4FS-B138')
    b.append('103763894')
    c.append('南馆四层自习室')

    a.append('4FS-B139')
    b.append('103763895')
    c.append('南馆四层自习室')

    a.append('4FS-B140')
    b.append('103763896')
    c.append('南馆四层自习室')

    a.append('4FS-B145')
    b.append('103763901')
    c.append('南馆四层自习室')

    a.append('4FS-B146')
    b.append('103763902')
    c.append('南馆四层自习室')

    a.append('4FS-B147')
    b.append('103763903')
    c.append('南馆四层自习室')

    a.append('4FS-B148')
    b.append('103763904')
    c.append('南馆四层自习室')

    a.append('4FS-B149')
    b.append('103763905')
    c.append('南馆四层自习室')

    a.append('4FS-B150')
    b.append('103763906')
    c.append('南馆四层自习室')

    a.append('4FS-B151')
    b.append('103763907')
    c.append('南馆四层自习室')

    a.append('4FS-B152')
    b.append('103763908')
    c.append('南馆四层自习室')

    a.append('4FS-B153')
    b.append('103763909')
    c.append('南馆四层自习室')

    a.append('4FS-B154')
    b.append('103763910')
    c.append('南馆四层自习室')

    a.append('4FS-B155')
    b.append('103763911')
    c.append('南馆四层自习室')

    a.append('4FS-B156')
    b.append('103763912')
    c.append('南馆四层自习室')

    a.append('4FS-B157')
    b.append('103763913')
    c.append('南馆四层自习室')

    a.append('4FS-B158')
    b.append('103763914')
    c.append('南馆四层自习室')

    a.append('4FS-B159')
    b.append('103763915')
    c.append('南馆四层自习室')

    a.append('4FS-B160')
    b.append('103763916')
    c.append('南馆四层自习室')

    a.append('4FS-B161')
    b.append('103763917')
    c.append('南馆四层自习室')

    a.append('4FS-B162')
    b.append('103763918')
    c.append('南馆四层自习室')

    a.append('4FS-B163')
    b.append('103763919')
    c.append('南馆四层自习室')

    a.append('4FS-B164')
    b.append('103763920')
    c.append('南馆四层自习室')

    a.append('4FS-B169')
    b.append('103763925')
    c.append('南馆四层自习室')

    a.append('4FS-B170')
    b.append('103763926')
    c.append('南馆四层自习室')

    a.append('4FS-B171')
    b.append('103763927')
    c.append('南馆四层自习室')

    a.append('4FS-B172')
    b.append('103763928')
    c.append('南馆四层自习室')

    a.append('4FS-B173')
    b.append('103763929')
    c.append('南馆四层自习室')

    a.append('4FS-B174')
    b.append('103763930')
    c.append('南馆四层自习室')

    a.append('4FS-B175')
    b.append('103763931')
    c.append('南馆四层自习室')

    a.append('4FS-B176')
    b.append('103763932')
    c.append('南馆四层自习室')

    a.append('4FS-B177')
    b.append('103763933')
    c.append('南馆四层自习室')

    a.append('4FS-B178')
    b.append('103763934')
    c.append('南馆四层自习室')

    a.append('4FS-B179')
    b.append('103763935')
    c.append('南馆四层自习室')

    a.append('4FS-B180')
    b.append('103763936')
    c.append('南馆四层自习室')

    a.append('4FS-B181')
    b.append('103763937')
    c.append('南馆四层自习室')

    a.append('4FS-B182')
    b.append('103763938')
    c.append('南馆四层自习室')

    a.append('4FS-B183')
    b.append('103763939')
    c.append('南馆四层自习室')

    a.append('4FS-B184')
    b.append('103763940')
    c.append('南馆四层自习室')

    a.append('4FS-B185')
    b.append('103763941')
    c.append('南馆四层自习室')

    a.append('4FS-B186')
    b.append('103763942')
    c.append('南馆四层自习室')

    a.append('4FS-B187')
    b.append('103763943')
    c.append('南馆四层自习室')

    a.append('4FS-B188')
    b.append('103763944')
    c.append('南馆四层自习室')

    a.append('4FS-B193')
    b.append('103763949')
    c.append('南馆四层自习室')

    a.append('4FS-B194')
    b.append('103763950')
    c.append('南馆四层自习室')

    a.append('4FS-B195')
    b.append('103763951')
    c.append('南馆四层自习室')

    a.append('4FS-B196')
    b.append('103763952')
    c.append('南馆四层自习室')

    a.append('4FS-B197')
    b.append('103763953')
    c.append('南馆四层自习室')

    a.append('4FS-B198')
    b.append('103763954')
    c.append('南馆四层自习室')

    a.append('4FS-B199')
    b.append('103763955')
    c.append('南馆四层自习室')

    a.append('4FS-B200')
    b.append('103763956')
    c.append('南馆四层自习室')

    a.append('4FS-C001')
    b.append('103763961')
    c.append('南馆四层自习室')

    a.append('4FS-C002')
    b.append('103763962')
    c.append('南馆四层自习室')

    a.append('4FS-C003')
    b.append('103763963')
    c.append('南馆四层自习室')

    a.append('4FS-C004')
    b.append('103763964')
    c.append('南馆四层自习室')

    a.append('4FS-C005')
    b.append('103763965')
    c.append('南馆四层自习室')

    a.append('4FS-C006')
    b.append('103763966')
    c.append('南馆四层自习室')

    a.append('4FS-C007')
    b.append('103763967')
    c.append('南馆四层自习室')

    a.append('4FS-C008')
    b.append('103763968')
    c.append('南馆四层自习室')

    a.append('4FS-C009')
    b.append('103763969')
    c.append('南馆四层自习室')

    a.append('4FS-C010')
    b.append('103763970')
    c.append('南馆四层自习室')

    a.append('4FS-C011')
    b.append('103763971')
    c.append('南馆四层自习室')

    a.append('4FS-C012')
    b.append('103763972')
    c.append('南馆四层自习室')

    a.append('4FS-C013')
    b.append('103763973')
    c.append('南馆四层自习室')

    a.append('4FS-C014')
    b.append('103763974')
    c.append('南馆四层自习室')

    a.append('4FS-C015')
    b.append('103763975')
    c.append('南馆四层自习室')

    a.append('4FS-C016')
    b.append('103763976')
    c.append('南馆四层自习室')

    a.append('4FS-C017')
    b.append('103763977')
    c.append('南馆四层自习室')

    a.append('4FS-C018')
    b.append('103763978')
    c.append('南馆四层自习室')

    a.append('4FS-C019')
    b.append('103763979')
    c.append('南馆四层自习室')

    a.append('4FS-C020')
    b.append('103763980')
    c.append('南馆四层自习室')

    a.append('4FS-C021')
    b.append('103763981')
    c.append('南馆四层自习室')

    a.append('4FS-C022')
    b.append('103763982')
    c.append('南馆四层自习室')

    a.append('4FS-C023')
    b.append('103763983')
    c.append('南馆四层自习室')

    a.append('4FS-C024')
    b.append('103763984')
    c.append('南馆四层自习室')

    a.append('4FS-C025')
    b.append('103763985')
    c.append('南馆四层自习室')

    a.append('4FS-C026')
    b.append('103763986')
    c.append('南馆四层自习室')

    a.append('4FS-C027')
    b.append('103763987')
    c.append('南馆四层自习室')

    a.append('4FS-C028')
    b.append('103763988')
    c.append('南馆四层自习室')

    a.append('4FS-C029')
    b.append('103763989')
    c.append('南馆四层自习室')

    a.append('4FS-C030')
    b.append('103763990')
    c.append('南馆四层自习室')

    a.append('4FS-C031')
    b.append('103763991')
    c.append('南馆四层自习室')

    a.append('4FS-C032')
    b.append('103763992')
    c.append('南馆四层自习室')

    a.append('4FS-C033')
    b.append('103763993')
    c.append('南馆四层自习室')

    a.append('4FS-C034')
    b.append('103763994')
    c.append('南馆四层自习室')

    a.append('4FS-C035')
    b.append('103763995')
    c.append('南馆四层自习室')

    a.append('4FS-C036')
    b.append('103763996')
    c.append('南馆四层自习室')

    a.append('4FS-C037')
    b.append('103763997')
    c.append('南馆四层自习室')

    a.append('4FS-C038')
    b.append('103763998')
    c.append('南馆四层自习室')

    a.append('4FS-C039')
    b.append('103763999')
    c.append('南馆四层自习室')

    a.append('4FS-C040')
    b.append('103764000')
    c.append('南馆四层自习室')

    a.append('4FS-C041')
    b.append('103764001')
    c.append('南馆四层自习室')

    a.append('4FS-C042')
    b.append('103764002')
    c.append('南馆四层自习室')

    a.append('4FS-C043')
    b.append('103764003')
    c.append('南馆四层自习室')

    a.append('4FS-C044')
    b.append('103764004')
    c.append('南馆四层自习室')

    a.append('4FS-C045')
    b.append('103764005')
    c.append('南馆四层自习室')

    a.append('4FS-C046')
    b.append('103764006')
    c.append('南馆四层自习室')

    a.append('4FS-C047')
    b.append('103764007')
    c.append('南馆四层自习室')

    a.append('4FS-C048')
    b.append('103764008')
    c.append('南馆四层自习室')

    a.append('4FS-C049')
    b.append('103764009')
    c.append('南馆四层自习室')

    a.append('4FS-C050')
    b.append('103764010')
    c.append('南馆四层自习室')

    a.append('4FS-C051')
    b.append('103764011')
    c.append('南馆四层自习室')

    a.append('4FS-C052')
    b.append('103764012')
    c.append('南馆四层自习室')

    a.append('4FS-C053')
    b.append('103764013')
    c.append('南馆四层自习室')

    a.append('4FS-C054')
    b.append('103764014')
    c.append('南馆四层自习室')

    a.append('4FS-C055')
    b.append('103764015')
    c.append('南馆四层自习室')

    a.append('4FS-C056')
    b.append('103764016')
    c.append('南馆四层自习室')

    a.append('4FS-C057')
    b.append('103764017')
    c.append('南馆四层自习室')

    a.append('4FS-C058')
    b.append('103764018')
    c.append('南馆四层自习室')

    a.append('4FS-C060')
    b.append('103764020')
    c.append('南馆四层自习室')

    a.append('4FS-C061')
    b.append('103764021')
    c.append('南馆四层自习室')

    a.append('4FS-C062')
    b.append('103764022')
    c.append('南馆四层自习室')

    a.append('4FS-C063')
    b.append('103764023')
    c.append('南馆四层自习室')

    a.append('4FS-C064')
    b.append('103764024')
    c.append('南馆四层自习室')

    a.append('4FS-C065')
    b.append('103764025')
    c.append('南馆四层自习室')

    a.append('4FS-C066')
    b.append('103764026')
    c.append('南馆四层自习室')

    a.append('4FS-C067')
    b.append('103764027')
    c.append('南馆四层自习室')

    a.append('4FS-C068')
    b.append('103764028')
    c.append('南馆四层自习室')

    a.append('4FS-C069')
    b.append('103764029')
    c.append('南馆四层自习室')

    a.append('4FS-C070')
    b.append('103764030')
    c.append('南馆四层自习室')

    a.append('4FS-C071')
    b.append('103764031')
    c.append('南馆四层自习室')

    a.append('4FS-C072')
    b.append('103764032')
    c.append('南馆四层自习室')

    a.append('4FS-C073')
    b.append('103764033')
    c.append('南馆四层自习室')

    a.append('4FS-C074')
    b.append('103764034')
    c.append('南馆四层自习室')

    a.append('4FS-C075')
    b.append('103764035')
    c.append('南馆四层自习室')

    a.append('4FS-C076')
    b.append('103764036')
    c.append('南馆四层自习室')

    a.append('4FS-C077')
    b.append('103764037')
    c.append('南馆四层自习室')

    a.append('4FS-C078')
    b.append('103764038')
    c.append('南馆四层自习室')

    a.append('4FS-C079')
    b.append('103764039')
    c.append('南馆四层自习室')

    a.append('4FS-C080')
    b.append('103764040')
    c.append('南馆四层自习室')

    a.append('4FS-C081')
    b.append('103764041')
    c.append('南馆四层自习室')

    a.append('4FS-C082')
    b.append('103764042')
    c.append('南馆四层自习室')

    a.append('4FS-C083')
    b.append('103764043')
    c.append('南馆四层自习室')

    a.append('4FS-C084')
    b.append('103764044')
    c.append('南馆四层自习室')

    a.append('4FS-C085')
    b.append('103764045')
    c.append('南馆四层自习室')

    a.append('4FS-C086')
    b.append('103764046')
    c.append('南馆四层自习室')

    a.append('4FS-C087')
    b.append('103764047')
    c.append('南馆四层自习室')

    a.append('4FS-C088')
    b.append('103764048')
    c.append('南馆四层自习室')

    a.append('4FS-C089')
    b.append('103764049')
    c.append('南馆四层自习室')

    a.append('4FS-C090')
    b.append('103764050')
    c.append('南馆四层自习室')

    a.append('4FS-C091')
    b.append('103764051')
    c.append('南馆四层自习室')

    a.append('4FS-C092')
    b.append('103764052')
    c.append('南馆四层自习室')

    a.append('4FS-C093')
    b.append('103764053')
    c.append('南馆四层自习室')

    a.append('4FS-C094')
    b.append('103764054')
    c.append('南馆四层自习室')

    a.append('4FS-C095')
    b.append('103764055')
    c.append('南馆四层自习室')

    a.append('4FS-C096')
    b.append('103764056')
    c.append('南馆四层自习室')

    a.append('4FS-C097')
    b.append('103764057')
    c.append('南馆四层自习室')

    a.append('4FS-C098')
    b.append('103764058')
    c.append('南馆四层自习室')

    a.append('4FS-C099')
    b.append('103764059')
    c.append('南馆四层自习室')

    a.append('4FS-C100')
    b.append('103764060')
    c.append('南馆四层自习室')

    a.append('4FS-C101')
    b.append('103764061')
    c.append('南馆四层自习室')

    a.append('4FS-C102')
    b.append('103764062')
    c.append('南馆四层自习室')

    a.append('4FS-C103')
    b.append('103764063')
    c.append('南馆四层自习室')

    a.append('4FS-C104')
    b.append('103764064')
    c.append('南馆四层自习室')

    a.append('4FS-C105')
    b.append('103764065')
    c.append('南馆四层自习室')

    a.append('4FS-C106')
    b.append('103764066')
    c.append('南馆四层自习室')

    a.append('4FS-C107')
    b.append('103764067')
    c.append('南馆四层自习室')

    a.append('4FS-C108')
    b.append('103764068')
    c.append('南馆四层自习室')

    a.append('4FS-C109')
    b.append('103764069')
    c.append('南馆四层自习室')

    a.append('4FS-C110')
    b.append('103764070')
    c.append('南馆四层自习室')

    a.append('4FS-C111')
    b.append('103764071')
    c.append('南馆四层自习室')

    a.append('4FS-C112')
    b.append('103764072')
    c.append('南馆四层自习室')

    a.append('4FS-C113')
    b.append('103764073')
    c.append('南馆四层自习室')

    a.append('4FS-C114')
    b.append('103764074')
    c.append('南馆四层自习室')

    a.append('4FS-C115')
    b.append('103764075')
    c.append('南馆四层自习室')

    a.append('4FS-C116')
    b.append('103764076')
    c.append('南馆四层自习室')

    d=[]
    d.append(a)
    d.append(b)
    d.append(c)
    return d


def login(username, password):
    print("in")
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/login.aspx'
    form = {
        'id': username,
        'pwd': password,
        'role': '512',
        'aliuserid': '',
        'schoolcode': '',
        'wxuserid': '',
        '_nocache': '1626938167456',
        'act': 'login',

    }
    s = requests.session();
    resp = s.post(url, headers=headers, data=form, cookies=cookies)
    res=''+json.loads(resp.text)['msg']
    # print(ret)
    if '错' in res or '未' in res:
        return res
    return s;
    # 提交登陆信息


# 指定抢座
def getSeat(s, dev_id, lab_id, start, end):
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
    data = {
        'dev_id': dev_id,
        'lab_id': lab_id,
        'start': start,
        'end': end,
        'type': 'dev',
        'act': 'set_resv',
    }
    re = s.get(url, headers=headers, data=data)
    print(re.text)

def getMySeat(s):
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/reserve.aspx?stat_flag=9&act=get_my_resv'
    re = s.get(url, headers=headers)
    res = json.loads(re.text)['data']
    return res


# 快速抢座
def quickGetSeat(s, date, dateRange, kind_id, interval):
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
    # stH = int(dateRange.split(':')[0])
    # stM = int(dateRange.split(':')[1].split('-')[0])
    # edH = int(dateRange.split(':')[1].split('-')[1])
    # edM = int(dateRange.split(':')[2])
    # interval = edH*60+edM-(stH*60+stM)
    # print(stH+':'+stM+' '+edH+':'+edM)
    data = {
        'classkind': '8',
        'date': date,
        'range': dateRange,
        'kind_id': kind_id,
        'act': 'quick_resv',
        'interval': interval,
    }
    # print(data)
    re = s.get(url, headers=headers, data=data)
    # print(re.text)
    ret=[]
    if(json.loads(re.text)['msg']=='ok'):
        ret.append(1)
    else:
        ret.append(0)
    ret.append(json.loads(re.text)['msg'])
    return ret

# 获取房间信息
def getRoom(s, date):
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/room.aspx'
    data = {
        'right': 'detail',
        'fr_all_day': 'false',
        'room_id': '104558576',
        'name': '电子阅览区',
        'open_start': '700',
        'open_end': '2200',
        'classkind': '8',
        'date': date,
        'start': '7:00',
        'end': '22:00',
        'act': 'get_rm_sta',
    }
    re = s.get(url, headers=headers, data=data)
    res = json.loads(re.text)
    roomData = res["data"]
    # print(roomData)
    roomList = []
    a = []
    b = []
    c = []
    i = 0
    for room in roomData:
        a.append(room['name'])
        b.append(room['labId'])
        c.append(room['id'])
        i += 1
    roomList.append(a)
    roomList.append(b)
    roomList.append(c)
    return roomList


def threadGetSeat(s):
    s = login(2019211001000925, 250417)
    dev_id = 100532031  # 座位号
    lab_id = 100531890  # 房间号
    start = '2021-07-22 20: 00'
    end = '2021-07-22 22: 00'
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
    data = {
        'dev_id': dev_id,
        'lab_id': lab_id,
        'start': start,
        'end': end,
        'type': 'dev',
        'act': 'set_resv',
    }
    while 1:
        re = s.get(url, headers=headers, data=data)
        # print(re.text)


# 获取自习室人员情况
def getAllPerson(s, room_id, date):
    url = 'http://lib2.ecjtu.edu.cn/ClientWeb/pro/ajax/device.aspx'
    data = {
        'right': 'detail',
        'fr_all_day': 'false',
        'room_id': room_id,
        'date': date,
        'start': '7:00',
        'end': '22:00',
        'classkind': '8',
        'act': 'get_rsv_sta',
    }
    re = s.get(url, headers=headers, data=data)
    res = json.loads(re.text)
    # print(res['data'])
    return res['data']


if __name__ == '__main__':
    userid = ''
    password = ''
    dev_id = 100532031  # 座位号
    lab_id = 100531890  # 自习室号
    room_id = '100531916'  # 房间号
    start = '2021-07-22 20: 00'
    end = '2021-07-22 22: 00'
    date = '2021-07-23'
    timeRange = '20:00-22:00'
    interval = '120'
    quick_id = ['100531888', '1005335015', '105364879']  # 北区自习室，电子阅览室，南区自习室id
    s = login(userid, password)
    roomList = []
    roomList = initRoom()
    seatList = []
    seatList = initSeat()
    # 直接初始化数据，不获取线上数据，节约时间
    # roomList = getRoom(s, date)
    # 下面用来构造房间数据
    # 所有lab_id 分别为名称，labid,roomid
    # for i in range(0, len(roomList[0])):
        # print('a.append(\'' + roomList[0][i] + "\')\nb.append(\'" + roomList[1][i] + "\')\nc.append(\'" + roomList[2][
        #     i] + '\')')
        # print(roomList[0][i]+roomList[1][i]+roomList[2][i])
    # 下面用来构造座位数据
    # for i in range(len(roomList[0])):
    #     allUser = getAllPerson(s, roomList[2][i], date)
    #     for one in allUser:
    #         print('a.append(\''+one['name'] + '\')\nb.append(\'' + one['devId']+'\')\n'+'c.append(\''+one['labName'] + '\')\n')
            # for user in one['ts']:
            #     print(user['start'] + '->' + user['end'] + '-' + user['owner'])
    quickGetSeat(s, date, timeRange, quick_id[0],interval)
    # getSeat(s, dev_id, lab_id, start, end)
    # pool = Pool()
    # urls = []
    # for i in range(0,100000):
    #     urls.append((0))
    # pool.map(threadGetSeat,urls)
