# joegit

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

I wanted to learn more about how the internals of git worked, for me the best way to do that was to try and build a subset of the features.

I found this [amazing tutorial](https://www.leshenko.net/p/ugit/#). The code in this repo is my interpretation of this tutorial (it is mostly the same, but in some small ways I have tweaked it to make it my own).

## Functionality

`joegit init`

`joegit commit -m 'message'`

`joegit branch`

`joegit checkout`

`joegit log`

`joegit k`

`joegit status`

`joegit reset`

`joegit show`

`joegit diff`

`joegit merge`

`joegit fetch` - only for local remotes, just to get an idea of how this process works

`joegit push` - like above

`joegit add`

\+ some internal functionality

## TODOs

* Branches aren't following HEAD at the moment, I need to fix that!
* Test force pushing is blocked
