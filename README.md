# OVOS Nemo STT


## Description

OpenVoiceOS STT plugin for [Nemo](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html#citrinet), GPU is **strongly recommended**

> **NOTE**: for onnx converted models use [ovos-stt-citrinet-plugin](https://github.com/OpenVoiceOS/ovos-stt-plugin-citrinet) instead

## Install

`pip install ovos-stt-plugin-nemo`

## Configuration

```json
  "stt": {
    "module": "ovos-stt-plugin-nemo",
    "ovos-stt-plugin-nemo": {
        "model": "stt_eu_conformer_ctc_large"
    }
  }
```
if `"model"` is not set, it will be automatically selected based on language

### Models

[HiTZ](https://huggingface.co/HiTZ) models:
- `"stt_eu_conformer_ctc_large"`

Pre-trained [models from Nvidia](https://ngc.nvidia.com/catalog/models/nvidia:nemospeechmodels):
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


## Credits
![img_1.png](img_1.png)

[HiTZ/Aholab's Basque Speech-to-Text model Conformer-CTC](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) - was trained on a composite dataset comprising of 548 hours of Basque speech. The model was fine-tuned from a pre-trained Spanish stt_es_conformer_ctc_large model. It is a non-autoregressive "large" variant of Conformer, with around 121 million parameters

> This project with reference 2022/TL22/00215335 has been partially funded by the Ministerio de Transformación Digital and by the Plan de Recuperación, Transformación y Resiliencia – Funded by the European Union – NextGenerationEU ILENIA and by the project IkerGaitu funded by the Basque Government. This model was trained at Hyperion, one of the high-performance computing (HPC) systems hosted by the DIPC Supercomputing Center.

![img.png](img.png)
> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337
