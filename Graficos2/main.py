from gl import Raytracer, V3, _color
from obj import Obj, Texture

from figures import Sphere, Material

width = 960
height = 960


nieve = Material(diffuse = _color(1,1,1))
boton = Material(diffuse = _color(0,0,0))
nariz = Material(diffuse = _color(1, 165/255,0))



rtx = Raytracer(width,height)

#Bolas de Nieve
rtx.scene.append( Sphere(V3(0,-2.5,-10), 2, nieve) )
rtx.scene.append( Sphere(V3(0,0.5,-10), 1.5, nieve) )
rtx.scene.append( Sphere(V3(0,3,-10), 1.2, nieve) )

#Botones
rtx.scene.append( Sphere(V3(0,-2.2,-8), 0.3, boton) )
rtx.scene.append( Sphere(V3(0,-0.6,-8), 0.3, boton) )
rtx.scene.append( Sphere(V3(0,1,-8), 0.3, boton) )

#Nariz
rtx.scene.append( Sphere(V3(0,2.5,-8), 0.25, nariz) )

#Ojos
rtx.scene.append( Sphere(V3(-0.5,2.7,-8), 0.1, boton) )
rtx.scene.append( Sphere(V3(0.5,2.7,-8), 0.1, boton) )


#Boca
rtx.scene.append( Sphere(V3(-0.4,2.2,-8), 0.1, boton) )
rtx.scene.append( Sphere(V3(-0.18,2,-8), 0.1, boton) )
rtx.scene.append( Sphere(V3(0.18,2,-8), 0.1, boton) )
rtx.scene.append( Sphere(V3(0.4,2.2,-8), 0.1, boton) )
#rtx.scene.append( Sphere(V3(0,-2.2,-8), 0.15, boton) )



rtx.glRender()

rtx.glFinish('output.bmp')