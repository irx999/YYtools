
import flet as ft
import pyperclip
name = "NavigationRail Example"
from time import sleep
process  =None

stop_flag =True



def NavigationRail(page:ft.Page):


    #键盘事件部分

    def on_keyboard(e: ft.KeyboardEvent):
        
        if e.key ==shortcutKey.value:
            clipboard_content = pyperclip.paste ()
            number_list = clipboard_content.split()  # 将字符串分割成列表
            unique_numbers = []
            for num in number_list:
                if num not in unique_numbers:
                    unique_numbers.append(num)

            result = ",".join(unique_numbers)  # 用逗号连接列表中的元素
            pyperclip.copy(result)
            prompt(f"已经成功复制\n{result}")
            sleep(2)
            page.banner.open = False
            
            page.update()

    page.on_keyboard_event = on_keyboard




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




    refresh_frequency = ft.Slider(
            round= 0,
            divisions=5,
            value= 30,
            min= 1,
            max=120,
            label="{value}分",
            width=200
            
        )
























    #关闭 banner
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
    
    #键盘切换
    shortcutKey = ft.Dropdown(
        label="快捷键",
        on_change=  lambda ___:   prompt("快捷键已经切换"),
        value= "F2",
        options=[
            ft.dropdown.Option("F1"),
            ft.dropdown.Option("F2"),
        ],
        width=200,
    )

    
    
    



    page0 = ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Column([ft.Text("数据净化"),shortcutKey]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
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
    dy_tool_3= ft.Container(
                content=ft.Column( [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("售后数据抓取器"),
                            subtitle=ft.Text(
                                "内部测试阶段,"
                            ),
                        ),
                        ft.Column([ft.TextField(label="机器人推送链接",width=280)
                            ,
                            ft.Row([refresh_frequency
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

    page0 = ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Column([ft.Text("数据净化"),shortcutKey]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    page1 = ft.Row([dy_tool_1,dy_tool_2,dy_tool_3],
                alignment=ft.MainAxisAlignment.CENTER,)
               
    page2 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "页面2",on_click= lambda __: (setattr(page3, 'text', 123), page.update()))
    
    page3 = page0
    
    pagelist = [page0,
                page1,
                page2,
                page3]
    card = ft.Container(pagelist[0],alignment=ft.alignment.top_left,
                        # bgcolor= ft.colors.AMBER,
                        # height= 700,width= 1031,expand= False
                        )
    
    def modifyingPages(e):
        card.content = pagelist[e.control.selected_index+1]
        print(e.control.selected_index)
        page.update()
        
        
    

    rail = ft.NavigationRail(
        # selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        leading=ft.FloatingActionButton(icon=ft.icons.DATASET_ROUNDED, text="主页面",on_click= lambda __: 
                                        (setattr(card,"content",pagelist[0]), setattr(rail,"selected_index",None)   ,page.update())),
        group_alignment=1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.TIKTOK,
                selected_icon=ft.icons.TIKTOK_OUTLINED, label="抖音"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        # on_change=lambda e: print("Selected destination:", e.control.selected_index),
        on_change= modifyingPages
        
    )

    return    ft.Row(
            [
                rail,
                ft.VerticalDivider(width=2),
                
                card
               
            ],
            expand=True,
            alignment= ft.MainAxisAlignment.START
        )
        
    
