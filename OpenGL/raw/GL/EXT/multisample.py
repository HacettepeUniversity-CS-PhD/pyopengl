'''OpenGL extension EXT.multisample

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/multisample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_multisample'
_DEPRECATED = False
GL_MULTISAMPLE_EXT = constant.Constant( 'GL_MULTISAMPLE_EXT', 0x809D )
GL_SAMPLE_ALPHA_TO_MASK_EXT = constant.Constant( 'GL_SAMPLE_ALPHA_TO_MASK_EXT', 0x809E )
GL_SAMPLE_ALPHA_TO_ONE_EXT = constant.Constant( 'GL_SAMPLE_ALPHA_TO_ONE_EXT', 0x809F )
GL_SAMPLE_MASK_EXT = constant.Constant( 'GL_SAMPLE_MASK_EXT', 0x80A0 )
GL_1PASS_EXT = constant.Constant( 'GL_1PASS_EXT', 0x80A1 )
GL_2PASS_0_EXT = constant.Constant( 'GL_2PASS_0_EXT', 0x80A2 )
GL_2PASS_1_EXT = constant.Constant( 'GL_2PASS_1_EXT', 0x80A3 )
GL_4PASS_0_EXT = constant.Constant( 'GL_4PASS_0_EXT', 0x80A4 )
GL_4PASS_1_EXT = constant.Constant( 'GL_4PASS_1_EXT', 0x80A5 )
GL_4PASS_2_EXT = constant.Constant( 'GL_4PASS_2_EXT', 0x80A6 )
GL_4PASS_3_EXT = constant.Constant( 'GL_4PASS_3_EXT', 0x80A7 )
GL_SAMPLE_BUFFERS_EXT = constant.Constant( 'GL_SAMPLE_BUFFERS_EXT', 0x80A8 )
GL_SAMPLES_EXT = constant.Constant( 'GL_SAMPLES_EXT', 0x80A9 )
GL_SAMPLE_MASK_VALUE_EXT = constant.Constant( 'GL_SAMPLE_MASK_VALUE_EXT', 0x80AA )
GL_SAMPLE_MASK_INVERT_EXT = constant.Constant( 'GL_SAMPLE_MASK_INVERT_EXT', 0x80AB )
GL_SAMPLE_PATTERN_EXT = constant.Constant( 'GL_SAMPLE_PATTERN_EXT', 0x80AC )
GL_MULTISAMPLE_BIT_EXT = constant.Constant( 'GL_MULTISAMPLE_BIT_EXT', 0x20000000 )
glSampleMaskEXT = platform.createExtensionFunction( 
'glSampleMaskEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLclampf,constants.GLboolean,),
doc='glSampleMaskEXT(GLclampf(value), GLboolean(invert)) -> None',
argNames=('value','invert',),
deprecated=_DEPRECATED,
)

glSamplePatternEXT = platform.createExtensionFunction( 
'glSamplePatternEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glSamplePatternEXT(GLenum(pattern)) -> None',
argNames=('pattern',),
deprecated=_DEPRECATED,
)


def glInitMultisampleEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
