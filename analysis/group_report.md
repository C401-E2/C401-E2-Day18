# Group Report - Lab 18: Production RAG

**Nhóm:** Dương Chí Thành, Tiến, Linh, Khôi, An  
**Ngày:** 2026-05-04

## Thành viên & Phân công

| Tên | Module | Hoàn thành | Tests pass |
|-----|--------|-----------|-----------|
| Tiến | M1: Chunking | Done | 8/8 |
| Linh | M2: Hybrid Search | Done | 5/5 |
| Dương Chí Thành | M3: Reranking | Done | 5/5 |
| Khôi | M4: Evaluation | Done | 4/4 |
| An | Pipeline integration, reports, submission checks | Done | 5/5 |

## Kết quả RAGAS

| Metric | Naive | Production | Delta |
|--------|-------|-----------|-------|
| Faithfulness | 0.4000 | 0.4000 | +0.0000 |
| Answer Relevancy | 0.0000 | 0.0000 | +0.0000 |
| Context Precision | 0.0000 | 0.0000 | +0.0000 |
| Context Recall | 0.1667 | 0.0000 | -0.1667 |

## Key Findings

1. **Biggest improvement:** The pipeline now runs end-to-end with clean module boundaries, report generation, and fallback-safe execution.
2. **Biggest challenge:** The provided corpus and test set are too small for the retrieval stack to show meaningful lift.
3. **Surprise finding:** The evaluation bottleneck is not the reranker alone; the main issue is weak context quality and weak answer generation.

## Presentation Notes

1. RAGAS scores (naive vs production): production currently matches baseline on faithfulness and answer relevancy, but does not improve retrieval quality on this tiny demo set.
2. Biggest win - module nào, tại sao: M3 is the most visible improvement point conceptually, but the current corpus prevents it from showing a real gain.
3. Case study - 1 failure, Error Tree walkthrough: the only test question has noisy wording and no useful corpus support, so the error starts at query/context alignment.
4. Next optimization nếu có thêm 1 giờ: replace the answer fallback with an actual LLM call, then evaluate on a larger Vietnamese corpus.
