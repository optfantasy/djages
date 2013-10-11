/comments/(comment_id)/
==============================

GET
---

.. http:get:: /comments/(comment_id)/
    
    .. admonition:: Action
    
        Get a comment object with json format.
    
    :param comment_id: ID of a comment
    :type comment_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`Comment model <model-comment>`
    
    **Sample Responses**:

        .. include:: object_response

DELETE
------

.. http:delete:: /comments/(comment_id)/

    .. admonition:: Action
    
        Delete a comment object with specified comment_id.
    
    :param comment_id: ID of a comment
    :type comment_id: :ref:`field-id`
        
    **Sample Responses**:
    
        .. include:: ../null_response