# CkbltDocument

A XML based CkbltDocument (with parser)  
The parser can convert a CkbltDocument file into a HTML file

`document`: Main.  
`document` -> `title`: CkbltDocument title.  
`text`: Display text in a web page.  
`text` -> `style`: Text style. Equal `font-style: xxx;` in CSS.  
`text` -> `size`: Text size. Equal `font-size: xxx;` in CSS.  
`text` -> `align`: Text align. Equal `text-align: xxx;` in CSS.  
`text` -> `color`: Text color, can write hex, rgb() and rgba(). Equal `color: xxx;` in CSS.  
`text` -> `indent`: Text indent. Equal `margin-left: xxx;` in CSS.  
`text` -> `css`: Make your text CSS style.

## example:
```xml
<document title="Test">
  <text style="italic">I like Italic very much!</text>
  <text size="100px">I'M BIG!</text>
  <text align="center">!CENTER!</text>
  <text color="#00ff00">I'm green.</text>
  <text indent="100px">Indent 100px!</text>
  <text css="background-color: aqua;">With CSS, My background is AQUA!</text>
</document>
```
## to HTML (formatted) :
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
</head>

<body>
    <title>Test</title>
    <h1 style="font-size:100px;display:flex;justify-content:center;">Test</h1>
    <p style="font-size:20px;font-style:italic;text-align:left;color:#000000;margin-left:0px;;">I like Italic very much!
    </p>
    <p style="font-size:100px;font-style:normal;text-align:left;color:#000000;margin-left:0px;;">I'M BIG!</p>
    <p style="font-size:20px;font-style:normal;text-align:center;color:#000000;margin-left:0px;;">!CENTER!</p>
    <p style="font-size:20px;font-style:normal;text-align:left;color:#00ff00;margin-left:0px;;">I'm green.</p>
    <p style="font-size:20px;font-style:normal;text-align:left;color:#000000;margin-left:100px;;">Indent 100px!</p>
    <p style="font-size:20px;font-style:normal;text-align:left;color:#000000;margin-left:0px;background-color: aqua;;">With CSS, My background is AQUA!</p>
</body>

```

