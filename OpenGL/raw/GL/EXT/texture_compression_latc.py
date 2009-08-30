'''OpenGL extension EXT.texture_compression_latc

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_compression_latc.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_compression_latc'
_DEPRECATED = False
GL_COMPRESSED_LUMINANCE_LATC1_EXT = constant.Constant( 'GL_COMPRESSED_LUMINANCE_LATC1_EXT', 0x8C70 )
GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT = constant.Constant( 'GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT', 0x8C71 )
GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT = constant.Constant( 'GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT', 0x8C72 )
GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT = constant.Constant( 'GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT', 0x8C73 )


def glInitTextureCompressionLatcEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
