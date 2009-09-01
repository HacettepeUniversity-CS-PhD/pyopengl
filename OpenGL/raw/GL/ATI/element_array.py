'''OpenGL extension ATI.element_array

Overview (from the spec)
    
    This extension provides a mechanism for an application to create
    an array of index data for use in specifying geometric primitives.
    
    This extension is most useful when used in conjunction with the
    ATI_vertex_array_object extension. ATI_vertex_array_object
    provides an interface for storing vertex array data in persistent,
    hardware-addressable memory. In cases where large amounts of
    vertex data are in use, the index data used to construct
    primitives (typically as passed to the GL through DrawElements)
    can impose a significant bandwidth burden. ATI_element_array
    allows the application to specify independent arrays of elements,
    which can then be cached using ATI_vertex_array_object.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ATI/element_array.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_element_array'
_DEPRECATED = False
GL_ELEMENT_ARRAY_ATI = constant.Constant( 'GL_ELEMENT_ARRAY_ATI', 0x8768 )
GL_ELEMENT_ARRAY_TYPE_ATI = constant.Constant( 'GL_ELEMENT_ARRAY_TYPE_ATI', 0x8769 )
glget.addGLGetConstant( GL_ELEMENT_ARRAY_TYPE_ATI, (1,) )
GL_ELEMENT_ARRAY_POINTER_ATI = constant.Constant( 'GL_ELEMENT_ARRAY_POINTER_ATI', 0x876A )
glElementPointerATI = platform.createExtensionFunction( 
'glElementPointerATI',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,ctypes.c_void_p,),
doc='glElementPointerATI(GLenum(type), c_void_p(pointer)) -> None',
argNames=('type','pointer',),
deprecated=_DEPRECATED,
)

glDrawElementArrayATI = platform.createExtensionFunction( 
'glDrawElementArrayATI',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,),
doc='glDrawElementArrayATI(GLenum(mode), GLsizei(count)) -> None',
argNames=('mode','count',),
deprecated=_DEPRECATED,
)

glDrawRangeElementArrayATI = platform.createExtensionFunction( 
'glDrawRangeElementArrayATI',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,constants.GLsizei,),
doc='glDrawRangeElementArrayATI(GLenum(mode), GLuint(start), GLuint(end), GLsizei(count)) -> None',
argNames=('mode','start','end','count',),
deprecated=_DEPRECATED,
)


def glInitElementArrayATI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )