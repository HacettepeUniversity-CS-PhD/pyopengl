'''OpenGL extension ATI.texture_float

Overview (from the spec)
    
    This extension adds texture internal formats with 32 and 16 bit
    floating-point components.  The 32 bit floating-point components
    are in the standard IEEE float format.  The 16 bit floating-point
    components have 1 sign bit, 5 exponent bits, and 10 mantissa bits.
    Floating-point components are clamped to the limits of the range
    representable by their format.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ATI/texture_float.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_texture_float'
_DEPRECATED = False
GL_RGBA_FLOAT32_ATI = constant.Constant( 'GL_RGBA_FLOAT32_ATI', 0x8814 )
GL_RGB_FLOAT32_ATI = constant.Constant( 'GL_RGB_FLOAT32_ATI', 0x8815 )
GL_ALPHA_FLOAT32_ATI = constant.Constant( 'GL_ALPHA_FLOAT32_ATI', 0x8816 )
GL_INTENSITY_FLOAT32_ATI = constant.Constant( 'GL_INTENSITY_FLOAT32_ATI', 0x8817 )
GL_LUMINANCE_FLOAT32_ATI = constant.Constant( 'GL_LUMINANCE_FLOAT32_ATI', 0x8818 )
GL_LUMINANCE_ALPHA_FLOAT32_ATI = constant.Constant( 'GL_LUMINANCE_ALPHA_FLOAT32_ATI', 0x8819 )
GL_RGBA_FLOAT16_ATI = constant.Constant( 'GL_RGBA_FLOAT16_ATI', 0x881A )
GL_RGB_FLOAT16_ATI = constant.Constant( 'GL_RGB_FLOAT16_ATI', 0x881B )
GL_ALPHA_FLOAT16_ATI = constant.Constant( 'GL_ALPHA_FLOAT16_ATI', 0x881C )
GL_INTENSITY_FLOAT16_ATI = constant.Constant( 'GL_INTENSITY_FLOAT16_ATI', 0x881D )
GL_LUMINANCE_FLOAT16_ATI = constant.Constant( 'GL_LUMINANCE_FLOAT16_ATI', 0x881E )
GL_LUMINANCE_ALPHA_FLOAT16_ATI = constant.Constant( 'GL_LUMINANCE_ALPHA_FLOAT16_ATI', 0x881F )


def glInitTextureFloatATI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )