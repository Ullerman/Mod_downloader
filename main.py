from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText, MDTextFieldLeadingIcon
import os,sys
from mod_downloader import download_mods
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
Config.set('input', 'mouse', 'mouse,disable_multitouch')




home_directory = os.path.expanduser("~")
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
                    icon="download-box-outline",
                ),
                MDButtonText(
                    text="Download",
                ),
                style="elevated",
                pos_hint={"center_x": 0.5, "center_y": 0.4},
                on_release= lambda x: download_mods() if button_released == False else None,
            ),
            md_bg_color=self.theme_cls.backgroundColor,
            )

        
        return screen
        
                

        


Example().run()