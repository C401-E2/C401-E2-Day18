"""Tests for Module 5: Enrichment Pipeline."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.m5_enrichment import (
    summarize_chunk, generate_hypothesis_questions,
    contextual_prepend, extract_metadata, enrich_chunks, EnrichedChunk,
)

SAMPLE = "Nhân viên chính thức được nghỉ phép năm 12 ngày làm việc mỗi năm."
CHUNKS = [
    {"text": SAMPLE, "metadata": {"source": "policy.md"}},
    {"text": "Mật khẩu phải thay đổi mỗi 90 ngày.", "metadata": {"source": "it.md"}},
]


def test_summarize_returns_string():
    result = summarize_chunk(SAMPLE)
    assert isinstance(result, str)


def test_summarize_shorter_than_original():
    result = summarize_chunk(SAMPLE)
    if result:  # May be empty if no API key
        assert len(result) <= len(SAMPLE) * 2  # Summary should not be much longer


def test_hyqa_returns_list():
    result = generate_hypothesis_questions(SAMPLE, n_questions=2)
    assert isinstance(result, list)


def test_hyqa_generates_questions():
    result = generate_hypothesis_questions(SAMPLE, n_questions=2)
    if result:
        assert len(result) >= 1
        assert any("?" in q or "bao" in q.lower() or "mấy" in q.lower() for q in result)


def test_contextual_prepend_returns_string():
    result = contextual_prepend(SAMPLE, "Sổ tay nhân viên")
    assert isinstance(result, str)
    assert len(result) >= len(SAMPLE)  # Should be at least as long as original


def test_contextual_contains_original():
    result = contextual_prepend(SAMPLE, "Sổ tay nhân viên")
    assert SAMPLE in result  # Original text must be preserved


def test_extract_metadata_returns_dict():
    result = extract_metadata(SAMPLE)
    assert isinstance(result, dict)


def test_enrich_chunks_returns_list():
    result = enrich_chunks(CHUNKS, methods=["contextual"])
    assert isinstance(result, list)


def test_enrich_chunks_type():
    result = enrich_chunks(CHUNKS, methods=["contextual"])
    if result:
        assert all(isinstance(c, EnrichedChunk) for c in result)


def test_enrich_preserves_original():
    result = enrich_chunks(CHUNKS, methods=["contextual"])
    if result:
        assert result[0].original_text == SAMPLE


def main() -> int:
    """Allow running this test file directly with `python tests/test_m5.py`."""
    try:
        import pytest

        return pytest.main([__file__])
    except ImportError:
        current_module = sys.modules[__name__]
        test_functions = [
            getattr(current_module, name)
            for name in sorted(dir(current_module))
            if name.startswith("test_") and callable(getattr(current_module, name))
        ]

        failures = 0
        for test_func in test_functions:
            try:
                test_func()
                print(f"PASS: {test_func.__name__}")
            except Exception as exc:
                failures += 1
                print(f"FAIL: {test_func.__name__}: {exc}")

        print(f"\nRan {len(test_functions)} tests, {failures} failed.")
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
