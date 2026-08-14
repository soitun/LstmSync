
<h1 align="center">LstmSync-v2</h1>
<div align="center">
<h2 align="center">超轻量无限时长数字人泛化模型！效果可行能否给个小星星！永久免费！</h2>
<a href="https://b23.tv/RL1mGQR">作者主页：一码超人</a><br/>
<a href="https://blog.csdn.net/weixin_47723549?type=blog">作者csdn：一码超人</a><br/>
<a href="https://b23.tv/4CKlq4Y">宣传大使：浪子之心科技</a><br/>
<a href="https://space.bilibili.com/3031494">宣传大使：刘悦的技术博客</a><br/>
</div>

## 🏋️‍♂️ 合作企业
- <a href="https://www.umi6.com">深圳优秘智能科技有限公司</a>
- 重庆爱文曲科技有限公司

## 🔥 更新

- `2026/04/28`: 发布云api版skills，适配openclaw龙虾等agent智能体，注意获取apikey的注册登录链接一定要有?invite=lstmsync参数，初始和充值积分优惠，地址：https://github.com/oneCodeSuperman/skyhuman-api
- `2026/08/15`: 采用全新网络架构！更强的唇形同时支持低显存无限音频时长推理，彻底解决显存不够，只能推理几分钟音频的问题同时保证唇形持续同步。推理速度全量模式在720P、1080P下可达到1:1。
  
## 📖 计划

- `2026/09/01`: web版页面。
- `2026/09/15`: 对trt推理加速的支持。
- `2026/10/15`: 对cpu、mac的支持。

## 🏗️ 注意事项【一定要看完！】

- 【商用说明】本项目作为sdk可免费商用，本项目非无私奉献核心代码与学术研究，仅仅是提供给大家免费使用，所以请攻击者或同行手下留情，核心不会开源的。莫要凉了这炽热的心~
- 本项目两个实例化类涉及api_key参数，请到：<a href="https://lstmsync.andclaw.cn/"> 注册地址 </a> 来注册获取。注意！api_key是永久有效的！
- 音频必须为16khz格式。
- 模型不含带超分功能，所以推理视频一定要清晰！清晰！清晰！不然如果推理视频不清晰，推理出来也不清晰！
- 注意！注意！注意！切勿修改权重onnx文件名称！
- python版本必须为3.10、pytorch建议2.0+、cuda12+等。
- onnxruntime-gpu版本根据cuda版本选定，如果cuda版本较高，建议装新版onnxruntime-gpu版本，因为实测过程中发现在新的cuda版本用旧的onnxruntime-gpu库推理速度会受影响。
- 4G+显存即可。
- 可能缺少C++库，无脑安装。64位：https://aka.ms/vs/17/release/vc_redist.x64.exe   32位：https://aka.ms/vs/17/release/vc_redist.x86.exe
- windows安装insightface库可能存在编译失败问题，需安装Desktop development with C++，无脑安装即可。链接地址：https://download.visualstudio.microsoft.com/download/pr/e514a25b-a89d-4051-a63c-05ccd9be41e9/88d8e1df44172b28e92df1c11fc900aef2d6d6e7e75491467f4c507c07d31f13/vs_BuildTools.exe
![image](https://github.com/user-attachments/assets/7c5ae4bf-e7d0-45dd-ae58-41f7c55ba25e)

## 🎬 Demo

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="33%"><b>原视频</b></td>
        <td width="33%"><b>256人脸美化</b></td>
        <td width="33%"><b>384人脸美化</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/08e8e933-8596-429c-b36c-dbb32c5b123c controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/b5b8716e-0407-4012-9d17-c0871c6034b2 controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/e39fafba-9116-4012-9502-45692a00be51 controls preload></video>
    </td>
  </tr>
</table>



## 📑 使用说明

- 注册api_key地址：
- 下载权重文件压缩包zip：https://pan.baidu.com/s/1g4BxwWvtvTiG8hq2Ib0P8w?pwd=kf8p 提取码: kf8p
- 下载后直接在根目录解压zip，目录结构：
```
checkpoints
inference.cp310-win_amd64.pyd  // windows系统
preprocess.cp310-win_amd64.pyd  // windows系统
inference.cpython-310-x86_64-linux-gnu.so // liunx系统
preprocess.cpython-310-x86_64-linux-gnu.so // liunx系统
requirements.txt
run.py
```
- 先安装好python3.10、cuda、pytorch等gpu环境，不懂则自行去csdn等平台查阅。
- 安装配置好ffmpeg环境变量
- 上述都完成后执行:
```
pip install -r requirements.txt // 50系显卡，python3.10版本支持
```
- 查看run.py脚本，参数说明有注释，该脚本为调用示例，可自行灵活使用。


## 联系
|  如需商务合作，加微信| 加群反馈与技术交流                                                                       |
|-------------------|------------------------------------------------------------------------------------------|
| ![微信](https://github.com/user-attachments/assets/e95e42a2-a6ec-4fbd-b65a-28a08aa11eaf) | ![微信群聊](https://github.com/user-attachments/assets/291b2914-19e4-45b2-9633-7d0b5bfaeb95) |




