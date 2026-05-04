# Failure Analysis - Lab 18: Production RAG

**Nhóm:** Lab 18  
**Thành viên:** Dương Chí Thành - M3 · Tiến - M1 · Linh - M2 · Khôi - M4 · An - integration/support

## RAGAS Scores

| Metric | Naive Baseline | Production | Delta |
|--------|----------------|------------|-------|
| Faithfulness | 0.7393 | 0.6409 | -0.0984 |
| Answer Relevancy | 0.0069 | 0.0382 | +0.0313 |
| Context Precision | 0.0083 | 0.0262 | +0.0179 |
| Context Recall | 0.0157 | 0.0280 | +0.0123 |

## Bottom-5 Failures

### #1
- **Question:** Nhan vien chinh thuc duoc nghi phep nam bao nhieu ngay moi nam?
- **Expected:** Retrieve the policy sentence about annual leave.
- **Got:** Retrieved context did not surface the exact policy sentence strongly enough.
- **Worst metric:** context_recall
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: the retrieval stack still misses some direct policy spans.
- **Suggested fix:** Improve chunking granularity and tighten BM25 + reranking on policy clauses.

### #2
- **Question:** So ngay nghi phep co tang them theo tham nien khong?
- **Expected:** Retrieve the thâm niên rule correctly.
- **Got:** Context was relevant but not ranked high enough.
- **Worst metric:** context_recall
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: chunking and retrieval are not preserving the exact clause.
- **Suggested fix:** Use structure-aware chunking plus better query expansion.

### #3
- **Question:** Nhan vien co the xin nghi phep khong luong toi da bao nhieu ngay mot nam?
- **Expected:** Context precision should be high for the leave-without-pay clause.
- **Got:** Retrieved chunks were still noisy.
- **Worst metric:** context_precision
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: the index contains too many long chunks and the relevant clause is diluted.
- **Suggested fix:** Split legal/policy sections more aggressively and add metadata filters.

### #4
- **Question:** Don xin nghi phep can ai phe duyet?
- **Expected:** Answer should identify the approving manager.
- **Got:** The approval clause was not retrieved cleanly.
- **Worst metric:** context_precision
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: ranking favors broader chunks over a precise approval clause.
- **Suggested fix:** Add clause-level chunking and rerank using exact-match signals.

### #5
- **Question:** Ho so nghi om can nop giay xac nhan trong bao lau?
- **Expected:** Retrieve the medical certificate deadline.
- **Got:** The retrieved context only partially matched the time constraint.
- **Worst metric:** context_precision
- **Error Tree:** Output sai -> Context đúng? -> Query OK? -> Root cause: overlapping chunks still mix unrelated policy text.
- **Suggested fix:** Preserve section boundaries better during chunking and improve rerank scoring.

## Case Study (presentation)

**Question:** Nhan vien co the xin nghi phep khong luong toi da bao nhieu ngay mot nam?

**Error Tree walkthrough:**
1. Output đúng? -> Partially, but the answer is not grounded enough.
2. Context đúng? -> Partially, the right policy exists but is not ranked first.
3. Query rewrite OK? -> Yes, the query is clean enough.
4. Fix ở bước: improve chunk boundaries and reranking around the policy section.

**Nếu có thêm 1 giờ:**
- Tighten structure-aware chunking for policy docs.
- Add metadata-based filters on section titles.
- Retune BM25 and reranker weighting for exact policy clauses.
