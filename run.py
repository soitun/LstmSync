import lstmsync_func

if __name__ == '__main__':
    '''
    def __init__(
        self,
        wav2lip_batch_size=4,
        sync_offset=0,
        scale_h=1,
        scale_w=1,
        key_file="./key.txt"
    ):
    '''
    c = lstmsync_func.LstmSync(
        batch_size=4,  # batch
        sync_offset=0,  # 音画同步调节
        scale_h=1.5,  # 遮罩高度大小控制，比例的，如果脸颊左右遮罩严重则调大
        scale_w=3,  # 遮罩宽度大小控制，比例的，如果脸颊左右遮罩严重则调大
        key_file="./key.txt"  # 必须存在
    )
    out = c.run(
        human_path="./checkpoints/192jm.pth",  # 同步权重
        hubert_path="./checkpoints/chinese-hubert-large",  # 音频权重
        video_path="./1.mp4",  # 输入的视频
        video_fps25_path="./fps25_temp.mp4",  # 输入的视频后转25fps的，最终会用这个去推理
        video_temp_path="./temp.mp4",  # 输出临时视频，最终会用这个去与音频合成
        audio_path="./1.wav",  # 输入的音频
        audio_temp_path="./temp.wav",  # 输入的音频后转16khz的，最终会用这个去推理
        video_out_path="./res.mp4"  # 输出的最终视频
    )
    print(out)