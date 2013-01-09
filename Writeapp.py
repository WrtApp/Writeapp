import sublime, sublime_plugin, subprocess, thread, os, urllib, urllib2, httplib
# import sublime, sublime_plugin, subprocess, thread, os, functools, glob, fnmatch


class WriteappCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get settings
        settings = sublime.load_settings("Preferences.sublime-settings")
        user = settings.get("writeapp_user")
        pswd = settings.get("writeapp_pass")

        # Run the plugin
        file_path = self.view.file_name()
        f = open(file_path, 'r')
        data = f.read()
        params = urllib.urlencode({'title': 'ST2 Note', 'content': data, 'user': user, 'pass': pswd})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection("staging.writeapp.me:80")
        conn.request("POST", "staging.writeapp.me/st2", params, headers)
        response = conn.getresponse()
        data2 = response.read()
        print data2
        conn.close()

        # self.view.insert(edit, 0, user)
