# Island

A Sublime Text 2 plugin for saving notes to Write.app.

## Usage

__Notice: Right now, Island is a work in progress and in development mode only. It makes requests to the Write.app API but responses are spotty at best. Nothing harmful or dangerous, just nothing useful. Will update when this plugin, at the very least, actually *does something* even if it isn't consistent.__

Because of the very early alpha development status this isn't so user friendly but if you want to send requests and see responses, do this:

1. Press `Ctrl+\``

2. In the prompt at the bottom enter: `view.run_command('writeapp')`

3. You'll see the server's response in the prompt.

__Connecting to your accout__

The plugin currently doesn't save notes yet but you can still get ready for when it does by entering your Write.app username and password. In your __User Preferences__ (that's USER preferences only) enter the following JSON:

```
"writeapp_user": "bill",
"writeapp_pass": "pass"
```

__Giving Notes Titles and other Meta Data__

Island uses YAML to determine how to save your note. At the beginning of your file enter your desired settings and Write.app will take care of the rest. Here's an example note with all of the currently proposed settings:

```
---
title: My title
public: true
notebook: my notebook
---

This is the content of mynote

```

YAML is *not required*. If you save a note without YAML front matter then it will automatically be saved to your default notebook as an untitled note. Adding preferences to the YAML front matter that don't exist in the app does nothing. They will just be ignored. You do not need to include all possible settings in your front matter. For example, if you only wanted to set a title or only wanted to set the note to be publicly visible you would only add the lines you need to the note.

__Accepted YAML Front Matter Settings__

*title*: A string of text. Defaults to "Untitled-{random-chars}" if empty or missing.

*public*: Boolean. Accepts values "true" or "false". Defaults to "false" if empty or missing. Anything other than "true" or "false" results in the app turning it into a FALSE.
