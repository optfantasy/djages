/searchcity/search
====================

.. http:get:: /searchcity/search

    .. admonition:: Action
    
        Search under the collection resource with RESTful parameters.
    
    :param q: The string to query objects.
    :type q: string
    
    :param location: Used when the **filter_type** is *"location"*.
    :type location: :ref:`field-location`
    
    :param filter_type: Specify this parameter to perform different search methods for the collection. 
    :type filter_type: string
        
    .. seealso:: :ref:`request-search` and the definition of :ref:`SearchCity model <model-search-city>`
        
        
    **Sample Responses**:
    
        .. include:: index_response