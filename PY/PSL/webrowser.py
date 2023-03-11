# The webbrowser modules lets you open new browser tabs and window.
# Can not do any interactions or window positioning or resizing.

import webbrowser

'''
# this opens the requested page in default browser.
webbrowser.open('http://www.python.org')

# this opens the page in a new window.
webbrowser.open_new('http://www.python.org')

# this opens page in new tab.
webbrowser.open_new_tab('http://www.python.org')
'''

'''
Browsers: 'opera', 'chrome', 'firefox', 'safari', etc.


browser = webbrowser.get('chrome')


browser.open_new_tab('http://docs.python.org')