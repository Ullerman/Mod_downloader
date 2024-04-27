from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
import kivymd.icon_definitions
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText, MDTextFieldLeadingIcon
import os,sys
from mod_downloader import download_mods
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window




screen_width, screen_height = Window.size

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Config.set('graphics', 'width', str(screen_width))
Config.set('graphics', 'height', str(screen_height))




home_directory = os.path.expanduser("~")
global minecraft_mods_directory
minecraft_mods_directory = os.path.join(home_directory,"AppData","Roaming", ".minecraft", "mods")
button_released = False
class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"
   
        screen = MDScreen(
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="subdirectory-arrow-right",
                ),
                MDTextFieldHintText(
                    text=f"{minecraft_mods_directory}",
                ),

                mode="outlined",
                size_hint_x=None,
                width="440dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            MDButton(
                MDButtonIcon(
                    icon="folder",
                ),
                MDButtonText(
                    text="Select Directory",
                ),
                style="elevated",
                pos_hint={"center_x": 0.5, "center_y": 0.4},
                on_release=self.select_directory,
            ),
            MDButton(
                MDButtonIcon(
                    icon="download-box-outline",
                ),
                MDButtonText(
                    text="Download",
                ),
                style="elevated",
                pos_hint={"center_x": 0.5, "center_y": 0.3},
                on_release= lambda x: download_mods(minecraft_mods_directory) if button_released == False else None,
            ),
            md_bg_color=self.theme_cls.backgroundColor,
        )
        return screen
        
    def select_directory(self, *args):
        layout = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(path=home_directory)
        layout.add_widget(filechooser)

        popup = Popup(title="Select Directory", content=layout, size_hint=(0.9, 0.9))

        select_button = MDButton(MDButtonText(text='Select'), size_hint=(1, 0.1))
        select_button.bind(on_release=lambda x: self.on_directory_select(filechooser.path, popup=popup))
        layout.add_widget(select_button)

        popup.open()

    def on_directory_select(self, selection, popup):
        
        print(f"Selected directory: {selection}")
        global minecraft_mods_directory
        minecraft_mods_directory = selection
        popup.dismiss()

        
        
        
                

        


Example().run()