<p align="center">
<img src="https://www.stairways.com/img/keyboardmaestro-256.png">
</p>

# Search Keyboard Maestro Variables/Clipboards

Search all Keyboard Maestro variables and named clipboards in [Alfred][alfredapp].
* * *
![searchvars](imgs/searchvars.gif)
* * *
![searchclips](imgs/searchclips.gif)
* * *

## Features

- Search all variables to: view, edit, or delete

- Search and view all named clipboard contents:

- **When searching variables**:
  - Press <kbd>↩︎</kbd> to open variable in an editor window.
    - _Editor window actions_:
      - _Edit_ the value of the variable, then click `OK` (or <kbd>↩︎</kbd> if value is not multiple lines) to update variable in Keyboard Maestro
      - _Delete_ variable by clicking `Delete` (or <kbd>⌘</kbd><kbd>D</kbd>)
  - Press <kbd>⌘</kbd><kbd>↩︎</kbd> to delete variable from Alfred window.
  - _NOTE:_ If the value of the variable is < 100 characters, it will display the value of the variable as the subtitle of search result
- **When searching clipboards**:
  - Press <kbd>↩︎</kbd> to display clipboard in window.

## Installation

Download [the latest release][gh-releases] and double-click the file to install in Alfred.

## Usage

The two main keywords are `kmv` & `kmc`:

- `kmv [<query>]` - Search all variables
  - <kbd>↩︎</kbd> or <kbd>⌘</kbd><kbd>NUM</kbd> — Open variable in editor window.
  - <kbd>⌘</kbd><kbd>↩︎</kbd> — Delete variable in Keyboard Maestro

- `kmc [<query>]` — Search all named clipboards in Keyboard Maestro.
  - <kbd>↩︎</kbd> or <kbd>⌘</kbd><kbd>NUM</kbd> — Display clipboard in window.

## Configuration

## Licensing & thanks

This workflow is released under the [MIT Licence][mit].

This workflow uses on the wonderful library [alfred-workflow](https://github.com/deanishe/alfred-workflow) by [@deanishe](https://github.com/deanishe).

## Changelog

- v1.0.0
  - First public release

[alfredapp]: https://www.alfredapp.com/
[gh-releases]: https://github.com/kevin-funderburg/alfred-search-keyboard-maestro-vars/releases/latest
[mit]: https://raw.githubusercontent.com/kevin-funderburg/alfred-search-keyboard-maestro-vars/master/LICENCE.txt
