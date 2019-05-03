import wx, wx.media
from wx import *

app = App()
root = Frame(None, title="Jayant Player", size=(1000,600))
panel = Panel(root)
root.timer = wx.Timer(root)

def ontimer(e):
    if root.video.GetState() == 1 or root.video.GetState() == 2:
        currenttime = root.video.Tell()/1000
        slider.SetValue(currenttime)
        nmin = int(currenttime//60)
        nsec = int(currenttime%60)
        if nmin < 10:
            nowm = str("0"+str(nmin))
        else:
            nowm = str(nmin)
        if nsec < 10:
            nows = str("0"+str(nsec))
        else:
            nows = str(nsec)
        current.SetLabel(nowm+":"+nows)
        totaltime = root.video.Length()/1000
        slider.SetMax(totaltime)
        minute = int(totaltime//60)
        sec = int(totaltime%60)
        if minute < 10:
            tmin = str("0"+str(minute))
        else:
            tmin = str(minute)
        if sec < 10:
            tsec = str("0"+str(sec))
        else:
            tsec = str(sec)
        total.SetLabel(tmin+":"+tsec)


root.Bind(EVT_TIMER,ontimer)
root.timer.Start(0)

def play_video(event):
    if root.video.GetState() == 2:
        root.video.Pause()
        play.SetBitmap(Bitmap("icon/play.png"))
    else:
        root.video.Play()
        root.video.SetVolume(float("0." + str(volume.GetValue())))
        play.SetBitmap(Bitmap("icon/pause.png"))

def stop_play(event):
    root.video.Stop()
    slider.SetValue(0)
    current.SetLabel("--:--")
    total.SetLabel("--:--")
    play.SetBitmap(Bitmap("icon/play.png"))

def open_file(event):
    file = FileDialog(panel,"Open",wildcard="*mp4")
    if file.ShowModal() == ID_OK:
        root.video.Load(file.GetPath())

def quit_win(event):
    root.Close()

def sound_ctrl(event):
    if root.video.GetVolume() > 0.0:
        root.video.SetVolume(0)
        volume.SetValue(0)
        sound.SetBitmap(Bitmap("icon/mute.jpg"))
    else:
        root.video.SetVolume(0.3)
        volume.SetValue(3)
        sound.SetBitmap(Bitmap("icon/volume.jpg"))

def volume_ctrl(event):
    if root.video.GetVolume() > 0.0:
        sound.SetBitmap(Bitmap("icon/volume.jpg"))
    else:
        sound.SetBitmap(Bitmap("icon/mute.jpg"))
    if volume.GetValue() < 10:
        root.video.SetVolume(float("0."+str(volume.GetValue())))
    else:
        root.video.SetVolume(1.0)


def move_time(event):
    root.video.Seek(slider.GetValue()*1000)

def forward(event):
    root.video.Seek(root.video.Tell()+10000)

def backward(event):
    root.video.Seek(root.video.Tell()-10000)


menubar = MenuBar()
media = Menu()
playback = Menu()
audio = Menu()
video = Menu()
subtitle = Menu()
tools = Menu()
view = Menu()
help = Menu()

menubar.Append(media,"Media")
menubar.Append(playback,"Playback")
menubar.Append(audio,"Audio")
menubar.Append(video,"Video")
menubar.Append(subtitle,"Subtitle")
menubar.Append(tools,"Tools")
menubar.Append(view,"View")
menubar.Append(help,"Help")

open = media.Append(1,"Open File...\tCtrl+O")
media.Bind(EVT_MENU,open_file,open)
openmulti = media.Append(ID_ANY,"Open Multiple Files...\tCtrl+Shift+O")
openfolder = media.Append(ID_ANY,"Open Folder...\tCtrl+F")
Opendisk = media.Append(ID_ANY,"Open Disk...\tCtrl+D")
quit = media.Append(ID_EXIT,"Quit\tCtrl+Q")
media.Bind(EVT_MENU,quit_win,quit)

mainbox = BoxSizer(VERTICAL)

root.video = wx.media.MediaCtrl(panel,1,szBackend=wx.media.MEDIABACKEND_WMP10)
root.Bind(wx.media.EVT_MEDIA_LOADED,play_video)
mainbox.Add(root.video,7,ALL|EXPAND)

slide = BoxSizer(HORIZONTAL)
current = StaticText(panel,label="--:--")
slide.Add(current,0,ALL)

slider = Slider(panel,minValue=0,value=0,maxValue=100,style=SL_HORIZONTAL)
slider.Bind(EVT_SLIDER,move_time,slider)
slide.Add(slider,1,EXPAND|ALL,border=2)

total = StaticText(panel,label="--:--")
slide.Add(total,0,ALL)
mainbox.Add(slide,0,EXPAND|ALL,border=10)

footer = BoxSizer(HORIZONTAL)
play = BitmapButton(panel,-1,Bitmap("icon/play.png"))
play.Bind(EVT_BUTTON,play_video,play)
footer.Add(play,0,ALL)

spback = BitmapButton(panel,-1,Bitmap("icon/swipeback.png"))
spback.Bind(EVT_BUTTON,backward,spback)
stop = BitmapButton(panel,-1,Bitmap("icon/stop.png"))
stop.Bind(EVT_BUTTON,stop_play,stop)
spfor = BitmapButton(panel,-1,Bitmap("icon/swipefor.png"))
spfor.Bind(EVT_BUTTON,forward,spfor)
footer.AddMany([
    (spback,0,ALL),(stop,0,ALL),(spfor,0,ALL)
])

sound = BitmapButton(panel,-1,Bitmap("icon/volume.jpg"))
sound.Bind(EVT_BUTTON,sound_ctrl,sound)
footer.Add(sound,0,ALL)

volume = Slider(panel,minValue=0,value=3,maxValue=10,style=SL_HORIZONTAL)
volume.Bind(EVT_SLIDER,volume_ctrl,volume)
footer.Add(volume,0,ALL)
mainbox.Add(footer,0,border=10)

panel.SetSizer(mainbox)
root.SetMenuBar(menubar)
root.Show()
app.MainLoop()
