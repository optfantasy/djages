/comments/
==============

.. _api-comments-query:

GET
---

.. http:get:: /comments/

    .. admonition:: Action
    
        Query comments.
    
    :param target_id: ID of a target object with comments. 
    :type target_id: :ref:`field-id`
    :param user_id: ID of user. 
    :type user_id: :ref:`field-id`
    
    .. seealso:: The definition of :ref:`Comment model <model-comment>`
    
    **Sample Responses**:
    
        .. include:: index_response
        .. include:: ../errors/10004
        .. include:: ../errors/10005

.. _api-comments-create:

POST
----

.. http:post:: /comments/

    .. admonition:: Action
    
        Create a comment.

    :param target_type: Target type.
    :type target_type: :ref:`field-type`
    :param target_id: Target id.
    :type target_id: :ref:`field-id`
    :param comment: Comment content.
    :type comment: string
    
    .. seealso:: The definition of :ref:`Comment model <model-comment>`
    
    **Sample Responses**:

        .. include:: object_response
