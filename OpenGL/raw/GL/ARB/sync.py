'''OpenGL extension ARB.sync

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/sync.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_sync'
_DEPRECATED = False
GL_MAX_SERVER_WAIT_TIMEOUT = constant.Constant( 'GL_MAX_SERVER_WAIT_TIMEOUT', 0x9111 )
GL_OBJECT_TYPE = constant.Constant( 'GL_OBJECT_TYPE', 0x9112 )
GL_SYNC_CONDITION = constant.Constant( 'GL_SYNC_CONDITION', 0x9113 )
GL_SYNC_STATUS = constant.Constant( 'GL_SYNC_STATUS', 0x9114 )
GL_SYNC_FLAGS = constant.Constant( 'GL_SYNC_FLAGS', 0x9115 )
GL_SYNC_FENCE = constant.Constant( 'GL_SYNC_FENCE', 0x9116 )
GL_SYNC_GPU_COMMANDS_COMPLETE = constant.Constant( 'GL_SYNC_GPU_COMMANDS_COMPLETE', 0x9117 )
GL_UNSIGNALED = constant.Constant( 'GL_UNSIGNALED', 0x9118 )
GL_SIGNALED = constant.Constant( 'GL_SIGNALED', 0x9119 )
GL_ALREADY_SIGNALED = constant.Constant( 'GL_ALREADY_SIGNALED', 0x911A )
GL_TIMEOUT_EXPIRED = constant.Constant( 'GL_TIMEOUT_EXPIRED', 0x911B )
GL_CONDITION_SATISFIED = constant.Constant( 'GL_CONDITION_SATISFIED', 0x911C )
GL_WAIT_FAILED = constant.Constant( 'GL_WAIT_FAILED', 0x911D )
GL_SYNC_FLUSH_COMMANDS_BIT = constant.Constant( 'GL_SYNC_FLUSH_COMMANDS_BIT', 0x1 )
GL_TIMEOUT_IGNORED = constant.Constant( 'GL_TIMEOUT_IGNORED', 0xFFFFFFFFFFFFFFFF )
glFenceSync = platform.createExtensionFunction( 
'glFenceSync',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLsync, 
argTypes=(constants.GLenum,constants.GLbitfield,),
doc='glFenceSync(GLenum(condition), GLbitfield(flags)) -> constants.GLsync',
argNames=('condition','flags',),
deprecated=_DEPRECATED,
)

glIsSync = platform.createExtensionFunction( 
'glIsSync',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLsync,),
doc='glIsSync(GLsync(sync)) -> constants.GLboolean',
argNames=('sync',),
deprecated=_DEPRECATED,
)

glDeleteSync = platform.createExtensionFunction( 
'glDeleteSync',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsync,),
doc='glDeleteSync(GLsync(sync)) -> None',
argNames=('sync',),
deprecated=_DEPRECATED,
)

glClientWaitSync = platform.createExtensionFunction( 
'glClientWaitSync',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLenum, 
argTypes=(constants.GLsync,constants.GLbitfield,constants.GLuint64,),
doc='glClientWaitSync(GLsync(sync), GLbitfield(flags), GLuint64(timeout)) -> constants.GLenum',
argNames=('sync','flags','timeout',),
deprecated=_DEPRECATED,
)

glWaitSync = platform.createExtensionFunction( 
'glWaitSync',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsync,constants.GLbitfield,constants.GLuint64,),
doc='glWaitSync(GLsync(sync), GLbitfield(flags), GLuint64(timeout)) -> None',
argNames=('sync','flags','timeout',),
deprecated=_DEPRECATED,
)

glGetInteger64v = platform.createExtensionFunction( 
'glGetInteger64v',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLint64Array,),
doc='glGetInteger64v(GLenum(pname), GLint64Array(params)) -> None',
argNames=('pname','params',),
deprecated=_DEPRECATED,
)

glGetSynciv = platform.createExtensionFunction( 
'glGetSynciv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsync,constants.GLenum,constants.GLsizei,arrays.GLsizeiArray,arrays.GLintArray,),
doc='glGetSynciv(GLsync(sync), GLenum(pname), GLsizei(bufSize), GLsizeiArray(length), GLintArray(values)) -> None',
argNames=('sync','pname','bufSize','length','values',),
deprecated=_DEPRECATED,
)


def glInitSyncARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
