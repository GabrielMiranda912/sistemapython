from flask import Flask
app  = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<html>
<head>
 <title>ProyectoPrueba</title>
 <script src="https://kit.fontawesome.com/5976ae6850.js" crossorigin="anonymous"></script>
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
 <style>  
body{
height: 100%;
width: 100%;
}
.uno{
 text-align: center;
 display: flex;
 justify-content: center;
 flex-direction: column;
 align-items: center;
}
</style>
<div class="uno">
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
    </div>
    <button class="btn btn-primary">Contact</button>
</body>
</html>'


if __name__=="__main__":
  app.run(debug = True)