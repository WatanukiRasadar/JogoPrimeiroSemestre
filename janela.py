import wx
def janela(Pergunta,Respostas,certa):
    class Perguntas(wx.Frame):
        def __init__(self,parent,id):
            wx.Frame.__init__(self,parent,id,"Perguntas",size=(500,300),style=wx.CAPTION|wx.MINIMIZE_BOX)
            self.panel=wx.Panel(self)
            wx.StaticText(self.panel,1,Pergunta,(30,30))
            self.resposta=wx.ComboBox(self.panel,5,"Escolha a sua resposta",(30,90),(300,-1),choices=Respostas,style=wx.CB_READONLY)
            self.button=wx.Button(self.panel,9,"confirmar",(200,200))

    if __name__=="__main__":
        app=wx.App()
        frame=Perguntas(parent=None,id=999)
        frame.Show()
        app.MainLoop()
