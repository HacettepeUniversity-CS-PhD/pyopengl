'''OpenGL extension IBM.vertex_array_lists

Overview (from the spec)
    
    This extension introduces seven (7) new functions that set the 
    vertex array pointers. However, instead of a single pointer, these
    functions provide a list of array pointers that can be used by the 
    EXT_multi_draw_arrays and IBM_multimode_draw_arrays extension 
    functions to draw from multiple of vertex arrays. The first 
    primitive will use the first array in the list, the second primitive
    will use the second array in the list, and so forth. If a glDrawArray,
    DrawElements, or DrawRangeElements function is used, then 
    only the first vertex array in the list is used.
    
    When a vertex array list is specified, only the list pointer
    is kept by the underlying OpenGL function. Therefore, the list
    must be staticly defined for the entire duration of its usage,
    much in the same manner as the vertex arrays themselves. Also
    note that the list function can therefore also be used to change
    array pointers without making a OpenGL API function call.
    
    A <ptrstride> value of zero (0) can be used to force all primitives
    of a multi-vertex array to use only the first vertex array in 
    the list. 
    
    The <stride> parameter of the list pointer functions differs from
    that of the non-list vertex array pointer functions in that 1)
    both negative and positive strides are accepted thusly allowing
    vertex lists to be rendered in reverse order; 2) a <stride> of
    zero (0) results in no stride and can be used to specify a single
    vertex attribute for each vertex of the primitive.
    
    These new functions are a superset of the standard OpenGL 1.2 vertex
    array (non-list) pointer functions and share common state. Therefore,
    the list pointer and non-list pointer functions can be used
    interchangably.
    
    New queries are provided by this extension so that ZAPdb can be extended
    to query the list pointer state whenever a vertex array function 
    is traced. The pointer returned by a query of *_ARRAY_POINTER returns
    the first entry in the array list.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/IBM/vertex_array_lists.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_IBM_vertex_array_lists'
_DEPRECATED = False

glColorPointerListIBM = platform.createExtensionFunction( 
'glColorPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glColorPointerListIBM(GLint(size), GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('size','type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glSecondaryColorPointerListIBM = platform.createExtensionFunction( 
'glSecondaryColorPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glSecondaryColorPointerListIBM(GLint(size), GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('size','type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glEdgeFlagPointerListIBM = platform.createExtensionFunction( 
'glEdgeFlagPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,ctypes.POINTER(ctypes.POINTER(constants.GLboolean)),constants.GLint,),
doc='glEdgeFlagPointerListIBM(GLint(stride), POINTER(ctypes.POINTER(constants.GLboolean))(pointer), GLint(ptrstride)) -> None',
argNames=('stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glFogCoordPointerListIBM = platform.createExtensionFunction( 
'glFogCoordPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glFogCoordPointerListIBM(GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glIndexPointerListIBM = platform.createExtensionFunction( 
'glIndexPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glIndexPointerListIBM(GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glNormalPointerListIBM = platform.createExtensionFunction( 
'glNormalPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glNormalPointerListIBM(GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glTexCoordPointerListIBM = platform.createExtensionFunction( 
'glTexCoordPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glTexCoordPointerListIBM(GLint(size), GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('size','type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)

glVertexPointerListIBM = platform.createExtensionFunction( 
'glVertexPointerListIBM',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLint,ctypes.POINTER(ctypes.c_void_p),constants.GLint,),
doc='glVertexPointerListIBM(GLint(size), GLenum(type), GLint(stride), POINTER(ctypes.c_void_p)(pointer), GLint(ptrstride)) -> None',
argNames=('size','type','stride','pointer','ptrstride',),
deprecated=_DEPRECATED,
)


def glInitVertexArrayListsIBM():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )