# XTTSv2 for text-generation-webui
This is a simple extension for [text-generation-webui](https://github.com/oobabooga/text-generation-webui/) that enables multilingual TTS, with voice cloning using XTTSv2 from [coqui/TTS](https://github.com/coqui-ai/TTS).

# Disclaimer
This is a very crude extension i threw together quickly based on the [barktts](https://github.com/RandomInternetPreson/) extension. It may or may not work. Feel free to improve the code and submit a PR.

# Installation
Clone this repo:
```
cd extensions
git clone <this repo>
```
Activate your environment. For example
```
conda activate textgen
```
Install dependencies for TTS
```
pip install -r requirements.txt
```
Install TTS. Their version requirements cause issues so we install the dependencies above, without version requirements.
```
pip install TTS --no-dependencies
```

# Usage
Once you finished the steps above, you can add some voices to the voices folder. This can be any short (3-6 seconds) audio clip of someone talking. Make sure it's high quality audio with no long gaps.
Then, run the webui with `--extensions xtts` and select your voice/language and other settings at the bottom. You might have to accept the terms and conditions via the console when you first run it.