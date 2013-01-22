import sublime, sublime_plugin, thread, urllib, urllib2, httplib
# import sublime, sublime_plugin, subprocess, thread, os, functools, glob, fnmatch

class WriteappCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.erase_status('writeapp')

        # Get settings
        settings = sublime.load_settings("Preferences.sublime-settings")
        user = settings.get("writeapp_user")
        pswd = settings.get("writeapp_pass")

        # Read the current file
        file_path = self.view.file_name()
        f = open(file_path, 'r')
        data = f.read()

        # Create and send the request
        self.view.set_status('writeapp', 'Sending to Write.app')
        params = urllib.urlencode({'content': data, 'user': user, 'pass': pswd})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "Accept-Encoding": "identity"}
        conn = httplib.HTTPSConnection("writeapp.me")
        conn.request("POST", "https://writeapp.me/st2", params, headers)
        response = conn.getresponse()
        data2 = response.read()
        print data2
        conn.close()

        # Show success message in status bar
        self.view.erase_status('writeapp')
        self.view.set_status('writeapp', 'Saved to Write.app')

        # self.view.insert(edit, 0, user)
