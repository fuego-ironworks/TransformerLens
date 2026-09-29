from transformer_lens.supported_models import get_official_model_name


def test_pythia_14m_deduped_is_registered():
    assert (
        get_official_model_name("EleutherAI/pythia-14m-deduped")
        == "EleutherAI/pythia-14m-deduped"
    )


def test_pythia_14m_deduped_short_alias_resolves():
    assert (
        get_official_model_name("pythia-14m-deduped")
        == "EleutherAI/pythia-14m-deduped"
    )
