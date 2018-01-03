from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '我想去美國玩'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '我想去韓國玩'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '我想看美國國旗'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '我想學英文的問好'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '我想看韓國國旗'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '我想學韓文的問好'

    def on_enter_state1(self, update):
        update.message.reply_text("以下是我幫您搜尋到的資料，希望對您有幫助\nhttps://ppt.cc/fs9YFx")
        update.message.reply_text("對了!我還能秀給你看此國國旗給你看或是教你基本問候語喔~")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("以下是我幫您搜尋到的資料，希望對您有幫助\nhttps://ppt.cc/fFZFKx")
        update.message.reply_text("對了!我還能秀給你看此國國旗給你看或是教你基本問候語喔~")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_photo(open("img/美國國旗.png","rb"))
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_audio(open("audio/你好_英文.ogg","rb"))
        self.go_back(update)        

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_photo(open("img/韓國國旗.png","rb"))
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_audio(open("audio/你好_韓文.ogg","rb"))
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')




