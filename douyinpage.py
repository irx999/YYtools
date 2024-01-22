
import flet as ft
from time import sleep

process  =None

stop_flag =True





def  douyinpage(page:ft.Page):

    def close_banner(e):
        page.banner.open = False
        page.update()
    customPrompt = ft.Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
            ,size= 30,

        )

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

    #抖音程序启动终端程序
    import subprocess
    def run_terminal_program__1(e):
        e.control.selected = not e.control.selected
        e.control.update()
    # 使用subprocess.run启动终端程序
        global process
        print("运行")
        if not hasattr(run_terminal_program__1, 'has_run'):
            run_terminal_program__2.has_run = True
            print("This function will only run once.")
            
            process = subprocess.Popen(("mitmdump  -s addons.py"), shell=False)
            print(process)
        else:
            print("My function has already run.")
            process.terminate()
            del run_terminal_program__1.has_run
            process = None

    def run_terminal_program__2(e):
        e.control.selected = not e.control.selected
        e.control.update()
    # 使用subprocess.run启动终端程序
        print("运行")
        if not hasattr(run_terminal_program__2, 'has_run'):
            run_terminal_program__2.has_run = True
            print("This function will only run once.")
            global process
            process = subprocess.Popen(("mitmdump  -s addons.py"), shell=False)
        else:
            print("My function has already run.")
            process.terminate()
            del run_terminal_program__2.has_run
            process = None


    

    # 抖音页面相关
    timeCarrier = ft.Dropdown(
        label="时间载体",
        on_change=  lambda ___:   prompt("没写可以切换的代码"),
        value= "自然日",
        options=[
            ft.dropdown.Option("自然日"),
            ft.dropdown.Option("近7日"),
        ],
        width=200,)
    
    url = ft.TextField(label="URL:",width=280,multiline= True,min_lines=1,max_lines=1,text_size=10,
                       value= "compass.jinritemai.com/shop/product-detail?date_type=20&product_id=")
    sku =  ft.TextField(label="SKU",width=280,multiline = True,min_lines=1,max_lines=2,text_size=10)

    
    startFrequency = ft.Slider(
            round= 1,
            divisions=20,
            value= 0.5,
            min= 0.001,
            max=2,
            label="{value}秒",
            width=130
            
        )
    

    # 多个连接打开函数

    
    def terminateWebPrograms():
        print("发起了终止")
        global stop_flag
        print(stop_flag)
        stop_flag = False
        
        # stop_flag = True



    def openMultipleWebPages(e):
        global stop_flag
        stop_flag  =True
        
        from selenium import webdriver
        proxy = "127.0.0.1:8080"
        options = webdriver.EdgeOptions()
        # options.add_argument('--proxy-server=%s'%proxy)
        driver = webdriver.Edge(options= options)
        
        print(url.value)
        skuurls = sku.value.split(",")
        js="window.open('{}{}','_blank');"       
        
        if skuurls == []:
            pass
        else:
            driver.get("https://fxg.jinritemai.com/login/common")   

            sleep(2)
            for i in skuurls:
                # driver.get(f'{url.value}{i}')
                # driver.get("http://y.irx999.fun/up/")
                driver.execute_script(js.format(url.value,i))

                sleep(startFrequency.value)
            while True:
                
                print("等待终止程序")
                sleep(2)
                print(stop_flag)
                if stop_flag == False:
                    break
    





    #抖音数据抓取启动器
    dy_tool_1 = ft.Container(
                content=ft.Column( [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("抖音数据抓取启动器"),
                            subtitle=ft.Text(
                                "内部测试阶段,"
                            ),
                        ),
                        ft.Row([timeCarrier
                            ,
                            ft.IconButton(
                                    icon=ft.icons.NOT_STARTED,
                                    icon_size = 50,
                                    selected_icon=ft.icons.PAUSE_CIRCLE_ROUNDED,
                                    on_click=run_terminal_program__1,
                                    selected=False,
                                    style=ft.ButtonStyle(color={"selected": ft.colors.RED, "": ft.colors.GREEN})),

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
    


    # 批量链接打开工具
    dy_tool_2 = ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.OPEN_IN_BROWSER_OUTLINED),
                            title=ft.Text("批量链接打开工具"),
                            height= 40

                        ),
                        ft.Column([ft.Column([url,sku,]),
                                ft.Row([startFrequency,
                                        ft.ElevatedButton("启动",icon="WEBHOOK_OUTLINED",icon_color="green400",on_click=openMultipleWebPages),
                                        ft.IconButton(icon=ft.icons.STOP_CIRCLE_OUTLINED,icon_color="red400",on_click=lambda __:(terminateWebPrograms()))])
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
    

    # 不知道写什么工具但是好还是需要写一个占位置
    dy_tool_3= ft.Container(
                content=ft.Column( [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("不知道写什么工具但是还是需要写一个占位置"),
                            subtitle=ft.Text(
                                "内部测试阶段,"
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
                                    on_click=run_terminal_program__2,
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
    dy_tool_4 =dy_tool_3



    return ft.Column([  ft.Row([dy_tool_1,dy_tool_2,dy_tool_3],alignment=ft.MainAxisAlignment.START,),
                        ft.Row([dy_tool_4],alignment=ft.MainAxisAlignment.START,)
                     
                     ])