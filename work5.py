import wx
import windowstest
import codecs
import wx.xrc
import wx.richtext
import sys

class MyWindows1(windowstest.MyFrame8):
    def p5(self,event):
        w=wx.App() #建立應用
        p=windowstest.MyDialog3(None) #括號內的值是要不要顯示上層視窗 p=由wxFormBuilder產生的class返回的變數
        p.Show() #顯示視窗
        # p.SetTitle("關於作者")
        w.MainLoop() #讓視窗持續顯示

    def p1( self, event ):#建立檔案
        self.m_textCtrl7.SetValue("")

    def p2(self,event):# 開啟檔案
        path=wx.FileSelector("請問要開啟的檔案",wildcard="文字檔案 (*.txt)|*.txt",flags=wx.FD_OPEN)

    def p3( self, event ):#儲存檔案
        path=wx.FileSelector("請問要儲存的檔名",wildcard="文字檔案 (*.txt)|*.txt",flags=wx.FD_SAVE)

    def p4( self, event ):#關閉程式
        sys.exit()

    # def timee( self, event ):
    #     txt=self.m_textCtrl6.GetValue()
    #     if txt !="" and txt.find("@")==-1:
    #         self.m_staticText2.SetLabel("email格式錯誤")
    #     elif txt !="":
    #         self.m_staticText2.SetLabel("email格式正確")
    #     else:
    #         self.m_staticText2.SetLabel("請輸入E-mail")

w=wx.App() #建立應用
p=MyWindows1(None) #括號內的值是要不要顯示上層視窗 p=由wxFormBuilder產生的class返回的變數
p.Show() #顯示視窗
p.SetTitle("記事本")
w.MainLoop() #讓視窗持續顯示










 # self.SetTitle("標題文字")
        # self.m_button20.SetLabel("HI 你好")
        # wx.MessageBox(self.m_button20.GetLabel)
        # self.m_filePicker2.SetPath("C:")
        # self.m_button20.SetLabel("我更新了")
        # self.m_comboBox2.Append("設定的資料")
        # wx.MessageBox(self.m_filePicker2.GetPath())
        # self.m_grid3.AppendCols(2)
        # self.m_grid3.SetColLabelValue(0, "標題1")
        # self.m_grid3.SetColLabelValue(1, "標題2")
        # self.m_grid3.SetColLabelValue(2, "標題3")
        # self.m_grid3.SetColLabelValue(3, "標題4")
        # self.m_grid3.AppendRows(2)
        # self.m_grid3.SetRowLabelValue(0, "標題1")
        # self.m_grid3.SetRowLabelValue(1, "標題2")
        # self.m_grid3.SetRowLabelValue(2, "標題3")
        # self.m_grid3.SetRowLabelValue(3, "標題4")
        # s=self.m_scrolledWindow4.GetSize()
        # self.m_grid3.SetSize(s[0]-100,s[1]-50)
        #wx.MessageBox(str())