# OVOS Nemo STT

## Description

This is an OpenVoiceOS speech-to-text (STT) plugin for [Nemo](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html). A GPU is **strongly recommended**.

> **NOTE**: for onnx converted models, use [ovos-stt-plugin-citrinet](https://github.com/OpenVoiceOS/ovos-stt-plugin-citrinet) instead.

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

The `"model"` value can be a full path or URL to a `.nemo` file, or a pretrained model ID (see the list below).

If you do not set `"model"`, the plugin selects a model automatically based on the configured language.

### Models

Supported languages: `'en', 'es', 'ca', 'fr', 'de', 'pl', 'it', 'ru', 'zh', 'nl', 'uk', 'pt', 'eu', 'eo', 'be', 'hr', 'rw', 'fa', 'ua'`

Pre-trained models come from:
- [Nvidia](https://ngc.nvidia.com/catalog/models/nvidia:nemospeechmodels)
- [HiTZ](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) (Basque)
- [AINA](https://huggingface.co/projecte-aina/stt-ca-citrinet-512) (Catalan)
- [NeonGeckoCom](https://huggingface.co/collections/neongeckocom/neon-stt-663ca3c1a55b063463cb0167) - `'en', 'es', 'fr', 'de', 'it', 'uk', 'nl', 'pt', 'ca'`

Nvidia default models from the Nemo toolkit:
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

The plugin downloads external models on demand to `~/.local/share/nemo_stt_models`:

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

## Related projects

- [ovos-stt-plugin-citrinet](https://github.com/OpenVoiceOS/ovos-stt-plugin-citrinet) - the companion plugin for onnx-converted models
- [ovos-stt-plugin-HiTZ](https://github.com/OpenVoiceOS/ovos-stt-plugin-HiTZ) - a dedicated plugin for HiTZ Basque models

## Credits

TigreGotico developed this plugin for OpenVoiceOS under the [ILENIA](https://proyectoilenia.es) project.

<img src="img.png" width="128"/>

> The Ministerio para la Transformación Digital y de la Función Pública and the Plan de Recuperación, Transformación y Resiliencia funded this plugin. The EU funded it through NextGenerationEU, within the framework of the project [ILENIA](https://proyectoilenia.es), reference 2022/TL22/00215337.

<img src="img_1.png"  width="64"/>

The [HiTZ/Aholab Basque speech-to-text model Conformer-CTC](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) was trained on a composite dataset of 548 hours of Basque speech. The model was fine-tuned from a pre-trained Spanish `stt_es_conformer_ctc_large` model. It is a non-autoregressive "large" variant of Conformer, with around 121 million parameters.

> The Ministerio de Transformación Digital and the Plan de Recuperación, Transformación y Resiliencia partially funded this project, reference 2022/TL22/00215335. The European Union funded it through NextGenerationEU ILENIA, and the Basque Government funded it through the project IkerGaitu. The model was trained at Hyperion, a high-performance computing (HPC) system hosted by the DIPC Supercomputing Center.

<img src="img_3.png"  width="128"/>

> The Generalitat de Catalunya funded [projecte-aina/stt-ca-citrinet-512](https://huggingface.co/projecte-aina/stt-ca-citrinet-512) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

<img src="img_2.png"  width="64"/>

[NeonGeckoCom](https://github.com/NeonGeckoCom) provides [models](https://huggingface.co/collections/neongeckocom/neon-stt-663ca3c1a55b063463cb0167) for `'en', 'es', 'fr', 'de', 'it', 'uk', 'nl', 'pt', 'ca'`.
