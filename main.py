from PIL import Image
from flask import Flask,request,send_file

app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return "ㅇㅅㅇ"

@app.route("/image.png",methods=["GET"])
def image_page():
    ip=request.remote_addr

    image=Image.open("image.png")
    px=image.load()
    for i in range(len(ip)):
        px[".0123456789".index(ip[i]),i]=(255,255,255,255)
    image.save(f"image_{ip}.png")

    return send_file(f"image_{ip}.png",mimetype="image/png")

if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")
