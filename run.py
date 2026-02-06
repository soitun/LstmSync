import lstmsync_func

if __name__ == '__main__':

    c = lstmsync_func.LstmSync(
        # human_path="./checkpoints/256.o.pth", # 256尺寸非美化版本，更偏向真实。非锐化！
        # human_path="./checkpoints/384.m.pth", # 384尺寸美化版本
        human_path="./checkpoints/256.m.pth", # 256尺寸美化版本
        hubert_path="./checkpoints/chinese-hubert-large", # 音频权重
        batch_size=4,  # batch
        sync_offset=0,  # 音画同步调节
        scale_h=1.6,  # 遮罩高度大小控制，比例的，如果脸颊左右遮罩严重则调大
        scale_w=3.6,  # 遮罩宽度大小控制，比例的，如果脸颊左右遮罩严重则调大
        weight_type="fp32",  # fp32 or fp16，数据类型，不支持fp16显卡使用fp32
        weight_sync=0.5, # 0 到 1， 0.5为默认值， 用于控制同步口型张合度。 
        gpu_idx=0,  # 使用的GPU编号，默认0
        key_file="./key.txt"  # 必须存在
    )
    out = c.run(
        video_path="./1.mp4",  # 输入的视频
        video_fps25_path="./fps25_temp.mp4",  # 输入的视频后转25fps的，最终会用这个去推理
        video_temp_path="./temp",  # 输出临时视频，最终会用这个去与音频合成，注意没有文件后缀，生成固定avi文件格式！
        audio_path="./1.wav",  # 输入的音频
        audio_temp_path="./temp.wav",  # 输入的音频后转16khz的，最终会用这个去推理
        video_out_path="./res.mp4"  # 输出的最终视频
    )

    print(out)

