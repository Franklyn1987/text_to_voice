��װ����Ҫ�Ŀ⣺
pip install git+https://github.com/suno-ai/bark.git
�Զ����ı�����
text_prompt = """
    I have a silky smooth voice, and today I will tell you about 
    the exercise regimen of the common sloth.
"""
audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_1")
CMD����������
python -m bark --text "Hello, my name is Suno." --output_filename "example.wav"
