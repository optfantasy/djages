/weibo/connect
=======================

.. http:get:: /weibo/connect

    .. admonition:: Action
    
        Conduct a complete flow to connect a weibo user to a Gulu user.
        The client will be redirected to weibo login page and be asked to authorize gulu to 
        access his data.
   

    **Responses**

    If connect success -> redirect to ``/connect_success``. If connect fail ->
    redirect to ``/connect_fail``
   