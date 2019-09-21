import wx
from wx import *

app = App()
frame = Frame(None, title="My new Player")
frame.Maximize()
frame.SetMinSize((1380,750))

# menubar creations

menu = MenuBar()
file = Menu()
opens = MenuItem(file, ID_OPEN, text="Open \tCtrl + O")
open_folder = MenuItem(file, ID_ANY, text="Open Folder.. \tCtrl + F")
close_window = MenuItem(file, ID_CLOSE, text="Close \tCtrl + Q")


file.Append(opens)
file.Append(open_folder)
file.Append(close_window)
menu.Append(file,"Media")
playback = Menu()
play = MenuItem(playback, ID_ANY, text="Play \tSpace")
pause = MenuItem(playback,ID_ANY, text="Pause \tSpace")
stop = MenuItem(playback,ID_ANY, text="Stop \tS")
mute = MenuItem(playback,ID_ANY, text="Mute \tM")

playback.Append(play)
playback.Append(pause)
playback.Append(stop)
playback.Append(mute)
menu.Append(playback, "Playback")
frame.SetMenuBar(menu)

# view area - panels and mainbox

panel = Panel(frame)
panel.SetBackgroundColour("#747d8c")
main = BoxSizer(VERTICAL)
background = StaticBitmap(panel,-1,Bitmap("icons/background.png"))
main.Add(background,0,EXPAND|ALL)


controls = BoxSizer(VERTICAL)
# first variable for slider area...

first = BoxSizer(HORIZONTAL)
starttime = StaticText(panel,label="00:00")
endtime = StaticText(panel,label="00:00")
slider = Slider(panel,style=SL_SELRANGE|SL_BOTH)

first.Add(starttime,0,TOP|EXPAND,border=5)
first.Add(slider,1,LEFT|RIGHT|EXPAND,border=5)
first.Add(endtime,0,TOP|EXPAND,border=5)

controls.Add(first,0,EXPAND|ALL,border=10)

# second variable for the buttons area...

second = BoxSizer(HORIZONTAL)

# buttons
playpause = BitmapButton(panel,-1,Bitmap("icons/play.png"))
previous = BitmapButton(panel,-1,Bitmap("icons/prev.png"))
backward = BitmapButton(panel,-1,Bitmap("icons/backward.png"))
stop = BitmapButton(panel,-1,Bitmap("icons/stop.png"))
forward = BitmapButton(panel,-1,Bitmap("icons/forward.png"))
next = BitmapButton(panel,-1,Bitmap("icons/next.png"))
mute = BitmapButton(panel,-1,Bitmap("icons/mute.png"))
volumeslider = Slider(panel,style=SL_SELRANGE|SL_BOTH)
fullscreen = BitmapButton(panel,-1,Bitmap("icons/fullscreen.png"))


# ctrl arrangements

second.Add(playpause,0,EXPAND|RIGHT,border=30)
second.Add(previous,0,EXPAND|ALL)
second.Add(backward,0,EXPAND|ALL)
second.Add(stop,0,EXPAND|ALL)
second.Add(forward,0,EXPAND|ALL)
second.Add(next,0,EXPAND|RIGHT,border=30)
second.Add(fullscreen,0,EXPAND|RIGHT,border=900)
second.Add(mute,0,EXPAND|ALL)
second.Add(volumeslider,0,EXPAND|TOP,border=5)


controls.Add(second,1,EXPAND|LEFT|RIGHT|BOTTOM,border=10)

main.Add(controls,1,EXPAND|ALL)

panel.SetSizer(main)
frame.Show()
app.MainLoop()