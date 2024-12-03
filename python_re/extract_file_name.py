import re

entry = "D:\STT_project\Keyword-Spotting-ConvMixer\dataset\google_speech_recognition_v2\\backward\\0a2b400e_nohash_0.wav"

pattern = re.compile(r"(.+[\\/])?(\w+)[\\/](\w+_\w+_\w+)\.wav")

r = re.match(pattern, entry) 

total_str, dir_path, label, uid = r.group(0), r.group(1), r.group(2), r.group(3)

print(r)
print(total_str)
print(dir_path)
print(label)
print(uid)