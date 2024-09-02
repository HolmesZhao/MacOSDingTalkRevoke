# MacOSDingTalkRevoke
MacOS 的钉钉防撤回脚本

支持 arm64 架构的 7.0.12 版本

支持 arm64 架构的 7.6.0 版本

支持 arm64 架构的 7.6.10 版本

主要是自用的, 里面的原理很简单, 就是替换 js 的代码, 有兴趣的可以自己看看

# Download APP
官方下载地址:

[https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.0.12.5_28488321_arm64.dmg](https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.0.12.5_28488321_arm64.dmg)

[https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.6.0_38510687_universal.dmg](https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.6.0_38510687_universal.dmg)

[https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.6.10_39731775_universal.dmg](https://dtapp-pub.dingtalk.com/dingtalk-desktop/mac_dmg/Release/M1-Beta/DingTalk_v7.6.10_39731775_universal.dmg)

# How to use

```python
// 7.0.12
python3 dingtalkrevoke.py

// 最新的, 所有版本都有在, 根据需要的换变量就好
python3 dingtalkrevoke7_6_0.py
```

# 感谢

感谢大佬的开源
https://github.com/wuyoukm/MAC-DingTalkRevokeMsgPatcher
