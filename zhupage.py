
import flet as ft
from time import sleep
from core import *
process  =None

stop_flag =True





def  zhupage(page:ft.Page):

    def close_banner(e):
        page.banner.open = False
        page.update()
    
    from NavigationRail import customPrompt 
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=30),
        content=customPrompt,
        actions=[
            ft.TextButton("确定", on_click=close_banner),
            ft.TextButton("我知道了", on_click=close_banner),
            ft.TextButton("关闭", on_click=close_banner)
        ],
    )
    def prompt(a):
        customPrompt.value =  a
        page.banner.open = True
        page.update()
        sleep(3)
        page.banner.open = False
        page.update()

    psd_name = ft.TextField(label="PSD名称:",width=280,multiline= True,min_lines=1,max_lines=1,text_size=10,
                       value= "主图配置单")
    sku =  ft.TextField(label="SKU",width=280,multiline = True,min_lines=1,max_lines=2,text_size=10)

    #抖音数据抓取启动器
    dy_tool_1 = ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.OPEN_IN_BROWSER_OUTLINED),
                            title=ft.Text("批量主图生成工具"),
                            height= 40

                        ),
                        ft.Column([ft.Column([psd_name,sku,]),
                                ft.Row([
                                        ft.ElevatedButton("启动",icon="WEBHOOK_OUTLINED",icon_color="green400",on_click=lambda __:(PS().main(psd_name = psd_name.value,sku_lst=sku.value.split(",")))),

                                        ])
                             ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ]
                ),
                margin=10,
                padding=10,
                alignment=ft.alignment.top_center,
                bgcolor=ft.colors.BLUE_100,
                width=300,
                height =240,
                # expand = True,
                border_radius=10,
                # on_click= lambda  __: (setattr(dy_tool_2, 'height', 600) if dy_tool_2.height == 240 else setattr(dy_tool_2, 'height', 240),page.update()),
                # on_click= lambda __ : print(dy_tool_2.height),
                ink=True,
                )
    


    # 批量链接打开工具

    

    # 不知道写什么工具但是还是需要写一个占位置
    dy_tool_2= ft.Container(
                content=ft.Column( [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("不知道写什么工具但是还是需要写一个占位置"),
                            subtitle=ft.Text(
                                "_____,"
                            ),
                        ),
                        ft.Column([ft.TextField(label="123",width=280)
                            ,
                            ft.Row([ft.Slider(
            round= 0,
            divisions=5,
            value= 30,
            min= 1,
            max=120,
            label="{value}分",
            width=200
            
        )
                                ,
                            ft.IconButton(
                                    icon=ft.icons.NOT_STARTED,
                                    icon_size = 50,
                                    selected_icon=ft.icons.PAUSE_CIRCLE_ROUNDED,
                                    # on_click=,
                                    selected=False,
                                    style=ft.ButtonStyle(color={"selected": ft.colors.RED, "": ft.colors.GREEN})),
                                    ])

                             ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ]
                ),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                width=300,
                height=240,
                border_radius=10,
                ink=True,
                )


    return ft.Column([  ft.Row([dy_tool_1,dy_tool_2,],alignment=ft.MainAxisAlignment.START,),
                        # ft.Row([dy_tool_4],alignment=ft.MainAxisAlignment.START,)
                     
                     ])