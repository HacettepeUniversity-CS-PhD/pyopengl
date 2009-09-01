'''OpenGL extension ARB.color_buffer_float

Overview (from the spec)
    
    The standard OpenGL pipeline is based on a fixed-point pipeline.
    While color components are nominally floating-point values in the
    pipeline, components are frequently clamped to the range [0,1] to
    accomodate the fixed-point color buffer representation and allow
    for fixed-point computational hardware.
    
    This extension adds pixel formats or visuals with floating-point
    RGBA color components and controls for clamping of color
    components within the pipeline.
    
    For a floating-point RGBA pixel format, the size of each float
    components is specified using the same attributes that are used
    for defining the size of fixed-point components.  32-bit
    floating-point components are in the standard IEEE float format.
    16-bit floating-point components have 1 sign bit, 5 exponent bits,
    and 10 mantissa bits.
    
    Clamping control provides a way to disable certain color clamps
    and allow programs, and the fixed-function pipeline, to deal in
    unclamped colors.  There are controls to modify clamping of vertex
    colors, clamping of fragment colors throughout the pipeline, and
    for pixel return data.
    
    The default state for fragment clamping is "FIXED_ONLY", which
    has the behavior of clamping colors for fixed-point color buffers
    and not clamping colors for floating-pont color buffers.
    
    Vertex colors are clamped by default.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/color_buffer_float.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_color_buffer_float'
_DEPRECATED = False
GL_RGBA_FLOAT_MODE_ARB = constant.Constant( 'GL_RGBA_FLOAT_MODE_ARB', 0x8820 )
glget.addGLGetConstant( GL_RGBA_FLOAT_MODE_ARB, (1,) )
GL_CLAMP_VERTEX_COLOR_ARB = constant.Constant( 'GL_CLAMP_VERTEX_COLOR_ARB', 0x891A )
glget.addGLGetConstant( GL_CLAMP_VERTEX_COLOR_ARB, (1,) )
GL_CLAMP_FRAGMENT_COLOR_ARB = constant.Constant( 'GL_CLAMP_FRAGMENT_COLOR_ARB', 0x891B )
glget.addGLGetConstant( GL_CLAMP_FRAGMENT_COLOR_ARB, (1,) )
GL_CLAMP_READ_COLOR_ARB = constant.Constant( 'GL_CLAMP_READ_COLOR_ARB', 0x891C )
glget.addGLGetConstant( GL_CLAMP_READ_COLOR_ARB, (1,) )
GL_FIXED_ONLY_ARB = constant.Constant( 'GL_FIXED_ONLY_ARB', 0x891D )
glClampColorARB = platform.createExtensionFunction( 
'glClampColorARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glClampColorARB(GLenum(target), GLenum(clamp)) -> None',
argNames=('target','clamp',),
deprecated=_DEPRECATED,
)


def glInitColorBufferFloatARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )