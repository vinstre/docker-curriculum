from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://webneel.com/sites/default/files/imagecache/660Thumbnail/images/blog/t-natuwal.jpg",
    "https://webneel.com/wallpaper/sites/default/files/images/08-2018/1-nature-wallpaper-grass-hd.preview.jpg",
    "https://webneel.com/wallpaper/sites/default/files/images/08-2018/2-nature-wallpaper-grass.preview.jpg",
    "https://webneel.com/wallpaper/sites/default/files/images/08-2018/3-nature-wallpaper-mountain.preview.jpg",
    "https://webneel.com/wallpaper/sites/default/files/images/08-2018/4-nature-wallpaper-sky.preview.jpg",
    "https://webneel.com/wallpaper/sites/default/files/images/06-2013/beautiful%20sky%20tree%20wallpaper.preview.jpg",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
