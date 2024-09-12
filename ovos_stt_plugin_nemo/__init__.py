import os.path
from tempfile import gettempdir
from typing import Optional

import requests
from ovos_utils.xdg_utils import xdg_data_home
from tempfile import NamedTemporaryFile
import nemo.collections.asr as nemo_asr
from ovos_plugin_manager.templates.stt import STT
from ovos_utils.log import LOG
from speech_recognition import AudioData


LANG2MODEL = {
    "eu": "stt_eu_conformer_ctc_large",
    "en": "stt_en_quartznet15x5",
    "es": "stt_es_quartznet15x5",
    "ca": "stt_ca_quartznet15x5",
    "fr": "stt_fr_quartznet15x5",
    "de": "stt_de_quartznet15x5",
    "pl": "stt_pl_quartznet15x5",
    "it": "stt_it_quartznet15x5",
    "ru": "stt_ru_quartznet15x5",
    "zh": 'stt_zh_citrinet_512'
}
MODEL2URL = {
    "stt_eu_conformer_ctc_large": "https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large/resolve/main/stt_eu_conformer_ctc_large.nemo"
}
PRETRAINED = ['stt_en_jasper10x5dr', 'stt_en_quartznet15x5', 'QuartzNet15x5Base-En',
              'stt_es_quartznet15x5', 'stt_fr_quartznet15x5', 'stt_ca_quartznet15x5', 'stt_de_quartznet15x5',
              'stt_pl_quartznet15x5', 'stt_it_quartznet15x5', 'stt_ru_quartznet15x5', 'stt_zh_citrinet_512',
              'stt_zh_citrinet_1024_gamma_0_25', 'asr_talknet_aligner']


class NemoSTT(STT):

    def __init__(self, config: dict = None):
        super().__init__(config)
        model = self.config.get("model")
        lang = self.lang.split("-")[0]
        if not model and lang in LANG2MODEL:
            model = LANG2MODEL[lang]
        if model not in PRETRAINED:
            if model in MODEL2URL:
                model = MODEL2URL[model]
            if model.startswith("http"):
                model = self.download(model)
            if not model:
                raise ValueError(f"'model' not set in config file")
            if not os.path.isfile(model):
                raise FileNotFoundError(f"'model' file does not exist - {model}")
            self.asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from(model)
        else:
            self.asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name=model)
        self.batch_size = self.config.get("batch_size", 8)

    @staticmethod
    def download(url):
        path = f"{xdg_data_home()}/nemo_stt_models"
        os.makedirs(path, exist_ok=True)
        # Get the file name from the URL
        file_name = url.split("/")[-1]
        file_path = f"{path}/{file_name}"
        if not os.path.isfile(file_path):
            LOG.info(f"downloading {url}  - this might take a while!")
            # Stream the download in chunks
            with requests.get(url, stream=True) as response:
                response.raise_for_status()  # Check if the request was successful
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
        return file_path

    @property
    def available_languages(self) -> set:
        return {"eu-es"}

    def execute(self, audio: AudioData, language: Optional[str] = None):
        with NamedTemporaryFile("wb", suffix=".wav") as f:
            f.write(audio.get_wav_data())
            audio_buffer = [f.name]
            transcriptions = self.asr_model.transcribe(audio_buffer, batch_size=self.batch_size)

        if not transcriptions:
            LOG.debug("Transcription is empty")
            return None
        return transcriptions[0]


if __name__ == "__main__":
    b = NemoSTT({"lang": "eu"})
    from speech_recognition import Recognizer, AudioFile

    eu = "/home/miro/PycharmProjects/ovos-stt-conformer-ctc-plugin/es.wav"
    ca = "/home/miro/PycharmProjects/ovos-stt-plugin-vosk/example.wav"
    with AudioFile(eu) as source:
        audio = Recognizer().record(source)

    a = b.execute(audio, language="eu")
    print(a)
    # asko eskertzen dut nirekin denbora ematea baina orain alde egin behar dut laster zurekin harrapatuko dudala agintzen dizut
