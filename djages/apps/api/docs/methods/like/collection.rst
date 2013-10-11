/:collection/(object_id)/likes/
=================================

.. _api-like-collection-post:

POST
-----

.. http:post:: /:collection/(object_id)/likes/

    .. admonition:: Action
    
        Likes an object as the currently authenticated user.

    :param object_id: ID of a object
    :type object_id: :ref:`field-id`
    
    Equivalent to :ref:`Like API <api-like-like>`.

    **Sample Responses**:

        .. include:: ../effective_response


.. _api-like-collection-delete:

DELETE
-------

.. http:delete:: /:collection/(object_id)/likes/

    .. admonition:: Action
    
        Unlikes an object as the currently authenticated user.

    :param object_id: ID of a object
    :type object_id: :ref:`field-id`

    Equivalent to :ref:`Unlike API <api-like-unlike>`.

    **Sample Responses**:

        .. include:: ../effective_response


.. _api-like-collection-get:

GET
-----

.. http:get:: /:collection/(object_id)/likes/

    .. admonition:: Action
    
        Get likers for an object.

    :param object_id: ID of a object
    :type object_id: :ref:`field-id`

    Return an array of basic user objects, which are likers of this object.

    .. seealso:: The definition of :ref:`User model <model-user>`
    
    **Sample Responses**:

        .. code-block:: js
        
            {
                "response": [{
                    "photo": {
                        "id": "4e5df4304aa015c4ba000004",
                        "thumb": "/media/cache/photos/image50x50/1L_1.jpeg"
                    },
                    "nickname": "Eric",
                    "id": "4e46434741b6994c70000000"
                }],
                "success": true
            }