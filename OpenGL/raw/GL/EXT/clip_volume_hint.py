'''OpenGL extension EXT.clip_volume_hint

Overview (from the spec)
    
    EXT_clip_volume_hint provides a mechanism for applications to
    indicate that they do not require clip volume clipping for
    primitives. It allows applications to maximize performance in
    situations where they know that clipping is unnecessary.
    EXT_clip_volume_hint is only an indication, though, and
    implementations are free to ignore it.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/clip_volume_hint.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_clip_volume_hint'
_DEPRECATED = False
GL_CLIP_VOLUME_CLIPPING_HINT_EXT = constant.Constant( 'GL_CLIP_VOLUME_CLIPPING_HINT_EXT', 0x80F0 )
glget.addGLGetConstant( GL_CLIP_VOLUME_CLIPPING_HINT_EXT, (1,) )


def glInitClipVolumeHintEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )