from mitmproxy import ctx
import mitmproxy
import pandas as pd
import  xlwings



# 抖音数据转化
def dy_to_df(json_data,sku,sale_type,date =None):
  json_data = eval(str(json_data))

  data = json_data["data"][0]["metrics"]

  dict   = {i["index_name"]:i["index_display"] for i  in json_data["attributes"]}

  dict2 = {dict[k]:v["value"]["value"] for k,v in data.items()}

  df =pd.DataFrame(dict2,index=[0])
  df.insert(0, 'sku',sku,allow_duplicates=True,)
  df.insert(1, '商品载体',sale_type,allow_duplicates=True,)
  df.insert(2, '时间',date,allow_duplicates=True,)

  return df


#函数外部存储 数据
df_sum =xlwings.books.active.sheets["记录"].range("A1:N10000").options(pd.DataFrame,header = 1 , index = False).value
df_sum=df_sum.dropna(axis=0, how='all', inplace=False)

print(df_sum)
def response(flow: mitmproxy.http.HTTPFlow):


  if  "https://compass.jinritemai.com/compass_api/shop/product/product_detail/core_data/index_data" not in flow.request.url :
    return
  if  "date_type=20" not in flow.request.url :
    return

  dict1 = dict(flow.request.query)
  sale_type1 = "未知"
  match int(dict1["content_type"]):
    case 0:
      sale_type1 = "全部"
    case 1:
      sale_type1 = "直播"
    case 2:
      sale_type1 = "短视频"
    case 3:
      sale_type1 = "商品卡"
    case 4:
      sale_type1 = "其他"
  ## 
  global df_sum
  df_sum = pd.concat([df_sum,dy_to_df(flow.response.text,dict1["product_id"],sale_type1,dict1["end_date"])],ignore_index= True)
  print(df_sum)
  df_sum = df_sum.drop_duplicates(ignore_index= True)

  try:
    xlwings.books.active.sheets["记录"].range("A2").options(header = False , index = False,).value  =df_sum
  except:
      print("当前没有表格存储数据123")
  return df_sum
  
  