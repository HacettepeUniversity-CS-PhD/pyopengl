'''OpenGL extension MESA.ycbcr_texture

Overview (from the spec)
	
	This extension supports texture images stored in the YCbCr format.
	There is no support for converting YCbCr images to RGB or vice versa
	during pixel transfer.  The texture's YCbCr colors are converted to
	RGB during texture sampling, after-which, all the usual per-fragment
	operations take place.  Only 2D texture images are supported (not
	glDrawPixels, glReadPixels, etc).
	
	A YCbCr pixel (texel) is a 16-bit unsigned short with two components.
	The first component is luminance (Y).  For pixels in even-numbered
	image columns, the second component is Cb.  For pixels in odd-numbered
	image columns, the second component is Cr.  If one were to convert the
	data to RGB one would need to examine two pixels from columns N and N+1
	(where N is even) to deduce the RGB color.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/MESA/ycbcr_texture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_MESA_ycbcr_texture'
_DEPRECATED = False
GL_UNSIGNED_SHORT_8_8_MESA = constant.Constant( 'GL_UNSIGNED_SHORT_8_8_MESA', 0x85BA )
GL_UNSIGNED_SHORT_8_8_REV_MESA = constant.Constant( 'GL_UNSIGNED_SHORT_8_8_REV_MESA', 0x85BB )
GL_YCBCR_MESA = constant.Constant( 'GL_YCBCR_MESA', 0x8757 )


def glInitYcbcrTextureMESA():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
