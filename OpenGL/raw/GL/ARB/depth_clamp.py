'''OpenGL extension ARB.depth_clamp

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/depth_clamp.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_depth_clamp'
_DEPRECATED = False
GL_DEPTH_CLAMP = constant.Constant( 'GL_DEPTH_CLAMP', 0x864F )


def glInitDepthClampARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
