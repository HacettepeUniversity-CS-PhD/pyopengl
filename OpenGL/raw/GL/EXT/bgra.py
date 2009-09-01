'''OpenGL extension EXT.bgra

Overview (from the spec)
    
    EXT_bgra extends the list of host-memory color formats.
    Specifically, it provides formats which match the memory layout of
    Windows DIBs so that applications can use the same data in both
    Windows API calls and OpenGL pixel API calls.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/bgra.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_bgra'
_DEPRECATED = False
GL_BGR_EXT = constant.Constant( 'GL_BGR_EXT', 0x80E0 )
GL_BGRA_EXT = constant.Constant( 'GL_BGRA_EXT', 0x80E1 )


def glInitBgraEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )