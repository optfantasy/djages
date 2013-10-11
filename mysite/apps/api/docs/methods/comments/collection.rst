/:collection/(object_id)/comments/
=====================================


.. _api-comment-collection-get:

GET
---

.. http:get:: /:collection/(object_id)/comments/

    .. admonition:: Action
    
        Query comments for an object.
    
    :param object_id: ID of an object
    :type object_id: :ref:`field-id`

    Equivalent to :ref:`Query Comment API <api-comments-query>`.
    
    .. seealso:: The definition of :ref:`Comment model <model-comment>`
    
    **Sample Responses**:
    
        .. include:: ../comments/index_response
        .. include:: ../errors/10004
        .. include:: ../errors/10005

.. _api-comment-collection-post:

POST
----

.. http:post:: /:collection/(object_id)/comments/

    .. admonition:: Action
    
        Create a comment for an object.

    :param object_id: ID of an object
    :type object_id: :ref:`field-id`
    :param comment: Comment content.
    :type comment: string

    Equivalent to :ref:`Create Comment API <api-comments-create>`.
    
    .. seealso:: The definition of :ref:`Comment model <model-comment>`
    
    **Sample Responses**:

        .. include:: ../comments/object_response
