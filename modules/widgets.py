from libqtile import widget
from libqtile import qtile

colors = [
    ["#282c34", "#282c34"], # panel background
    ["#3d3f4b", "#434758"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font color for group names
    ["#ff5555", "#ff5555"], # border line color for current tab
    ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
    ["#e1acff", "#e1acff"], # window name
    ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
] 
widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=3,
)
icon_ = [
    ["/usr/share/icons/ePapirus-Dark/symbolic/status/display-brightness-off-symbolic.svg"],
    ["/usr/share/icons/ePapirus-Dark/symbolic/status/display-brightness-low-symbolic.svg"],
    ["/usr/share/icons/ePapirus-Dark/symbolic/status/display-brightness-medium-symbolic.svg"],
    ["/usr/share/icons/ePapirus-Dark/symbolic/status/display-brightness-high-symbolic.svg"],
]

extension_defaults = widget_defaults.copy()
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '󰆪'
        elif self.volume <= 35:
            self.text = ''
        elif self.volume < 75:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '󰆪'
        elif self.volume <= 35:
            self.text = ''
        elif self.volume < 75:
            self.text = ''
        else:
            self.text = ''
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize=32,
    font='Font Awesome 5 Free',
    foreground=colors[4],
    background='#2f343f',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

# class MyBrightness(widget.Brightness):
#     def _configure(self, qtile, bar):
#         widget.Brightness._configure(self, qtile, bar)
#         self.brightness = self.get_brightness()
#         if self.brightness <= 0:
#             self.filename = icon_[0]
#         elif self.brightness <= 35:
#             self.filename = icon_[1]
#         elif self.brightness < 75:
#             self.filename = icon_[2]
#         else:
#             self.filename = icon_[3]
#         # drawing here crashes Wayland

#     def _update_drawer(self, wob=False):
#         if self.brightness <= 0:
#             self.filename = icon_[0]
#         elif self.brightness <= 35:
#             self.filename = icon_[1]
#         elif self.brightness < 75:
#             self.filename = icon_[2]
#         else:
#             self.filename = icon_[3]
#         self.draw()

#         if wob:
#             with open(self.wob, 'a') as f:
#                 f.write(str(self.brightness) + "\n")

# brightness = MyBrightness(
#     fontsize=32,
#     foreground=colors[4],
#     background='#2f343f',
# )