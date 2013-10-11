/notify/seen
==============================

.. http:post:: /notify/seen

    .. admonition:: Action
    
        Mark all notifications of request user as "seen". The client can specify the **app** parameter
        to constrain the realm to a specific app like "wantto" or "dare".
    
    :param app: A parameter to constrain the realm of notifications to be marked as seen. For detail, please see :ref:`enum-app`
    :type app: *string*
    
    .. seealso:: The definition of :ref:`Notify model <model-notify>`
    
    **Sample Responses**:

        .. include:: ../null_response
