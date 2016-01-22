# ASCII Punctuation Maker

**Quickstart**

Install in Sublime Text.  Hit `alt-a`.  "Smart quotes" and other insidious unicode punctuation that might have slipped into your document from copy-pasting from MS Word, web, etc. magically disappear.  Be happy.

Details follow.

**YOUR PROBLEM**: 

You're working in Sublime Text with some kind of text that you copied and pasted in from the web, or from a Word document.  You don't *think* it has any international characters in it, so you aren't bothing with specifying any kind of encoding.  Maybe you're making a quick and dirty HTML page.  Maybe you're processing text in Python 2.  Either way, ugliness ensues: Python throws a bunch of horrible unicode errors, your web page has a bunch of weird question marks in black diamonds.  

**YOUR OPTIONS**: 

1.  Manually search and replace all the horrible "smart quotes" and all the rest.  Hope you didn't miss any.
2.  Learn how unicode works.  A year later, go back and try your web page/text processing task again.  (Oh, wait, you've been fired for unproductivity.  Never mind.)
3.  Install this plugin.  Be happy.

**In other words**: This is a very simple plugin to take horrible unicode punctuation in a Sublime Text buffer and convert it to nice sane ASCII punctuation.  It fixes "smart quotes" (single and double, as well as the apostrophe that is also a single quote) as well as weird dashes and ellipses. 

**Installation and usage**: Install via package control, or ordinary Sublime Text package methods (save in your packages directory).  Then `alt-a` will replace all the evil punctuation in the current buffer with non-evil punctuation.  There's also an entry in the command palette and in the edit menu.  

If you'd rather do this in the filesystem instead, see [cleanpunct](https://github.com/paultopia/cleanpunct), which is basically the same thing, but as a Python module instead of a ST package.

I've only tested this under ST3, but it should work fine in ST2 too.  I think.
