import inspect

from ovos_plugin_manager.templates.stt import STT

from ovos_stt_plugin_nemo import LANG2MODEL, MODEL2URL, NemoSTT


def test_is_stt_subclass():
    assert issubclass(NemoSTT, STT)


def test_execute_signature():
    assert callable(getattr(NemoSTT, "execute", None))
    params = inspect.signature(NemoSTT.execute).parameters
    assert "audio" in params
    assert "language" in params


def test_available_languages():
    langs = NemoSTT.available_languages
    assert isinstance(langs, set)
    assert langs == set(LANG2MODEL.keys())
    assert "en" in langs


def test_lang_model_maps():
    # every default language maps to a non-empty model name
    assert LANG2MODEL
    for lang, model in LANG2MODEL.items():
        assert isinstance(lang, str) and lang
        assert isinstance(model, str) and model

    # every model URL is a resolvable https link to a .nemo checkpoint
    assert MODEL2URL
    for name, url in MODEL2URL.items():
        assert url.startswith("https://")
        assert url.endswith(".nemo")


def test_download_is_static():
    assert isinstance(inspect.getattr_static(NemoSTT, "download"), staticmethod)
