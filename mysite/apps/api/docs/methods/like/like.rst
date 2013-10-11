/like/like
================

.. _api-like-like:

.. http:post:: /like/like

    .. admonition:: Action
    
        Likes (me toos) a target object as the currently authenticated user.

    :param target_type: Target object's type.
    :type target_type: :ref:`field-type`
    :param target_id: Target object's id
    :type target_id: :ref:`field-id`

    **Sample Responses**:

        .. include:: ../effective_response
        .. include:: ../errors/10005