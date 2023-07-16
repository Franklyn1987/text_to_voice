text_to_voice（文字转语音）
================================

## 安装所需要的库：
```python
pip install git+https://github.com/suno-ai/bark.git
```
## 自定义文本内容
```python
text_prompt = """
    I have a silky smooth voice, and today I will tell you about
    the exercise regimen of the common sloth.
"""
audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_1")
```

## CMD命令行运行
```Shell
python -m bark --text "Hello, my name is Suno." --output_filename "example.wav"
```
