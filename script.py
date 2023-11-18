from TTS.api import TTS
import os
import json
import time
from pathlib import Path
import gradio as gr
from modules import shared

streaming_state = shared.args.no_stream

tts = None
this_dir = os.path.dirname(os.path.abspath(__file__))
params = json.load(open(f"{this_dir}/config.json"))
languages = params["available_languages"]
voice_presets = sorted(os.listdir(f"{this_dir}/voices"))


def preprocess(raw_input):
    raw_input = raw_input.replace("&amp;", "&")
    raw_input = raw_input.replace("&lt;", "<")
    raw_input = raw_input.replace("&gt;", ">")
    raw_input = raw_input.replace("&quot;", '"')
    return raw_input

def history_modifier(history):
    if len(history['internal']) > 0:
        history['visible'][-1] = [
            history['visible'][-1][0],
            history['visible'][-1][1].replace(
                'controls autoplay>', 'controls>')
        ]
    return history


def input_modifier(string):
    if not params['activate']:
        shared.processing_message = "*Is typing...*"
        return string
    shared.processing_message = "*Is recording a voice message...*"
    shared.args.no_stream = True
    return string


def output_modifier(string):
    global tts
    string = string.replace("&#x27;", "'")
    if not params['activate']:
        return string

    if tts is None:
        print("[XTTS] Loading XTTS...")
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

    ttstext = preprocess(string)
    time_label = int(time.time())
    tts.tts_to_file(text=ttstext,
                    file_path=f"{this_dir}/generated/{time_label}.wav",
                    speaker_wav=[f"{this_dir}/voices/{params['voice']}"],
                    language=languages[params['language']])

    autoplay = 'autoplay' if params['autoplay'] else ''
    if params['show_text']:
        string = f'<audio src="file/{this_dir}/generated/{time_label}.wav" controls {autoplay}></audio><br>{ttstext}'
    else:
        string = f'<audio src="file/{this_dir}/generated/{time_label}.wav" controls {autoplay}></audio>'

    shared.args.no_stream = streaming_state
    return string


def setup():
    global tts
    print("[XTTS] Loading XTTS...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
    print("[XTTS] Creating directories (if they don't exist)...")
    if not Path(f"{this_dir}/generated").exists():
        Path(f"{this_dir}/generated").mkdir(parents=True)
    print("[XTTS] Done!")


def ui():
    with gr.Accordion("XTTS"):
        with gr.Row():
            activate = gr.Checkbox(
                value=params['activate'], label='Activate TTS')
            autoplay = gr.Checkbox(value=params['autoplay'], label='Autoplay')
            show_text = gr.Checkbox(
                value=params['show_text'], label='Show text')
        with gr.Row():
            voice = gr.Dropdown(
                voice_presets, label='Voice Preset', value=params['voice'])
            language = gr.Dropdown(
                languages.keys(), label='Language', value=params['language'])

    activate.change(lambda x: params.update({'activate': x}), activate, None)
    autoplay.change(lambda x: params.update({'autoplay': x}), autoplay, None)
    show_text.change(lambda x: params.update({'show_text': x}), show_text, None)
    voice.change(lambda x: params.update({'voice': x}), voice, None)
    language.change(lambda x: params.update({'language': x}), language, None)
