各种流程图时序图
==========

### 二维码登录/注册流程

> 第三方、商家同指第三方

<div class="diagram">
participant 第三方
participant 大众版
participant 服务器
participant 验签服务
第三方->大众版: 生成二维码或者唤醒大众版
Note over 大众版: 得到第三方数据
大众版->服务器: 发送签名密文
服务器-->验签服务: 转发密文
验签服务-->服务器: 返回验签解密数据
Note over 服务器: 处理登录/注册业务流程
服务器-->验签服务: 发送返回数据
验签服务-->服务器: 返回签名密文
服务器->大众版: 返回签名密文

服务器->第三方: 回调第三方接口(sdk原文)
Note over 第三方: 验证数据
第三方-->验签服务: 发送返回数据
验签服务-->第三方: 返回签名密文
Note over 第三方: 处理结果
</div>

### 第三方支付流程 初稿

> 第三方、商家同指第三方

<div class="diagram">
participant 第三方
participant 大众版
participant 服务器
participant 验签服务
participant 银行业务

第三方->大众版: 生成二维码或者唤醒大众版
Note over 大众版: 得到第三方数据
大众版->服务器: 发送签名密文
服务器-->验签服务: 转发密文
验签服务-->服务器: 返回验签解密数据
Note over 服务器: 判断支付数据是否正确
服务器->银行业务: 发送银行渠道
Note over 银行业务: 处理扣款业务
银行业务->服务器: 完成扣款
服务器-->验签服务: 发送返回数据
验签服务-->服务器: 返回签名密文
服务器->大众版: 返回签名密文
Note over 大众版: 验证数据
服务器->第三方: 回调第三方接口
Note over 第三方: 处理结果
</div>

<script src="https://bramp.github.io/js-sequence-diagrams/js/webfont.js"></script>
<script src="https://bramp.github.io/js-sequence-diagrams/js/snap.svg-min.js"></script>
<script src="https://bramp.github.io/js-sequence-diagrams/js/underscore-min.js"></script>
<script src="https://bramp.github.io/js-sequence-diagrams/js/sequence-diagram-min.js"></script>


<script>
  // var diagram = Diagram.parse("A->B: Message");
  // diagram.drawSVG("diagram", {theme: 'hand'});
  $(".diagram").sequenceDiagram({theme: 'simple'});
</script>
