import pandas as pd
import numpy as np

def format_number(val):
    if isinstance(val, (int, np.integer)):
        return str(val)
    elif isinstance(val, (float, np.floating)):
        return f"{val:,.4f}"
    return str(val)

def execute_plan(df: pd.DataFrame, plan: dict) -> str:
    """
    Executes a multi-step analytical plan on the dataframe.
    """
    if "operation" in plan and plan.get("operation") == "error":
        return f"Error: {plan.get('message', 'Unknown error during planning.')}"
        
    # Support backward compatibility with single operation plan
    if "operation" in plan and "steps" not in plan:
        steps = [plan]
    else:
        steps = plan.get("steps", [])
        
    goal = plan.get("goal", "Execute analytical plan")
    evidence_log = [f"GOAL: {goal}"]
    
    current_df = df.copy()
    final_result_text = None
    
    try:
        for i, step in enumerate(steps):
            op = step.get("operation")
            evidence_log.append(f"\n--- Step {i+1}: {op} ---")
            
            if op == "filter":
                conditions = step.get("conditions", [])
                logical_op = step.get("logical_operator", "AND").upper()
                mask = pd.Series(True, index=current_df.index) if logical_op == "AND" else pd.Series(False, index=current_df.index)
                
                for cond in conditions:
                    col = cond.get("column")
                    opr = cond.get("operator")
                    val = cond.get("value")
                    
                    if col not in current_df.columns:
                        raise ValueError(f"Column '{col}' not found for filtering.")
                        
                    # Handle typing
                    if pd.api.types.is_numeric_dtype(current_df[col]):
                        try:
                            val = float(val)
                        except:
                            pass
                            
                    if opr == "==": c_mask = current_df[col] == val
                    elif opr == "!=": c_mask = current_df[col] != val
                    elif opr == ">": c_mask = current_df[col] > val
                    elif opr == "<": c_mask = current_df[col] < val
                    elif opr == ">=": c_mask = current_df[col] >= val
                    elif opr == "<=": c_mask = current_df[col] <= val
                    elif opr == "contains": c_mask = current_df[col].astype(str).str.contains(str(val), case=False, na=False)
                    elif opr == "starts_with": c_mask = current_df[col].astype(str).str.startswith(str(val), na=False)
                    elif opr == "ends_with": c_mask = current_df[col].astype(str).str.endswith(str(val), na=False)
                    else: raise ValueError(f"Unsupported filter operator: {opr}")
                        
                    if logical_op == "AND":
                        mask = mask & c_mask
                    else:
                        mask = mask | c_mask
                        
                current_df = current_df[mask]
                evidence_log.append(f"Applied filters resulting in {len(current_df)} rows.")

            elif op == "derive":
                out_col = step.get("output_column")
                method = step.get("method")
                
                if method == "arithmetic":
                    op1 = step.get("operand1")
                    opr = step.get("operator")
                    op2 = step.get("operand2")
                    
                    val1 = current_df[op1] if op1 in current_df.columns else float(op1)
                    val2 = current_df[op2] if op2 in current_df.columns else float(op2)
                    
                    if opr == "+": current_df[out_col] = val1 + val2
                    elif opr == "-": current_df[out_col] = val1 - val2
                    elif opr == "*": current_df[out_col] = val1 * val2
                    elif opr == "/": current_df[out_col] = val1 / val2.replace(0, np.nan)
                    elif opr == "percentage": current_df[out_col] = (val1 / val2.replace(0, np.nan)) * 100
                    else: raise ValueError(f"Unsupported arithmetic operator: {opr}")
                        
                    evidence_log.append(f"Derived column '{out_col}' using arithmetic.")
                    
                else:
                    raise ValueError(f"Unsupported derive method: {method}")

            elif op == "normalize":
                out_col = step.get("output_column")
                in_col = step.get("input_column")
                method = step.get("method")
                
                if method == "zscore":
                    mean = current_df[in_col].mean()
                    std = current_df[in_col].std()
                    if pd.isna(std) or std == 0:
                        current_df[out_col] = 0
                    else:
                        current_df[out_col] = (current_df[in_col] - mean) / std
                elif method == "minmax":
                    cmin = current_df[in_col].min()
                    cmax = current_df[in_col].max()
                    if cmax == cmin:
                        current_df[out_col] = 0
                    else:
                        current_df[out_col] = (current_df[in_col] - cmin) / (cmax - cmin)
                else:
                    raise ValueError(f"Unsupported normalize method: {method}")
                    
                evidence_log.append(f"Normalized '{in_col}' into '{out_col}' using {method}.")

            elif op == "group_derive":
                out_col = step.get("output_column")
                group_col = step.get("group_column")
                in_col = step.get("input_column")
                method = step.get("method")
                
                if method == "zscore":
                    def safe_zscore(x):
                        std = x.std()
                        if pd.isna(std) or std == 0: return pd.Series(0, index=x.index)
                        return (x - x.mean()) / std
                    current_df[out_col] = current_df.groupby(group_col)[in_col].transform(safe_zscore)
                elif method == "percentage_of_group_total":
                    current_df[out_col] = current_df.groupby(group_col)[in_col].transform(lambda x: (x / x.sum()) * 100)
                else:
                    raise ValueError(f"Unsupported group_derive method: {method}")
                    
                evidence_log.append(f"Derived '{out_col}' grouped by '{group_col}' using {method}.")

            elif op == "aggregate":
                g_cols = step.get("group_columns", [])
                m_cols = step.get("metric_columns", [])
                aggs = step.get("aggregations", [])
                
                if len(m_cols) == 0:
                    # Backward compat with old plan
                    m_col = step.get("metric_column")
                    if m_col: m_cols = [m_col]
                if len(aggs) == 0:
                    agg = step.get("aggregation")
                    if agg: aggs = [agg]
                if len(g_cols) == 0:
                    g_col = step.get("group_column")
                    if g_col: g_cols = [g_col]
                    
                agg_dict = {col: aggs for col in m_cols}
                
                if g_cols:
                    current_df = current_df.groupby(g_cols).agg(agg_dict).reset_index()
                    # Flatten columns
                    current_df.columns = [f"{c[0]}_{c[1]}" if c[1] else c[0] for c in current_df.columns]
                    evidence_log.append(f"Aggregated {m_cols} by {g_cols}.")
                else:
                    res = {}
                    for col in m_cols:
                        for agg in aggs:
                            res[f"{col}_{agg}"] = current_df[col].agg(agg)
                    current_df = pd.DataFrame([res])
                    evidence_log.append(f"Aggregated {m_cols} globally.")

            elif op == "rank":
                col = step.get("column")
                asc = step.get("ascending", False)
                limit = step.get("limit", 10)
                
                if col not in current_df.columns:
                    # Find any aggregated version of this column
                    possible_cols = [c for c in current_df.columns if c.startswith(f"{col}_")]
                    if possible_cols:
                        col = possible_cols[0]
                    else:
                        m_col = step.get("metric_column")
                        if m_col:
                            possible_m_cols = [c for c in current_df.columns if c.startswith(f"{m_col}_")]
                            if possible_m_cols:
                                col = possible_m_cols[0]
                                
                if col not in current_df.columns:
                    raise ValueError(f"Column '{col}' not found for ranking.")
                    
                current_df = current_df.sort_values(by=col, ascending=asc).head(limit)
                evidence_log.append(f"Ranked by {col} {'ascending' if asc else 'descending'} (limit {limit}).")
                
            elif op == "time_series":
                d_col = step.get("date_column")
                m_col = step.get("metric_column")
                agg = step.get("aggregation", "sum")
                freq = step.get("frequency", "M")
                
                temp_df = current_df.copy()
                temp_df[d_col] = pd.to_datetime(temp_df[d_col], errors='coerce')
                temp_df = temp_df.dropna(subset=[d_col])
                
                if freq == "monthly" or freq == "M": temp_df['period'] = temp_df[d_col].dt.to_period('M')
                elif freq == "yearly" or freq == "Y": temp_df['period'] = temp_df[d_col].dt.to_period('Y')
                elif freq == "weekly" or freq == "W": temp_df['period'] = temp_df[d_col].dt.to_period('W')
                else: temp_df['period'] = temp_df[d_col].dt.to_period('D')
                    
                current_df = temp_df.groupby('period')[m_col].agg(agg).reset_index()
                current_df['period'] = current_df['period'].astype(str)
                evidence_log.append(f"Generated time series for {m_col} ({agg}) by {freq}.")
                
            elif op == "comparison":
                g_col = step.get("group_column")
                m_col = step.get("metric_column")
                agg = step.get("aggregation", "mean")
                f_vals = step.get("filter_values", [])
                
                res = []
                for val in f_vals:
                    sub = current_df[current_df[g_col].astype(str).str.lower() == str(val).lower()]
                    val_res = sub[m_col].agg(agg) if not sub.empty else None
                    res.append(f"{val}: {format_number(val_res) if val_res is not None else 'No data'}")
                final_result_text = f"Comparison of {agg} {m_col} by {g_col}:\n" + "\n".join(res)
                evidence_log.append(final_result_text)

            elif op == "distinct_count":
                col = step.get("column")
                val = current_df[col].nunique()
                final_result_text = f"There are {format_number(val)} distinct values in {col}."
                evidence_log.append(final_result_text)
                
            elif op == "percentage":
                g_col = step.get("group_column")
                m_col = step.get("metric_column")
                grouped = current_df.groupby(g_col)[m_col].sum()
                total = grouped.sum()
                if total > 0:
                    current_df = (grouped / total * 100).reset_index()
                    evidence_log.append(f"Calculated percentage of {m_col} by {g_col}.")
                
            elif op == "correlation":
                col1 = step.get("column1")
                col2 = step.get("column2")
                corr = current_df[col1].corr(current_df[col2])
                final_result_text = f"Pearson correlation between {col1} and {col2} is {format_number(corr)}."
                evidence_log.append(final_result_text)
                
            elif op == "outliers":
                col = step.get("metric_column")
                Q1 = current_df[col].quantile(0.25)
                Q3 = current_df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                outliers = current_df[(current_df[col] < lower) | (current_df[col] > upper)]
                final_result_text = f"Outliers for {col}:\nLower bound: {format_number(lower)}, Upper bound: {format_number(upper)}\nFound {len(outliers)} outliers."
                evidence_log.append(final_result_text)
                if len(outliers) > 0:
                    current_df = outliers
                
            elif op == "data_quality":
                missing = current_df.isnull().sum()
                missing = missing[missing > 0]
                res = f"Rows: {len(current_df)}, Columns: {len(current_df.columns)}, Duplicates: {current_df.duplicated().sum()}\n"
                if len(missing) > 0:
                    res += "Missing:\n" + "\n".join([f"- {k}: {v}" for k, v in missing.items()])
                else:
                    res += "Missing: None"
                final_result_text = res
                evidence_log.append("Performed data quality check.")
                
            elif op == "report":
                res = f"Rows: {len(current_df)}, Columns: {len(current_df.columns)}\n"
                num_cols = current_df.select_dtypes(include=['number']).columns
                if len(num_cols) > 0:
                    res += "Sums:\n" + "\n".join([f"- {c}: {format_number(current_df[c].sum())}" for c in num_cols])
                final_result_text = res
                evidence_log.append("Generated generic report.")
                
            elif op == "clarification_request":
                final_result_text = step.get("message", "Could you please clarify your question?")
                evidence_log.append(f"Requesting clarification: {final_result_text}")
                
            else:
                # Handle backwards compatibility for single step things that might not be matched above
                if op in ["comparison", "growth", "distribution"]:
                    final_result_text = f"Operation '{op}' executed (Legacy mode)."
                else:
                    evidence_log.append(f"Warning: Operation '{op}' was recognized but might not fully modify the dataframe.")
                    
        # Formatting the final state of current_df if final_result_text wasn't set
        if final_result_text is None:
            # We print the dataframe as evidence
            if len(current_df) > 50:
                df_str = current_df.head(50).to_string(index=False)
                df_str += f"\n... (truncated {len(current_df) - 50} rows)"
            else:
                df_str = current_df.to_string(index=False)
                
            final_result_text = f"Final Dataframe Result:\n{df_str}"
            
        evidence_log.append("\n=== FINAL VERIFIED EVIDENCE ===")
        evidence_log.append(final_result_text)
        
        return "\n".join(evidence_log)
        
    except Exception as e:
        return f"Error executing plan step '{step.get('operation')}': {str(e)}\nTrace:\n" + "\n".join(evidence_log)
