"""
run_live.py —— 实时推流版（preprocess_live + inference_live）的执行脚本
与 run.py 同风格：直接 import 模块 + 调函数，无 argparse。

使用流程：
1. 先调用 run_preprocess() 做预处理（生成 face_latents.dat 等）
2. 再调用 run_inference() 起推流服务（pyvirtualcam + FastAPI）

按需改下面两个函数里的参数即可；不需要命令行参数。
"""

# ======================== 预处理（直播版） ========================
from preprocess_live import PreprocessLive


def run_preprocess():
    """
    实时推流版预处理：视频转 25fps + 人脸关键点 + VAE Encoder
    音频走 HuBERT 切片 + 44.1kHz 立体声 wav

    输入：原始视频 + 音频文件夹
    输出：live_data/ 目录下的 .dat/.npy 文件 + video_25fps.mp4 + meta.json
    """
    pre = PreprocessLive(
        face_size=256,                                              # 人脸大小，与模型匹配（256 / 384）
        vae_encoder_path="./checkpoints/256.encoder.onnx",          # 与 face_size 匹配
        hubert_path="./checkpoints/chinese-hubert-large/",          # HuBERT 模型目录
        device="cuda",                                              # 仅支持 cuda / cuda:N
        api_key="xxx",              # https://lstmsync.andclaw.cn/ 注册获取
        sync_offset=0,                                              # 音频同步偏移（帧）
    )

    pre.run(
        video_path="1.mp4",                                     # 输入视频
        audios_dir="./audios_src",                                  # 输入音频文件夹
        output_dir="./live_data",                                   # 预处理输出目录
        fps=25,                                                     # 视频帧率
        frame_batch_size=64,                                        # 每批处理帧数，显存不足可调小
        res_preset="1080p",                                         # 压缩档位：None / "480p" / "720p" / "1080p"
    )


# ======================== 推理（直播版） ========================
from inference_live import InferenceLive


def run_inference():
    """
    实时推流推理（video 模式）：推理 → VAE Decode → 贴回原图 → 推 pyvirtualcam + pyaudio
    内置 FastAPI 服务（默认 8886 端口，POST /set_audio 接收外部音频）

    输入：预处理数据
    输出：虚拟摄像头 + 扬声器实时输出
    """
    infer = InferenceLive(
        human_path="./checkpoints/256.m.onnx",                      # 与 face_size 匹配
        vae_decoder_path=None,                                      # None 自动从 human_path 同目录获取
        hubert_path="./checkpoints/chinese-hubert-large/",          # HuBERT 模型目录
        device="cuda",                                              # 仅支持 cuda / cuda:N
        video_load_mode="full",                                     # full=全量 / streaming=流式
        audio_loop_mode="random",                                   # random=随机 / sequential=顺序
        frame_w=None,                                               # 虚拟摄像头宽度（None=按 meta.json）
        frame_h=None,                                               # 虚拟摄像头高度（None=按 meta.json）
        sync_offset=0,
        batch_size=2,                                               # 实时建议 1
        api_key="xxx",                                              # https://lstmsync.andclaw.cn/ 注册获取
        port=8886,
        cam_backend="obs",                                          # obs / unitycapture，必须指定避免探测失败
        reverse_random_prob=0,                                    # 随机反转人脸关键点，0%
    )

    infer.start(data_dir="./live_data")


# ======================== 完整流程 ========================
if __name__ == "__main__":
    # 选择要执行的模式：

    # 流程1：对视频预处理（一次性，跑完即退）
    run_preprocess()

    # 流程2：启动实时推流推理
    #   - run_inference()        ：block=True，Ctrl+C 自动 stop + wait（最简单）
    #   - 非阻塞模式：infer.start(block=False) 返回 handle，可在别处 handle["stop"]()
    USE_BLOCKING = True

    if USE_BLOCKING:
        run_inference()
    else:
        infer = InferenceLive(
            human_path="./checkpoints/256.m.onnx",
            vae_decoder_path=None,
            hubert_path="./checkpoints/chinese-hubert-large/",
            device="cuda",
            video_load_mode="full",
            audio_loop_mode="random",
            frame_w=None,
            frame_h=None,
            sync_offset=0,
            batch_size=3,
            api_key="xxx",
            port=8886,
            cam_backend="obs",
            reverse_random_prob=0.1,
        )
        handle = infer.start(data_dir="./live_data", block=False)
        print("已启动，工作线程：")
        for name, t in handle["threads"].items():
            print(f"  - {name}: {t.name} (ident={t.ident}, alive={t.is_alive()})")
        print(f"API 服务: {handle['server']}")

        try:
            import time
            while handle["is_running"]():
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\n[Ctrl+C] 触发 stop() ...")
        finally:
            handle["stop"]()
            handle["wait"](timeout=10)
            print("已完全停止。")