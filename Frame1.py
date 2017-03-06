#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)
 
[wxID_FRAME1, wxID_FRAME1CLICK1, wxID_FRAME1CLICK2, wxID_FRAME1CLICKPLUS, 
 wxID_FRAME1CLICKRAVNO, wxID_FRAME1PANEL1, wxID_FRAME1RADIOBOX1, 
 wxID_FRAME1STATUSBAR1, wxID_FRAME1TEXTCTRL, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(256, 125), size=wx.Size(683, 333),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(683, 333))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(683, 333),
              style=wx.TAB_TRAVERSAL)

        self.Click1 = wx.Button(id=wxID_FRAME1CLICK1, label=u'1',
              name=u'Click1', parent=self.panel1, pos=wx.Point(88, 96),
              size=wx.Size(56, 30), style=0)
        self.Click1.Bind(wx.EVT_BUTTON, self.OnClick1Button,
              id=wxID_FRAME1CLICK1)

        self.textCtrl = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL, name=u'textCtrl',
              parent=self.panel1, pos=wx.Point(120, 40), size=wx.Size(200, 27),
              style=0, value=u'')

        self.Click2 = wx.Button(id=wxID_FRAME1CLICK2, label=u'2',
              name=u'Click2', parent=self.panel1, pos=wx.Point(168, 96),
              size=wx.Size(56, 30), style=0)
        self.Click2.Bind(wx.EVT_BUTTON, self.OnClick2Button,
              id=wxID_FRAME1CLICK2)

        self.ClickPlus = wx.Button(id=wxID_FRAME1CLICKPLUS, label=u'+',
              name=u'ClickPlus', parent=self.panel1, pos=wx.Point(352, 88),
              size=wx.Size(95, 104), style=0)
        self.ClickPlus.Bind(wx.EVT_BUTTON, self.OnClickPlusButton,
              id=wxID_FRAME1CLICKPLUS)

        self.ClickRavno = wx.Button(id=wxID_FRAME1CLICKRAVNO, label=u'=',
              name=u'ClickRavno', parent=self.panel1, pos=wx.Point(88, 184),
              size=wx.Size(200, 86), style=0)
        self.ClickRavno.Bind(wx.EVT_BUTTON, self.OnClickRavnoButton,
              id=wxID_FRAME1CLICKRAVNO)

        self.radioBox1 = wx.RadioBox(choices=['1', '23', '46'],
              id=wxID_FRAME1RADIOBOX1, label=u'radioBox1', majorDimension=1,
              name='radioBox1', parent=self.panel1, pos=wx.Point(504, 112),
              size=wx.Size(71, 96), style=wx.RA_SPECIFY_COLS)
        self.radioBox1.Bind(wx.EVT_RADIOBOX, self.OnRadioBox1Radiobox,
              id=wxID_FRAME1RADIOBOX1)

        

    def __init__(self, parent):
        self._init_ctrls(parent)
 
    def OnClick1Button(self, event):
        #event.Skip()
        self.textCtrl.SetValue(self.textCtrl.GetValue()+'1')
 
    def OnClick2Button(self, event):
        #event.Skip()
        self.textCtrl.SetValue(self.textCtrl.GetValue()+'2')
 
    def OnClickPlusButton(self, event):
        #event.Skip()
        self.textCtrl.SetValue(self.textCtrl.GetValue()+'+')
 
    def OnClickRavnoButton(self, event):
        #event.Skip()
        self.textCtrl.SetValue(str(eval(self.textCtrl.GetValue())))
 
    def OnRadioBox1Radiobox(self, event):
        #event.Skip()
        self.textCtrl.SetValue(self.textCtrl.GetValue())
   
