
import flet as ft

name = "NavigationRail Example"

def NavigationRail(page:ft.Page):
    
    page1 = ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "12312312312")
    def modifyingPages(e):
        
        page1.text = e.control.selected_index
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
                ft.ElevatedButton(icon=ft.icons.SETTINGS,text= "123"),
                page1 
               
            ],
            expand=True,
            alignment= ft.alignment.center_left
        )
    
