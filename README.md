<h1 align="center">LstmSync</h1>
<div align="center">
<h2 align="center">无需网络，本地4G显存即可使用的数字人泛化模型！效果可行能否给个小星星！</h2>
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
  
## 📖 计划

- `-`: 对mac的推理支持【暂时搁置】。
- `2026/06/06`: web版页面。

## 🏗️ 注意事项【一定要看完！】

- 【商用说明】本项目作为sdk可免费商用，本项目非无私奉献核心代码与学术研究，仅仅是提供给大家免费使用，所以请攻击者或同行手下留情，核心不会开源的。莫要凉了这炽热的心~
- key.txt文件说明：当提示key无法使用时，请关注本仓库来更新替换key.txt。在此声明本项目不会因key导致断档使用，所以当发现key无法使用时只需关注仓库去更新key.txt文件就好了，如果觉得麻烦可以联系商务合作。
- 新版本请重新去下方百度云盘地址下载权重文件！内包含192、256、384权重文件。
- 音频必须为16khz格式。
- 模型不含带超分功能，所以推理视频一定要清晰！清晰！清晰！不然如果推理视频不清晰，推理出来也不清晰！
- 注意！注意！注意！切勿修改权重pth文件名称！使用不同分辨率推理，请在human_path参数上更换pth即可，pth名称就是模型的人脸尺寸。
- weight_sync参数为调节口型开合度，又可以理解为强制唇同步，默认0.5，如果感觉过于夸张则调小，如感觉同步还是差一些则调大，最小为0，最大为无限制，过高可能破坏图像。
- 推理后的脸部左右遮罩模糊，可通过scale_h，scale_w进行调节，越大遮罩范围越小，该设置为比例，所以一次调整好后续无需调整。一般设置：scale_h=1.6， scale_w=3.6， 可自行再进行精调。
- python版本必须为3.10、pytorch建议2.0+、cuda12+等。
- 4G+显存即可。
- windows安装insightface库可能存在编译失败问题，需安装Desktop development with C++，无脑安装即可。链接地址：https://download.visualstudio.microsoft.com/download/pr/e514a25b-a89d-4051-a63c-05ccd9be41e9/88d8e1df44172b28e92df1c11fc900aef2d6d6e7e75491467f4c507c07d31f13/vs_BuildTools.exe
![image](https://github.com/user-attachments/assets/7c5ae4bf-e7d0-45dd-ae58-41f7c55ba25e)

## 🎬 Demo

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="33%"><b>原视频</b></td>
        <td width="33%"><b>非美化256.o</b></td>
        <td width="33%"><b>美化版256.m</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/5d02ac75-0ce1-40e5-91e1-2f592918c414 controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/4eeed293-202b-4d6a-a32f-50d072c89db1 controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/be85fec2-bf51-4065-ac2c-c6e69de23c43 controls preload></video>
    </td>
  </tr>
</table>


## 📑 使用说明

- 下载权重文件压缩包zip：https://pan.baidu.com/s/1IuYvbpCD1tOkyyiq_uIYvw 提取码: maiw
- 下载后直接在根目录解压zip，目录结构：
```
checkpoints
key.txt
lstmsync_func.cp310-win_amd64.pyd  // windows系统
lstmsync_func.cpython-310-x86_64-linux-gnu.so // liunx系统
requirements.txt
run.py
```
- 先安装好python3.10、cuda、pytorch等gpu环境，不懂则自行去csdn等平台查阅。
- 安装配置好ffmpeg环境变量
- 上述都完成后执行:
```
pip install -r requirements-50.txt // 50系显卡，python3.10版本支持
```
- 查看run.py脚本，参数说明有注释，该脚本为调用示例，可自行灵活使用。


## 联系
|  如需商务合作，加微信| 加群反馈与技术交流                                                                       |
|-------------------|------------------------------------------------------------------------------------------|
| ![微信](https://github.com/user-attachments/assets/e95e42a2-a6ec-4fbd-b65a-28a08aa11eaf) | ![微信群聊](https://github.com/user-attachments/assets/dc231287-5313-4f04-a5dd-cafac0b89d8e) |




