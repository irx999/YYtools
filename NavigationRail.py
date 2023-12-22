
import flet as ft

name = "NavigationRail Example"

process  =None
def NavigationRail(page:ft.Page):

    import subprocess

    def run_terminal_program(e):
    # 使用subprocess.run启动终端程序
        print("运行")
        if not hasattr(run_terminal_program, 'has_run'):
            run_terminal_program.has_run = True
            print("This function will only run once.")
            global process
            process = subprocess.Popen(("mitmdump  -s addons.py"), shell=False)
        else:
            print("My function has already run.")
            process.terminate()
            del run_terminal_program.has_run
            process = None



    page0 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "主页面",on_click= lambda __: print("页面按钮被按下"))
    page1 = ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("抖音数据抓取启动器"),
                            subtitle=ft.Text(
                                "内部测试阶段,"
                            ),
                        ),
                        ft.Row([
                            ft.TextButton("启动",on_click= run_terminal_program), 
                            ft.TextButton("关闭",on_click= run_terminal_program)
                             ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                height=300,
                padding=10,
                alignment= ft.alignment.center_right
            )

    page2 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "页面2",on_click= lambda __: (setattr(page3, 'text', 123), page.update()))
    page3 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "页面3",on_click= lambda __: print("页面按钮被按下"))
    

    
    pagelist = [page0,
                page1,
                page2,
                page3
            ]
    card = ft.Card(pagelist[0])
    
    def modifyingPages(e):
        card.content = pagelist[e.control.selected_index+1]
        print(e.control.selected_index)
        page.update()
        
        


    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        leading=ft.FloatingActionButton(icon=ft.icons.DATASET_ROUNDED, text="主页面",on_click= lambda __: (setattr(card,"content",pagelist[0]),page.update())),
        group_alignment=1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
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
                ft.VerticalDivider(width=0),
                
                card
               
            ],
            expand=True,
            alignment= ft.alignment.center_left
        )
    
