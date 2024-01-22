
import flet as ft
import pyperclip
name = "NavigationRail Example"
from time import sleep
process  =None

stop_flag =True
customPrompt = ft.Text(
            "这是第二个页面的"
            ,size= 30,

        )


def NavigationRail(page:ft.Page):


    

    




    #关闭 banner
    def close_banner(e):
        page.banner.open = False
        page.update()
    

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
        global customPrompt
        customPrompt.value =  a
        page.banner.open = True
        page.update()
        sleep(3)
        page.banner.open = False
        page.update()


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


    import douyinpage
    douyinpage  = douyinpage.douyinpage(page)
    
               
    page1 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "页面2",on_click= lambda __: (setattr(page3, 'text', 123), page.update()))
    
    page3 = page0
    
    pagelist = [page0,
                page1,
                douyinpage,
                page3]
    card = ft.Container(pagelist[0],alignment=ft.alignment.top_center,
                        # bgcolor= ft.colors.AMBER,
                        # height= 700,width= 1317,expand= True
                        )
    # 切换页面 函数
    def modifyingPages(e):
        card.content = pagelist[e.control.selected_index+1]
        print(e.control.selected_index)
        page.update()
        
        
    
    # 侧边栏# 
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
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.TIKTOK,
                selected_icon=ft.icons.TIKTOK_OUTLINED, label="抖音"
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
        
    
