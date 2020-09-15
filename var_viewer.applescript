--
--	Created by: Kevin Funderburg
--	Created on: 9/11/20
--
--	Copyright © 2020 funderburg, All Rights Reserved
--

use AppleScript version "2.4" -- Yosemite (10.10) or later
use framework "Foundation"
use framework "AppKit"
use scripting additions
use script "Dialog Toolkit Plus"
property ICON_KM : "/System/Volumes/Data/Applications/Keyboard Maestro.app/Contents/Resources/Variable.icns"

on run argv
	
	if class of argv = script then
		set argv to {"_path", "System/Volumes/Data/Applications/Keyboard Maestro.app/Contents/Resources/Variable.icn"}
	end if
	set {_name, val} to argv
	set {width, height} to screensize()
	set maxFieldHeight to height * 0.75
	set lineCount to count of paragraphs of val
	set fieldHeight to 15 * lineCount
	if fieldHeight > maxFieldHeight then
		set fieldHeight to maxFieldHeight
	end if
	set maxWidth to 550
	set minWidth to 400
	set accWidth to getLongestLine(val)
	set accWidth to (accWidth / 1.5) * 10
	if accWidth > maxWidth then
		set accWidth to maxWidth
	else if accWidth < minWidth then
		set accWidth to minWidth
	end if
	set accViewWidth to accWidth
	set {theButtons, minWidth} to ¬
		create buttons {"Cancel", "Delete", "OK"} ¬
			button keys {"", "d", ""} ¬
			default button 3 ¬
			cancel button 1
	if minWidth > accViewWidth then set accViewWidth to minWidth -- make sure buttons fit
	set {theField, theTop} to ¬
		create field (val) ¬
			placeholder text ("Enter your text here") ¬
			bottom 0 ¬
			field width accViewWidth ¬
			extra height fieldHeight ¬
			with accepts linebreak and tab
	
	set {regLabel, theTop} to ¬
		create label ("OK:" & tab & tab & "Dismiss or set variable to new value" & return & ¬
			"Delete:" & tab & "Delete variable from Keyboard Maestro (⌘D)" & return & ¬
			"Cancel:" & tab & "⎋") ¬
			bottom theTop + 10 ¬
			max width accViewWidth ¬
			left inset 75 ¬
			control size regular size ¬
			aligns left aligned
	
	set {theRule, theTop} to ¬
		create rule (theTop + 12) ¬
			left inset 75 ¬
			rule width accViewWidth - 60
	
	set {boldLabel, theTop} to ¬
		create label ("View or edit the Keyboard Maestro variable here.") ¬
			bottom theTop + 10 ¬
			max width accViewWidth ¬
			left inset 75 ¬
			control size regular size ¬
			aligns left aligned ¬
			with bold type
	set {imgView, theTop} to ¬
		create image view (ICON_KM) ¬
			left inset 10 ¬
			bottom theTop - 50 ¬
			view width 50 ¬
			view height 50 ¬
			scale image scale proportionally ¬
			align image top left aligned
	set {buttonName, controlsResults} to ¬
		display enhanced window ("Keyboard Maestro Variable Viewer") ¬
			acc view width accViewWidth ¬
			acc view height theTop + 5 ¬
			acc view controls {theField, regLabel, theRule, boldLabel, imgView} ¬
			buttons theButtons ¬
			active field theField ¬
			initial position {0, 0} ¬
			with align cancel button
	
	if buttonName = "OK" then
		set newVal to item 1 of controlsResults
		if newVal ≠ val then
			tell application "Keyboard Maestro Engine"
				setvariable _name to newVal
			end tell
			display notification ("'" & _name & "' updated to " & newVal)
		end if
	end if
end run

on getLongestLine(txt)
	set max to 0
	repeat with p in paragraphs of txt
		if (count of characters of contents of p) > max then
			set max to count of characters of contents of p
		end if
	end repeat
	return max
end getLongestLine

on screensize()
	set theScreen to current application's NSScreen's mainScreen()
	set theFrame to theScreen's visibleFrame()
	set width to item 1 of item 2 of theFrame
	set height to item 2 of item 2 of theFrame
	return {width, height}
end screensize

