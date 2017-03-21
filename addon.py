import xbmcaddon
import xbmcgui
 
class RateWindow(xbmcgui.WindowDialog):
  def __init__(self)
    addonname = xbmcaddon.Addon()getAddonInfo('name')
    self.title_bar = xbmcgui.ControlLabel(-10, -10, 1, 1, addonname, alignment=ALIGN_CENTER)
    self.addControl(self.title_bar)
    self.setAnimation(self.title_bar)


if __name__ == '__main__':
  #window = RateWindow()
  #window.show()
  xbmc.executebuiltin(Action(setrating[,musicosd])




