# Codename: Island (Beta)

The official Sublime Text plugin for Write.app. Island lets you save notes to Write.app directly from within Sublime Text 2.

## Installation

### Package Control

__Coming Soon__

### Manual Install

(Only use this if you aren't comfortable with the command line or don't have package control installed)

1. Download the latest plugin version from GitHub

2. Unzip the file and place the Writeapp folder in your Packages directory

3. Restart Sublime Text and you're ready to go!

__Can't find the folder?__

Windows:  `%APPDATA%\Sublime Text 2`
Mac: ~/Library/Application Support/Sublime Text 2
Linux: ~/.config/sublime-text-2

### Via Git

1. In a terminal window, navigate to your Packages folder (locations for each platform are listed above).

2. Run `git clone https://github.com/WrtApp/Island.git Writeapp`

3. Restart Sublime. You're done.

## Usage

__Setup__

Before you can use the plugin you have to add your username and password to your User settings file. Add the following lines to the JSON that may already be there:

```
"writeapper_user": "bill",
"writeapp_pass": "ih8ny1"
```

If your User Settings file is empty, use this code instead:

```
{
	"writeapper_user": "yourUsername",
	"writeapp_pass": "yourPassword"
}
```

__Saving notes__

There are two ways to save notes; through a kayboard shortcut or the context menu.

So save the contents of the currently open file to Write.app just press `alt+s`. You can also right click anywhere inside the open file and choose "Save to Write.app".

*Note: Currently there's no way to update notes. If you save the same note using this plugin twice, two separate notes will be created. This will change with further development. Also, you must first save what you are working on to disk. Currently the plugin can only send data that has already been saved. This will also change with future development*

__Setting titles and other options__

Island uses [YAML front matter](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter) to determine how to save your note. At the beginning of your file enter your desired settings and Write.app will take care of the rest. Here's an example note with all of the currently proposed settings:

```
---
title: My title
public: true
notebook: my notebook
---

This is the content of mynote

```

YAML is *not required*. If you save a note without YAML front matter then it will automatically be saved to your default notebook as an untitled note. Adding preferences to the YAML front matter that don't exist in the app does nothing. They will just be ignored. You do not need to include all possible settings in your front matter. For example, if you only wanted to set a title or only wanted to set the note to be publicly visible but nothing else you would only add the lines you need to the note. Missing settings are considered false and have sane defaults.

__Accepted YAML Front Matter Settings__

*title*: A string of text. Defaults to "Untitled-{random-chars}" if empty or missing.

*public*: Boolean. Accepts values "true" or "false". Defaults to "false" if empty or missing. Anything other than "true" or "false" results in the app turning it into a FALSE.

More settings to come.