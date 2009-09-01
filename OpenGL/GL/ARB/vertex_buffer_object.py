'''OpenGL extension ARB.vertex_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_buffer_object to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.vertex_buffer_object import *
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy
from OpenGL.arrays import ArrayDatatype

glDeleteBuffersARB = arrays.setInputArraySizeType(
    glDeleteBuffersARB,
    None,
    arrays.GLuintArray,
    'buffers',
)

glGenBuffersARB = wrapper.wrapper( glGenBuffersARB ).setOutput(
    'buffers', lambda n: (n,), 'n',
)

def _sizeOfArrayInput( pyArgs, index, wrapper ):
    return (
        arrays.ArrayDatatype.arrayByteCount( pyArgs[index] )
    )

@lazy( glBufferDataARB )
def glBufferDataARB( baseOperation, target, size, data=None, usage=None ):
    """Copy given data into the currently bound vertex-buffer-data object
    
    target -- the symbolic constant indicating which buffer type is intended
    size -- if provided, the count-in-bytes of the array
    data -- data-pointer to be used, may be None to initialize without 
        copying over a data-set 
    usage -- hint to the driver as to how to set up access to the buffer 
    
    Note: parameter "size" can be omitted, which makes the signature
        glBufferData( target, data, usage )
    instead of:
        glBufferData( target, size, data, usage )
    """
    if usage is None:
        usage = data 
        data = size 
        size = None 
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, size, data, usage )

@lazy( glBufferSubDataARB )
def glBufferSubDataARB( baseOperation, target, offset, size, data=None ):
    """Copy subset of data into the currently bound vertex-buffer-data object
    
    target -- the symbolic constant indicating which buffer type is intended
    offset -- offset from beginning of buffer at which to copy bytes
    size -- the count-in-bytes of the array (if an int/long), if None,
        calculate size from data, if an array and data is None, use as 
        data (i.e. the parameter can be omitted and calculated)
    data -- data-pointer to be used, may be None to initialize without 
        copying over a data-set 
    
    Note that if size is not an int/long it is considered to be data
    """
    try:
        if size is not None:
            size = int( size )
    except TypeError, err:
        if data is not None:
            raise TypeError(
                """Expect an integer size *or* a data-array, not both"""
            )
        data = size 
        size = None 
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, offset, size, data )