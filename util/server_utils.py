from typing import Dict

from util.helpers import get_aggregated_metrics

def evaluate_metrics_aggregation(eval_metrics):
    """Return an aggregated metrics for evaluation."""
    metrics_aggregated = get_aggregated_metrics(eval_metrics)
    return metrics_aggregated

def config_func(rnd: int) -> Dict[str, str]:
    return {
        "global_round": str(rnd)
    }

SERVER_ADDRESS = "0.0.0.0:8081"