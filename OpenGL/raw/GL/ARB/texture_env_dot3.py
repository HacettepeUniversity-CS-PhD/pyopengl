'''OpenGL extension ARB.texture_env_dot3

Overview (from the spec)
	
	Adds new operation to the texture combiner operations.
	
	    DOT3_RGB_ARB                    Arg0 <dotprod> Arg1
	    DOT3_RGBA_ARB                   Arg0 <dotprod> Arg1
	
	where Arg0, Arg1 are specified by <params> parameter of 
	TexEnvf, TexEnvi, TexEnvfv, and TexEnviv when the <pname>
	parameter value is SOURCE0_RGB_ARB and SOURCE1_RGB_ARB.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_env_dot3.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_env_dot3'
_DEPRECATED = False
GL_DOT3_RGB_ARB = constant.Constant( 'GL_DOT3_RGB_ARB', 0x86AE )
GL_DOT3_RGBA_ARB = constant.Constant( 'GL_DOT3_RGBA_ARB', 0x86AF )


def glInitTextureEnvDot3ARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
