title = """<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
  <title></title>
  <style type="text/css">
    *,*:before,*:after{margin:0;padding:0;overflow-x:hidden;}
    html,body{width:100%;height:100%;}
    main{display:flex;font-family: "Arial",monospace;font-size: 1.7rem;}
    p{margin-bottom:3rem;}
    ruby{user-select:none;margin-top:-1.3rem;margin-bottom:0.3rem;position:relative;display:block;width:100%;height:1rem;background: linear-gradient(90deg,rgba(0,0,0,1) 5%,rgba(200,200,200,0.5) 10%,rgba(0,0,0,0.5) 90%);text-align:left;font-size:1rem;color:white!important}
    article{flex:1;padding: 4%;}
    article:nth-child(odd){color: white; text-shadow: 0 0 .01vw white; background-color: black;}
    article:nth-child(even){color: black; text-shadow: 0 0 .01vw black; background-color: white;}
  </style>
</head>
<main>
"""
from zhconv import convert
with open('book.txt','r') as book:
  content = ''
  for line in book:
    if len(line) > 1:
      content += f'\n<p>{line}</p>'
  articles = '<article><br/>\n' + convert(content,'zh-tw').replace('「','"').replace('」','"') + '\n</article>\n\n<article><br/>\n' + content.replace('“','"').replace('”','"') + '\n</article>\n</main>\n</body>\n</html>'
  import os
  os.system('touch book.html')
  with open('book.html','w') as html:
    html.write(title + articles)