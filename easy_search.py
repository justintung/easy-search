import webbrowser
import sublime, sublime_plugin

def search(q):
    settings = sublime.load_settings("easy_search.sublime-settings")
    # Attach the suffix and the prefix
    q = settings.get('prefix', '') + q + settings.get('suffix', '')

    fullUrl = settings.get('searchbase', 'http://www.baidu.com/s?wd=') + "%s" % q

    webbrowser.open(fullUrl)


class EasySearchCommand(sublime_plugin.TextCommand):
    """
    Search the selected text or the current word
    """
    def run(self, edit):

        querys = []
        for region in self.view.sel():
            if region.empty():
                # if we have no selection grab the current word
                word = self.view.word(region)
                if not word.empty():
                    querys.append(self.view.substr(word))
            else:
                # append the selection
                if not region.empty():
                    querys.append(self.view.substr(region))


        if len(querys) != 0:
            selection = " ".join(querys)
            search(selection)
        else:
            sublime.status_message(" Nothing to search !")
            print("Easy Search Plugin: Nothing to search !")


class EasySearchAnyCommand(sublime_plugin.WindowCommand):
    """
    A command that prompts the user to enter search query text.
    """

    def run(self):

        def show_input_panel():
            self.window.show_input_panel(
                'Enter a search query',
                '',
                self.on_done,
                self.on_change,
                self.on_cancel
                )
        sublime.set_timeout(show_input_panel, 10)

    def on_done(self, text):
        search(text)

    def on_change(self):
        pass

    def on_cancel(self):
        pass
