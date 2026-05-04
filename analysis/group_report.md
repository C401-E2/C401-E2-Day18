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
| Faithfulness | 0.7393 | 0.6409 | -0.0984 |
| Answer Relevancy | 0.0069 | 0.0382 | +0.0313 |
| Context Precision | 0.0083 | 0.0262 | +0.0179 |
| Context Recall | 0.0157 | 0.0280 | +0.0123 |

## Key Findings

1. **Biggest improvement:** The pipeline now runs end-to-end with clean module boundaries, report generation, and fallback-safe execution.
2. **Biggest challenge:** The retrieved chunks are still too coarse, so exact policy clauses get diluted.
3. **Surprise finding:** The production pipeline improved retrieval metrics over baseline, but faithfulness still dropped because generation remains heuristic.

## Presentation Notes

1. RAGAS scores (naive vs production): retrieval-oriented metrics improved, but faithfulness fell because the answer step is still not a real generator.
2. Biggest win - module nào, tại sao: M2 and M3 together gave the clearest gain on answer relevancy, context precision, and context recall.
3. Case study - 1 failure, Error Tree walkthrough: the leave-without-pay question still misses the exact clause because chunking and ranking are not clause-aware enough.
4. Next optimization nếu có thêm 1 giờ: make chunking more section-aware and add a real generation step for faithful answers.
