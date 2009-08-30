'''OpenGL extension IBM.cull_vertex

Overview (from the spec)
	
	IBM_cull_vertex provides a subset of the vertex culling functionality
	found in EXT_cull_vertex without providing a guarantee that faces will
	be culled because of it.  EXT_cull_vertex is a technically superior
	solution, but the vertex culling aspect of IBM_cull_vertex provides
	generally useful function cheaply (without imposing the mandated
	culling found in EXT_cull_vertex).

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/IBM/cull_vertex.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_IBM_cull_vertex'
_DEPRECATED = False



def glInitCullVertexIBM():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
