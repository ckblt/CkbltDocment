"""
CkbltDocument parser
"""

import xml.sax

# can be changed
name = "demo"  # filename, no suffix
delay = 0.3  # render interval

# cannot be changed
write_prefix = '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body>'
write = ""
write_suffix = "</body></html>"
save = write_prefix + write_suffix


class handler(xml.sax.ContentHandler):
    def __init__(self):  # init MANYMANY variables
        self.tag = ""
        self.title = ""
        self.text = ""
        self.text_style = ""
        self.text_size = ""
        self.text_align = ""
        self.text_color = ""
        self.text_indent = ""
        self.text_css = ""

    def startElement(self, tag, attributes):
        self.tag = ""
        self.title = ""
        self.text = ""
        self.text_style = ""
        self.text_size = ""
        self.text_align = ""
        self.text_indent = ""
        self.text_color = ""
        self.text_css = ""

        global write

        self.tag = tag

        if tag == "document":
            try:
                self.title = attributes["title"]
            except:
                self.title = "A Story"
            write += "<title>" + self.title + "</title>"
            write += (
                '<h1 style="font-size:100px;display:flex;justify-content:center;">'
                + self.title
                + "</h1>"
            )
        elif tag == "text":
            try:
                self.text_style = attributes["style"]
            except:
                self.text_style = "normal"

            try:
                self.text_size = attributes["size"]
            except:
                self.text_size = "20px"

            try:
                self.text_align = attributes["align"]
            except:
                self.text_align = "left"

            try:
                self.text_color = attributes["color"]
            except:
                self.text_color = "#000000"

            try:
                self.text_indent = attributes["indent"]
            except:
                self.text_indent = "0px"

            try:
                self.text_css = attributes["css"]
            except:
                self.text_css = ""

    def endElement(self, tag):
        global write
        if self.tag == "text":
            write += (
                '<p style="font-size:'
                + self.text_size
                + ";font-style:"
                + self.text_style
                + ";text-align:"
                + self.text_align
                + ";color:"
                + self.text_color
                + ";margin-left:"
                + self.text_indent
                + ";"
                + self.text_css
                + ';">'
                + self.text
                + "</p>"
            )

        self.tag = ""

    def characters(self, content):
        if self.tag == "text":
            self.text = content


try:
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(handler())
    parser.parse("./in/" + name + ".xml")

    save = write_prefix + write + write_suffix
    write = ""

    print("success!")
    with open("./out/" + name + ".html", "w", encoding="UTF-8") as f:
        f.write(save)

except:
    print("fail!")
