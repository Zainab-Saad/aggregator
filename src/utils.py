from typing import Dict

def evaluate_metrics_aggregation(eval_metrics):
    """Return an aggregated metric (mae in this case) for evaluation."""
    total_num = sum([num for num, _ in eval_metrics])
    mae_aggregated = (
        sum([metrics["mae"] * num for num, metrics in eval_metrics]) / total_num
    )
    metrics_aggregated = {"mae": mae_aggregated}
    return metrics_aggregated

def config_func(rnd: int) -> Dict[str, str]:
    return {
        "global_round": str(rnd)
    }