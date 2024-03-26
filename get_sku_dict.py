from ERP import ERP
from pw import *

import requests
import pymysql
import pandas as pd
requests.urllib3.disable_warnings() # type: ignore








def get_sql_to_df(table_name):
    from sqlalchemy import create_engine

    pymysql.install_as_MySQLdb()

    DB_STRING= f"mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    engine = create_engine(DB_STRING)
    sql=f"SELECT * FROM `{table_name}`"
    data = pd.read_sql(sql,con=engine)
    # print(data)
    return data







class ERP(ERP):
    # 获取SKU 对应的套餐商品信息
    def getNetGoodsList(self,sku):
        url =  f"https://cqzs.3cerp.com/pages/net/getNetGoodsList.htm?pageIndex=0&shop_id=&c_status=&is_res=-1&beginDate=&endDate=&search_date_key=search_sku_date&search_name_key=search_spu_name&search_name_value=&search_code_key=search_sku_code&search_code_value={sku}&search_delivery_templet_id=&search_depot_id=&search_data_source=&search_net_stock_sync=&pageSize=100&sortField=&sortOrder="
        r = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
        json_data = r.json()["data"]
        return json_data[0]["goods_id"]
    

    # 获取套餐商品信息的对应的子商品信息
    def searchGoodsDetail(self,goodsid):
        url = f"https://cqzs.3cerp.com/pages/goods/searchGoodsDetail.htm?onlyComponent=-1&goodsId={goodsid}"
        r = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
        json_data = r.json()["data"]
        goods_id_list = [[item['goods_id'],
                           item['c_sub_category_name'],
                           item['n'],
                           item['c_name']
                           ] 
                          
                                                for item in json_data ]
        
        return goods_id_list 
    
    def get_Goods_goodsinfo(self,goodsid):
        url = f"https://cqzs.3cerp.com/pages/basgoods/searchBasGoodsDetailInfo.htm?goodsId={goodsid}"
        r = requests.get(url=url,headers=self.headers,cookies=self.cookies,verify= False)
        json_data = r.json()["data"]["goodsInfo"][0]["c_remark"].split("丨")
        if json_data != [""]:
            return json_data
        else:
            return ["(≧∇≦)ﾉ","(*/ω＼*)"]
        


    def main(self,sku):
        goodsid = self.getNetGoodsList(sku=sku)
        goosinfo = self.get_Goods_goodsinfo(goodsid=goodsid)
        goods_id_list  = self.searchGoodsDetail(goodsid=goodsid)
        print(goods_id_list)

        #获取商品信息
        Goods_Stock = get_sql_to_df(table_name = 'Erp_Goods_Stock')
        GoodsDetail = []
        for i in goods_id_list:
            print(i ,"商品信息")
            
            try:
                备注 = Goods_Stock.loc[Goods_Stock["goods_id"]==  i[0]]["优化名称"].values[0].split("丨")
                print(备注)
                if 备注 != ['']:
                    dict = [i[1],i[2]]
                    for i in 备注:
                        dict.append(i)
                    GoodsDetail.append(dict)
                else:
                    dict = [i[1],i[2],i[3],""]
                    GoodsDetail.append(dict)
                        
            except:
                dict = [i[1],i[2],i[3],""]
                GoodsDetail.append(dict)

        for item in GoodsDetail:
            print(item, end='\n')

        GoodsDetail_dict = {
            "CPU": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["英特尔CPU","英特尔CPU散","AMDCPU","AMDCPU散"])][0],
            "主板": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉主板","技嘉AMD平台","华硕主板","七彩虹主板"])][0],
            "散热": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉散热器","其他散热器","乔思伯散热器","华硕散热器"])][0],
            "内存": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["威刚内存","技嘉内存","宏碁内存"])][0],
            "硬盘": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["威刚SSD","三星SSD","技嘉SSD"])][0],
            "电源": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉电源","其他电源","威刚电源","鑫谷电源","航嘉电源"])][0],
            "机箱": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉机箱","乔思伯机箱","其他机箱","航嘉机箱","鑫谷机箱","威刚机箱","追风者机箱","恩杰机箱","爱国者机箱","先马机箱"])][0],
            "赠品": [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["风扇光效","其他赠品礼品","其他设备","其他耗材"])][0],
            }

        # 显卡专用
        if [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉显卡",""])] == []:
            if  GoodsDetail_dict["CPU"][2]!= '':
                GoodsDetail_dict["显卡"] =  ["核显",1,GoodsDetail_dict["CPU"][4],"联系客服加装显卡享粉丝价"]
            else:
                GoodsDetail_dict["显卡"] =  ["无显卡",1,"无显卡(需要搭载独显才能正常使用)","联系客服加装显卡享粉丝价"]
        else:
            GoodsDetail_dict["显卡"] = [item for item in GoodsDetail if any(item[0] in sublist for sublist in ["技嘉显卡","华硕显卡","七彩虹显卡"])][0]



        

        return GoodsDetail_dict , goosinfo



if __name__ == "__main__":
    # ERP(erpcookies= px_erpcookies).main(sku=3399162200489730)
    print(ERP(erpcookies= px_erpcookies).main(sku=10043560704720))