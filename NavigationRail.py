
import flet as ft

name = "NavigationRail Example"

def NavigationRail(page:ft.Page):

    page2 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "页面2",on_click= lambda __: print(123))
    def a():
        page2.text = 123
    
    pagelist = [ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("页面一功能开发区域"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen",on_click= lambda: [setattr(page2, 'text', 123), page.update()][0])],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            ),page2]
    card = ft.Card(pagelist[0])
    
    def modifyingPages(e):
        global page1
        card.content = pagelist[e.control.selected_index]
        print(e.control.selected_index)
        page.update()
        
        


    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
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
    
