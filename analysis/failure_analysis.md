# Failure Analysis - Lab 18: Production RAG

**Nhóm:** Lab 18  
**Thành viên:** Dương Chí Thành - M3 · Tiến - M1 · Linh - M2 · Khôi - M4 · An - integration/support

## RAGAS Scores

| Metric | Naive Baseline | Production | Delta |
|--------|----------------|------------|-------|
| Faithfulness | 0.4000 | 0.4000 | +0.0000 |
| Answer Relevancy | 0.0000 | 0.0000 | +0.0000 |
| Context Precision | 0.0000 | 0.0000 | +0.0000 |
| Context Recall | 0.1667 | 0.0000 | -0.1667 |

## Bottom-5 Failures

### #1
- **Question:** hihi cả nhà tự tạo testset bằng cờm nhé
- **Expected:** Answer should stay semantically close to the question and be grounded in context.
- **Got:** Output drifted away from the question; answer relevancy is 0.0.
- **Worst metric:** answer_relevancy
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: generation fallback is too weak and the query has no useful lexical overlap with retrieved text.
- **Suggested fix:** Replace the extractive fallback in `pipeline.py` with a constrained LLM prompt, and add query normalization before search.

### #2
- **Question:** hihi cả nhà tự tạo testset bằng cờm nhé
- **Expected:** Relevant context should be retrieved from the corpus.
- **Got:** Context recall is 0.0 in production.
- **Worst metric:** context_recall
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: the demo corpus and the evaluation question are too mismatched.
- **Suggested fix:** Add a real Vietnamese corpus and rerun evaluation on a meaningful test set.

### #3
- **Question:** hihi cả nhà tự tạo testset bằng cờm nhé
- **Expected:** Retrieval should surface useful policy text or related content.
- **Got:** Context precision stayed at 0.0.
- **Worst metric:** context_precision
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: retrieval ranking is not calibrated for this dataset.
- **Suggested fix:** Tune BM25/dense fusion and use a stronger reranker.

### #4
- **Question:** hihi cả nhà tự tạo testset bằng cờm nhé
- **Expected:** Faithful answer grounded in retrieved context.
- **Got:** Faithfulness stayed at baseline level because generation is still heuristic.
- **Worst metric:** faithfulness
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: answer generation is a fallback, not an LLM completion.
- **Suggested fix:** Switch to a controlled generation prompt and pass the top contexts directly to an LLM.

### #5
- **Question:** hihi cả nhà tự tạo testset bằng cờm nhé
- **Expected:** Production pipeline should improve retrieval quality over baseline.
- **Got:** The current corpus is too small to show a measurable lift.
- **Worst metric:** context_precision
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: insufficient indexed data.
- **Suggested fix:** Use a larger corpus and more than one evaluation question.

## Case Study (presentation)

**Question:** hihi cả nhà tự tạo testset bằng cờm nhé

**Error Tree walkthrough:**
1. Output đúng? -> No.
2. Context đúng? -> No.
3. Query rewrite OK? -> No, the query is noisy and not aligned with the corpus.
4. Fix ở bước: improve query normalization, add real generation, and evaluate on a meaningful corpus.

**Nếu có thêm 1 giờ:**
- Replace the answer fallback with a real constrained LLM response.
- Add a larger Vietnamese corpus and a cleaner test set.
- Tune hybrid search weights and reranker thresholds against actual failures.
