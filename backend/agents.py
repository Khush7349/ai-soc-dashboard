from detection import predict
from rules import apply_rules
from severity import compute_severity
from llm import explain
def analyze_logs(df):
    try:
        preds = predict(df)
    except Exception as e:
        return [{"error": f"Prediction failed: {str(e)}"}]
    results = []
    for i, row in df.iterrows():
        try:
            log_data = row.to_dict()
            rules = apply_rules(row)
            severity = compute_severity(preds[i], rules)
            explanation = None
            if severity in ["High", "Critical"]:
                try:
                    explanation = explain(log_data)
                except Exception:
                    explanation = "LLM explanation failed"
            reasoning = {
                "ml_anomaly": int(preds[i]),
                "rules_triggered": rules,
                "severity_logic": f"Score based on ML + {len(rules)} rule(s)"
            }
            results.append({
                "log": log_data,
                "anomaly": int(preds[i]),
                "rules": rules,
                "severity": severity,
                "reasoning": reasoning,
                "explanation": explanation
            })
        except Exception as e:
            results.append({
                "error": f"Processing failed for row {i}: {str(e)}"
            })
    return results