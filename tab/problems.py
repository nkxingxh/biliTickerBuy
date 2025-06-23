import gradio as gr


def problems_tab():
    gr.Markdown("""
> **分享一下经验**
> - 抢票前，不要去提前抢还没有发售的票，账号会异常。
> - 热门票要提前练习过验证码，热门项目填好并测好ctoken服务器
> - 使用不同的多个账号抢票 （可以每一个exe文件都使用不同的账号， 或者在使用这个程序的时候，手机使用其他的账号去抢）
> - 程序能保证用最快的速度发送订单请求，但是不保证这一次订单请求能够成功。所以不要完全依靠程序
> - 现在各个平台抢票和秒杀机制都是进抽签池抽签，网速快发请求多快在拥挤的时候基本上没有效果
> 此时就要看你有没有足够的设备和账号来提高中签率
> - 欢迎前往 [discussions](https://github.com/miaowuawa/MyGO/discussions) 分享你的经验
""")

    gr.Markdown("""
- **项目地址**：[miaowuawa/MyGO](https://github.com/miaowuawa/MyGO)
- **讨论区**：[Discussions](https://github.com/miaowuawa/MyGO/discussions)
- **问题反馈**：[Issues](https://github.com/miaowuawa/MyGO/issues)
  - [漏洞反馈](https://github.com/miaowuawa/MyGO/issues/new?assignees=&labels=bug%3F&projects=&template=bug-report.yml&title=%5BBug%5D%3A+)
  - [需求建议](https://github.com/miaowuawa/MyGO/issues/new?assignees=&labels=enhancement&projects=&template=feature-request.yml&title=%5BFeature%5D%3A+)
    """)
