排序参数
===

如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

下面是一些常见的参数:

-  **?ordering=-name**：指定返回结果按照哪个属性排序，以及排序顺序。通过+，-符号设置升序还是倒序，-为倒序，不写或者+为升序。
