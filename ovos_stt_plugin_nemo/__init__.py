import os.path
from tempfile import NamedTemporaryFile
from typing import Optional

import nemo.collections.asr as nemo_asr
import requests
from ovos_plugin_manager.templates.stt import STT
from ovos_utils.log import LOG
from ovos_utils.xdg_utils import xdg_data_home
from speech_recognition import AudioData

PRETRAINED = [m.pretrained_model_name for m in nemo_asr.models.EncDecCTCModel.list_available_models()]
LANG2MODEL = {
    "en": "stt_en_quartznet15x5",
    "es": "stt_es_quartznet15x5",
    "ca": "stt-ca-citrinet-512",
    "fr": "stt_fr_quartznet15x5",
    "de": "stt_de_quartznet15x5",
    "pl": "stt_pl_quartznet15x5",
    "it": "stt_it_quartznet15x5",
    "ru": "stt_ru_quartznet15x5",
    "zh": 'stt_zh_citrinet_512',
    "nl": "stt_nl_citrinet_512_gamma_0_25",
    "uk": "stt_uk_citrinet_512_gamma_0_25",
    "pt": "stt_pt_citrinet_512_gamma_0_25",
    "eu": "stt_eu_conformer_ctc_large",
    "eo": "stt_eo_conformer_ctc_large",
    "be": "stt_be_conformer_ctc_large",
    "hr": "stt_hr_conformer_ctc_large",
    "rw": "stt_rw_conformer_ctc_large",
    "fa": "stt_fa_fastconformer_hybrid_large",
    "ua": "stt_ua_fastconformer_hybrid_large_pc"
}
MODEL2URL = {
    "stt-ca-citrinet-512": "https://huggingface.co/projecte-aina/stt-ca-citrinet-512/resolve/main/stt-ca-citrinet-512.nemo",

    "stt_en_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_en_citrinet_512_gamma_0_25/resolve/main/stt_en_citrinet_512_gamma_0_25.nemo",
    "stt_es_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_es_citrinet_512_gamma_0_25/resolve/main/stt_es_citrinet_512_gamma_0_25.nemo",
    "stt_fr_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_fr_citrinet_512_gamma_0_25/resolve/main/stt_fr_citrinet_512_gamma_0_25.nemo",
    "stt_de_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_de_citrinet_512_gamma_0_25/resolve/main/stt_de_citrinet_512_gamma_0_25.nemo",
    "stt_it_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_it_citrinet_512_gamma_0_25/resolve/main/stt_it_citrinet_512_gamma_0_25.nemo",
    "stt_uk_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_uk_citrinet_512_gamma_0_25/resolve/main/stt_uk_citrinet_512_gamma_0_25.nemo",
    "stt_nl_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_nl_citrinet_512_gamma_0_25/resolve/main/stt_nl_citrinet_512_gamma_0_25.nemo",
    "stt_pt_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_pt_citrinet_512_gamma_0_25/resolve/main/stt_pt_citrinet_512_gamma_0_25.nemo",
    "stt_ca_citrinet_512_gamma_0_25": "https://huggingface.co/neongeckocom/stt_ca_citrinet_512_gamma_0_25/resolve/main/stt_ca_citrinet_512_gamma_0_25.nemo",

    "stt_en_citrinet_256_ls": "https://huggingface.co/nvidia/stt_en_citrinet_256_ls/resolve/main/stt_en_citrinet_256_ls.nemo",
    "stt_en_citrinet_384_ls": "https://huggingface.co/nvidia/stt_en_citrinet_384_ls/resolve/main/stt_en_citrinet_384_ls.nemo",
    'stt_en_citrinet_512_ls': "https://huggingface.co/nvidia/stt_en_citrinet_512_ls/resolve/main/stt_en_citrinet_512_ls.nemo",
    'stt_en_citrinet_768_ls': "https://huggingface.co/nvidia/stt_en_citrinet_768_ls/resolve/main/stt_en_citrinet_768_ls.nemo",
    'stt_en_citrinet_1024_ls': "https://huggingface.co/nvidia/stt_en_citrinet_1024_ls/resolve/main/stt_en_citrinet_1024_ls.nemo",
    "stt_uk_citrinet_1024_gamma_0_25": "https://huggingface.co/nvidia/stt_uk_citrinet_1024_gamma_0_25/resolve/main/stt_uk_citrinet_1024_gamma_0_25.nemo",
    "stt_en_citrinet_1024_gamma_0_25": "https://huggingface.co/nvidia/stt_en_citrinet_1024_gamma_0_25/resolve/main/stt_en_citrinet_1024_gamma_0_25.nemo",
    "stt_zh_citrinet_1024_gamma_0_25": "https://huggingface.co/nvidia/stt_zh_citrinet_1024_gamma_0_25/resolve/main/stt_zh_citrinet_1024_gamma_0_25.nemo",

    "stt_eu_conformer_transducer_large": "https://huggingface.co/HiTZ/stt_eu_conformer_transducer_large/resolve/main/stt_eu_conformer_transducer_large.nemo",
    "stt_eu_conformer_ctc_large": "https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large/resolve/main/stt_eu_conformer_ctc_large.nemo",
    "stt_en_conformer_ctc_small": "https://huggingface.co/nvidia/stt_en_conformer_ctc_small/resolve/main/stt_en_conformer_ctc_small.nemo",
    "stt_en_conformer_ctc_large": "https://huggingface.co/nvidia/stt_en_conformer_ctc_large/resolve/main/stt_en_conformer_ctc_large.nemo",
    "stt_es_conformer_ctc_large": "https://huggingface.co/nvidia/stt_es_conformer_ctc_large/resolve/main/stt_es_conformer_ctc_large.nemo",
    "stt_ca_conformer_ctc_large": "https://huggingface.co/nvidia/stt_ca_conformer_ctc_large/resolve/main/stt_ca_conformer_ctc_large.nemo",
    "stt_it_conformer_ctc_large": "https://huggingface.co/nvidia/stt_it_conformer_ctc_large/resolve/main/stt_it_conformer_ctc_large.nemo",
    "stt_fr_conformer_ctc_large": "https://huggingface.co/nvidia/stt_fr_conformer_ctc_large/resolve/main/stt_fr_conformer_ctc_large.nemo",
    "stt_de_conformer_ctc_large": "https://huggingface.co/nvidia/stt_de_conformer_ctc_large/resolve/main/stt_de_conformer_ctc_large.nemo",
    "stt_hr_conformer_ctc_large": "https://huggingface.co/nvidia/stt_be_conformer_ctc_large/resolve/main/stt_hr_conformer_ctc_large.nemo",
    "stt_be_conformer_ctc_large": "https://huggingface.co/nvidia/stt_be_conformer_ctc_large/resolve/main/stt_be_conformer_ctc_large.nemo",
    "stt_ru_conformer_ctc_large": "https://huggingface.co/nvidia/stt_ru_conformer_ctc_large/resolve/main/stt_ru_conformer_ctc_large.nemo",
    "stt_rw_conformer_ctc_large": "https://huggingface.co/nvidia/stt_rw_conformer_ctc_large/resolve/main/stt_rw_conformer_ctc_large.nemo",
    "stt_eo_conformer_ctc_large": "https://huggingface.co/nvidia/stt_eo_conformer_ctc_large/resolve/main/stt_eo_conformer_ctc_large.nemo",

    "stt_fa_fastconformer_hybrid_large": "https://huggingface.co/nvidia/stt_fa_fastconformer_hybrid_large/resolve/main/stt_fa_fastconformer_hybrid_large.nemo",
    "stt_kk_ru_fastconformer_hybrid_large": "https://huggingface.co/nvidia/stt_kk_ru_fastconformer_hybrid_large/resolve/main/stt_kk_ru_fastconformer_hybrid_large.nemo",

    "stt_it_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_it_fastconformer_hybrid_large_pc/resolve/main/stt_it_fastconformer_hybrid_large_pc.nemo",
    "stt_es_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_es_fastconformer_hybrid_large_pc/resolve/main/stt_es_fastconformer_hybrid_large_pc.nemo",
    "stt_de_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_de_fastconformer_hybrid_large_pc/resolve/main/stt_de_fastconformer_hybrid_large_pc.nemo",
    "stt_en_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_en_fastconformer_hybrid_large_pc/resolve/main/stt_en_fastconformer_hybrid_large_pc.nemo",
    "stt_ua_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_ua_fastconformer_hybrid_large_pc/resolve/main/stt_ua_fastconformer_hybrid_large_pc.nemo",
    "stt_pl_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_pl_fastconformer_hybrid_large_pc/resolve/main/stt_pl_fastconformer_hybrid_large_pc.nemo",
    "stt_hr_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_hr_fastconformer_hybrid_large_pc/resolve/main/stt_hr_fastconformer_hybrid_large_pc.nemo",
    "stt_be_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_be_fastconformer_hybrid_large_pc/resolve/main/stt_be_fastconformer_hybrid_large_pc.nemo",
    "stt_fr_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_fr_fastconformer_hybrid_large_pc/resolve/main/stt_fr_fastconformer_hybrid_large_pc.nemo",
    "stt_ru_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_ru_fastconformer_hybrid_large_pc/resolve/main/stt_ru_fastconformer_hybrid_large_pc.nemo",
    "stt_nl_fastconformer_hybrid_large_pc": "https://huggingface.co/nvidia/stt_nl_fastconformer_hybrid_large_pc/resolve/main/stt_nl_fastconformer_hybrid_large_pc.nemo",

    "stt_en_fastconformer_transducer_large": "https://huggingface.co/nvidia/stt_en_fastconformer_transducer_large/resolve/main/stt_en_fastconformer_transducer_large.nemo",
    "stt_en_fastconformer_transducer_xlarge": "https://huggingface.co/nvidia/stt_en_fastconformer_transducer_xlarge/resolve/main/stt_en_fastconformer_transducer_xlarge.nemo",
    "stt_en_fastconformer_transducer_xxlarge": "https://huggingface.co/nvidia/stt_en_fastconformer_transducer_xxlarge/resolve/main/stt_en_fastconformer_transducer_xxlarge.nemo",

    "stt_en_fastconformer_ctc_large": "https://huggingface.co/nvidia/stt_en_fastconformer_ctc_large/resolve/main/stt_en_fastconformer_ctc_large.nemo",
    "stt_en_fastconformer_ctc_xlarge": "https://huggingface.co/nvidia/stt_en_fastconformer_ctc_xlarge/resolve/main/stt_en_fastconformer_ctc_xlarge.nemo",
    "stt_en_fastconformer_ctc_xxlarge": "https://huggingface.co/nvidia/stt_en_fastconformer_ctc_xxlarge/resolve/main/stt_en_fastconformer_ctc_xxlarge.nemo",

}


class NemoSTT(STT):

    def __init__(self, config: dict = None):
        super().__init__(config)
        model = self.config.get("model")
        lang = self.lang.split("-")[0]
        if not model and lang in LANG2MODEL:
            model = LANG2MODEL[lang]
        if not model:
            raise ValueError(f"'lang' {lang} not supported, a 'model' needs to be explicitly set in config file")

        if model not in PRETRAINED:
            if model in MODEL2URL:
                model = MODEL2URL[model]
            if model.startswith("http"):
                model = self.download(model)
            elif not os.path.isfile(model):
                raise FileNotFoundError(f"'model' file does not exist - {model}")
            # the class used here doesnt matter, when restoring from file the correct one is loaded regardless
            # no need to worry about EncDecRNNTBPEModel vs EncDecCTCModelBPE vs ....
            self.asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from(model)
        else:
            self.asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name=model)

        # Load model with CUDA if available
        if self.config.get("use_cuda"):
            import torch
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            if device == "cuda":
                LOG.debug("Loading nemo model in GPU")
                self.asr_model.to(device)
            else:
                LOG.warning("'use_cuda' is set in config, but GPU is not available")

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
        return set(LANG2MODEL.keys())

    def execute(self, audio: AudioData, language: Optional[str] = None):
        with NamedTemporaryFile("wb", suffix=".wav") as f:
            f.write(audio.get_wav_data())
            audio_buffer = [f.name]
            transcriptions = self.asr_model.transcribe(audio_buffer, batch_size=self.batch_size)

        if not transcriptions:
            LOG.debug("Transcription is empty")
            return None

        if isinstance(transcriptions[0], list):  # observed in EncDecRNNTBPEModels
            return transcriptions[0][0]
        return transcriptions[0].text

