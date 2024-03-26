

from pw import *
import requests
requests.urllib3.disable_warnings() # type: ignore
import pandas as pd
import datetime








class ERP(): #这里是写3Cerp相关功能的地方
    def __init__(self,erpcookies=None) -> None:
        self.cookies = {'3cu':erpcookies}
        self.headers = {"Accept-Encoding":"gzip, deflate","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    
    #获取erp库存等信息
    def get_Goods_Stock(self):
        

        url =  f'http://cqzs.3cerp.com/pages/stock/searchGoodsExtendStock.htm?filter=&cBrand=&product=0&inStock=0&search_depot_id=&b_no_cost=0&noStock=0&subCategoryId=2%2C4%2C198%2C288%2C23%2C289%2C5%2C239%2C240%2C241%2C242%2C243%2C244%2C245%2C247%2C248%2C249%2C26%2C246%2C6%2C199%2C38%2C36%2C35%2C155%2C157%2C158%2C331%2C37%2C7%2C39%2C40%2C41%2C148%2C149%2C204%2C216%2C217%2C312%2C337%2C44%2C8%2C200%2C52%2C53%2C54%2C55%2C57%2C135%2C141%2C147%2C58%2C9%2C59%2C60%2C61%2C62%2C63%2C205%2C210%2C212%2C213%2C214%2C215%2C338%2C64%2C11%2C65%2C66%2C211%2C12%2C68%2C69%2C70%2C71%2C72%2C73%2C75%2C76%2C207%2C218%2C219%2C220%2C221%2C222%2C223%2C227%2C228%2C229%2C327%2C74%2C13%2C77%2C78%2C79%2C80%2C81%2C143%2C224%2C225%2C226%2C231%2C230%2C324%2C325%2C326%2C82%2C14%2C83%2C84%2C85%2C86%2C139%2C159%2C206%2C232%2C87%2C15%2C88%2C89%2C90%2C91%2C92%2C93%2C140%2C150%2C314%2C94%2C97%2C250%2C251%2C252%2C253%2C254%2C255%2C238%2C256%2C18%2C95%2C101%2C102%2C103%2C104%2C105%2C107%2C257%2C16%2C17%2C202%2C203%2C3%2C108%2C112%2C160%2C161%2C171%2C113%2C162%2C163%2C114%2C164%2C115%2C116%2C118%2C165%2C166%2C167%2C119%2C168%2C169%2C120%2C170%2C121%2C117%2C122%2C123%2C124%2C125%2C128%2C129%2C172%2C174%2C175%2C130%2C176%2C177%2C131%2C178%2C132%2C144%2C179%2C180%2C181%2C145%2C182%2C183%2C184%2C185%2C186%2C146%2C188%2C189%2C258%2C191%2C192%2C193%2C194%2C195%2C196%2C197%2C259%2C260%2C261%2C262%2C263%2C264%2C265%2C266%2C267%2C268%2C269%2C270%2C271%2C272%2C273%2C274%2C275%2C276%2C277%2C278%2C279%2C281%2C282%2C317%2C318%2C319%2C320%2C322%2C323%2C328%2C339%2C340%2C290%2C291%2C292%2C293%2C294%2C295%2C296%2C298%2C297%2C299%2C300%2C301%2C302%2C303%2C304%2C305%2C306%2C307%2C308%2C309%2C310%2C311%2C313%2C315%2C332%2C333%2C334%2C335%2C336%2C341%2C342%2C343%2C344%2C345%2C&searchTagName=&pageSize=2000&pageIndex=0&sortField=&sortOrder='
        r = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
        dict_sum = r.json()["data"]
        total = r.json()["total"]
        import math
        if total >2000:
            pageindex = 1
            while pageindex < math.ceil(total / 2000)  :
                url = f"http://cqzs.3cerp.com/pages/stock/searchGoodsExtendStock.htm?filter=&cBrand=&product=0&inStock=0&search_depot_id=&b_no_cost=0&noStock=0&subCategoryId=2%2C4%2C198%2C288%2C23%2C289%2C5%2C239%2C240%2C241%2C242%2C243%2C244%2C245%2C247%2C248%2C249%2C26%2C246%2C6%2C199%2C38%2C36%2C35%2C155%2C157%2C158%2C331%2C37%2C7%2C39%2C40%2C41%2C148%2C149%2C204%2C216%2C217%2C312%2C337%2C44%2C8%2C200%2C52%2C53%2C54%2C55%2C57%2C135%2C141%2C147%2C58%2C9%2C59%2C60%2C61%2C62%2C63%2C205%2C210%2C212%2C213%2C214%2C215%2C338%2C64%2C11%2C65%2C66%2C211%2C12%2C68%2C69%2C70%2C71%2C72%2C73%2C75%2C76%2C207%2C218%2C219%2C220%2C221%2C222%2C223%2C227%2C228%2C229%2C327%2C74%2C13%2C77%2C78%2C79%2C80%2C81%2C143%2C224%2C225%2C226%2C231%2C230%2C324%2C325%2C326%2C82%2C14%2C83%2C84%2C85%2C86%2C139%2C159%2C206%2C232%2C87%2C15%2C88%2C89%2C90%2C91%2C92%2C93%2C140%2C150%2C314%2C94%2C97%2C250%2C251%2C252%2C253%2C254%2C255%2C238%2C256%2C18%2C95%2C101%2C102%2C103%2C104%2C105%2C107%2C257%2C16%2C17%2C202%2C203%2C3%2C108%2C112%2C160%2C161%2C171%2C113%2C162%2C163%2C114%2C164%2C115%2C116%2C118%2C165%2C166%2C167%2C119%2C168%2C169%2C120%2C170%2C121%2C117%2C122%2C123%2C124%2C125%2C128%2C129%2C172%2C174%2C175%2C130%2C176%2C177%2C131%2C178%2C132%2C144%2C179%2C180%2C181%2C145%2C182%2C183%2C184%2C185%2C186%2C146%2C188%2C189%2C258%2C191%2C192%2C193%2C194%2C195%2C196%2C197%2C259%2C260%2C261%2C262%2C263%2C264%2C265%2C266%2C267%2C268%2C269%2C270%2C271%2C272%2C273%2C274%2C275%2C276%2C277%2C278%2C279%2C281%2C282%2C317%2C318%2C319%2C320%2C322%2C323%2C328%2C339%2C340%2C290%2C291%2C292%2C293%2C294%2C295%2C296%2C298%2C297%2C299%2C300%2C301%2C302%2C303%2C304%2C305%2C306%2C307%2C308%2C309%2C310%2C311%2C313%2C315%2C332%2C333%2C334%2C335%2C336%2C341%2C342%2C343%2C344%2C345%2C&searchTagName=&pageSize=2000&pageIndex={pageindex}&sortField=&sortOrder="
                r = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
                dict_sum += r.json()['data']
                pageindex += 1
        df_sum = pd.DataFrame(dict_sum)                      
        df_sum.rename(columns={"b_c_name":"erp名称",
                            "n_stock" :"总数量",
                            "category_name":"商品类别",
                            "n_able":"可销数",
                            "n_purchase":"待入",
                            "t_last_purchase":"最后采购时间",
                            "b_c_sku":"商品编码",
                            "d_cost":"单价成本",
                            "n_sale":"待出",
                            "n_sale_net":"待审",
                            "c_remark":"优化名称",
                            "kc_d_amount":"总金额"

                            },inplace=True)
        

        df_sum_new = df_sum.dropna(axis=0, subset=['最后采购时间'])
        df_sum_new.loc[:,['time']] = df_sum_new['最后采购时间'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").date())
        df1 = df_sum_new[df_sum_new["总数量"]> 0] 

        s_date = datetime.datetime.strptime('2023-01-01 00:00:00', "%Y-%m-%d %H:%M:%S").date() #最后采购时间
        df2 = df_sum_new[(df_sum_new["time"] > s_date) & (df_sum_new["总数量"]<= 0)]
        df_sum_jhs_all = pd.concat([df1, df2],ignore_index = True)


        
        df_sum_jh = df_sum.loc[:,["商品编码","商品类别","erp名称","优化名称","单价成本","总金额","总数量","可销数","待出","待审","待入","最后采购时间","goods_id"]]
        df_sum_jhs = df_sum_jhs_all.loc[:,["商品编码","商品类别","erp名称","优化名称","单价成本","总数量","可销数","待出","待审","待入","最后采购时间","goods_id"]]
        df_sum_jhss = df_sum.loc[:,["商品编码","商品类别","erp名称","优化名称","单价成本","总数量","可销数","待出","待审","待入","最后采购时间","goods_id"]]
                #原始数据版本    单纯去掉列版本     简化商品版本  #总行数
                #    0               1               2          3        4                         5
        return    df_sum,         df_sum_jh,       df_sum_jhs ,total , df_sum["总金额"].sum() ,df_sum_jhss
    # 获取erp 指定商品的销售信息
    def get_OutGoodsSnalysis(self,mode,goods_name,beginTime,endTime,transform_data=None):

        total = 2000
        pageindex  = 0
        from math import ceil

        while pageindex < ceil(total / 2000)  :
            print(pageindex,total / 2000)
            url = f"https://cqzs.3cerp.com/pages/sales/searchOutGoodsSnalysis.htm?b_net=0&filter={goods_name}&beginTime={beginTime}&endTime={endTime}&b_return_goods=0&b_cod=0&time_type=0&c_tag_name=&pageIndex={pageindex}&pageSize=2000"
            res = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
            if pageindex == 0 :
                dict_sum = res.json()["data"]
                total = res.json()["total"]

            else:
                dict_sum +=res.json()["data"]
            pageindex +=1

        match mode:
            case 1:
                return pd.DataFrame(dict_sum)
            case 2:

                df_cache = pd.DataFrame(dict_sum)
                try:
                    df_cache["是否整机"] = df_cache['sales_billcode'].apply(lambda x: '是' if x in transform_data else '否') 
                except:
                    return df_cache

                return df_cache

    def get_AllSalesList(self,mode,beginTime,endTime,transform_data=None):
        total = 2000
        pageindex  = 0
        from math import ceil

        while pageindex < ceil(total / 2000)  :
            url = f"http://cqzs.3cerp.com/pages/sales/searchAllSalesList.htm?time_type=1&begin_date={beginTime}&end_date={endTime}&shop_id=&delivery_templet_id=&emp=&bill_type=c_billcode&bill_filter=&c_type=&vip_type=c_vip_code&vip_filter=&depot_id=&yc=1&dc=0&pageIndex={pageindex}&pageSize=2000&sortField=&sortOrder="
            print(pageindex,total / 2000)
            res = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
            if pageindex == 0 :
                dict_sum = res.json()["data"]
                total = res.json()["total"]

            else:
                dict_sum +=res.json()["data"]
            pageindex +=1
        match mode:
            case 1:
                return pd.DataFrame(dict_sum)
            case 2:
                df_cache = pd.DataFrame(dict_sum)
                try:
                    df_cache["是否整机"] = df_cache['c_billcode'].apply(lambda x: '是' if x in transform_data else '否')
                except:
                    return df_cache

                return df_cache