
from photoshop import Session

from psd_tools import PSDImage
import os ,datetime
import xlwings as xw
import pandas as pd
import requests
from pw import *


class PS:
    def __init__(self):
        self.folder = "导出图片/"
        self.path = f"{os.path.split(os.path.realpath(__file__ ))[0]}/{self.folder}"    

    def 主图1(self,psd,sku_dict):
        with Session(action= psd) as ps:
        
            doc = ps.active_document

            doc.artLayers.getByName("配置X").textItem.contents = sku_dict["配置X"]
            doc.artLayers.getByName("SKU名称").textItem.contents = sku_dict["SKU名称"]

            goodsid_lst = sku_dict["商品信息"]
            print(goodsid_lst)
            for i  in list(goodsid_lst.keys()):
                # print(i)
                # if len(goodsid_lst[i][2]) >40:
                #     doc.artLayers.getByName(i+"-1").textItem.size = 5
                # elif len(goodsid_lst[i][2]) >33:
                #     doc.artLayers.getByName(i+"-1").textItem.size = 5.8
                # elif len(goodsid_lst[i][2]) >27:
                #     doc.artLayers.getByName(i+"-1").textItem.size = 7
                # else:
                #     doc.artLayers.getByName(i+"-1").textItem.size = 8

                doc.artLayers.getByName(i+"-1").textItem.contents = goodsid_lst[i][2] + str([""  if goodsid_lst[i][1]  == 1  else f"  * {int(goodsid_lst[i][1])}"][0])
                doc.artLayers.getByName(i+"-2").textItem.contents = goodsid_lst[i][3]



            


            options = ps.PNGSaveOptions() #ps.JPEGSaveOptions()
            export_file_name = f'{self.path}{sku_dict["sku"]}.png' 
            doc.saveAs(export_file_name, options, asCopy=True)
            # ps.app.doJavaScript(f'alert("save to jpg: {sku_dict["sku"]}")') #脚本提示
    def main(self,psd_name,sku_lst):
        import time
        statr_time = time.time()

        sku_dict_test = {"sku":123,"配置X":"配置三","SKU名称":"狂拽炫酷","商品信息":{
                                                "CPU":["i5 12600K",1,"i1 12600K","酷睿i1 超级强","升级项"],
                                                "主板":["i5 12600K",2,"i2 12600K","酷睿i2 超级强","升级项"],
                                                "散热":["i5 12600K",3,"i3 12600K","酷睿i3 超级强","升级项"],
                                                "显卡":["i5 12600K",4,"i4 12600K","酷睿i4 超级强","升级项"],
                                                "内存":["i5 12600K",5,"i5 12600K","酷睿i5 超级强","升级项"],
                                                "硬盘":["i5 12600K",6,"i6 12600K","酷睿i6 超级强","升级项"],
                                                "电源":["i5 12600K",7,"i7 12600K","酷睿i7 超级强","升级项"],
                                                "机箱":["i5 12600K",8,"i8 12600K","酷睿i8 超级强","升级项"],
                                                "赠品":["i5 12600K",9,"i9 12600K","酷睿i9 超级强","升级项"],
                                                                        }}
        
        from get_sku_dict import ERP
        
        # sku_dict = {"sku":10092600821975,"配置X":"配置三","SKU名称":"R9 7950X3D/无显卡","商品信息":ERP(erpcookies= px_erpcookies).main(sku=10092600821975)}

    
        # sku_lst = [10043560704720]
        for i in range(len(sku_lst)):
            sku = sku_lst[i] 
            goodsinfo = ERP(erpcookies= px_erpcookies).main(sku=sku)[1]
            sku_dict = {"sku":sku,"配置X":goodsinfo[0],"SKU名称":goodsinfo[1],"商品信息":ERP(erpcookies= px_erpcookies).main(sku=sku)[0]}
            self.主图1(psd_name,sku_dict)









        print(f"代码执行时间:{time.time()-statr_time}秒")


        



if __name__ == "__main__":


    sku_lst = [3399162200489730,3399162200489986,3399162200490242,3399162200490498]
    sku_lst = [10043560704720,10079373765280,10043560704721,10043560704722,10096095867564]
    sku_lst = [10041791993200]
    PS().main(psd_name="主图配置单2",sku_lst=sku_lst)

