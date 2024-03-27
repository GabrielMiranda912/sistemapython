from flask import Flask
app  = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<div class="uno">
    <h1>Perfil de usuario</h1>
    <img src="https://us.123rf.com/450wm/improvisor/improvisor1804/improvisor180400027/100035761-retrato-en-blanco-y-negro-de-serio-hombre-joven-sobre-fondo-negro-y-mirando-a-    la-c%C3%A1mara-concepto.jpg" height="200px" width="200px" >
    <h2>Marcus </h2>
    <h3>Programador Fronted</h3>
    <p>Harvard University</p>
    <div>
      <img src="https://cdn-icons-png.flaticon.com/512/246/246507.png" height="20px" width="20px">
      <img src="https://cdn.icon-icons.com/icons2/2157/PNG/512/twitter_logo_icon_132881.png" height="20px" width="20px">
      <img src="https://e7.pngegg.com/pngimages/342/689/png-clipart-linkedin-logo-icon-others-blue-text.png" height="20px" width="40px">
      <img src="https://cdn.icon-icons.com/icons2/2429/PNG/512/facebook_logo_icon_147291.png" height="20px" width="20px">
    </div>
    <br>
     <button>Contact</button>
</div>'


if __name__=="__main__":
  app.run(debug = True)
