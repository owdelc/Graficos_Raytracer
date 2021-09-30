from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensiones
width = 512
height = 512

# Materiales
wood = Material(diffuse = (0.6,0.2,0.2), spec = 64)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)

gold = Material(diffuse = (1, 0.8, 0 ),spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)

zafiro = Material(diffuse = (0.46,0.45,0.65), spec = 64, ior = 1.33, matType = OPAQUE)
esmeralda = Material(diffuse = (0,0.61,0.44), spec = 64, ior = 1.33, matType = OPAQUE)

# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('parque.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))

# Objetos
rtx.scene.append( Sphere(V3(-2,3,-8), 1, mirror) )
rtx.scene.append( Sphere(V3(2,3,-8), 1, gold) )

rtx.scene.append( Sphere(V3(-2,0,-8), 1, glass) )
rtx.scene.append( Sphere(V3(2,0,-8), 1, diamond) )

rtx.scene.append( Sphere(V3(-2,-3,-8), 1, zafiro) )
rtx.scene.append( Sphere(V3(2,-3,-8), 1, esmeralda) )



# Terminar
rtx.glRender()
rtx.glFinish('output.bmp')