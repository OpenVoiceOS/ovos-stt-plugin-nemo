# OVOS Nemo STT


## Description

OpenVoiceOS STT plugin for [Nemo](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html), GPU is **strongly recommended**


> **NOTE**: for onnx converted models use [ovos-stt-citrinet-plugin](https://github.com/OpenVoiceOS/ovos-stt-plugin-citrinet) instead

## Install

`pip install ovos-stt-plugin-nemo`

## Configuration

```json
  "stt": {
    "module": "ovos-stt-plugin-nemo",
    "ovos-stt-plugin-nemo": {
        "model": "stt_eu_conformer_ctc_large",
        "use_cuda": false
    }
  }
```

> `"model"` can be a full path or url to a `.nemo` file, or a pretrained model id (see list below)

if `"model"` is not set, it will be automatically selected based on language

### Models

Supported languages: `'en', 'es', 'ca', 'fr', 'de', 'pl', 'it', 'ru', 'zh', 'nl', 'uk', 'pt', 'eu', 'eo', 'be', 'hr', 'rw', 'fa', 'ua'`

Pre-trained models from:
- [Nvidia](https://ngc.nvidia.com/catalog/models/nvidia:nemospeechmodels)
- [HiTz](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) (basque)
- [AINA](https://huggingface.co/projecte-aina/stt-ca-citrinet-512) (catalan)
- [NeonGeckoCom](https://huggingface.co/collections/neongeckocom/neon-stt-663ca3c1a55b063463cb0167) - `'en', 'es', 'fr', 'de', 'it', 'uk', 'nl', 'pt', 'ca'`

NVidia default models from nemo toolkit:
- `"stt_en_jasper10x5dr"`
- `"stt_en_quartznet15x5"`
- `"QuartzNet15x5Base-En"`
- `"stt_es_quartznet15x5"`
- `"stt_fr_quartznet15x5"`
- `"stt_ca_quartznet15x5"`
- `"stt_de_quartznet15x5"`
- `"stt_pl_quartznet15x5"`
- `"stt_it_quartznet15x5"`
- `"stt_ru_quartznet15x5"`
- `"stt_zh_citrinet_512"`

external models will be downloaded on demand to `~/.local/share/nemo_stt_models`:

```python
{
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
```

## Credits

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337

<img src="img_1.png"  width="64"/>

[HiTZ/Aholab's Basque Speech-to-Text model Conformer-CTC](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) - was trained on a composite dataset comprising of 548 hours of Basque speech. The model was fine-tuned from a pre-trained Spanish stt_es_conformer_ctc_large model. It is a non-autoregressive "large" variant of Conformer, with around 121 million parameters

> This project with reference 2022/TL22/00215335 has been partially funded by the Ministerio de Transformación Digital and by the Plan de Recuperación, Transformación y Resiliencia – Funded by the European Union – NextGenerationEU ILENIA and by the project IkerGaitu funded by the Basque Government. This model was trained at Hyperion, one of the high-performance computing (HPC) systems hosted by the DIPC Supercomputing Center.

<img src="img_3.png"  width="128"/>

> [projecte-aina/stt-ca-citrinet-512](https://huggingface.co/projecte-aina/stt-ca-citrinet-512) was funded by the Generalitat de Catalunya within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


<img src="img_2.png"  width="64"/>

[NeonGeckoCom](https://github.com/NeonGeckoCom) - [models](https://huggingface.co/collections/neongeckocom/neon-stt-663ca3c1a55b063463cb0167) for `'en', 'es', 'fr', 'de', 'it', 'uk', 'nl', 'pt', 'ca'`
