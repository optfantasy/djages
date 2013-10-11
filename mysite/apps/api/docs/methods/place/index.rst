/place/
==============

GET
---

.. http:get:: /place/

    .. admonition:: Action
    
        Query places.
    
    :param name: Name of the place.
    :type name: string
        
    .. seealso:: The definition of :ref:`Place model <model-place>`
        
        
    **Sample Responses**:
    
        .. include:: index_response
        

POST
----

.. http:post:: /place/

    .. admonition:: Action
    
        Create a place.
    
    :param name: Name of the place.
    :type name: string
    
    :param address: Address of the place.
    :type address: string
    
    :param city: The city of the place.
    :type city: string
    
    :param location: The location of the place.
    :type location: :ref:`field-location`
    
    :param photo_id: **[opt]** The profile photo of the place.
    :type photo_id: :ref:`field-id`

    .. seealso:: The definition of :ref:`Place model <model-place>`
    
    **Sample Responses**:
    
        .. include:: object_response

