'''OpenGL extension ARB.occlusion_query

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.occlusion_query to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines a mechanism whereby an application can query
	the number of pixels (or, more precisely, samples) drawn by a
	primitive or group of primitives.
	
	The primary purpose of such a query (hereafter referred to as an
	"occlusion query") is to determine the visibility of an object.
	Typically, the application will render the major occluders in the
	scene, then perform an occlusion query for the bounding box of each
	detail object in the scene.  Only if said bounding box is visible,
	i.e., if at least one sample is drawn, should the corresponding object
	be drawn.
	
	The earlier HP_occlusion_test extension defined a similar mechanism,
	but it had two major shortcomings.
	
	- It returned the result as a simple GL_TRUE/GL_FALSE result, when in
	  fact it is often useful to know exactly how many samples were
	  drawn.
	- It provided only a simple "stop-and-wait" model for using multiple
	  queries.  The application begins an occlusion test and ends it;
	  then, at some later point, it asks for the result, at which point
	  the driver must stop and wait until the result from the previous
	  test is back before the application can even begin the next one.
	  This is a very simple model, but its performance is mediocre when
	  an application wishes to perform many queries, and it eliminates
	  most of the opportunities for parallelism between the CPU and GPU.
	
	This extension solves both of those problems.  It returns as its
	result the number of samples that pass the depth and stencil tests,
	and it encapsulates occlusion queries in "query objects" that allow
	applications to issue many queries before asking for the result of
	any one.  As a result, they can overlap the time it takes for the
	occlusion query results to be returned with other, more useful work,
	such as rendering other parts of the scene or performing other
	computations on the CPU.
	
	There are many situations where a pixel/sample count, rather than a
	boolean result, is useful.
	
	- Objects that are visible but cover only a very small number of
	  pixels can be skipped at a minimal reduction of image quality.
	- Knowing exactly how many pixels an object might cover may help the
	  application decide which level-of-detail model should be used.  If
	  only a few pixels are visible, a low-detail model may be
	  acceptable.
	- "Depth peeling" techniques, such as order-independent transparency,
	  need to know when to stop rendering more layers; it is difficult to
	  determine a priori how many layers are needed.  A boolean result
	  allows applications to stop when more layers will not affect the
	  image at all, but this will likely result in unacceptable
	  performance.  Instead, it makes more sense to stop rendering when
	  the number of pixels in each layer falls below a given threshold.
	- Occlusion queries can replace glReadPixels of the depth buffer to
	  determine whether (for example) a light source is visible for the
	  purposes of a lens flare effect or a halo to simulate glare.  Pixel
	  counts allow you to compute the percentage of the light source that
	  is visible, and the brightness of these effects can be modulated
	  accordingly.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/occlusion_query.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.occlusion_query import *
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy
from OpenGL.GL import glget
from OpenGL import converters
@lazy( glDeleteQueriesARB )
def glDeleteQueriesARB( baseOperation, n, ids=None ):
    """Delete the given queries 
    
    n -- either the number of queries to delete, or an array of query values 
    ids -- if provided, the array/pointer to the queries to delete 
    """
    if ids is None:
        ids = arrays.GLuintArray.asArray( n )
        n = arrays.GLuintArray.arraySize( ids )
    else:
        ids = arrays.GLuintArray.asArray( ids )
    return baseOperation( n,ids )
@lazy( glGenQueriesARB )
def glGenQueriesARB( baseOperation, n, ids=None ):
    """Generate n queries, if ids is None, is allocated

    returns array of ids
    """
    if ids is None:
        ids = arrays.GLuintArray.zeros( (n,))
    else:
        ids = arrays.GLuintArray.asArray( ids )
    baseOperation( n, ids )
    return ids

for func in (
    'glGetQueryivARB','glGetQueryObjectivARB','glGetQueryObjectuivARB',
):
    globals()[func] = wrapper.wrapper(globals()[func]).setOutput(
        "params", (1,)
    )
try:
    del func, glget
except NameError as err:
    pass
