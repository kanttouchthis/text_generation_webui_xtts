# XTTSv2 for text-generation-webui
This is a simple extension for [text-generation-webui](https://github.com/oobabooga/text-generation-webui/) that enables multilingual TTS, with voice cloning using XTTSv2 from [coqui-ai/TTS](https://github.com/coqui-ai/TTS).

# Update
XTTSv2 is now built into [text-generation-webui](https://github.com/oobabooga/text-generation-webui/tree/main/extensions/coqui_tts) (coqui_tts). I might still update this extension for the Narrator feature, but if you don't care about that, use the official extension.

# Disclaimer
This is a very crude extension i threw together quickly based on the [barktts](https://github.com/RandomInternetPreson/text-generation-webui-barktts) extension. It may or may not work. Feel free to improve the code and submit a PR.

# Installation
Activate your environment by running `cmd_windows.bat`/`cmd_linux.sh`/`cmd_macos.sh`/`cmd_wsl.bat` depending on your platform, or activate your conda environment if you installed it manually.
Clone this repo:
```
cd extensions
git clone https://github.com/kanttouchthis/text_generation_webui_xtts
```
Install dependencies for TTS.
```
cd text_generation_webui_xtts
pip install -r requirements.txt
```
Install TTS. Their version requirements cause issues so we install the dependencies above, without version requirements.
```
pip install TTS --no-dependencies
```

# Usage
Once you finished the steps above, you can add some voices to the voices folder. This can be any short (3-6 seconds) wav clip of someone talking. Make sure it's high quality audio with no long gaps.
Then, run the webui with `--extensions text_generation_webui_xtts` and select your voice/language and other settings at the bottom. You might have to accept the terms and conditions via the console when you first run it.
