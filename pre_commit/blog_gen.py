import glob
import os
import datetime

files = glob.glob("./blog_posts/*.html")
files.sort(key=os.path.getctime)
files.reverse()

outfile = open("./blog.html", "w")

# header
outfile.write(
    """
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Miredly: Interactive Media Developer</title>

  <link rel="stylesheet" href="/css/main.css" />
  <div class="portfolio">
    <div class="navigation dashed-border">
      <ul id="menu">
        <li><a href="/index.html">About</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="/p_gamedev.html">Portfolio</a></li>
      </ul>
    </div>
  </div>
</head>

<body>
<div class="blog">
"""
)

for post in files:
    with open(post) as infile:
        date = str(datetime.datetime.fromtimestamp(os.path.getmtime(post)))
        date = date.split(" ")[0]
        date = date.split("-")

        outfile.write(f"<h3>{date[1]}/{date[2]}/{date[0]}</h3>")
        outfile.write('<div class = "post dashed-border dark">')
        for line in infile:
            print(line)
            outfile.write(line)
        outfile.write("</div>")

# end body
outfile.write(
    """
</div>
</body>
"""
)
