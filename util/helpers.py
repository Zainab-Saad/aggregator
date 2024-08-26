from util.constants import EvalMetrics

def get_aggregated_metrics(eval_metrics):
    metrics_aggregated = dict()
    total_num = sum([num for num, _ in eval_metrics])
    for eval_metric in EvalMetrics:
        metric_aggregated = (
            sum([metrics[eval_metric.value] * num for num, metrics in eval_metrics]) / total_num
        )
        metrics_aggregated[eval_metric.value] = metric_aggregated
    return metrics_aggregated