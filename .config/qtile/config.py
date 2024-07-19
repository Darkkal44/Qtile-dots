# ASCII Art from https://www.asciiart.eu/text-to-ascii-art (ANSI-Shadow, Two-lines Frame[V.Padding=1, H.Padding=1], Bash Comment:#)

#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░
#
#                                                                                    - DARKKAL44
<<<<<<< HEAD
<<<<<<< HEAD
  

=======
<<<<<<< HEAD
>>>>>>> e31c2f498b1c4660bf26a5aee0604bf432355330

=======
>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440
=======
  

>>>>>>> parent of 59c16d9 (Synced:)

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
<<<<<<< HEAD
<<<<<<< HEAD
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
<<<<<<< HEAD
from libqtile import hook
from pathlib import Path
=======
from libqtile import hook
>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440
import os
import subprocess
=======
from time import sleep
>>>>>>> parent of 59c16d9 (Synced:)
=======
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep
>>>>>>> parent of 59c16d9 (Synced:)

mod = "mod4"
terminal = "alacritty"
home = str(Path.home())

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======

# ASCII Art from https://www.asciiart.eu/text-to-ascii-art (ANSI-Shadow, Two-lines Frame[V.Padding=1, H.Padding=1], Bash Comment:#)
>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440
>>>>>>> e31c2f498b1c4660bf26a5aee0604bf432355330
# /==================================================================\
# ||                                                                ||
# || ██╗  ██╗███████╗██╗   ██╗██████╗ ██╗███╗   ██╗██████╗ ███████╗ ||
# || ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔══██╗██╔════╝ ||
# || █████╔╝ █████╗   ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ██║███████╗ ||
# || ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║██║╚██╗██║██║  ██║╚════██║ ||
# || ██║  ██╗███████╗   ██║   ██████╔╝██║██║ ╚████║██████╔╝███████║ ||
# || ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝ ||
# ||                                                                ||
# \==================================================================/
=======
# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█


>>>>>>> parent of 59c16d9 (Synced:)
=======
# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█


>>>>>>> parent of 59c16d9 (Synced:)


keys = [

    # Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),

    # Move
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Swap
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),

    # Size/Grow
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),

    # Split
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # System
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='Open Powermenu'),
    Key([mod, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='Select Themes'),
    Key([mod, "control"], "m", lazy.spawn("code Themes/Cozy/.config/qtile/config.py"), desc="Open Qtile Config"),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Browser"),
    Key([mod],"e", lazy.spawn("thunar"), desc='Launch File Manager'),
    Key([mod], "v", lazy.spawn("roficlip"), desc='Launch Clipboard History'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),


# C U S T O M

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
]

<<<<<<< HEAD
# jocim's keybinds
# keys = [

<<<<<<< HEAD
<<<<<<< HEAD
=======
#     # Focus
#     Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
#     Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
#     Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
#     Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
#     Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),

#     # Move
#     Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
#     Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
#     Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
#     Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

#     # Swap
#     Key([mod, "shift"], "h", lazy.layout.swap_left()),
#     Key([mod, "shift"], "l", lazy.layout.swap_right()),

#     # Size/Grow
#     Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
#     Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
#     Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
#     Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
#     Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

#     # Floating
#     Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),

#     # Split
#     Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

#     # Toggle Layouts
#     Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

#     # Fullscreen
#     Key([mod], "f", lazy.window.toggle_fullscreen()),

#     # System
#     Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
#     Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
#     Key([mod, "control"], "q", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='Open Powermenu'),
#     Key([mod, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
#     Key([mod, "control"], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='Select Themes'),
#     Key([mod, "control"], "m", lazy.spawn("code Themes/Cozy/.config/qtile/config.py"), desc="Open Qtile Config"),

#     # Apps
#     Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
#     Key([mod, "control"], "Return", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
#     Key([mod], "b", lazy.spawn("firefox"), desc="Launch Browser"),
#     Key([mod],"e", lazy.spawn("thunar"), desc='Launch File Manager'),
#     Key([mod], "v", lazy.spawn("roficlip"), desc='Launch Clipboard History'),
#     Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
=======
>>>>>>> parent of 59c16d9 (Synced:)

<<<<<<< HEAD
=======

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

<<<<<<< HEAD
#     Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
#     Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
#     Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
#     Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
#     Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
#     Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
#     Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
#     Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
# ]


>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440
>>>>>>> e31c2f498b1c4660bf26a5aee0604bf432355330
# /========================================================\
# ||                                                      ||
# ||  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗  ||
# || ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝  ||
# || ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗  ||
# || ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║  ||
# || ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║  ||
# ||  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝  ||
# ||                                                      ||
# \========================================================/
=======

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

>>>>>>> parent of 59c16d9 (Synced:)
=======
>>>>>>> parent of 59c16d9 (Synced:)


groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]

for i in groups:
    keys.extend(
<<<<<<< HEAD
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        ]
    )
=======
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )
>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440




# L A Y O U T S


<<<<<<< HEAD


layouts = [
<<<<<<< HEAD
    layout.Columns(
        margin= [0,2,5,2],
        border_focus='#FFFFFF',
        border_normal='#1F1D2E',
        border_width=3,
        radius=1,
=======
    layout.Columns( margin=10, border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        border_width=0
>>>>>>> parent of 59c16d9 (Synced:)
=======


# L A Y O U T S




layouts = [
    layout.Columns( margin=10, border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        border_width=0
>>>>>>> parent of 59c16d9 (Synced:)
    ),

    # layout.Max(	
    #     border_focus='#1F1D2E',
    #     border_normal='#1F1D2E',
    #     margin=10,
    #     border_width=0,
    # ),

    # layout.Floating(	
    #     border_focus='#1F1D2E',
    #     border_normal='#1F1D2E',
    #     margin=10,
    #     border_width=0,
    # ),
    # Try more layouts by unleashing below layouts
<<<<<<< HEAD
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    # layout.Matrix(	
        # border_focus='#1F1D2E',
        # border_normal='#1F1D2E',
        # margin=10,
        # border_width=0,
    # ),
    # layout.MonadTall(	
        # border_focus='#1F1D2E',
        # border_normal='#1F1D2E',
        # margin=10,
        # border_width=0,
    # ),
    # layout.MonadWide(	
        # border_focus='#1F1D2E',
        # border_normal='#1F1D2E',
        # margin=10,
        # border_width=0,
    # ),
    #  layout.RatioTile(),
    # layout.Tile(	
        # border_focus='#1F1D2E',
        # border_normal='#1F1D2E',
    # ),
    #  layout.TreeTab(),
    #  layout.VerticalTile(),
    #  layout.Zoomy(),
=======
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
     layout.Matrix(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),
     layout.MonadTall(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        margin=4,
	    border_width=0,
	),
    layout.MonadWide(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),
   #  layout.RatioTile(),
     layout.Tile(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
>>>>>>> parent of 59c16d9 (Synced:)
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy()
        ]



def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
=======


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄



>>>>>>> parent of 59c16d9 (Synced:)
=======
def audio():
    qtile.cmd_spawn("pavucontrol")
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 59c16d9 (Synced:)



# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄



<<<<<<< HEAD
#                 widget.Image(
#                     filename='~/.config/qtile/Assets/6.png',
#                 ),


#                 widget.GroupBox(
#                     fontsize=24,
#                     borderwidth=3,
#                     highlight_method='block',
#                     active='#CAA9E0',
#                     block_highlight_text_color="#91B1F0",
#                     highlight_color='#4B427E',
#                     inactive='#282738',
#                     foreground='#4B427E',
#                     background='#353446',
#                     this_current_screen_border='#353446',
#                     this_screen_border='#353446',
#                     other_current_screen_border='#353446',
#                     other_screen_border='#353446',
#                     urgent_border='#353446',
#                     rounded=True,
#                     disable_drag=True,
#                  ),


#                 widget.Spacer(
#                     length=8,
#                     background='#353446',
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/1.png',
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/layout.png',
#                     background="#353446"
#                 ),


#                 widget.CurrentLayout(
#                     background='#353446',
#                     foreground='#CAA9E0',
#                     fmt='{}',
#                     font="JetBrains Mono Bold",
#                     fontsize=13,
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/5.png',
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/search.png',
#                     margin=2,
#                     background='#282738',
#                     mouse_callbacks={"Button1": search},
#                 ),

#                 widget.TextBox(
#                     fmt='Search',
#                     background='#282738',
#                     font="JetBrains Mono Bold",
#                     fontsize=13,
#                     foreground='#CAA9E0',
#                     mouse_callbacks={"Button1": search},
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/4.png',
#                 ),


#                 widget.WindowName(
#                     background = '#353446',
#                     format = "{name}",
#                     font='JetBrains Mono Bold',
#                     foreground='#CAA9E0',
#                     empty_group_string = 'Desktop',
#                     fontsize=13,

#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/3.png',
#                 ),


#                 widget.Systray(
#                     background='#282738',
#                     fontsize=2,
#                 ),


#                 widget.TextBox(
#                     text=' ',
#                     background='#282738',
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/6.png',
#                     background='#353446',
#                 ),


#                 # widget.Image(
#                 # filename='~/.config/qtile/Assets/Drop1.png',
#                 # ),

#                 # widget.Net(
#                 # format=' {up}   {down} ',
#                 # background='#353446',
#                 # foreground='#CAA9E0',
#                 # font="JetBrains Mono Bold",
#                 # prefix='k',
#                 # ),

#                 # widget.Image(
#                     # filename='~/.config/qtile/Assets/2.png',
#                 # ),

#                 # widget.Spacer(
#                     # length=8,
#                     # background='#353446',
#                 # ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/Misc/ram.png',
#                     background='#353446',
#                 ),


#                 widget.Spacer(
#                     length=-7,
#                     background='#353446',
#                 ),


#                 widget.Memory(
#                     background='#353446',
#                     format='{MemUsed: .0f}{mm}',
#                     foreground='#CAA9E0',
#                     font="JetBrains Mono Bold",
#                     fontsize=13,
#                     update_interval=5,
#                 ),


#                 # widget.Image(
#                 # filename='~/.config/qtile/Assets/Drop2.png',
#                 # ),


>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440

#                 widget.Image(
#                     filename='~/.config/qtile/Assets/2.png',
#                 ),


#                 widget.Spacer(
#                     length=8,
#                     background='#353446',
#                 ),


#                 widget.BatteryIcon(
#                     theme_path='~/.config/qtile/Assets/Battery/',
#                     background='#353446',
#                     scale=1,
#                 ),


#                 widget.Battery(
#                     font='JetBrains Mono Bold',
#                     background='#353446',
#                     foreground='#CAA9E0',
#                     format='{percent:2.0%}',
#                     fontsize=13,
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/2.png',
#                 ),


#                 widget.Spacer(
#                     length=8,
#                     background='#353446',
#                 ),


#                 # widget.Battery(format=' {percent:2.0%}',
#                     # font="JetBrains Mono ExtraBold",
#                     # fontsize=12,
#                     # padding=10,
#                     # background='#353446',
#                 # ),

#                 # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
#                     # font="JetBrains Mono Bold",
#                     # fontsize=12,
#                     # padding=10,
#                     # background='#4B4D66',
#                 # ),

#                 widget.Volume(
#                     font='JetBrainsMono Nerd Font',
#                     theme_path='~/.config/qtile/Assets/Volume/',
#                     emoji=True,
#                     fontsize=13,
#                     background='#353446',
#                 ),


#                 widget.Spacer(
#                     length=-5,
#                     background='#353446',
#                     ),


#                 widget.Volume(
#                     font='JetBrains Mono Bold',
#                     background='#353446',
#                     foreground='#CAA9E0',
#                     fontsize=13,
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/5.png',
#                     background='#353446',
#                 ),


#                 widget.Image(
#                     filename='~/.config/qtile/Assets/Misc/clock.png',
#                     background='#282738',
#                     margin_y=6,
#                     margin_x=5,
#                 ),


#                 widget.Clock(
#                     format='%I:%M %p',
#                     background='#282738',
#                     foreground='#CAA9E0',
#                     font="JetBrains Mono Bold",
#                     fontsize=13,
#                 ),


#                 widget.Spacer(
#                     length=18,
#                     background='#282738',
#                 ),



#             ],
#             30,
#             border_color = '#282738',
#             border_width = [0,0,0,0],
#             margin = [15,60,6,60],

#         ),
#     ),
# ]

# jocim's config
>>>>>>> e31c2f498b1c4660bf26a5aee0604bf432355330
=======
>>>>>>> parent of 59c16d9 (Synced:)
screens = [

    Screen(
        top=bar.Bar(
            [
				widget.Spacer(length=15,
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#E5B9C6',
                    block_highlight_text_color="#CFB3E5",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),


                widget.CurrentLayout(
                    background='#353446',
                    foreground='#E5B9C6',
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#E5B9C6',
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#E5B9C6',
                    empty_group_string = 'Desktop',

                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),


                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),


                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),


                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop1.png',
                # ),

                # widget.Net(
                # format=' {up}   {down} ',
                # background='#353446',
                # foreground='#E5B9C6',
                # font="JetBrains Mono Bold",
                # prefix='k',
                # ),

                # widget.Image(
                    # filename='~/.config/qtile/Assets/2.png',
                # ),

                # widget.Spacer(
                    # length=8,
                    # background='#353446',
                # ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                ),


                widget.Spacer(
                    length=-7,
                    background='#353446',
                ),


                widget.Memory(
                    background='#353446',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#E5B9C6',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),

    
                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background='#353446',
                    scale=1,
                ),


                widget.Battery(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background='#353446',
                    foreground='#E5B9C6',
                    format='{percent:2.0%}',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                # widget.Battery(format=' {percent:2.0%}',
                    # font="JetBrains Mono ExtraBold",
                    # fontsize=12,
                    # padding=10,
                    # background='#353446',
                # ),

                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                    # font="JetBrains Mono Bold",
                    # fontsize=12,
                    # padding=10,
                    # background='#4B4D66',
                # ),

                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background='#353446',
                ),


                widget.Spacer(
                    length=-5,
                    background='#353446',
                    ),


                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background='#353446',
                    foreground='#E5B9C6',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#282738',
                    foreground='#E5B9C6',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background='#282738',
                ),



            ],
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [15,60,6,60],

        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('.config/qtile/autostart_once.sh')])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



<<<<<<< HEAD
<<<<<<< HEAD
@hook.subscribe.startup_once
def autostart_once():
    autostartscript = "~/.config/qtile/autostart_once.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
=======
<<<<<<< HEAD
# E O F
>>>>>>> parent of 59c16d9 (Synced:)
=======

@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('.config/qtile/autostart_once.sh')])

# E O F
>>>>>>> 59c16d9292c711cd50974fcaede9d2e007f24440
>>>>>>> e31c2f498b1c4660bf26a5aee0604bf432355330
=======
# E O F
>>>>>>> parent of 59c16d9 (Synced:)
