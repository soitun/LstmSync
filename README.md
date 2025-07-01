<h1 align="center">LstmSync</h1>
<div align="center">
<h2 align="center">无需网络，本地4G显存即可使用的数字人泛化模型！效果可行能否给个小星星！</h2>
<a href="https://b23.tv/RL1mGQR">作者主页：一码超人</a><br/>
<a href="https://b23.tv/4CKlq4Y">宣传大使：浪子之心科技</a><br/>
<a href="https://blog.csdn.net/weixin_47723549?type=blog">作者csdn：一码超人</a><br/>
</div>

## 🏋️‍♂️ 合作企业
- <a href="https://www.umi6.com">深圳优秘智能科技有限公司</a>

## 🔥 更新

- `2025/06/30`: 开源192尺寸泛化权重
- `2025/07/01`: 支持liunx系统兼容

## 📖 计划

- `2025/07/15`: 开发api接口及界面支持

## 🏗️ 注意事项

- 推理后的脸部左右遮罩模糊，可通过scale_h，scale_w进行调节，越大遮罩范围越小，该设置为比例，所以一次调整好后续无需调整。一般设置：scale_h=1.6， scale_w=3.6， 可自行再进行精调。
- python版本必须为3.8、pytorch建议2.0+、cuda11.8等。
- 4G+显存即可。
- windows安装insightface库可能存在编译失败问题，需安装Desktop development with C++，无脑安装即可。链接地址：https://download.visualstudio.microsoft.com/download/pr/e514a25b-a89d-4051-a63c-05ccd9be41e9/88d8e1df44172b28e92df1c11fc900aef2d6d6e7e75491467f4c507c07d31f13/vs_BuildTools.exe
![image](https://github.com/user-attachments/assets/7c5ae4bf-e7d0-45dd-ae58-41f7c55ba25e)


## 🎬 Demo

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="50%"><b>demo1</b></td>
        <td width="50%"><b>demo2</b></td>
  </tr>
  <tr>
    <td>
      <video src=https://github.com/user-attachments/assets/e8067ba9-b239-40c0-afda-40fc006cd369 controls preload></video>
    </td>
    <td>
      <video src=https://github.com/user-attachments/assets/d3490d66-ed7d-4245-abd8-a55b4ca7e8e2 controls preload></video>
    </td>
  </tr>
</table>

## 📑 使用说明

- 下载权重文件压缩包zip：https://pan.baidu.com/s/1_taYmPkm6mMWd0eCEUzeiA 提取码: nv7n
- 下载后直接在根目录解压zip，目录结构：
```
checkpoints
key.txt
lstmsync_func.cp38-win_amd64.pyd
lstmsync_func.cpython-38-x86_64-linux-gnu.so
requirements.txt
run.py
```
- 先安装好python3.8、cuda、pytorch等gpu环境，不懂则自行去csdn等平台查阅。
- 安装配置好ffmpeg环境变量
- 上述都完成后执行:
```
pip install -r requirements.txt
```
- 查看run.py脚本，参数说明有注释，该脚本为调用示例，可自行灵活使用。


## 联系
|  如需商务合作，加微信| 项目捐赠，您的鼓励是我最大的动力。                                                                        |
|-------------------|------------------------------------------------------------------------------------------|
| ![微信](https://github.com/user-attachments/assets/e95e42a2-a6ec-4fbd-b65a-28a08aa11eaf) | ![微信群聊](https://github.com/user-attachments/assets/6324f3c2-b3e7-43f3-9a27-b8d9bbf5986d) |


