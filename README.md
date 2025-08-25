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

- `2025/06/30`: 开源192尺寸泛化权重
- `2025/07/01`: 支持liunx系统兼容
- `2025/07/17`: 新增python3.10版本支持，用于兼容50系显卡
- `2025/08/14`: 新增256、384人脸尺寸，更新了key文件，新增fp32 or fp16设置、口型大小调节等超参数设置。

## 📖 计划

- `2025/09/01`: 开发api接口及界面支持

## 🏗️ 注意事项【一定要看完！】

- 【商用说明】本项目作为sdk可免费商用，本项目非无私奉献核心代码与学术研究，仅仅是提供给大家免费使用，所以请攻击者或同行手下留情，核心不会开源的。莫要凉了这炽热的心~
- 新版本请重新去下方百度云盘地址下载权重文件！内包含192、256、384权重文件。
- 音频必须为16khz格式。
- 模型不含带超分功能，所以推理视频一定要清晰！清晰！清晰！不然如果推理视频不清晰，推理出来也不清晰！
- 注意！注意！注意！切勿修改权重pth文件名称！使用不同分辨率推理，请在human_path参数上更换pth即可，pth名称就是模型的人脸尺寸。
- weight_sync参数为调节口型开合度，又可以理解为强制唇同步，默认0.5，如果感觉过于夸张则调小，如感觉同步还是差一些则调大，最小为0，最大为1。
- 推理后的脸部左右遮罩模糊，可通过scale_h，scale_w进行调节，越大遮罩范围越小，该设置为比例，所以一次调整好后续无需调整。一般设置：scale_h=1.6， scale_w=3.6， 可自行再进行精调。
- python版本必须为3.8，如果显卡为50系则版本必须为3.10、pytorch建议2.0+、cuda11.8等。
- 4G+显存即可。
- windows安装insightface库可能存在编译失败问题，需安装Desktop development with C++，无脑安装即可。链接地址：https://download.visualstudio.microsoft.com/download/pr/e514a25b-a89d-4051-a63c-05ccd9be41e9/88d8e1df44172b28e92df1c11fc900aef2d6d6e7e75491467f4c507c07d31f13/vs_BuildTools.exe
![image](https://github.com/user-attachments/assets/7c5ae4bf-e7d0-45dd-ae58-41f7c55ba25e)


## 🎬 Demo

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="50%"><b>192人脸尺寸【demo1】</b></td>
        <td width="50%"><b>192人脸尺寸【demo2】</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/08a01251-b682-49d3-8243-cd5ceeb2f6f5 controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/6c00f041-cddc-417e-9f90-6cb86693f43d controls preload></video>
    </td>
  </tr>
</table>


<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="50%"><b>256人脸尺寸【demo1】</b></td>
        <td width="50%"><b>256人脸尺寸【demo2】</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/738bddd1-b46d-448b-b67e-d67d3226222b controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/c52c4ffc-1ea9-4e51-907c-bbb9b8d8a9e0 controls preload></video>
    </td>
  </tr>
</table>


<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="50%"><b>384人脸尺寸【demo1】</b></td>
        <td width="50%"><b>384人脸尺寸【demo2】</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/abe3a2ac-b71c-449c-aa19-c0d1cf90a72d controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/daefb100-b776-45b3-9d9b-fc26e3d04a20 controls preload></video>
    </td>
  </tr>
</table>


## 📑 使用说明

- 下载权重文件压缩包zip：https://pan.baidu.com/s/1DvR4P0rqPsU0qL_dOWnG0g 提取码: uvyp
- 下载后直接在根目录解压zip，目录结构：
```
checkpoints
key.txt
lstmsync_func.cp38-win_amd64.pyd or lstmsync_func.cp310-win_amd64.pyd // 根据自己python版本决定
lstmsync_func.cpython-38-x86_64-linux-gnu.so or lstmsync_func.cpython-310-x86_64-linux-gnu.so // 根据自己python版本决定
requirements.txt
run.py
```
- 先安装好python3.8或python3.10、cuda、pytorch等gpu环境，不懂则自行去csdn等平台查阅。
- 安装配置好ffmpeg环境变量
- 上述都完成后执行:
```
pip install -r requirements.txt // python3.8版本支持
```
```
pip install -r requirements-50.txt // 50系显卡，python3.10版本支持
```
- 查看run.py脚本，参数说明有注释，该脚本为调用示例，可自行灵活使用。


## 联系
|  如需商务合作，加微信| 项目捐赠，您的鼓励是我最大的动力。                                                                        |
|-------------------|------------------------------------------------------------------------------------------|
| ![微信](https://github.com/user-attachments/assets/e95e42a2-a6ec-4fbd-b65a-28a08aa11eaf) | ![微信群聊](https://github.com/user-attachments/assets/6324f3c2-b3e7-43f3-9a27-b8d9bbf5986d) |


