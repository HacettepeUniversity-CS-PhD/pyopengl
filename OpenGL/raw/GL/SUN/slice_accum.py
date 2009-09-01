'''OpenGL extension SUN.slice_accum

Overview (from the spec)
    
    
    This extension defines a new accumulation operation which enables the accumulation
    buffer to be used for alpha compositing. This enables higher precision alpha
    blending than what can be accomplished using the blend operation.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SUN/slice_accum.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SUN_slice_accum'
_DEPRECATED = False
GL_SLICE_ACCUM_SUN = constant.Constant( 'GL_SLICE_ACCUM_SUN', 0x85CC )


def glInitSliceAccumSUN():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )