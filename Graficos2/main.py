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

zafiro = Material(diffuse = (0.46,0.45,0.65), spec = 64, ior = 1.33, matType = REFLECTIVE)
esmeralda = Material(diffuse = (0,0.61,0.44), spec = 64, ior = 1.33, matType = TRANSPARENT)
rubi = Material(diffuse= (0.60, 0.06, 0.12), spec = 64, ior = 1.33, matType= TRANSPARENT)
r_quartz = Material(diffuse=(0.97, 0.79, 0.84), spec= 64, ior = 1.33, matType= OPAQUE)

'''
# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('d3.bmp')

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
'''

earth = Material(texture = Texture('earthDay.bmp'))
box = Material(texture = Texture('box.bmp'))
sand = Material(texture= Texture('sand2.bmp'))


# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('d3.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
#rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.dirLight = DirectionalLight(direction = V3(-2, 5, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(-3, 0, 0), intensity = 0.5))

# Objetos
#rtx.scene.append( Sphere(V3(0,0,-8), 2, earth) )

#piramide
rtx.scene.append( AABB(V3(0,-4,-8), V3(6,1,6), mirror) )
rtx.scene.append( AABB(V3(0,-3,-8), V3(5,1,5), zafiro) )
rtx.scene.append( AABB(V3(0,-2,-8), V3(4,1,4), esmeralda) )
rtx.scene.append( AABB(V3(0,-1,-8), V3(3,1,3), gold) )
rtx.scene.append( AABB(V3(0,0,-8), V3(2,1.2,2), rubi) )
rtx.scene.append( AABB(V3(0,1,-8), V3(1,1,1), r_quartz) )

#esferas
rtx.scene.append( Sphere(V3(0,2,-8), 0.5, earth ))
rtx.scene.append( Sphere(V3(-3,-3,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(3,-3,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(-2,-2,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(2,-2,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(-1,-1,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(1,-1,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(-0.5,0.5,-4), 0.2, diamond) )
rtx.scene.append( Sphere(V3(0.5,0.5,-4), 0.2, diamond) )




'''
rtx.scene.append( AABB(V3(-3,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(-2.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(-2,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(-1.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(-1,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(-0.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(0,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(0.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(1,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(1.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(2,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(2.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(3,-2,-8), V3(0.5,0.5,0.5), zafiro) )
rtx.scene.append( AABB(V3(3.5,-2,-8), V3(0.5,0.5,0.5), zafiro) )
'''

# Terminar
rtx.glRender()
rtx.glFinish('output.bmp')

