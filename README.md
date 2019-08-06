# HTMLie

HTMLie is a command line HTML Parser.

## Installation

`pip install htmlie`

## Usage

html [css selectors][:attr]

- css selectors: The same as jquery css selector.
- attr: text, html, outer_html, href, src, etc. Anything in the HTML tag.

```
$ http example.com | html title
$ curl example.com | html title
$ cat index.html | html a :href
```
