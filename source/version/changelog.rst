Release Notes
======================

V 1.5.2
------------------------------------------

Date: 2019-07-23

New Features
````````````````
- added *<input>* name attribute (in detail panel)
- added header, footer, table-caption property (in style panel)
- added *editor-hidden* property (in structure)
- added shortcut

    - ruler mode (ctrl+ r) / outline mode (ctrl + l)
    - tracing command (ctrl + t)
- applied license
- css code preview in developer view
- project custom code

Improvements
````````````````````
- synchronized image popup state
- synchronized color mode (color picker popup)
- added splash screen
- added function on numbericupdown, multiply 10 (with shift key)
- added shift key interaction (with drag resize), same width and height are increased
- updated project menu and commands
- checked files in project directory, tracked files in the project
- grouped widgets in creation view
- change mouse behaviours (thumb) when center properties are applied

Fixes
````````````
- fixed window maximize (blank)
- fixed zoom at canvas
- copy resources when creating a custom widget
- focus issue (selection changed)
- fixed file management (external changed)
- fixed ime conflict when change file name


V 1.4
----------------------
Date: 2019-06-14

New Features
````````````````
- canvas’s context menu
- added animation property to event panel (carousel, transition …)
- created style panel

Improvements
```````````````````
- changed directory name (in file navigation)
- separated save/saveall command from one save command
- preserved expanded state treeviewitem (widget navigation)
- shown recent files up to 30
- changed alpha slider (wpttoolkit) 0~255 -> 0~100
- changed avalondock to default tabcontrol
- changed icon (png -> xaml or xaml -> xaml), checked pixel issue
- separated IsEnabled between widget and project properties

Fixes
`````````````````
- fixed canvas selection’s position
- fixed cancopy/canadd/canmove
- handled removed files on load usersettings
- fixed shift key event treeviewitem (widget navigation)
- fixed binding error & project setting constraint
- fixed preset object (widget)
- fixed webbrowser load issue (widgets are changed while webbrowser is loading)
- fixed multiselection issue
- fixed page layout (structure notification)


V 1.3.1
-------------------------
date: 2019-02-28

New Features
`````````````````````````````````
- bind :kbd:`F2` with text mode
- added scroll event
- created custom widgets

Improvements
```````````````````````````````
- saved opened page/composition list
- performance (import -> update css/html)
- updated link (div widget) design
- updated project setting design (min/max width)

Fixes
``````````````````
- saved resource file
- fixed html / css files
- fixed alert message (no internet connection)