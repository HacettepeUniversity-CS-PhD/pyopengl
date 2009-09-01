'''OpenGL extension SGIX.resample

Overview (from the spec)
    
    This extension enhances the unpacking resampling capabilities
    of the SGIX_subsample extension.
    
    When pixel data is received from the client and an unpacking
    upsampling mode other than PIXEL_SUBSAMPLE_RATE_4444_SGIX is
    specified, the upsampling is performed via one of two methods:
    RESAMPLE_REPLICATE_SGIX, RESAMPLE_ZERO_FILL_SGIX.
    Replicate and zero fill are provided to
    give the application greatest performance and control over the
    filtering process.
    
    However, when pixel data is read back to the client and a
    packing downsampling mode other than PIXEL_SUBSAMPLE_RATE_4444_SGIX
    is specified, downsampling is
    performed via simple component decimation (point sampling). That is,
    only the RESAMPLE_DECIMATE_SGIX is valid.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/resample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_resample'
_DEPRECATED = False
GL_PACK_RESAMPLE_SGIX = constant.Constant( 'GL_PACK_RESAMPLE_SGIX', 0x842C )
glget.addGLGetConstant( GL_PACK_RESAMPLE_SGIX, (1,) )
GL_UNPACK_RESAMPLE_SGIX = constant.Constant( 'GL_UNPACK_RESAMPLE_SGIX', 0x842D )
glget.addGLGetConstant( GL_UNPACK_RESAMPLE_SGIX, (1,) )
GL_RESAMPLE_REPLICATE_SGIX = constant.Constant( 'GL_RESAMPLE_REPLICATE_SGIX', 0x842E )
GL_RESAMPLE_ZERO_FILL_SGIX = constant.Constant( 'GL_RESAMPLE_ZERO_FILL_SGIX', 0x842F )
GL_RESAMPLE_DECIMATE_SGIX = constant.Constant( 'GL_RESAMPLE_DECIMATE_SGIX', 0x8430 )


def glInitResampleSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )