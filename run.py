"""
VAE-LSTM-Sync 完整执行脚本
包含预处理和推理的执行示例

使用流程：
1. 先运行 preprocess() 预处理视频，生成 npy 数据
2. 再运行 inference() 进行推理，生成数字人视频
"""

# ======================== 预处理 ========================
from preprocess import Preprocessor


def run_preprocess():
    """
    预处理视频，提取人脸关键点和VAE特征
    
    输入：原始视频文件
    输出：./1 目录下的 .dat/.npy 文件
    """
    pre = Preprocessor(
        face_size=256,                        # 人脸大小，可选 256 或 384，需与模型匹配
        vae_encoder_path="./checkpoints/256.encoder.onnx",  # 256选择256.encoder.onnx，384选择384.encoder.onnx，需与模型匹配
        device="cuda",                          # 推理设备："cuda" 或 "cpu", cuda:0等指定具体GPU
        api_key="xxx", # https://lstmsync.andclaw.cn/ 注册获取
    )
    
    pre.run(
        video_path="1.mp4",                # 输入视频路径
        output_dir="./1",               # 预处理输出目录（会自动创建）,建议与视频同名便于区分。
        video_fps25_path=None,                # 可选，转25fps后的视频临时路径
        frame_batch_size=32,                  # 每批处理的帧数，显存不足可调小
    )


# ======================== 推理 ========================
from inference import Inference


def run_inference():
    """
    推理生成数字人视频
    
    输入：预处理数据 + 音频文件
    输出：最终合成视频
    """
    infer = Inference(
        human_path="./checkpoints/384.m.onnx",     # 要与face_size匹配，256选择256.m.onnx，384选择384.m.onnx
        vae_decoder_path=None,                     # None则自动从human_path同目录获取，256选择256.decoder.onnx，384选择384.decoder.onnx，需与模型匹配
        hubert_path="./checkpoints/chinese-hubert-large/",  # HuBERT模型目录
        batch_size=4,                   # 推理批次大小，显存不足可调小(2或1)
        sync_offset=0,                  # 音视频同步偏移(帧)，正数=音频延后，负数=音频提前
        device="cuda",                  # 推理设备："cuda" / "cpu" / "mps" / "mps:0" / "cuda:0" 等，cuda:0等指定具体GPU
        data_load_mode="auto",          # 视频数据加载模式：auto(自动)/full(全量)/streaming(流式)
        audio_mode="full",              # 音频模式：full(全量)/streaming(流式，长音频推荐)
        api_key="xxx", # https://lstmsync.andclaw.cn/ 注册获取
    )
    
    infer.run(
        data_dir="./1",                  # 预处理输出目录
        audio_path="./1.wav",                # 输入音频文件
        video_out_path="./output.mp4",            # 最终输出视频路径
        audio_temp_path=None,                  # 可选，16kHz音频临时路径
        video_temp_path=None,                  # 可选，临时无音轨视频路径(会自动加.avi后缀)
    )

# ======================== 完整流程 ========================
if __name__ == "__main__":
    # 选择要执行的模式：
    
    # 流程1: 对视频预处理
    run_preprocess()
    
    # 流程2: 输入音频执行推理(需要先预处理)
    run_inference()
