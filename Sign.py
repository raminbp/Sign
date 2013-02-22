import sublime, sublime_plugin, datetime


class SignCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #Loading UserName and AuthorName
        setting = sublime.load_settings(__name__ + '.sublime-settings')
        #Stamp stringBuffer
        stampStringBuffer = '/**\n' + ' * Created by Sublime Text 2\n'\
        + ' * User    : ' + setting.get('user_name') + '\n'\
        + ' * Date    : ' + datetime.datetime.now().strftime("%Y/%m/%d")\
        + '\n'\
        + ' * Time    : ' + datetime.datetime.now().strftime("%H:%M") + '\n'\
        + ' * Author  : ' + setting.get('author_name') + '\n'\
        + ' * Email   : ' + setting.get('author_email') + '\n'\
        + '*/'
        self.view.insert(edit, 0, stampStringBuffer)
